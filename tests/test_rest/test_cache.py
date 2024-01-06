from githubkit import GitHub
from githubkit.versions import LATEST_VERSION


def test_cache(g: GitHub):
    assert g.rest(LATEST_VERSION) is g.rest(LATEST_VERSION)
    assert g.rest(LATEST_VERSION).repos is g.rest(LATEST_VERSION).repos

    assert g.rest is g.rest
    assert g.rest.repos is g.rest.repos
