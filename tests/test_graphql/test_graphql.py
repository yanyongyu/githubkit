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
TEST_PAGINATION_QUERY = """
query($owner:String!, $repo: String!, $cursor: String) {
  repository(owner:$owner, name:$repo) {
    issues(first: 10, after: $cursor) {
      nodes {
        number
      }
      pageInfo {
        hasNextPage
        endCursor
      }
    }
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


def test_paginate(g: GitHub):
    paginator = g.graphql.paginate(TEST_PAGINATION_QUERY, TEST_VARS)
    for result in paginator:
        assert isinstance(result["repository"]["issues"]["nodes"], list)


@pytest.mark.anyio
async def test_async_paginate(g: GitHub):
    paginator = g.graphql.paginate(TEST_PAGINATION_QUERY, TEST_VARS)
    async for result in paginator:
        assert isinstance(result["repository"]["issues"]["nodes"], list)
