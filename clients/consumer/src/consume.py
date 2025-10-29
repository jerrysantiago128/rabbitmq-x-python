from rabbitmq import RabbitMQ
import json

def callback(ch, method, properties, body):
    print(f"Received {body}")
    
    # convert from byte to string to python dictionary
    message = json.loads(body.decode('utf-8'))
    onMessage(message)

def onMessage(message):
    print(f"Processing new message...")
    for key in message:
        if message[key].find('SENSOR'):
            # do something
        #print(key, ":", message[key])
        # print(type(message[key]))
    # strip out content from json message



queue_name = 'json_data'
rabbitmq = RabbitMQ()
print("Starting RabbitMQ Consumer")
rabbitmq.consume(queue_name, callback)