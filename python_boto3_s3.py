 import boto3

# Create an S3 client
s3_client = boto3.client('s3')

# Define the bucket name and file paths
bucket_name = 'your-bucket-name'
local_file_path = '/path/to/local/file.txt'
s3_key = 'path/in/s3/file.txt'

# Upload a file to S3
s3_client.upload_file(local_file_path, bucket_name, s3_key)
print('File uploaded to S3')

# Download the file from S3
download_path = '/path/to/downloaded/file.txt'
s3_client.download_file(bucket_name, s3_key, download_path)
print('File downloaded from S3')
