# Python OpenAPI Flask
openapi python server with flask

hint: in various places below, the description is based on the assumption that you have installed docker

## Edit OpenAPI Specification

for additional info see https://github.com/swagger-api/swagger-editor

`cd <to your local git project directory>`

`docker run -d -p 80:8080 -v $(pwd):/tmp -e SWAGGER_FILE="/tmp/openapi-fruit.yaml" swaggerapi/swagger-editor`

now open the following url in your browser

http://localhost:80/

## Generate the Python Server Project

for additional info see https://github.com/OpenAPITools/openapi-generator

the command below starts the openapi generator in a docker container that

* reads the spec file `openapi-fruit.yaml`
* generates a Flask server project into the output directory `out`
* be careful, existing content in the output directory will be overwritten

`docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate -i /local/openapi-fruit.yaml -g python-flask -o /local/out`

## Add/implement Program Logic to generated Python Server

the commands below assume that you have vs code installed

`cd out`
`vscode .`

## Run the Server in a Docker Container

build the docker image (repeat this step whenever you change some of the code/config)

`docker build -t openapi_server .`

run the server 

`docker run -p 8080:8080 openapi_server`

now open the following url in your browser

http://localhost:8080/q/openapi/ui/#/
