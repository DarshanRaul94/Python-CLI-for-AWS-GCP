
"""
This module will be utilized for using the AWS S3 related tasks of the package
"""

import boto3
import botocore

from ...utlities.colored import coloredtext
from ...utlities.progressbar import progressbar
s3 = boto3.client('s3')

def getbuckets(show):
    bucketlist=[]
    try:
        buckets=s3.list_buckets()
    except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while getting bucket data: \n\n\n")
                    print(e)
    for i in buckets['Buckets']:
        bucket= i['Name']
        if show:
            print("> " +bucket)
        bucketlist.append({'name':bucket})
    #print(bucketlist)
    return bucketlist

def deletebucket(bucket_choices):
    #print("deleting bucket")
    progressbar("Deleting Bucket")
    
    bucketname=bucket_choices['bucket'][0]
    try:
        s3.delete_bucket(  Bucket=str(bucketname))
        print("\n \n Bucket " +bucketname +" has been deleted \n \n")
    except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while deleting Bucket: \n\n\n")
                    print(e)       

