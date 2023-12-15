import boto3

client = boto3.client('s3')
response = client.list_objects(
    Bucket='hellopy-120',
)

for file in response['Contents']:
    print(file['Key'],file['Size'])