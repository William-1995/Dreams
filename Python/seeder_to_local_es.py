from elasticsearch import Elasticsearch as ES
import boto3
import os
import json
import asyncio
from boto3.dynamodb.conditions import Key, Attr

def connectAws(region_name):
    aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
    aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
    boto3.session.Session(aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,region_name=region_name)

from queue import Queue
class DynamoDB():
    def __init__(self, tableName, s3Name,queue):
        self.s3Name = s3Name
        self.S3Client = boto3.client('s3')
        self.table = boto3.resource('dynamodb').Table(tableName)
        self.queue = queue

    async def getData(self,logType):
        response = await self.getItem(logType)
        self.queue.put(response)
        return response['Items']

    async def getItem(self,logType):
        return self.table.query(KeyConditionExpression=Key('logType').eq(logType)) 

    def putItemToS3(self,s3Name,item):
        self.S3Client.put_object(Bucket=s3Name,Body=self.dict_to_binary(item), Key=item['id']['S'])

    def dict_to_binary(self, the_dict):
        str = json.dumps(the_dict)
        binary = ' '.join(format(ord(letter), 'b') for letter in str)
        return binary

    def binary_to_dict(self, the_binary):
        jsn = ''.join(chr(int(x, 2)) for x in the_binary.split())
        d = json.loads(jsn)  
        return d

if __name__ == "__main__":
    # connectAws('us-east-1')
    # queue = Queue()
    # db = DynamoDB('ehm-auditlog-qc-upgrade','dynamodb-backup-qc-upgrade-2020-6-29',queue)
    # loop = asyncio.get_event_loop()
    # logTypes = ['Workflow']#['AD Sync after Login','AD Sync All', 'UserAccess','Notification','Workflow', 'Subscription', 'Add Role' , 'Modifying Group','User Login','Add Group']
    # tasks = [db.getData(type) for type in logTypes]
    # results = loop.run_until_complete(asyncio.gather(*tasks))
    # #db.putItemToS3('dynamodb-backup-qc-upgrade-2020-6-29',tasks.result())
    # loop.close()
    # print (results)
    dynamodb  = boto3.resource('dynamodb')
    table = dynamodb.Table('ehm-auditlog-qc-upgrade')
    # response = table.scan()
    response = table.scan(FilterExpression=Attr('logType').contains('Workflow'))
    print (response)