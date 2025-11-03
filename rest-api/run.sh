#!/bin/bash

if [[ $(docker ps -a | grep sensor-api) ]];then 
	echo "removing current instance of sensor-api..."
	docker stop sensor-api && docker rm sensor-api
	echo "starting new sensor-api..."
	docker run -p 8000:8000 -d --name sensor-api sensor-api:0.0.1
else
	echo "starting new sensor-api..."
    docker run -p 8000:8000  -d --name sensor-api sensor-api:0.0.1
fi
