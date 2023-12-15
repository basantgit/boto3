import boto3

client = boto3.client('ec2')
response = client.describe_volumes(
    Filters=[
        {
            'Name': 'status',
            'Values': [
                'in-use',
            ]
        },
    ],
    
)
for volume in response['Volumes']:
    print(volume['VolumeId'],volume['Size'])