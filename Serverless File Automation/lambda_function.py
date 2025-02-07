import os
import boto3
import csv

# Initialize AWS clients
s3_client = boto3.client('s3')
ses_client = boto3.client('ses')
sns_client = boto3.client('sns')

# Environment variables (make sure these are set in your Lambda environment or local .env file)
SES_SENDER_EMAIL = os.environ.get('SES_SENDER_EMAIL', 'your-sender-email@example.com')
SNS_TOPIC_ARN = os.environ.get('SNS_TOPIC_ARN', 'your-sns-topic-arn')

def lambda_handler(event, context):
    try:
        # Step 1: Get the uploaded file information
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        object_key = event['Records'][0]['s3']['object']['key']

        # Step 2: Download the CSV file
        local_file_path = f'/tmp/{object_key}'
        print(f"Downloading {object_key} from bucket {bucket_name} to {local_file_path}")
        s3_client.download_file(bucket_name, object_key, local_file_path)

        # Step 3: Parse the CSV file
        with open(local_file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                recipient = row['Email']
                name = row['Name']
                # Step 4: Send email using SES
                print(f"Sending email to {recipient}...")
                send_email(recipient, name)

        # Step 5: Send SNS summary notification
        message = f"Emails sent successfully to recipients from {object_key}."
        sns_client.publish(TopicArn=SNS_TOPIC_ARN, Message=message)
        print("SNS summary notification sent successfully.")

        return {"statusCode": 200, "body": "Process completed successfully"}

    except Exception as e:
        print(f"Error: {e}")
        return {"statusCode": 500, "body": f"Error: {str(e)}"}

def send_email(recipient, name):
    subject = "Hello from AWS SES"
    body = f"Dear {name},\n\nThis is a test email sent from AWS Lambda and SES.\n\nRegards,\nYour Cloud App"
    ses_client.send_email(
        Source=SES_SENDER_EMAIL,
        Destination={"ToAddresses": [recipient]},
        Message={
            "Subject": {"Data": subject},
            "Body": {"Text": {"Data": body}},
        }
    )
    print(f"Email sent to {recipient}.")
