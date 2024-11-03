"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""

from __future__ import annotations

from typing_extensions import TypedDict, NotRequired


class WorkflowRunUsageType(TypedDict):
    """Workflow Run Usage

    Workflow Run Usage
    """

    billable: WorkflowRunUsagePropBillableType
    run_duration_ms: NotRequired[int]


class WorkflowRunUsagePropBillableType(TypedDict):
    """WorkflowRunUsagePropBillable"""

    ubuntu: NotRequired[WorkflowRunUsagePropBillablePropUbuntuType]
    macos: NotRequired[WorkflowRunUsagePropBillablePropMacosType]
    windows: NotRequired[WorkflowRunUsagePropBillablePropWindowsType]


class WorkflowRunUsagePropBillablePropUbuntuType(TypedDict):
    """WorkflowRunUsagePropBillablePropUbuntu"""

    total_ms: int
    jobs: int
    job_runs: NotRequired[
        list[WorkflowRunUsagePropBillablePropUbuntuPropJobRunsItemsType]
    ]


class WorkflowRunUsagePropBillablePropUbuntuPropJobRunsItemsType(TypedDict):
    """WorkflowRunUsagePropBillablePropUbuntuPropJobRunsItems"""

    job_id: int
    duration_ms: int


class WorkflowRunUsagePropBillablePropMacosType(TypedDict):
    """WorkflowRunUsagePropBillablePropMacos"""

    total_ms: int
    jobs: int
    job_runs: NotRequired[
        list[WorkflowRunUsagePropBillablePropMacosPropJobRunsItemsType]
    ]


class WorkflowRunUsagePropBillablePropMacosPropJobRunsItemsType(TypedDict):
    """WorkflowRunUsagePropBillablePropMacosPropJobRunsItems"""

    job_id: int
    duration_ms: int


class WorkflowRunUsagePropBillablePropWindowsType(TypedDict):
    """WorkflowRunUsagePropBillablePropWindows"""

    total_ms: int
    jobs: int
    job_runs: NotRequired[
        list[WorkflowRunUsagePropBillablePropWindowsPropJobRunsItemsType]
    ]


class WorkflowRunUsagePropBillablePropWindowsPropJobRunsItemsType(TypedDict):
    """WorkflowRunUsagePropBillablePropWindowsPropJobRunsItems"""

    job_id: int
    duration_ms: int


__all__ = (
    "WorkflowRunUsageType",
    "WorkflowRunUsagePropBillableType",
    "WorkflowRunUsagePropBillablePropUbuntuType",
    "WorkflowRunUsagePropBillablePropUbuntuPropJobRunsItemsType",
    "WorkflowRunUsagePropBillablePropMacosType",
    "WorkflowRunUsagePropBillablePropMacosPropJobRunsItemsType",
    "WorkflowRunUsagePropBillablePropWindowsType",
    "WorkflowRunUsagePropBillablePropWindowsPropJobRunsItemsType",
)
