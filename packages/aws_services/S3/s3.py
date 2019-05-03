
"""
This module will be utilized for using the AWS S3 related tasks of the package
"""

import boto3
import botocore

from ...utlities import colored

s3 = boto3.client('s3')

def getbuckets(show):
    bucketlist=[]
    try:
        buckets=s3.list_buckets()
    except botocore.exceptions.ClientError as e:
                    colored.coloredtext("There was an error while getting bucket data: \n\n\n")
                    print(e)
    for i in buckets['Buckets']:
        bucket= i['Name']
        if show:
            print("> " +bucket)
        bucketlist.append({'name':bucket})
    #print(bucketlist)
    return bucketlist

