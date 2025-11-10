# Consumer

Consume, process, analyze, update, and send off JSON data to a REST API

## Assumptions

Docker is installed on your machine

## Usage

### Docker

#### Pull the Image
 
Simply run the command below to pull to RabbitMQ image locally:

    docker pull python:3.11

More images can be found at the link below:
    
    https://hub.docker.com/_/python/tags

#### Build the Image

Using the build script provided, run the command below to buld the image for the consumer service

    ./build-image.sh

#### Start the service

    docker run --name <some-name> --hostname <some-hostname> -d python:3.11

    - Note: the `-d` flag will run the container in "detatched" mode
    - Remove the `-d` or use `docker logs -f <container-name> to view the logs for the container.

Verify that the image is built and run 

## Connectivity

Using Default RabbitMQ Deployment:
- username: guest
- password: guest
- host: Docker IP OR localhost
- port: 5672

## Methods
### callback(bytes: body)

- ingest byte string data from a given queue on a RabbitMQ broker
- convert byte string to python dictionary

### process(dict: message)

- checks for valid value on a given key *sensor_id*
- if valid value, calls determineShape()
- results from determineShape() are added to the 'message' dictionary and passed to sendToAPI

### determineShape(list: data_points)

- takes a python list of N data points and calculates the 'shape' based on the number of data points
    - ex: 3 sets of data points makes a triangle
- returns a string of the calculated shape

### sendToAPI(dict: message)

- the python dictionary message is sent as JSON object to the defined API endpoint