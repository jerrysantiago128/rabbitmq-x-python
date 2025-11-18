from pika.exceptions import AMQPConnectionError
import argparse
from producer import RabbitMQ, generate_data


def parse_arguments():

    parser = argparse.ArgumentParser(
        description="Takes User Input for RabbitMQ Queue Name and Number of random data messages to publish",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        'queue_name',
        type=str,
        help="Name of the Queue to Publish a Message (required)"
    )

    parser.add_argument(
        'num_msg',
        type=int,
        help="Number of messages to publish (required)"
    )

    return parser.parse_args()


def main():

    try:
        # parsing CLI arguments
        args = parse_arguments()

        # validate arguments
        if not args.queue_name:
            raise ValueError(f"Error: Queue Name must not be empty")


        if not args.num_msg or args.num_msg <= 0:
            raise ValueError(f"Error: Number of messages must be positive integer")


        # initialize vars
        queue_name = args.queue_name
        num_msg = args.num_msg
        count = 0
    
    except ValueError as e:
        # Handle cases where argument values are invalid (like num_msg <= 0)
        print(f"Value Error: {e}")
        exit(1)

    rabbitmq = None
    try:
        # initialize connection with RabbitMQ Broker
        print("Attempting to connect to RabbitMQ...")
        rabbitmq = RabbitMQ()
        print("Connection successful. Starting publish loop...")
        

        # main loop
        for count in range(num_msg):

            # generate json data
            message = generate_data.generate_json_data()
            
            # publish message to queue
            rabbitmq.publish(queue_name, message)   
            count += 1
        
        print(f"{num_msg} messages sent successfully!")


    except AMQPConnectionError as e: 
        print(f"Connection Error: Could not connect to the broker. Details: {e}")
        exit(1)

    except Exception as e:
        # Catch any other unexpected errors during execution
        print(f"Error: Unexpected error message: {e}")
        exit(1)

    finally:
        if rabbitmq: 
            print("Closing RabbitMQ Connection...")
            try: 
                rabbitmq.close()
            except Exception as e:
                print(f"Warning: Failed to gracefully clsoe connection. Details: {e}")



if __name__ == "__main__":
    main()