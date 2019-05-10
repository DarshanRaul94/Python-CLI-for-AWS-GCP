
"""
This module will be utilized for using the AWS EC2 related tasks of the package
"""



import boto3
import botocore

from packages.utlities.colored import coloredtext
from packages.utlities.progressbar import progressbar


ec2 = boto3.client('ec2')


def getinstances(show):
    """
    This function is used to get the list of all the instances in EC2 in that region

    """
    serverlist=[]
    count=0
    try:
        servers=ec2.describe_instances()
    except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while getting ec2 instance data: \n\n\n")
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
    """
    This function is used to get the list of all the Security Groups in that region

    """
    securitygrouplist=[]
    
    try:
        securitygroups=ec2.describe_security_groups()
    except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while getting security group data: \n\n\n")
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
    """
    This function is used to get the list of all the keypairs in EC2 in that region

    """
    keypairlist=[]
    
    try:
        keypairs=ec2.describe_key_pairs()
    except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while getting keypair data: \n\n\n")
                    print(e)
    for keypair in keypairs['KeyPairs']:
        name=keypair['KeyName']
        
        if show:
            print("name: "+name)
        keypairlist.append({ "name":name})
    return keypairlist

def getvpcs(show):
    """
    This function is used to get the list of all the VPC's in that region

    """
    vpclist=[]
    
    try:
        vpcs=ec2.describe_vpcs()
    except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while getting vpc data: \n\n\n")
                    print(e)
    for vpc in vpcs['Vpcs']:
        name=vpc['VpcId']
        cidr=vpc['CidrBlock']
        if show:
            print("VPC Id:  "+name+"           CIDR: "+cidr)
        vpclist.append({ "name":name})
    return vpclist







def startinstance(instance_choices):
    """
    This function is used to start instances by giving/selecting parameters
    """
    progressbar(" Starting Instance")
    instancename=instance_choices['instance'][0]
    try:
        
        ec2.start_instances( InstanceIds=[
            str(instancename),
        ])
        print("\n \n Instance " +instancename +" has been started \n \n")
    except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while starting instance: \n\n\n")
                    print(e)    

def stopinstance(instance_choices):
    """
    This function is used to stop instances by giving/selecting parameters
    """
    #print("Stopping Instance")
    progressbar("Stopping Instances")
    instancename=instance_choices['instance'][0]
    try:  
        ec2.stop_instances( InstanceIds=[
            str(instancename),
        ])
        print("\n \n Instance " +instancename +" has been stopped \n \n")
    except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while stopping instance: \n\n\n")
                    print(e)

def terminateinstance(instance_choices):
    """
    This function is used to terminate instances by giving/selecting parameters
    """
    #print("Terminating Instance")
    progressbar("Terminating Instance")
    instancename=instance_choices['instance'][0]
    try:
        ec2.terminate_instances( InstanceIds=[
            str(instancename),
        ])
        print("\n \n Instance " +instancename +" has been terminated \n \n")
    except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while terminating instance: \n\n\n")
                    print(e) 


def deletekeypair(keypair_choices):
    """
    This function is used to delete keypair by giving/selecting parameters
    """
    #print("deleting keypair")
    progressbar("Deleting Keypair")
    keypairname=keypair_choices['keypair'][0]
    try:
        ec2.delete_key_pair(KeyName=str(keypairname))
        print("\n \n Keypair " +keypairname +" has been deleted \n \n")
    except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while deleting keypair: \n\n\n")
                    print(e)    


def deletevpc(vpc_choices):
    """
    This function is used to delete vpc by giving/selecting parameters
    """
    progressbar("Deleting VPC")
    vpcname=vpc_choices['vpc'][0]
    try:
        ec2.delete_vpc(VpcId=str(vpcname))
        print("\n \n vpc " +vpcname +" has been deleted \n \n")
    except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while deleting vpc: \n\n\n")
                    print(e)    

def deletesecuritygroup(securitygroup_choices):
    """
    This function is used to delete security group by giving/selecting parameters
    """
    progressbar("Deleting Security Group")
    securitygroupname=securitygroup_choices['securitygroup'][0]
    try:

        print("\n \n securitygroup " +securitygroupname +" has been deleted \n \n")
        ec2.delete_security_group(GroupId=str(securitygroupname))
    except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while deleting security group: \n\n\n")
                    print(e)    

