# FastAPI Sensor Data Management Service

This service provides a simple RESTful API for managing a collection of sensor data entries. It uses the FastAPI framework for high performance and automatic interactive documentation.

It allows users to retrieve the entire list of sensors, fetch a specific sensor by its unique ID, and add new sensor entries. The data is currently held in an in-memory list.

## Assumptions

- Unique `sensor_id`: Every sensor must have a unique sensor_id (a string). The system will return a 409 Conflict if an attempt is made to add a sensor with an ID that already exists.

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

## Connectivity/Endpoints

`/sensors`:
- Retrieves a list of all sensor entries.
- Status Code: 200
- Model: List[sensors]

`/sensors/{sensor_id}`:
- Retrieves a single sensor by its sensor_id.
- Status Codes: 200, 404
- Model: sensor


## Data Model
`sensor`:
- `sensor_id(str)`:   The unique identifier for the sensor.
- `data_points(list)`:    A list containing the recorded data points (e.g., coordinates, values).
- `notes(str)`:	Any relevant notes or metadata about the sensor or data.
- `timestamp(str)`:   The time of the last data capture or record creation (expected to be an ISO 8601 string).
- `shape(str)`:   Describes the shape of the data points (e.g., "point", "line", "polygon")