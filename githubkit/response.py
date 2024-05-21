from typing import Any, Type, Generic, TypeVar

import httpx

from .compat import type_validate_json

RT = TypeVar("RT")


class Response(Generic[RT]):
    def __init__(self, response: httpx.Response, data_model: Type[RT]):
        self._response = response
        self._data_model = data_model

    def __repr__(self) -> str:
        return f"Response({self._status_reason}, data_model={self._data_model})"

    @property
    def raw_request(self) -> httpx.Request:
        return self._response.request

    @property
    def raw_response(self) -> httpx.Response:
        return self._response

    @property
    def status_code(self) -> int:
        return self._response.status_code

    @property
    def reason_phrase(self) -> str:
        return self._response.reason_phrase

    @property
    def _status_reason(self) -> str:
        return (
            f"{self.status_code} {reason}"
            if (reason := self.reason_phrase)
            else str(self.status_code)
        )

    @property
    def headers(self) -> httpx.Headers:
        return self._response.headers

    @property
    def url(self) -> httpx.URL:
        return self._response.url

    @property
    def content(self) -> bytes:
        return self._response.content

    @property
    def text(self) -> str:
        return self._response.text

    def json(self, **kwargs: Any) -> Any:
        return self._response.json(**kwargs)

    @property
    def parsed_data(self) -> RT:
        return type_validate_json(self._data_model, self.content)
