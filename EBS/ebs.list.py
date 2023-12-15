import boto3

client = boto3.client('ebs')
response = client.start_snapshot(
    VolumeSize=10,    
)

print(response)