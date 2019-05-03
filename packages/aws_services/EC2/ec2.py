import boto3
import botocore

from ...utlities import colored

ec2 = boto3.client('ec2')


def getinstances(show):
    serverlist=[]
    count=0
    try:
        servers=ec2.describe_instances()
    except botocore.exceptions.ClientError as e:
                    colored.coloredtext("There was an error while getting ec2 instance data: \n\n\n")
                    print(e)
    for reservation in servers['Reservations']:
        for inst in reservation['Instances']:
            count+=1
            name=inst['InstanceId']
            state=inst['State']['Name']
            serverid="server"+str(count)
            if show:
                print("Id: "+name+"      State: "+ state)
            serverlist.append({ "name":name})
    return serverlist

def getsecuritygroups(show):
    securitygrouplist=[]
    count=0
    try:
        securitygroups=ec2.describe_security_groups()
    except botocore.exceptions.ClientError as e:
                    colored.coloredtext("There was an error while getting security group data: \n\n\n")
                    print(e)
    for securitygroup in securitygroups['SecurityGroups']:
        name=securitygroup['GroupName']
        
        gid=securitygroup['GroupId']
        description=securitygroup['Description']
        if show:
            print("name: "+name+"      Descripton: "+ description)
        securitygrouplist.append({ "name":gid})
    return securitygrouplist

def getkeypairs(show):
    keypairlist=[]
    count=0
    try:
        keypairs=ec2.describe_key_pairs()
    except botocore.exceptions.ClientError as e:
                    colored.coloredtext("There was an error while getting keypair data: \n\n\n")
                    print(e)
    for keypair in keypairs['KeyPairs']:
        name=keypair['KeyName']
        
        if show:
            print("name: "+name)
        keypairlist.append({ "name":name})
    return keypairlist

def getvpcs(show):
    vpclist=[]
    count=0
    try:
        vpcs=ec2.describe_vpcs()
    except botocore.exceptions.ClientError as e:
                    colored.coloredtext("There was an error while getting vpc data: \n\n\n")
                    print(e)
    for vpc in vpcs['Vpcs']:
        name=vpc['VpcId']
        cidr=vpc['CidrBlock']
        if show:
            print("VPC Id:  "+name+"           CIDR: "+cidr)
        vpclist.append({ "name":name})
    return vpclist