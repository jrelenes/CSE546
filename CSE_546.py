import logging
import sys

import boto3
from botocore.exceptions import ClientError

import queue_wrapper

logger = logging.getLogger(__name__)
sqs = boto3.resource('sqs')


def send_message(queue, message_body, message_attributes=None):
    
    if not message_attributes:
        message_attributes = {}


    response = queue.send_message(
            MessageBody=message_body,
            MessageAttributes=message_attributes)
            
    return response


def send_messages(queue, images):
    

    	#need to change this to image format and send images as entries
    	#break into small pieces to pass to server the format is binary
        entries = [{
            'Id': str(ind),
            'MessageBody': msg['body'],
            'MessageAttributes': msg['attributes']
        } 
        
        
        
        
        for ind, msg in enumerate(images)]
        response = queue.send_messages(Entries=entries)
        if 'Successful' in response:
            for msg_meta in response['Successful']:
                logger.info(
                    "Message sent: %s: %s",
                    msg_meta['MessageId'],
                    images[int(msg_meta['Id'])]['body'])
                    
                    
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
