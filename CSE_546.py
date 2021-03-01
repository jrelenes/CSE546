import logging
import sys
import boto3
from botocore.exceptions import ClientError
import queue_wrapper
logger = logging.getLogger(__name__)
sqs = boto3.resource('sqs')
#image
#png <->bites, add separate atribute for hash id
#def send_message(queue, image, hash_id, message_attributes=None):


#    response = queue.send_message(
#            Image=image,
#            Hash_Id=hash_id)

#text
def send_message(queue, hash_id):
    response = queue.send_message(
            MessageBody=hash_id)

#receives images and text
def receive_messages(queue):
    for message in queue.receive_messages():
        # Print out the body of the message
        print('{0}'.format(message.body))

        # Let the queue know that the message is processed
        message.delete()

#str('x10\x06\x00\x00\x00\xfd')
def main():
    queue = queue_wrapper.create_queue('sqs-usage-demo-message-wrapper')
    hash_id = "b'\\x89PNG\\r\\n\\x1a\\n\\x00\\x00\\x00\\rIHDR\\x00\\x00\\x00\\xc8\\x00\\x00\\x00\\xc8\\x10\\x06\\x00\\x00\\x00\\xfd'"
    send_message(queue, hash_id)
    receive_messages(queue)

if __name__ == '__main__':
    main()
