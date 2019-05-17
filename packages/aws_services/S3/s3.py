
"""
This module will be utilized for using the AWS S3 related tasks of the package
"""

import boto3
import botocore

from packages.utlities.colored import coloredtext
from packages.utlities.progressbar import progressbar



s3 = boto3.client('s3')

def getbuckets(show):
    """
    This function is used to get the list of all buckets in S3

    """
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
    """
    This function is used to delete the bucket/s in S3

    """
    progressbar("Deleting Bucket")
    
    bucketname=bucket_choices['bucket'][0]
    try:
        s3.delete_bucket(  Bucket=str(bucketname))
        print("\n \n Bucket " +bucketname +" has been deleted \n \n")
    except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while deleting Bucket: \n\n\n")
                    print(e)       

def listobjects(bucket_choices):
    """
    This function is used to list the objects in a bucket

    """
    
    
    bucketname=bucket_choices['bucket'][0]
    try:
        objects=s3.list_objects(Bucket=str(bucketname))
        
    except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while deleting Bucket: \n\n\n")
                    print(e) 
    print("\n\n These are the objects in the bucket: "+ bucketname+"\n\n")
    for i in objects['Contents']:
        object= i['Key']
        
        print("> " +object)