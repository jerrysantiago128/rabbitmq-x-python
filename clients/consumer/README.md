# Consumer

Consume, process, analyze, update, and send off JSON data to a REST API

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


## Connectivity
- username: guest
- password: guest
- host: Docker IP OR localhost
- port: 5672
