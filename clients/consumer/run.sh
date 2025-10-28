#!/bin/bash

if [[ $(docker ps -a | grep rmq-consumer) ]];then 
	echo "removing current instance of rmq-consumer..."
	docker stop rmq-consumer && docker rm rmq-consumer
	echo "starting new rqm-consumer..."
	docker run  -d --name rmq-consumer rmq-consumer:0.0.1
else
	echo "starting new rqm-consumer..."
        docker run  -d --name rmq-consumer rmq-consumer:0.0.1
fi
