import boto3
import botocore
#from moto import mock_s3
s3 = boto3.client('s3')

def test_createbucket():
    try:
        s3.create_bucket(Bucket='testingforpytest', CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})
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

# def deletebucket():

#     bucketname=bucket_choices['bucket'][0]
#     try:
#         s3.delete_bucket(  Bucket=str(bucketname))
#         print("\n \n Bucket " +bucketname +" has been deleted \n \n")
#     except botocore.exceptions.ClientError as e:
#                     coloredtext("There was an error while deleting Bucket: \n\n\n")
#                     print(e) 


