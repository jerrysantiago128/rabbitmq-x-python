# RabbitMQ-X-Python 

## Purpose
This project exists to experiment with rabbitMQ configuration, deployment and client connectivity for producing and consuming various message types to then perform standard ETL
processes.

### Tech Stack
Docker/Docker Compose
Python/Pip
Bash Scripting
RabbitMQ

## Project Organization

#### docs
- markdown files to track resources and other documentation for the project
#### clients
- producer: code and scripts to create a containerized RabbitMQ producer via Python to send data to a given RabbitMQ queue.
- consumer: code and scripts to create a containerized RabbitMQ consumer via Python to ingest data and perform ETL on said data.
#### infra
- code and scripts to spin up and maintain RabbitMQ via Docker