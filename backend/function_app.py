import json
import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="Foo", auth_level=func.AuthLevel.ANONYMOUS)
def Foo(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing Foo request.')

    foobar_fizzbuzz = {
        "foo": "bar",
        "fizz": "buzz"
    }

    return func.HttpResponse(
        json.dumps(foobar_fizzbuzz),
        status_code=200
    )