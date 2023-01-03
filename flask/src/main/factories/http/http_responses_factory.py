from src.main.http.http_responses import HttpResponses, HttpResponsesInterface


def make() -> HttpResponsesInterface:
    return HttpResponses()
