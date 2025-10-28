#!/bin/bash

if [[ $(docker ps -a | grep rmq-producer) ]];then 
	echo "removing current instance of rmq-producer..."
	docker stop rmq-producer && docker rm rmq-producer
	echo "starting new rqm-producer..."
	docker run  -d --name rmq-producer rmq-producer:0.0.1
else
	echo "starting new rqm-producer..."
        docker run  -d --name rmq-producer rmq-producer:0.0.1
fi
