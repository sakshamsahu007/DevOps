'''
client = boto3.client('lambda')

response = client.add_permission(
    Action='lambda:InvokeFunction',
    FunctionName='my-function',
    Principal='s3.amazonaws.com',
    SourceAccount='123456789012',
    SourceArn='arn:aws:s3:::my-bucket-1xpuxmplzrlbh/*',
    StatementId='s3',
)

print(response)


import json
import boto3

# boto3 S3 initialization
s3_client = boto3.client("s3")


def lambda_handler(event, context):
   destination_bucket_name = 'destination-test-bucket-006'

   # event contains all information about uploaded object
   print("Event :", event)

   # Bucket Name where file was uploaded
   source_bucket_name = event['Records'][0]['s3']['bucket']['name']

   # Filename of object (with path)
   file_key_name = event['Records'][0]['s3']['object']['key']

   # Copy Source Object
   copy_source_object = {'Bucket': source_bucket_name, 'Key': file_key_name}

   # S3 copy object operation
   s3_client.copy_object(CopySource=copy_source_object, Bucket=destination_bucket_name, Key=file_key_name)

   return {
       'statusCode': 200,
       'body': json.dumps('Hello from S3 events Lambda!')
   }
'''

import boto3



#s3_client = boto3.client("s3")
#response = s3_client.get_object(Bucket='sakshamtest', Key='files.zip')
#package_content = response['Body'].read()

client=boto3.client('lambda')

response = client.update_function_code(
    FunctionName='testlambda',
    #ZipFile=package_content,
    S3Bucket='sakshamtest',
    S3Key='files.zip',
    #S3ObjectVersion='string',
    #Publish=True|False,
    #DryRun=True|False,
    #RevisionId='string'
)   

print(response)