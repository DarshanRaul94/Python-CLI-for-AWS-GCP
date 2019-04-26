

from __future__ import print_function, unicode_literals

from pprint import pprint

from PyInquirer import style_from_dict, Token, prompt, Separator

from examples import custom_style_2

from pyfiglet import Figlet
import boto3
from time import sleep
import sys

s3 = boto3.client('s3')
iam = boto3.client('iam')
ec2 = boto3.client('ec2')
f = Figlet(font='big')
def progressbar():
    for i in range(21):
        sys.stdout.write('\r')
        # the exact output you're looking for:
        sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
        sys.stdout.flush()
        sleep(0.05)

 ##########################getters#########################   
 # s3    
def getbuckets():
    bucketlist=[]
    buckets=s3.list_buckets()
    for i in buckets['Buckets']:
        bucket= i['Name']
        print("> " +bucket)
        bucketlist.append({'name':bucket})
    #print(bucketlist)
    return bucketlist


# iam
def getusers():
    users=iam.list_users()
    userlist=[]
    
    for user in users['Users']:
        name=user['UserName']
        print("> "+name)
        userlist.append({"name":name})
    return userlist

def getgroups():
    groups=iam.list_groups()
    grouplist=[]
        
    for group in groups['Groups']:
        name=group['GroupName']
        print("> "+name)
        grouplist.append({"name":name})

    return grouplist

# ec2
def getinstances():
    serverlist=[]
    count=0
    servers=ec2.describe_instances()
    for reservation in servers['Reservations']:
        for inst in reservation['Instances']:
            count+=1
            name=inst['InstanceId']
            state=inst['State']['Name']
            serverid="server"+str(count)
            print("Id: "+name+"      State: "+ state)
            serverlist.append({ "name":name})
    return serverlist

def getsecuritygroups():
    securitygrouplist=[]
    count=0
    securitygroups=ec2.describe_security_groups()
    for securitygroup in securitygroups['SecurityGroups']:
        name=securitygroup['GroupName']
        description=securitygroup['Description']
        print("name: "+name+"      Descripton: "+ description)
        securitygrouplist.append({ "name":name})
    return securitygrouplist

def getkeypairs():
    keypairlist=[]
    count=0
    keypairs=ec2.describe_key_pairs()
    for keypair in keypairs['KeyPairs']:
        name=keypair['KeyName']
        
        print("name: "+name)
        keypairlist.append({ "name":name})
    return keypairlist

##########################option loaders###########################
def bucket_list(bucket_choices):
    bucketlist=getbuckets()
    return bucketlist

def user_list(bucket_choices):
    userlist=getusers()
    return userlist

def group_list(bucket_choices):
    grouplist=getgroups()
    return grouplist

def instance_list(instance_choices):
    instancelist=getinstances()
    return instancelist

def securitygroup_list(securitygroup_choices):
    securitygrouplist=getsecuritygroups()
    return securitygrouplist

def keypair_list(keypair_choices):
    keypairlist=getkeypairs()
    return keypairlist




