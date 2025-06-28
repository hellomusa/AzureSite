import json
import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="Foo", auth_level=func.AuthLevel.ANONYMOUS)
def Foo(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing Foo request.')

    foo_with_buzz = {
        "foo": "bar",
        "fizz": "buzz"
    }

    return func.HttpResponse(
        json.dumps(foo_with_buzz),
        status_code=200
    )