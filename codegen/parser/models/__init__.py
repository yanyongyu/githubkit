from collections import deque

from ...log import logger
from ..data import ModelGroup
from ..schemas import ModelSchema


def dependent(group: ModelGroup, groups: list[ModelGroup]) -> list[ModelGroup]:
    """Return the dependents of the group"""
    return [g for g in groups if group in g.group_dependencies]


def in_degree(group: ModelGroup, groups: list[ModelGroup]) -> int:
    """Return the number of groups that depend on this group."""
    return len(dependent(group, groups))


def out_degree(group: ModelGroup) -> int:
    """Return the number of groups this group depends on."""
    return len(group.group_dependencies)


def parse_models(models: list[ModelSchema]) -> list[ModelGroup]:
    """Separate models into groups based on their dependencies."""

    logger.info(f"Start grouping {len(models)} models")

    tmp_mapping = {id(model): ModelGroup(models=[model]) for model in models}
    for model in models:
        tmp_mapping[id(model)].group_dependencies = [
            tmp_mapping[id(dependency)]
            for dependency in tmp_mapping[id(model)].model_dependencies
        ]

    groups: list[ModelGroup] = list(tmp_mapping.values())
    del tmp_mapping

    # merge groups if one group is depended by only one group and has no dependencies
    logger.info("Do merge leaf groups")
    pending_groups = deque(groups)
    while pending_groups:
        group = pending_groups.popleft()
        dependents = dependent(group, groups)
        if len(dependents) == 1 and out_degree(group) == 0:
            # do merge
            target = dependents[0]
            target.merge_group(group)
            # remove merged group from result
            groups.remove(group)
            # add modified target to pending queue
            if target not in pending_groups:
                pending_groups.append(target)

    # merge groups if one group is not depended by any group and has only one dependency
    logger.info("Do merge root groups")
    pending_groups = deque(groups)
    while pending_groups:
        group = pending_groups.popleft()
        if (
            in_degree(group, groups) == 0
            and out_degree(group) == 1
            and in_degree(group.group_dependencies[0], groups) == 1
        ):
            # do merge
            dependency = group.group_dependencies[0]
            dependency.merge_group(group)
            # remove merged group from result
            groups.remove(group)
            # add modified dependency to pending queue
            if dependency not in pending_groups:
                pending_groups.append(dependency)

    # merge groups if two groups have same dependents and dependencies
    logger.info("Do merge groups with same dependents and dependencies")
    pending_groups = [(group, dependent(group, groups)) for group in groups]
    while pending_groups:
        group, dependents = pending_groups.pop(0)
        # if group is root, skip
        if not dependents:
            continue
        dependencies = group.group_dependencies
        for other, other_dependents in pending_groups:
            if (
                other_dependents == dependents
                and other.group_dependencies == dependencies
            ):
                group.merge_group(other)
                for other_dependent in other_dependents:
                    other_dependent.group_dependencies.remove(other)
                groups.remove(other)
                pending_groups.remove((other, other_dependents))

    logger.info("Finish grouping models")
    return groups
