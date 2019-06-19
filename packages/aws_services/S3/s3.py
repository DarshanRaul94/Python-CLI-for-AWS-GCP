
"""
This module will be utilized for using the AWS S3 related tasks of the package
"""

import boto3
import botocore
import os
from packages.utlities.colored import coloredtext
from packages.utlities.progressbar import progressbar



s3 = boto3.client('s3')
s3r = boto3.resource('s3')

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
    
    bucketnames=bucket_choices['bucket']
    try:
        for bucketname in bucketnames:
            s3.delete_bucket(  Bucket=str(bucketname))
            print("\n \n Bucket " +bucketname +" has been deleted \n \n")
    except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while deleting Bucket: \n\n\n")
                    print(e)       
def deleteobject(bucket_choices,object_choices):
    """
    This function is used to delete the objects/s in S3

    """
    progressbar("Deleting Object")
    bucketname=bucket_choices['bucket'][0]
    objectnames=object_choices['object']
    try:
        for objectname in objectnames:
            s3.delete_object(
            Bucket=str(bucketname),
            Key=str(objectname))
            print("\n \n Object " +objectname +" has been deleted \n \n")
    except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while deleting object: \n\n\n")
                    print(e) 
    

def listobjects(bucket_choices):
    """
    This function is used to list the objects in a bucket

    """
    
    objectlist=[]
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
        objectlist.append({'name':object})
    return objectlist

def download_object(bucket_choices,object_choices):
    ### ERROR : Getting file not found error
    
    progressbar("Downloading Object")
    bucketname=bucket_choices['bucket'][0]
    objectnames=object_choices['object']
    try:
        for objectname in objectnames:
            print(objectname)
            
            s3r.Bucket(str(bucketname)).download_file(str(objectname), objectname)
            #s3r.meta.client.download_file(str(bucketname), str(objectname), '~/')
            
            print("\n \n Object " +objectname +" has been downloaded \n \n")
    except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while deleting object: \n\n\n")
                    print(e) 
    