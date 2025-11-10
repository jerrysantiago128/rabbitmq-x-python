# Producer

Generate and publish a JSON object to a RabbitMQ queue

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
###  generate_json_data(string: sensor_id_prefix, int: min_length, int: max_length):

- returns a JSON object with the following format:
        
        "sensor_id": string,
        "data_points": list of list,
        "notes": string,
        "timestamp": string
    - "sensor_id" and the number of data points is generated at random


### publish(string: queue_name, string: message)

- publishes a string message to defined queue on RabbitMQ broker
    - number of messages published is based on while loop counter


## Connectivity
- username: guest
- password: guest
- host: Docker IP OR localhost
- port: 5672
