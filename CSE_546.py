import logging
import sys
import boto3
from botocore.exceptions import ClientError
import queue_wrapper
logger = logging.getLogger(__name__)
sqs = boto3.resource('sqs')
#image
#png <->bites, add separate atribute for hash id
def send_message_image(queue, data):
    response = queue.send_message(
            MessageBody=data)

#receives images and text
def receive_messages(queue):
    for message in queue.receive_messages():
        # Print out the body of the message
        print(message.body)

        # Let the queue know that the message is processed
        message.delete()

#str('x10\x06\x00\x00\x00\xfd')
def main():
    queue = queue_wrapper.create_queue('sqs-usage-demo-message-wrapper')
    #hash_id = "b'\\x89PNG\\r\\n\\x1a\\n\\x00\\x00\\x00\\rIHDR\\x00\\x00\\x00\\xc8\\x00\\x00\\x00\\xc8\\x10\\x06\\x00\\x00\\x00\\xfd'"
    image_data = bytearray()
    with open("test.png", "rb") as fp:
        image_data = fp.read()

    print(image_data)
    send_message_image(queue, str(image_data))
    receive_messages(queue)

if __name__ == '__main__':
    main()
