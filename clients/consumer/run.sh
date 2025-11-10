#!/bin/bash
ENV_FILE=.env

if [[ $(docker ps -a | grep rmq-consumer) ]];then 
	echo "removing current instance of rmq-consumer..."
	docker stop rmq-consumer && docker rm rmq-consumer
	echo "starting new rmq-consumer..."
	if [ -f "$ENV_FILE" ]; then
		docker run  -d --env-file $ENV_FILE --name rmq-consumer rmq-consumer:0.0.1
	else
		docker run  -d --name rmq-consumer rmq-consumer:0.0.1
	fi
else
	echo "starting new rmq-consumer..."
	if [ -f "$ENV_FILE" ]; then
		docker run  -d --env-file $ENV_FILE --name rmq-consumer rmq-consumer:0.0.1
	else
    	docker run  -d --name rmq-consumer rmq-consumer:0.0.1
	fi
fi
