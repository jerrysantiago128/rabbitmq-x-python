# Producer

Generate and publish a JSON object to a RabbitMQ queue

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