########   MAIN QUESTIONS ###############################
def take_action(mainanswers):
    options=[]
    
    if mainanswers['service'] == 'S3':
        if mainanswers['action'] == 'Create Bucket':
            bucket_name=input("What is the name of the bucket you want to create ( Use comma if you want to create multiple buckets): ")###Need to add this functionality later (from mobile app script)
            location=input("In which region do you want to create the bucket")
            progressbar()
            s3.create_bucket(Bucket=str(bucket_name), CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})
            print("\n \n Bucket " +bucket_name +" has been created \n \n")
            options.extend(['Create more buckets','Exit'])
        if mainanswers['action'] == 'Delete Bucket':
            print("delete me aa")
            bucket_choices = prompt(bucket_choice, style=custom_style_2)
            pprint(bucket_choices) 
            deletebucket(bucket_choices)
            options.extend(['Delete more buckets','Exit'])
    if mainanswers['service'] == 'IAM':
        if mainanswers['action'] == 'Create User':
            username=input("What is the name of the user you want to create: ")
            print("Creating user")
            iam.create_user( UserName=str(username))
            options.extend(['Create More users','Exit'])
        if mainanswers['action'] == 'Create Group':
            groupname=input("What is the name of the group you want to create: ")
            print("Creating group")
            iam.create_group(GroupName=str(groupname))
            options.extend(['Create More Groups','Exit']) 
        if mainanswers['action'] == 'Delete User':
            print("delete user me aa")
            user_choices = prompt(user_choice, style=custom_style_2)
            pprint(user_choices) 
            deleteuser(user_choices)
            
            #pprint(bucket_choices) 
            #deletebucket(bucket_choices)
            options.extend(['Delete more users','Exit'])
        if mainanswers['action'] == 'Delete Group':
            print("Make sure that the Group is empty before you delete it")
            group_choices = prompt(group_choice, style=custom_style_2)
            pprint(group_choices) 
            deletegroup(group_choices)
            options.extend(['Delete more groups','Exit'])   
    if mainanswers['service'] == 'EC2':

        ############################INSTANCE ########################
        if mainanswers['action'] == 'Run Instances': ######### Will need to add more features here like ami id according to region
            os=input("What is the OS? ")
            count=input("How many servers you want to run? ")
            instance_type=input("Which Instance type you want to run")
            keyname=input("Which key pair you want to use")
            ec2.run_instances( ImageId=str(os),
            InstanceType=str(instance_type),MaxCount=int(count),
            MinCount=int(count),KeyName=str(keyname))
            print("Running instances now")
            options.extend(['Run more servers','Exit'])
        if mainanswers['action'] == 'Start Instances':
            instance_choices = prompt(instance_choice, style=custom_style_2)
            pprint(instance_choices) 
            startinstance(instance_choices)
            options.extend(['Start more servers','Exit'])
        if mainanswers['action'] == 'Stop Instances':
            instance_choices = prompt(instance_choice, style=custom_style_2)
            pprint(instance_choices) 
            stopinstance(instance_choices)
            options.extend(['Stop more servers','Exit'])
        if mainanswers['action'] == 'Terminate Instances':
            instance_choices = prompt(instance_choice, style=custom_style_2)
            pprint(instance_choices) 
            terminateinstance(instance_choices)
            options.extend(['Terminate more servers','Exit'])


        #########################SECURITY GROUP ################################
        if mainanswers['action'] == 'Create Security Groups':
            
            groupname=input("What is the name you want to give to the group? ")
            vpcid=input("Select the vpc for the Security group") ##currenty manually entering will add vpc selection later
            description=input("Give a short description for the group: ")
            ec2.create_security_group(
            Description=str(description),
            GroupName=str(groupname),
            VpcId=str(vpcid)
            
            )
            options.extend(['Start more servers','Exit'])
        if mainanswers['action'] == 'List Security Groups':
            getsecuritygroups()
            
            options.extend(['Create Security Groups','Delete Security Groups','Exit'])
        if mainanswers['action'] == 'Delete Security Groups':
            instance_choices = prompt(instance_choice, style=custom_style_2)
            pprint(instance_choices) 
            stopinstance(instance_choices)
            options.extend(['Stop more servers','Exit'])

   #########################KEYPAIRS ################################
        if mainanswers['action'] == 'Create Keypairs':
            keyname=input("What is the name of the keypair you want to create? ")
            #path=input("Whre do you want to save the keypair? ")
            key=ec2.create_key_pair(
            KeyName=str(keyname)
            )
            #key.save(str(path))
            options.extend(['Create more keypairs','Exit'])
        if mainanswers['action'] == 'List Keypairs':
            getkeypairs()
            
            options.extend(['Create Keypairs','Delete Keypairs','Exit'])
        if mainanswers['action'] == 'Delete Keypairs':
            
            options.extend(['Stop more servers','Exit'])
    return options


def deletebucket(bucket_choices):
    print("deleting bucket")
    progressbar()
    
    bucketname=bucket_choices['bucket'][0]
    print("\n \n Bucket " +bucketname +" has been deleted \n \n")
    s3.delete_bucket(  Bucket=str(bucketname))

