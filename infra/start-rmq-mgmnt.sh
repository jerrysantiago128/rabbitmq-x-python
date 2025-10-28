#!/bin/bash

if [[ $(docker ps -a | grep rabbitMQ) ]]; then
	echo "stopping the running instance of RabbitMQ-server..."
	docker stop rabbitMQ-server && docker rm rabbitMQ-server	
	echo "starting a clean instance of RabbitMQ--server..."
	docker run --name rabbitMQ-server --hostname rabbitMQ-server -p 5672:5672 -p 15672:15672 -d rabbitmq:4.2.0-management
else
	echo "starting an instance of RabbitMQ-server..."
	docker run --name rabbitMQ-server --hostname rabbitMQ-server -p 5672:5672 -p 15672:15672 -d rabbitmq:4.2.0-management
fi

echo "Access the Management Console by opening the browser and naivagting to: \nhttp://localhost:15672"
echo "User Credentials: 'guest:guest'"
