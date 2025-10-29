from rabbitmq import RabbitMQ
import json



def determine_shape(data_points):
    num_data_points = len(data_points)
    
    if num_data_points == 1:
        shape = "point"
    elif num_data_points == 2:
        shape = "line"
    elif num_data_points == 3:
        shape = "triangle"
    elif num_data_points == 4:
        shape = "rectangle"
    elif num_data_points == 5:
        shape = "pentagon"
    elif num_data_points == 6:
        shape = "hexagon"
    elif num_data_points == 7:
        shape = "pentagon"
    elif num_data_points == 8:
        shape = "octagon"
    elif num_data_points == 9:
        shape = "heptagon"
    elif num_data_points == 10:
        shape = "decagon"
    else:
        raise ValueError(f"ERROR: The number of data points: {num_data_points} provided is not in  valid range. Must be between 1 and 10 points")
    
    return shape


#def sendToUI(message):
    # implement code to send message to REST API


def callback(ch, method, properties, body):
    #print(f"Received {body}")
    # convert from byte to string to python dictionary
    message = json.loads(body.decode('utf-8'))
    process(message)


def process(message):
    print(f"Processing new message...")
    if "SENSOR" in message["sensor_id"]:
        try:
            shape = determine_shape(message["data_points"]) # input is type list; output is a string
            # update message dictionary to pass to REST API
            message["shape"] = shape
            print(message)
            #sendToUI(message)
        except ValueError as error:
            print(error)
    else:
        print(f"ERROR: \nSensor ID: {message['sensor_id']} not valid")


queue_name = 'json_data'
rabbitmq = RabbitMQ()
print("Starting RabbitMQ Consumer")
rabbitmq.consume(queue_name, callback)