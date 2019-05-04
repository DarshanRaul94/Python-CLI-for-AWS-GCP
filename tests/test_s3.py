import boto3
import botocore
import pytest
#from moto import mock_s3
s3 = boto3.client('s3')

bucketname='testingforpytest'
def test_createbucket():
    try:
        s3.create_bucket(Bucket=str(bucketname), CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})
        assert True
    except botocore.exceptions.ClientError as e:
        assert False
        



def test_getbuckets():
    
    bucketlist=[]
    buckets=s3.list_buckets()
    
    for i in buckets['Buckets']:
        bucket= i['Name']
        bucketlist.append({'name':bucket})
    #print(bucketlist)
    assert bucketlist!=[]



@pytest.mark.parametrize("input,expected", [
    (bucketname, True)
])
def test_deletebucket(input, expected):

    bucketname=str(input)
    s3.delete_bucket(  Bucket=str(bucketname))
    
    try:
        s3.delete_bucket(  Bucket=str(bucketname))
        assert expected
    except botocore.exceptions.ClientError as e:
        assert False
                    


