import time
import os

def connect_to_queue():
    """Simulates connecting to a message queue."""
    print("Connecting to message queue...")
    # (e.g., pika.BlockingConnection(...))
    time.sleep(2)
    print("Connection established.")

def on_message(channel, method, properties, body):
    """Callback for when a message is received."""
    print(f"Received message: {body.decode()}")
    # (Process the message, sync to CRM, etc.)
    time.sleep(1)
    print("Message processed and acknowledged.")

def start_worker():
    """Main worker loop."""
    print("Starting novahub-worker-sync...")
    connect_to_queue()
    
    print("Worker is waiting for messages. To exit press CTRL+C")
    # A real worker would use a blocking consume loop
    # (e.g., channel.start_consuming())
    try:
        while True:
            # Simulate receiving a message
            on_message(None, None, None, b'{"project_id": 123, "name": "Test Project"}')
            time.sleep(10)
    except KeyboardInterrupt:
        print("Stopping worker.")

if __name__ == "__main__":
    start_worker()