def deleteuser(user_choices):
    print("deleting user")
    progressbar()
    username=user_choices['user'][0]
    print("\n \n User " +username +" has been deleted \n \n")
    iam.delete_user( UserName=str(username))

def deletegroup(group_choices):
    print("deleting group")
    progressbar()
    groupname=group_choices['group'][0]
    print("\n \n Group " +groupname +" has been deleted \n \n")
    iam.delete_group( GroupName=str(groupname))

def startinstance(instance_choices):
    print("Starting Instance")
    progressbar()
    instancename=instance_choices['instance'][0]
    print("\n \n Instance " +instancename +" has been started \n \n")
    ec2.start_instances( InstanceIds=[
        str(instancename),
    ])    

def stopinstance(instance_choices):
    print("Stopping Instance")
    progressbar()
    instancename=instance_choices['instance'][0]
    print("\n \n Instance " +instancename +" has been stopped \n \n")
    ec2.stop_instances( InstanceIds=[
        str(instancename),
    ])
def terminateinstance(instance_choices):
    print("Terminating Instance")
    progressbar()
    instancename=instance_choices['instance'][0]
    print("\n \n Instance " +instancename +" has been terminated \n \n")
    ec2.terminate_instances( InstanceIds=[
        str(instancename),
    ]) 
    
def get_service_data(mainanswers):
    options = []
    if mainanswers['service'] == 'S3':
        print("\n #############Buckets############ \n ")
        getbuckets()
        options.extend(['Create Bucket','Delete Bucket','List Bucket Objects','Upload file to Bucket','Go Back'])
        

    
    elif mainanswers['service'] == 'EC2':
        print("\n #############Instances############ \n ")
        getinstances()
        options.extend(['Run Instances','Start Instances','Stop Instances','Terminate Instances',
        Separator('---------Keypairs---------'),'List Keypairs','Create Keypairs','Delete Keypairs',
        Separator('---------Security Groups---------'),'List Security Groups','Create Security Groups','Delete Security Groups','Go Back'])

    elif mainanswers['service'] == 'IAM':
        print("\n #############Users############ \n ")
        getusers()
        print("\n #############Groups############ \n ")
        getgroups()
        options.extend(['Create User','Create Group','Delete User','Delete Group','Go Back'])
             
    
    return options

mainquestions = [
    {
        'type': 'list',
        'name': 'service',
        'message': 'Which AWS service you want to use ?',
        'choices': [
            Separator('---------Compute Services---------'),
            'EC2',
            'Lambda',
            Separator('---------Storage Services---------'),
            'S3',
            'RDS',
            Separator('---------Network Services---------'),
            'Route53',
            'VPC',
            Separator('---------Management Services---------'),
            'IAM',
            'Cloudwatch'

        ]
    },
    {
        'type': 'list',
        'name': 'action',
        'message': "Actions" ,
        'choices': get_service_data
        
    },
    {
        'type': 'list',
        'name': 'next',
        'message': '>',
        'choices': take_action
    },
]


bucket_choice=[{
        'type': 'checkbox',
        'qmark': '😃',
        'message': 'Select Buckets',
        'name': 'bucket',
        #'choices': ['test1','test2'],
        'choices': bucket_list
}
        ]

user_choice=[{
        'type': 'checkbox',
        'qmark': '😃',
        'message': 'Select Users',
        'name': 'user',
        #'choices': ['test1','test2'],
        'choices': user_list
}
        ]

group_choice=[{
        'type': 'checkbox',
        'qmark': '😃',
        'message': 'Select Groups',
        'name': 'group',
        #'choices': ['test1','test2'],
        'choices': group_list
}
        ]

instance_choice=[{
        'type': 'checkbox',
        'qmark': '😃',
        'message': 'Select instances',
        'name': 'instance',
        #'choices': ['test1','test2'],
        'choices': instance_list
}
        ]


print (f.renderText('AWS CLI'))
print('A small little CLI to interact with AWS Services')
print('Made with <3 by Darshan Raul \n')
mainanswers = prompt(mainquestions, style=custom_style_2)

pprint(mainanswers)



