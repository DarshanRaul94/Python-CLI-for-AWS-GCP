import boto3
import pytest
s3=boto3.client('s3')
@pytest.mark.xfail
def test_getbuckets():
    bucketlist=[]
    buckets=s3.list_buckets()
    for i in buckets['Buckets']:
        bucket= i['Name']
        bucketlist.append(bucket)
    #print(bucketlist)
    assert bucketlist!=[] 
    

def test_getbuckets():
    bucketlist=[]
    buckets=s3.list_buckets()
    for i in buckets['Buckets']:
        bucket= i['Name']
        
        bucketlist.append(bucket)
    #print(bucketlist)
    assert bucketlist!=[] 


