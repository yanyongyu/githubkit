<!-- markdownlint-disable MD046 -->

# Webhooks

Webhooks provide a way for notifications to be delivered to an external web server whenever certain events occur on GitHub. See the [GitHub Webhooks Documentation](https://docs.github.com/en/webhooks) for more information.

## Webhook Verification

GitHub always sends a signature in the headers of the webhook request. You can verify the signature to ensure that the webhook request is from GitHub. See the [GitHub Docs - Validating webhook deliveries](https://docs.github.com/en/webhooks/using-webhooks/validating-webhook-deliveries) for more information.

githubkit provides a `verify` function to help you verify the webhook payload. Note that you should provide the raw request body to ensure the integrity of the payload. For example:

```python
from githubkit.webhooks import verify

valid: bool = verify(secret, request.body, request.headers["X-Hub-Signature-256"])
```

!!! note

    The `verify` function is **time-constant**. This is to prevent timing attacks.

!!! warning

    The `verify` function also supports the `X-Hub-Signature` header. GitHub recommends that you use the `X-Hub-Signature-256` header, which uses the HMAC-SHA256 algorithm. The `X-Hub-Signature` header uses the HMAC-SHA1 algorithm and is only included for legacy purposes.

You can also use the `sign` function to generate the signature for the payload. For example:

```python
from githubkit.webhooks import sign

signature: str = sign(secret, payload, method="sha256")
```

## Webhook Event Parsing

You can use githubkit to validate the webhook payload and convert it into a Pydantic model. githubkit provides a `parse` function and the function accepts the event name and the raw request body. For example:

```python
from githubkit.webhooks import parse

event = parse(request.headers["X-GitHub-Event"], request.body)
```

(**NOT RECOMMENDED**) If you do not have the event name, you can use the `parse_without_name` function. This function will try to parse the payload with all supported event names. This will cost longer time, more memory and may return the wrong event type. For example:

```python
from githubkit.webhooks import parse_without_name

event = parse_without_name(request.body)
```

!!! tip

    The behavior of function `parse_without_name` is not the same between pydantic v1 and v2.

    When using pydantic v1, the function will return the first valid event model (known as `left-to-right` mode).

    When using pydantic v2, the function will return the highest scored valid event model (known as `smart` mode).

    See: [Union Modes](https://docs.pydantic.dev/latest/concepts/unions/#union-modes).

If you want to parse the payload as a dict, you can use the `parse_obj` function. For example:

```python
from githubkit.webhooks import parse_obj, parse_obj_without_name

event = parse_obj(request.headers["X-GitHub-Event"], request.json())
event = parse_obj_without_name(request.json())  # NOT RECOMMENDED
```

!!! note

    The `parse` and `parse_obj` function supports type overload, if you provide static value for the `event_name` parameter, the return type will be inferred automatically.

## Webhook Versioning

Usually, you don't need to specify the version of the webhook payload. githubkit uses the latest version by default. If you want to use a specific version (including GHEC), you can switch between versions as follows:

```python
from githubkit import GitHub

event = GitHub.webhooks("2022-11-28").parse(request.headers["X-GitHub-Event"], request.body)
```
