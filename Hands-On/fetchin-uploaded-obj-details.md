# Fetching Uploaded Object details from S3 Bucket using Lambda

AWS Lambda function that retrieves the name of an object that was added to an S3 bucket using an S3 trigger, you can use the following code. This function will extract the bucket name and object key (i.e., the file name) from the event passed to the Lambda function.

``` python
import json

def lambda_handler(event, context):
    # The event contains information about the S3 event, such as the bucket and object key (name).
    
    # Retrieve bucket name and object key from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    
    # Log or process the bucket name and object key
    print(f"New object added in bucket: {bucket_name}")
    print(f"Object key (name): {object_key}")
    
    # You can perform additional operations here if needed
    
    # Return response
    return {
        'statusCode': 200,
        'body': json.dumps(f"New object added: {object_key} in bucket {bucket_name}")
    }

```


`event['Records'][0]['s3']['bucket']['name']:` This extracts the name of the S3 bucket where the object was uploaded.

`event['Records'][0]['s3']['object']['key']:` This retrieves the key (file name) of the object that was uploaded to the bucket.

`print(f"..."):` Logs the bucket name and object key to CloudWatch Logs for debugging purposes.

