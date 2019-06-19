
"""
This module will be utilized for using the AWS IAM related tasks of the package
"""



import boto3
import botocore


from packages.utlities.colored import coloredtext
from packages.utlities.progressbar import progressbar

iam = boto3.client('iam')




def getusers(show):
    """
    This function is used to get the list of all users in IAM

    """
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
    """
    This function is used to get the list of all Groups in IAM

    """
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
    """
    This function is used to get the list of all accesskeys

    """
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

def getroles(show):
    """
    This function is used to get the list of all roles in IAM

    """
    try:
        roles=iam.list_roles()
    except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while getting user data: \n\n\n")
                    print(e)
    roleslist=[]
    
    for role in roles['Roles']:
        name=role['RoleName']
        if show:
            print("> "+name)
        roleslist.append({"name":name})
    return roleslist


############################ DELETE FUNCTIONS ################################






def deleteuser(user_choices):
    """
    This function is used to delete user by giving/selecting parameters
    """
    progressbar("Deleting user")
    username=user_choices['user'][0]
    try:
        iam.delete_user( UserName=str(username))
        print("\n \n User " +username +" has been deleted \n \n")
    except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while deleting user: \n\n\n")
                    print(e)

def deletegroup(group_choices):
    """
    This function is used to delete group by giving/selecting parameters
    """
    progressbar("Deleting Group")
    groupname=group_choices['group'][0]
    try:
        iam.delete_group( GroupName=str(groupname))
        print("\n \n Group " +groupname +" has been deleted \n \n")
    except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while deleting group: \n\n\n")
                    print(e)
def deleteaccesskey(accesskey_choices):
    """
    This function is used to delete accesskey by giving/selecting parameters
    """
    progressbar("Deleting Access Key")
    accesskeyname=accesskey_choices['accesskey'][0]
    try:
    
        iam.delete_access_key(
        AccessKeyId=str(accesskeyname)
        )
        print("\n \n Accesskey " +accesskeyname +" has been deleted \n \n")
    except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while deleting access key: \n\n\n")
                    print(e)


def deleterole(role_choices):
    """
    This function is used to delete IAM role by giving/selecting parameters
    """
    progressbar("Deleting IAM role")
    rolenames=role_choices['role']
    try:
        for rolename in rolenames:
            iam.delete_role(
            RoleName=str(rolename)
            )
            print("\n \n IAM role " +rolename +" has been deleted \n \n")
    except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while deleting access key: \n\n\n")
                    print(e)

