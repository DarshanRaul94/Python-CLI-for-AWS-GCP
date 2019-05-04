
import boto3
import botocore
import pytest

iam = boto3.client('iam')




def test_getusers():
    
    users=iam.list_users()
    userlist=[]
    
    for user in users['Users']:
        name=user['UserName']
        userlist.append({"name":name})
    assert userlist!=[]