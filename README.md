
# HTTP Data Store

A simple server built on FastAPI and Python which can be used to store and retrieve a file or piece of data.

## Storing

### String

`curl http://localhost:8000/anything -d "hello"`

### File

`curl http://localhost:8000/myfile --request POST --data-binary "@test.jpg"`

## Fetching 

### String

`url http://localhost:8000/anything`

### File

`curl http://localhost:8000/myfile --output test-out.jpg`