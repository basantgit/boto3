import boto3

client = boto3.client('s3')
client.upload_file('hello', 'hellopy-120', 'hello')