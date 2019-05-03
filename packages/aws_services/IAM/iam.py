import boto3
import botocore

from ...utlities import colored

iam = boto3.client('iam')




def getusers(show):
    try:
        users=iam.list_users()
    except botocore.exceptions.ClientError as e:
                    colored.coloredtext("There was an error while getting user data: \n\n\n")
                    print(e)
    userlist=[]
    
    for user in users['Users']:
        name=user['UserName']
        if show:
            print("> "+name)
        userlist.append({"name":name})
    return userlist

def getgroups(show):
    try:
        groups=iam.list_groups()
    except botocore.exceptions.ClientError as e:
                    colored.coloredtext("There was an error while getting group data: \n\n\n")
                    print(e)
    grouplist=[]
        
    for group in groups['Groups']:
        name=group['GroupName']
        if show:
            print("> "+name)
        grouplist.append({"name":name})

    return grouplist

def getaccesskeys(show):
    try:
        accesskeys=iam.list_access_keys()
    except botocore.exceptions.ClientError as e:
                    colored.coloredtext("There was an error while getting access key data: \n\n\n")
                    print(e)
    accesskeylist=[]
        
    for accesskey in accesskeys['AccessKeyMetadata']:
        name=accesskey['UserName']
        accesskeyid=accesskey['AccessKeyId']
        if show:
            print("> "+name)
        accesskeylist.append({"name":accesskeyid})

    return accesskeylist