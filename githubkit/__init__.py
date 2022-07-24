from functools import cached_property

from .core import GitHubCore
from .rest import RestNamespace
from .response import Response as Response
from .paginator import paginate as paginate
from .paginator import Paginator as Paginator
from .auth import BasicAuthStrategy as BasicAuthStrategy
from .auth import TokenAuthStrategy as TokenAuthStrategy


class GitHub(GitHubCore):

    paginate = staticmethod(paginate)

    @cached_property
    def rest(self) -> RestNamespace:
        return RestNamespace(self)
