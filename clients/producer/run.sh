#!/bin/bash
ENV_FILE=.env

if [[ $(docker ps -a | grep rmq-producer) ]];then 
	echo "removing current instance of rmq-producer..."
	docker stop rmq-producer && docker rm rmq-producer
	echo "starting new rmq-producer..."
	if [ -f "$ENV_FILE" ]; then
		docker run  -d --env-file $ENV_FILE --name rmq-producer rmq-producer:0.0.1
	else
		docker run  -d --name rmq-producer rmq-producer:0.0.1
	fi
else
	echo "starting new rmq-producer..."
	if [ -f "$ENV_FILE" ]; then
		docker run  -d --env-file $ENV_FILE --name rmq-producer rmq-producer:0.0.1
	else
    	docker run  -d --name rmq-producer rmq-producer:0.0.1
	fi
fi
