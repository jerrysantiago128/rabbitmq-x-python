from rabbitmq import RabbitMQ
import generate_data
import time

rabbitmq = RabbitMQ()

count = 0
queue_name = 'json_data'

while count < 10:
    # generate json data
    message = generate_data.generate_json_data()
    
    # publish message to queue
    rabbitmq.publish(queue_name, message)   

    # print out message
    # print(f"Sent message: {message}")
     # increment
    count += 1
    #time.sleep(1)

rabbitmq.close()