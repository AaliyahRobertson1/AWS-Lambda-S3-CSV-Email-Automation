# AWS Lambda and S3 CSV Email Automation
![AWS Lambda and S3 CSV Email Automation](https://github.com/user-attachments/assets/754754ec-7109-49c3-a9cc-b3cedc022ab0)

This project automates the processing of CSV files uploaded to an Amazon S3 bucket using an AWS Lambda function. It extracts recipient details from the CSV and sends personalized emails via Amazon Simple Email Service (SES). After processing, it sends a summary notification via Amazon SNS.

## Features
✅ Automatically triggers AWS Lambda when a CSV file is uploaded to S3  
✅ Reads recipient details (name, email) from the CSV file  
✅ Sends personalized emails via AWS SES  
✅ Sends a summary notification via AWS SNS  

## Architecture Overview
- **S3 Bucket**: Stores the uploaded CSV files  
- **Lambda Function**: Processes CSV files and triggers email notifications  
- **SES**: Sends emails to recipients  
- **SNS**: Sends a summary notification after processing  

## Prerequisites
- AWS account with **S3, Lambda, SES, and SNS** permissions  
- AWS CLI installed and configured  
- Verified **SES sender email**  
- A sample CSV file  


