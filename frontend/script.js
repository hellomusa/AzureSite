console.log("loaded!")

const localAzureFunctionEndpoint = "http://localhost:7071/api/foo"
const productionAzureFunctionEndpoint = "https://myazurecloudfunction.azurewebsites.net/api/foo"

const url = window.location.href.includes("127.0.0.1") ? localAzureFunctionEndpoint : productionAzureFunctionEndpoint;

console.log(url)

fetch(url)
    .then((response) => {
        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`)
        }

        return response.json();
    })
    .then((json) => {
        console.log(json);
    })
    .catch((error) => {
        console.log(`Could not fetch foo: ${error}`)
    })