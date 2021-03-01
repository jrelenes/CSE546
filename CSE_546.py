import logging
import sys

import boto3
from botocore.exceptions import ClientError

import queue_wrapper

logger = logging.getLogger(__name__)
sqs = boto3.resource('sqs')


#image
#png <->bites, add separate atribute for hash id
def send_message(queue, image, message_attributes=None):

    if not message_attributes:
	data = [{
		    'Hash_Id': str(Hash_Id),
		    'Array': msg['image'],

		} 
        
        for Hash_Id, msg in enumerate(image)]
	
    response = queue.send_message(Entries=data)
            
    return response
    
#text
def send_message(queue, message_body, message_attributes=None):

    
    if not message_attributes:
        message_attributes = {}


    response = queue.send_message(
            MessageBody=message_body,
            MessageAttributes=message_attributes)
            
    return response



def receive_messages(queue, max_number, wait_time):
	

    images = queue.receive_messages(
            MessageAttributeNames=['All'],
            MaxNumberOfMessages=max_number,
            WaitTimeSeconds=wait_time
        )
    for msg in images:
            #need to alter to images format in message labeled as message_id and body
            logger.info("Received message: %s: %s", msg.message_id, msg.body)
    
    #returns images
    return images


def main():

if __name__ == '__main__':
    main()
