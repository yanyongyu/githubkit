import pytest

from githubkit import GitHub

TEST_QUERY = """
query($owner:String!, $repo: String!) {
  repository(owner:$owner, name:$repo) {
    owner {
      login
    },
    name
  }
}
"""
TEST_VARS = {"owner": "yanyongyu", "repo": "githubkit"}
TEST_RESULT = {"repository": {"owner": {"login": "yanyongyu"}, "name": "githubkit"}}


def test_graphql(g: GitHub):
    result = g.graphql(TEST_QUERY, TEST_VARS)
    assert result == TEST_RESULT


@pytest.mark.anyio
async def test_async_graphql(g: GitHub):
    result = await g.async_graphql(TEST_QUERY, TEST_VARS)
    assert result == TEST_RESULT
