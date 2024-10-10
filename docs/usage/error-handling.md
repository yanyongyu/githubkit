# Error Handling

githubkit will raise exceptions when it encounters an error. Here shows all the exceptions that githubkit may raise. The most common exception is `RequestFailed`, which is raised when the http response status code is not successful.

```plaintext title="Exceptions"
GitHubException
├── AuthCredentialError
├── AuthExpiredError
├── RequestError
│   ├── RequestTimeout
│   └── RequestFailed
│       └── RateLimitExceeded
│           ├── PrimaryRateLimitExceeded
│           └── SecondaryRateLimitExceeded
├── GraphQLError
│   ├── GraphQLFailed
│   └── GraphQLPaginationError
│       ├── GraphQLMissingPageInfo
│       └── GraphQLMissingCursorChange
└── WebhookTypeNotFound
```

## Authentication Error

githubkit will raise `AuthCredentialError` when you missing or provide invalid credentials. `AuthExpiredError` will be raised when the token or refresh token is expired.

## Request Error

All githubkit requests (including REST API and GraphQL API) may raise `RequestError` when the request failed. `RequestTimeout` will be raised when the request timeout. `RequestFailed` will be raised when the http response status code is not successful.

```python
from githubkit.exception import RequestError, RequestFailed, RequestTimeout

try:
    resp = github.rest.repos.get("owner", "repo")
except RequestFailed as e:
    print(e.response.status_code)
except RequestTimeout as e:
    print("Timeout")
except RequestError as e:
    print(f"Unknown Request Error: {e}")
```

Specially, `RateLimitExceeded` will be raised when githubkit detects the rate limit error message in the response. `PrimaryRateLimitExceeded` will be raised when the primary rate limit is exceeded. `SecondaryRateLimitExceeded` will be raised when the secondary rate limit is exceeded. See [GitHub Docs - Rate Limit](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api) for more information.

## GraphQL Error

githubkit may raise `GraphQLFailed` when the query failed. Note that this is not the same as `RequestFailed`.

```python
from githubkit.exception import GraphQLFailed

try:
    resp = github.graphql.query(some_query)
except GraphQLFailed as e:
    print(e.response.errors)
```

`GraphQLMissingPageInfo` will be raised when the page info missing in the response data. This usually happens when you miss the `pageInfo` field in the query. `GraphQLMissingCursorChange` will be raised when the cursor is not changed in the response data.

## Webhook Error

`WebhookTypeNotFound` will be raised when the webhook event name is not found. Please check the event name and the webhook version you are using or report an issue to githubkit.
