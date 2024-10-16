# AWS Lambda with Python

### To trigger an AWS Lambda function when an upload occurs in an S3 bucket and send a notification email using Gmail, you'll need to follow these steps:

1. Set Up an S3 Bucket
2. Create an AWS Lambda Function
3. Add an S3 Trigger to the Lambda Function
4. Send Email Using Gmail SMTP in the Lambda Function
5. Configure IAM Permissions
6. Deploy and Test

### Step 1: Set Up an S3 Bucket
- Follow the prompts to configure the bucket (name, region, etc.).
### Step 2: Create an AWS Lambda Function
- Go to the AWS Lambda Console.
- Click on Create function.
- Choose Author from scratch.
- Give your function a name (e.g., S3UploadNotification).
Select a runtime (Python 3.x).
- Choose or create an execution role that has the necessary permissions (more on this later).
- Click on Create function.
### Step 3: Add an S3 Trigger to the Lambda Function
- In the Lambda function's configuration page, scroll down to the Function overview section.
- Click on Add trigger.
- Choose S3 as the trigger.
- Select the bucket you created in Step 1.
- Choose the event type (e.g., PUT for uploads).
- Optionally, you can specify a prefix or suffix for the files that trigger the Lambda function.
- Click on Add.
### Step 4: Send Email Using Gmail SMTP in the Lambda Function
Here's a basic example of how to send an email using Gmail's SMTP server from within your Lambda function.

``` python
import json
import smtplib
import ssl
import os

def lambda_handler(event, context):
    # Set up Gmail SMTP server
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = os.environ['GMAIL_USER']  # Replace with your email
    sender_password = os.environ['GMAIL_PASSWORD']  # Replace with your email password

    # Extract bucket name and object key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    subject = "New File Uploaded"
    body = f"A new file has been uploaded to your S3 bucket:\n\nBucket: {bucket}\nKey: {key}"

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Send email
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)  # Secure the connection
            server.ehlo()  # Can be omitted
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, sender_email, f"Subject: {subject}\n\n{body}")
            print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

    return {
        'statusCode': 200,
        'body': json.dumps('Email notification sent!')
    }
```

#### Set Environment Variables
- In the AWS Lambda console, go to the Configuration tab.
- Under Environment variables, add the following:
`GMAIL_USER:` Your Gmail email address.
`GMAIL_PASSWORD:` Your Gmail password (or an App Password if you have 2FA enabled).

##### Note: If you have 2-Step Verification enabled on your Google account, you will need to create an App Password instead of using your regular Gmail password. You can do this from your Google Account settings under "Security" > "App passwords".

### Step 5: Configure IAM Permissions
Ensure your Lambda function's execution role has the necessary permissions to access the S3 bucket:

1. Go to the IAM console.
2. Find the role associated with your Lambda function.
3. Attach the following policy (or customize as needed):

``` json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME/*"
        }
    ]
}
```

### Step 6: Deploy and Test
- Deploy your Lambda function.
- Upload a file to the S3 bucket that you configured.
- Check your email for the notification.
