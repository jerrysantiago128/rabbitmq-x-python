from pika.exceptions import AMQPConnectionError
import argparse
from  consumer import RabbitMQ, callback

def parse_arguments():

    parser = argparse.ArgumentParser(
        description="Takes User Input for RabbitMQ Queue Name",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        'queue_name',
        type=str,
        help="Name of the Queue to Consume a Message (required)"
    )

    return parser.parse_args()


def main():

    try:
        # parsing CLI arguments
        args = parse_arguments()

        # validate arguments
        if not args.queue_name:
            raise ValueError(f"Error: Queue Name must not be empty")

    
    
        # initialize vars
        queue_name = args.queue_name
    
    except ValueError as e:
        # Handle cases where argument values are invalid (like num_msg <= 0)
        print(f"Value Error: {e}")
        exit(1)

    rabbitmq = None
    try:
        # initialize connection with RabbitMQ Broker
        print("Attempting to connect to RabbitMQ...")
        rabbitmq = RabbitMQ()
        print(f"Connection successful. Starting consumer for queue: {queue_name}")
        

        rabbitmq.consume(queue_name, callback)


    except AMQPConnectionError as e: 
        print(f"Connection Error: Could not connect to the broker. Details: {e}")
        exit(1)

    except Exception as e:
        # Catch any other unexpected errors during execution
        print(f"Error: Unexpected error message: {e}")
        exit(1)

    # finally:
    #     if rabbitmq: 
    #         print("Closing RabbitMQ Connection...")
    #         try: 
    #             rabbitmq.close()
    #         except Exception as e:
    #             print(f"Warning: Failed to gracefully clsoe connection. Details: {e}")



if __name__ == "__main__":
    main()