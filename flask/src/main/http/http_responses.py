from typing import Any
from flask import make_response, jsonify, Response
from abc import ABC, abstractmethod


class HttpResponsesInterface(ABC):
    @abstractmethod
    def create_http_response(
        self, status_code: int, request_success: bool, body: Any
    ) -> Response:
        pass

    @abstractmethod
    def success_request(self, data) -> Response:
        pass

    @abstractmethod
    def bad_request(self, error) -> Response:
        pass

    @abstractmethod
    def server_error(self, error) -> Response:
        pass

    @abstractmethod
    def unauthorized(self, error) -> Response:
        pass


class HttpResponses(HttpResponsesInterface):
    def create_http_response(
        self, status_code: int, request_success: bool, body: Any
    ) -> Response:
        return make_response(
            jsonify(
                {
                    "success": request_success,
                    "response": body,
                }
            ),
            status_code,
        )

    def success_request(self, data) -> Response:
        return self.create_http_response(
            status_code=200,
            request_success=True,
            body=data,
        )

    def bad_request(self, error) -> Response:
        return self.create_http_response(
            status_code=400,
            request_success=False,
            body=error,
        )

    def server_error(self, error) -> Response:
        return self.create_http_response(
            status_code=500,
            request_success=False,
            body=str(error),
        )

    def unauthorized(self, error) -> Response:
        return self.create_http_response(
            status_code=401,
            request_success=False,
            body=error,
        )
