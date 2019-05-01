import boto3

s3=boto3.client('s3')

def test_getbuckets():
    bucketlist=[]
    buckets=s3.list_buckets()
    for i in buckets['Buckets']:
        bucket= i['Name']
        
        bucketlist.append(bucket)
    #print(bucketlist)
    assert bucketlist!=[] 
    



