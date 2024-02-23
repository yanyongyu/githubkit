"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

bash ./scripts/run-codegen.sh

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Optional
from weakref import ref

from githubkit.utils import UNSET, exclude_unset
from githubkit.typing import Missing

if TYPE_CHECKING:
    from typing import List

    from githubkit import GitHubCore
    from githubkit.utils import UNSET
    from githubkit.typing import Missing
    from githubkit.response import Response

    from ..models import (
        Classroom,
        SimpleClassroom,
        ClassroomAssignment,
        ClassroomAssignmentGrade,
        SimpleClassroomAssignment,
        ClassroomAcceptedAssignment,
    )


class ClassroomClient:
    _REST_API_VERSION = "2022-11-28"

    def __init__(self, github: GitHubCore):
        self._github_ref = ref(github)

    @property
    def _github(self) -> GitHubCore:
        if g := self._github_ref():
            return g
        raise RuntimeError(
            "GitHub client has already been collected. "
            "Do not use this client after the client has been collected."
        )

    def get_an_assignment(
        self,
        assignment_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[ClassroomAssignment]:
        """See also: https://docs.github.com/rest/classroom/classroom#get-an-assignment"""

        from ..models import BasicError, ClassroomAssignment

        url = f"/assignments/{assignment_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=ClassroomAssignment,
            error_models={
                "404": BasicError,
            },
        )

    async def async_get_an_assignment(
        self,
        assignment_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[ClassroomAssignment]:
        """See also: https://docs.github.com/rest/classroom/classroom#get-an-assignment"""

        from ..models import BasicError, ClassroomAssignment

        url = f"/assignments/{assignment_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=ClassroomAssignment,
            error_models={
                "404": BasicError,
            },
        )

    def list_accepted_assigments_for_an_assignment(
        self,
        assignment_id: int,
        page: Missing[int] = UNSET,
        per_page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[ClassroomAcceptedAssignment]]:
        """See also: https://docs.github.com/rest/classroom/classroom#list-accepted-assignments-for-an-assignment"""

        from typing import List

        from ..models import ClassroomAcceptedAssignment

        url = f"/assignments/{assignment_id}/accepted_assignments"

        params = {
            "page": page,
            "per_page": per_page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[ClassroomAcceptedAssignment],
        )

    async def async_list_accepted_assigments_for_an_assignment(
        self,
        assignment_id: int,
        page: Missing[int] = UNSET,
        per_page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[ClassroomAcceptedAssignment]]:
        """See also: https://docs.github.com/rest/classroom/classroom#list-accepted-assignments-for-an-assignment"""

        from typing import List

        from ..models import ClassroomAcceptedAssignment

        url = f"/assignments/{assignment_id}/accepted_assignments"

        params = {
            "page": page,
            "per_page": per_page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[ClassroomAcceptedAssignment],
        )

    def get_assignment_grades(
        self,
        assignment_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[ClassroomAssignmentGrade]]:
        """See also: https://docs.github.com/rest/classroom/classroom#get-assignment-grades"""

        from typing import List

        from ..models import BasicError, ClassroomAssignmentGrade

        url = f"/assignments/{assignment_id}/grades"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=List[ClassroomAssignmentGrade],
            error_models={
                "404": BasicError,
            },
        )

    async def async_get_assignment_grades(
        self,
        assignment_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[ClassroomAssignmentGrade]]:
        """See also: https://docs.github.com/rest/classroom/classroom#get-assignment-grades"""

        from typing import List

        from ..models import BasicError, ClassroomAssignmentGrade

        url = f"/assignments/{assignment_id}/grades"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=List[ClassroomAssignmentGrade],
            error_models={
                "404": BasicError,
            },
        )

    def list_classrooms(
        self,
        page: Missing[int] = UNSET,
        per_page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[SimpleClassroom]]:
        """See also: https://docs.github.com/rest/classroom/classroom#list-classrooms"""

        from typing import List

        from ..models import SimpleClassroom

        url = "/classrooms"

        params = {
            "page": page,
            "per_page": per_page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[SimpleClassroom],
        )

    async def async_list_classrooms(
        self,
        page: Missing[int] = UNSET,
        per_page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[SimpleClassroom]]:
        """See also: https://docs.github.com/rest/classroom/classroom#list-classrooms"""

        from typing import List

        from ..models import SimpleClassroom

        url = "/classrooms"

        params = {
            "page": page,
            "per_page": per_page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[SimpleClassroom],
        )

    def get_a_classroom(
        self,
        classroom_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[Classroom]:
        """See also: https://docs.github.com/rest/classroom/classroom#get-a-classroom"""

        from ..models import Classroom, BasicError

        url = f"/classrooms/{classroom_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=Classroom,
            error_models={
                "404": BasicError,
            },
        )

    async def async_get_a_classroom(
        self,
        classroom_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[Classroom]:
        """See also: https://docs.github.com/rest/classroom/classroom#get-a-classroom"""

        from ..models import Classroom, BasicError

        url = f"/classrooms/{classroom_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=Classroom,
            error_models={
                "404": BasicError,
            },
        )

    def list_assignments_for_a_classroom(
        self,
        classroom_id: int,
        page: Missing[int] = UNSET,
        per_page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[SimpleClassroomAssignment]]:
        """See also: https://docs.github.com/rest/classroom/classroom#list-assignments-for-a-classroom"""

        from typing import List

        from ..models import SimpleClassroomAssignment

        url = f"/classrooms/{classroom_id}/assignments"

        params = {
            "page": page,
            "per_page": per_page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[SimpleClassroomAssignment],
        )

    async def async_list_assignments_for_a_classroom(
        self,
        classroom_id: int,
        page: Missing[int] = UNSET,
        per_page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[SimpleClassroomAssignment]]:
        """See also: https://docs.github.com/rest/classroom/classroom#list-assignments-for-a-classroom"""

        from typing import List

        from ..models import SimpleClassroomAssignment

        url = f"/classrooms/{classroom_id}/assignments"

        params = {
            "page": page,
            "per_page": per_page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[SimpleClassroomAssignment],
        )
