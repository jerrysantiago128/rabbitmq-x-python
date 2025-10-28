from rabbitmq import RabbitMQ

def callback(ch, method, properties, body):
    print(f"Received {body}")
    onMessage(body)

def onMessage(message):
    print(f"Processing new message...")
    
    # strip out content from json message



queue_name = 'json_data'
rabbitmq = RabbitMQ()
rabbitmq.consume(queue_name, callback)