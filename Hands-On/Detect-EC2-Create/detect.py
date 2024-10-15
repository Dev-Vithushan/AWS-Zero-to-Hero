import boto3
import json

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    

    user = event['detail']['userIdentity']['userName']
    instanceID = event['details']['responseElements']['instanceSet']['item'][0]['instanceId']

    ec2.create_tags(
        
    ) 


 