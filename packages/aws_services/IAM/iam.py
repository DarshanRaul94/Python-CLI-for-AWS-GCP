import boto3
import botocore


from ...utlities.colored import coloredtext
from ...utlities.progressbar import progressbar

iam = boto3.client('iam')




def getusers(show):
    try:
        users=iam.list_users()
    except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while getting user data: \n\n\n")
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
                    coloredtext("There was an error while getting group data: \n\n\n")
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
                    coloredtext("There was an error while getting access key data: \n\n\n")
                    print(e)
    accesskeylist=[]
        
    for accesskey in accesskeys['AccessKeyMetadata']:
        name=accesskey['UserName']
        accesskeyid=accesskey['AccessKeyId']
        if show:
            print("> "+name)
        accesskeylist.append({"name":accesskeyid})

    return accesskeylist




############################ DELETE FUNCTIONS ################################






def deleteuser(user_choices):
    #print("deleting user")
    progressbar("Deleting user")
    username=user_choices['user'][0]
    try:
        iam.delete_user( UserName=str(username))
        print("\n \n User " +username +" has been deleted \n \n")
    except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while deleting user: \n\n\n")
                    print(e)

def deletegroup(group_choices):
    #print("deleting group")
    progressbar("Deleting Group")
    groupname=group_choices['group'][0]
    try:
        iam.delete_group( GroupName=str(groupname))
        print("\n \n Group " +groupname +" has been deleted \n \n")
    except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while deleting group: \n\n\n")
                    print(e)
