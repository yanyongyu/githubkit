# Calling GraphQL API

The GitHub GraphQL API offers flexibility and the ability to define precisely the data you want to fetch. See the [GitHub GraphQL API documentation](https://docs.github.com/en/graphql) for more information.

## The Basics

Before calling the GraphQL API, you could create your query from the [GitHub GraphQL Explorer](https://docs.github.com/en/graphql/overview/explorer). For example, to get current login user:

```python
query = """
{
  viewer {
    login
  }
}
"""
```

Then, you can call the GraphQL API with the query:

=== "Sync"

    ```python
    data: dict[str, Any] = github.graphql(query)
    user_login: str = data["viewer"]["login"]
    ```

=== "Async"

    ```python
    data: dict[str, Any] = await github.async_graphql(query)
    user_login: str = data["viewer"]["login"]
    ```

Calling GraphQL API with variables:

=== "Sync"

    ```python
    query = """
    query ($owner: String!, $repo: String!) {
      repository(owner: $owner, name: $repo) {
        name
      }
    }
    """

    data: dict[str, Any] = github.graphql(query, variables={"owner": "owner", "repo": "repo"})
    repo_name: str = data["repository"]["name"]
    ```

=== "Async"

    ```python
    query = """
    query ($owner: String!, $repo: String!) {
      repository(owner: $owner, name: $repo) {
        name
      }
    }
    """

    data: dict[str, Any] = await github.async_graphql(query, variables={"owner": "owner", "repo": "repo"})
    repo_name: str = data["repository"]["name"]
    ```

## GraphQL Pagination

githubkit also provides a helper function to paginate the GraphQL API.

First, You must accept a `cursor` parameter and return a `pageInfo` object in your query. For example:

```graphql hl_lines="1 3 7-10"
query ($owner: String!, $repo: String!, $cursor: String) {
  repository(owner: $owner, name: $repo) {
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
```

The `pageInfo` object in your query must be one of the following types depending on the direction of the pagination:

For forward pagination, use:

```graphql
pageInfo {
  hasNextPage
  endCursor
}
```

For backward pagination, use:

```graphql
pageInfo {
  hasPreviousPage
  startCursor
}
```

If you provide all 4 properties in a `pageInfo`, githubkit will default to **forward pagination**.

Then, you can iterate over the paginated results by using the graphql `paginate` method:

```python
for result in github.graphql.paginate(
    query, variables={"owner": "owner", "repo": "repo"}
):
    print(result)
```

Note that the `result` is a dict containing the list of nodes/edges for each page and the `pageInfo` object. You should iterate over the `nodes` or `edges` list to get the actual data. For example:

```python
for result in g.graphql.paginate(query, {"owner": "owner", "repo": "repo"}):
    for issue in result["repository"]["issues"]["nodes"]:
        print(issue)
```

You can also provide a initial cursor value to start pagination from a specific point:

```python hl_lines="2"
for result in github.graphql.paginate(
    query, variables={"owner": "owner", "repo": "repo", "cursor": "initial_cursor"}
):
    print(result)
```

!!! tips

    Nested pagination is not supported.
