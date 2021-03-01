import logging
import sys
import boto3
from botocore.exceptions import ClientError
import queue_wrapper
logger = logging.getLogger(__name__)
sqs = boto3.resource('sqs')
QUEUE_SIZE = 0
#image
#png <->bites, add separate atribute for hash id
def send_image(queue, data):
    global QUEUE_SIZE
    response = queue.send_message(
            MessageBody=data)
    QUEUE_SIZE+=1

#receives images and text
def get_image(queue):
    global QUEUE_SIZE
    for message in queue.receive_messages():
        # Print out the body of the message
        #print(message.body)

        # Let the queue know that the message is processed
        message.delete()
        QUEUE_SIZE-=1

def get_size(queue):
	global QUEUE_SIZE
	return QUEUE_SIZE


#str('x10\x06\x00\x00\x00\xfd')
def main():
    queue = queue_wrapper.create_queue('sqs-usage-demo-message-wrapper')
    #hash_id = "b'\\x89PNG\\r\\n\\x1a\\n\\x00\\x00\\x00\\rIHDR\\x00\\x00\\x00\\xc8\\x00\\x00\\x00\\xc8\\x10\\x06\\x00\\x00\\x00\\xfd'"
    image_data = bytearray()
    with open("test.png", "rb") as fp:
        image_data = fp.read()
    print(get_size(queue))
    send_image(queue, str(image_data))
    print(get_size(queue))
    get_image(queue)
    print(get_size(queue))

if __name__ == '__main__':
    main()
