import json
import azure.functions as func
import logging
import time

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="Foo", auth_level=func.AuthLevel.ANONYMOUS)
@app.cosmos_db_output(arg_name="outputDocument", database_name="my-database", container_name="my-container", connection="CosmosDbConnectionString")
def Foo(req: func.HttpRequest, outputDocument: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Processing Foo request.')

    foobar_fizzbuzz = {
        "foo": "bar",
        "fizz": "buzz"
    }

    outputDocument.set(func.Document.from_dict({"id": str(int(time.time() % 86400))}))

    return func.HttpResponse(
        json.dumps(foobar_fizzbuzz),
        status_code=200
    )