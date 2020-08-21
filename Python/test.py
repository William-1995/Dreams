import boto3
import time

s3 = boto3.resource('s3')

if __name__ == '__main__':
    print ("Start : %s" % time.ctime())
    time.sleep(10)
    print ("End : %s" % time.ctime())
