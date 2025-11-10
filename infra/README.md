# RabbitMQ

RabbitMQ is a powerful, enterprise grade open source messaging and streaming broker that enables efficient, reliable and versatile communication for applications — perfect for distributed microservices, real-time data, and IoT.

https://www.rabbitmq.com/

Default Credentials: guest:guest

## Assumptions

Docker is installed on your machine

## Usage
### Docker

#### Pull the Image
 
Simply run the command below to pull to RabbitMQ image locally:

    docker pull rabbitmq:4.2.0-managment

More images can be found at the link below:
    
    https://hub.docker.com/_/rabbitmq/tags

#### Start the service

    docker run --name rabbitMQ-server --hostname rabbitMQ-server -p 5672:5672 -p 15672:15672 -d rabbitmq:4.2.0-management

#### Access the Webpage

    http://localhost:15672

## Connectivity

Protocols (TCP):
- AMQP 0-9-1
- AMQP 1.0

Ports: 
    - AMQP: 5672
    - HTTP API: 15672

## Security

N/A in this deployment

## Other Considerations

N/A in this deployment