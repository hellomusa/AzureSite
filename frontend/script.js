const PROD_HOSTNAME = "azure.hellomusa.com";
const PROD_FUNCTION_ENDPOINT = "https://myazurecloudfunction.azurewebsites.net/api/foo";
const DEV_FUNCTION_ENDPOINT = "http://localhost:7071/api/foo";

const hostname = window.location.hostname;
const isProduction = hostname === PROD_HOSTNAME;
const functionEndpoint = isProduction ? PROD_FUNCTION_ENDPOINT : DEV_FUNCTION_ENDPOINT;

fetch(functionEndpoint)
    .then((response) => {
        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`)
        }
        return response.json();
    })
    .then((json) => console.log(json))
    .catch((error) => console.log(`Could not fetch foo: ${error}`))