
"""
This is the main module where the questions and operations are initialized
"""

################ PYenquirer ##################
from __future__ import print_function, unicode_literals

from pprint import pprint

from PyInquirer import style_from_dict, Token, prompt, Separator

from examples import custom_style_2

count = 0

################ Logo #####################
from pyfiglet import Figlet

########### AWS #####################
import boto3
import botocore
############ progress bar ##########################
from time import sleep
import sys
import os



from termcolor import colored
from packages.aws_services.S3 import s3 as s3class

from packages.aws_services.IAM import iam as iamclass

from packages.aws_services.EC2 import ec2 as ec2class
from packages.utlities.progressbar import progressbar
from packages.utlities.colored import coloredtext
### initialize service clients #############
s3 = boto3.client('s3')
iam = boto3.client('iam')
ec2 = boto3.client('ec2')

f = Figlet(font='big')




def getconfirmation():
    confirmation = prompt(confirmquestions, style=custom_style_2) # initialize questions

    pprint(confirmation)

    return confirmation['continue']





##########################option loaders###########################

def bucket_list(bucket_choices):
    bucketlist=s3class.getbuckets(False)
    return bucketlist

def user_list(bucket_choices):
    userlist=iamclass.getusers(False)
    return userlist

def group_list(bucket_choices):
    grouplist=iamclass.getgroups(False)
    return grouplist


def accesskey_list(accesskey_choices):
    accesskeylist=iamclass.getaccesskeys(False)
    return accesskeylist

    
def instance_list(instance_choices):
    instancelist=ec2class.getinstances(False)
    return instancelist

def securitygroup_list(securitygroup_choices):
    securitygrouplist=ec2class.getsecuritygroups(False)
    return securitygrouplist

def keypair_list(keypair_choices):
    keypairlist=ec2class.getkeypairs(False)
    return keypairlist

def vpc_list(vpc_choices):
    vpclist=ec2class.getvpcs(False)
    return vpclist

def region_list(region_choices):
    regionlist=['ap-south-1','us-east-1']
    return regionlist





confirmquestions = [
    {
        'type': 'confirm',
        'message': 'Do you want to continue?',
        'name': 'continue',
        'default': True,
    },
    
]

region_choice = [
{
        'type': 'list',
        'name': 'region',
        'message': 'Select region',
        'choices': region_list
    },
]
###########################CHECKBOXES############################

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

accesskey_choice=[{
        'type': 'checkbox',
        'qmark': '😃',
        'message': 'Select accesskeys',
        'name': 'accesskey',
        #'choices': ['test1','test2'],
        'choices': accesskey_list
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


keypair_choice=[{
        'type': 'checkbox',
        'qmark': '😃',
        'message': 'Select keypairs',
        'name': 'keypair',
        #'choices': ['test1','test2'],
        'choices': keypair_list
}
        ]

vpc_choice=[{
        'type': 'checkbox',
        'qmark': '😃',
        'message': 'Select vpcs',
        'name': 'vpc',
        #'choices': ['test1','test2'],
        'choices': vpc_list
}
        ]


securitygroup_choice=[{
        'type': 'checkbox',
        'qmark': '😃',
        'message': 'Select securitygroups',
        'name': 'securitygroup',
        #'choices': ['test1','test2'],
        'choices': securitygroup_list
}
        ]

def getservice():

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
            'Cloudwatch',
            'Exit'
        ]
    }
  
    ]       

    answers=prompt(mainquestions, style=custom_style_2) 

    if answers['service']=='Exit':
        sys.exit()
    return answers['service']



def gotoservice(service):

    if service=='S3':
        text = colored("\n #############Buckets############ ", 'green', attrs=['reverse', 'blink'])
        print(text +'\n')
        s3class.getbuckets(True)
        #
        s3questions = [
        {
        'type': 'list',
        'name': 'action',
        'message': 'Which AWS service you want to use ?',
        'choices': ['Create Bucket','Delete Bucket','List Bucket Objects','Upload file to Bucket','Go Back'
            
        ]
        }
  
        ]
        s3prompt=prompt(s3questions, style=custom_style_2)
        s3action=s3prompt['action']
        if s3action=='Go Back':
            main()
        else:
            s3actions(s3action)
    if service=='EC2':
        text = colored("\n #############Instances############ ", 'green', attrs=['reverse', 'blink'])
        print(text +'\n')
        ec2class.getinstances(True)
        #
        ec2questions = [
        {
        'type': 'list',
        'name': 'action',
        'message': 'Which AWS service you want to use ?',
        'choices': ['Run Instances','Start Instances','Stop Instances','Terminate Instances',
        Separator('---------Keypairs---------'),'List Keypairs','Create Keypair','Delete Keypair',
        Separator('---------Security Groups---------'),'List Security Groups','Create Security Groups','Delete Security Groups','Go Back'
            
        ]
        }
  
        ]
        ec2prompt=prompt(ec2questions, style=custom_style_2)
        ec2action=ec2prompt['action']
        if ec2action=='Go Back':
            main()
        else:
            ec2actions(ec2action)
        
    if service=='IAM':
        print("\n #############Users############ \n ")
        iamclass.getusers(True)
        print("\n #############Groups############ \n ")
        iamclass.getgroups(True)
        iamquestions = [
        {
        'type': 'list',
        'name': 'action',
        'message': 'Which AWS service you want to use ?',
        'choices': ['Create User','Create Group','Add User to Group','Delete User','Delete Group',
        Separator('---------Keys---------'),'List Access Keys','Create Access Key','Delete Access Key',
        Separator('---------Roles---------'),'List Roles','Create Roles','Delete Roles',
        Separator('---------Policy---------'),'List Policies','Create Policies','Delete Policies','Go Back'
        ]
        }
  
        ]
        iamprompt=prompt(iamquestions, style=custom_style_2)
        iamaction=iamprompt['action']
        if iamaction=='Go Back':
            main()
        else:
            iamactions(iamaction)

    if service=='VPC':
        print("\n #############VPC's############ \n ")
        ec2class.getvpcs(True)
        vpcquestions = [
        {
        'type': 'list',
        'name': 'action',
        'message': 'Which AWS service you want to use ?',
        'choices': ['Create VPC','Delete VPC','Go Back'
        ]
        }
  
        ]
        vpcprompt=prompt(vpcquestions, style=custom_style_2)
        vpcaction=vpcprompt['action']
        if vpcaction=='Go Back':
            main()
        else:
            vpcactions(vpcaction)   




def s3actions(action):

    if action == 'Create Bucket':

        bucket_name=input("What is the name of the bucket you want to create ( Use comma if you want to create multiple buckets): ")###Need to add this functionality later (from mobile app script)
        region_choices = prompt(region_choice, style=custom_style_2)
        pprint(region_choices)
        region=region_choices['region']
            
        if getconfirmation():

            progressbar("Creating Bucket")
            try:
                s3.create_bucket(Bucket=str(bucket_name), CreateBucketConfiguration={'LocationConstraint': str(region)})
                print("\n \n Bucket " +bucket_name +" has been created \n \n")
            except botocore.exceptions.ClientError as e:
                coloredtext("There was an error while creating Bucket: \n\n\n")
                print(e)

        confirm_or_exit('S3')

        
    if action == 'Delete Bucket':
            
        bucket_choices = prompt(bucket_choice, style=custom_style_2)
        pprint(bucket_choices)
        if getconfirmation():
                
            s3class.deletebucket(bucket_choices)

        confirm_or_exit('S3')        
        
    

def ec2actions(action):

    #####################INSTANCES################
    if action == 'Run Instances':
                 
        os=input("What is the OS? ")
        count=input("How many servers you want to run? ")
        instance_type=input("Which Instance type you want to run")
        keyname=input("Which key pair you want to use")
        if getconfirmation():
            try:
                ec2.run_instances( ImageId=str(os),
                InstanceType=str(instance_type),MaxCount=int(count),
                MinCount=int(count),KeyName=str(keyname))
                print("Running instances now")
            except botocore.exceptions.ClientError as e:
                coloredtext("There was an error while run instance: \n\n\n")
                print(e)
        confirm_or_exit('EC2')  

    if action == 'Start Instances':
        instance_choices = prompt(instance_choice, style=custom_style_2)
        pprint(instance_choices)
        if getconfirmation(): 
            ec2class.startinstance(instance_choices)
        confirm_or_exit('EC2')

    if action == 'Stop Instances':
        instance_choices = prompt(instance_choice, style=custom_style_2)
        pprint(instance_choices)
        if getconfirmation(): 
            ec2class.stopinstance(instance_choices)
        confirm_or_exit('EC2')

    if action == 'Terminate Instances':
        instance_choices = prompt(instance_choice, style=custom_style_2)
        pprint(instance_choices) 
        if getconfirmation():

            ec2class.terminateinstance(instance_choices)
        confirm_or_exit('EC2')


    #########################SECURITY GROUP ################################
    if action == 'Create Security Groups':
            
        groupname=input("What is the name you want to give to the group? ")
        #vpcid=input("Select the vpc for the Security group") ##currenty manually entering will add vpc selection later
        description=input("Give a short description for the group: ")
        vpc_choices = prompt(vpc_choice, style=custom_style_2)
        pprint(vpc_choices)
        vpcid=vpc_choices['vpc'][0]
        if getconfirmation():
            try:
                ec2.create_security_group(
                Description=str(description),
                GroupName=str(groupname),
                VpcId=str(vpcid)
                
                )
            except botocore.exceptions.ClientError as e:
                coloredtext("There was an error while creating security group: \n\n\n")
                print(e)
        confirm_or_exit('EC2')  

    if action == 'List Security Groups':
        ec2class.getsecuritygroups(True)
            
        confirm_or_exit('EC2')
    
    if action == 'Delete Security Groups':
        securitygroup_choices = prompt(securitygroup_choice, style=custom_style_2)
        pprint(securitygroup_choices) 
        if getconfirmation():
            ec2class.deletesecuritygroup(securitygroup_choices)
        confirm_or_exit('EC2')

    #########################KEYPAIRS ################################
    if action == 'Create Keypair':
        keyname=input("What is the name of the keypair you want to create? ")
        #path=input("Whre do you want to save the keypair? ")
        if getconfirmation():
            try:
                key=ec2.create_key_pair(
                KeyName=str(keyname)
                )
                print("\n \n Keypair " +keyname +" has been created \n \n")
            except botocore.exceptions.ClientError as e:
                coloredtext("There was an error while creating keypair: \n\n\n")
                print(e)
        confirm_or_exit('EC2')

    if action == 'List Keypairs':
        ec2class.getkeypairs(True)
        confirm_or_exit('EC2')    
        #options.extend(['Create Keypairs','Delete Keypairs','Exit'])
    if action == 'Delete Keypair':
        keypair_choices = prompt(keypair_choice, style=custom_style_2)
        pprint(keypair_choices)
        if getconfirmation(): 
            ec2class.deletekeypair(keypair_choices)
        confirm_or_exit('EC2')
    

def iamactions(action):

    if action == 'Create User':
        username=input("What is the name of the user you want to create: ")
        if getconfirmation():
            try:
                print("Creating user")
                iam.create_user( UserName=str(username))
                print("\n \n User " +username +" has been created \n \n")
            except botocore.exceptions.ClientError as e:
                coloredtext("There was an error while creating user: \n\n\n")
                print(e)
        confirm_or_exit('IAM')
        
    if action == 'Create Group':
        groupname=input("What is the name of the group you want to create: ")
        if getconfirmation():
            try:
                print("Creating group")
                iam.create_group(GroupName=str(groupname))
                print("\n \n GRoup " +groupname +" has been created \n \n")
            except botocore.exceptions.ClientError as e:
                coloredtext("There was an error while creating group: \n\n\n")
                print(e)
        confirm_or_exit('IAM') 
    if action == 'Delete User':
            
        user_choices = prompt(user_choice, style=custom_style_2)
        pprint(user_choices)
        if getconfirmation():

            iamclass.deleteuser(user_choices)
            
        confirm_or_exit('IAM')

    if action == 'Delete Group':
        print("Make sure that the Group is empty before you delete it")
        group_choices = prompt(group_choice, style=custom_style_2)
        pprint(group_choices)
        if getconfirmation():

            iamclass.deletegroup(group_choices)
        confirm_or_exit('IAM')
        
    if action == 'Add User to Group':
        print("Select the user you want to add")
        user_choices = prompt(user_choice, style=custom_style_2)
        pprint(user_choices)
        userid=user_choices['user'][0]
        group_choices = prompt(group_choice, style=custom_style_2)
        pprint(group_choices)
        groupid=group_choices['group'][0]
        if getconfirmation():
            try:
                iam.add_user_to_group(
                GroupName=str(groupid),
                UserName=str(userid)
                )    
            except botocore.exceptions.ClientError as e:
                coloredtext("There was an error while adding user to group: \n\n\n")
                print(e)
            
        confirm_or_exit('IAM')  

    if action == 'List Access Keys':
            
        iamclass.getaccesskeys(True)
            
        confirm_or_exit('IAM')  

    if action == 'Create Access Key':
        print("Select the user you want to create accesskey for")
        user_choices = prompt(user_choice, style=custom_style_2)
        pprint(user_choices)
        userid=user_choices['user'][0]
        if getconfirmation():
            try:
                iam.create_access_key(
                UserName=str(userid)
                )
            except botocore.exceptions.ClientError as e:
                coloredtext("There was an error while creating access key: \n\n\n")
                print(e)
        confirm_or_exit('IAM')

    if action == 'Delete Access Key':
            
        accesskey_choices = prompt(accesskey_choice, style=custom_style_2)
        pprint(accesskey_choices)
        if getconfirmation():

            iamclass.deleteaccesskey(accesskey_choices)
        confirm_or_exit('IAM')
    

def vpcactions(action):
    if action == 'Create VPC':
        cidrblock=input("Insert the CIDR block for the vpc example, 10.0.0.0/16 :  ")
        #path=input("Whre do you want to save the keypair? ")
        if getconfirmation():
            try:
                ec2.create_vpc(
                CidrBlock=str(cidrblock))
            except botocore.exceptions.ClientError as e:
                coloredtext("There was an error while creating VPC: \n\n\n")
                print(e)
        #key.save(str(path))
        confirm_or_exit('VPC')
       
    if action == 'Delete VPC':
        vpc_choices = prompt(vpc_choice, style=custom_style_2)
        pprint(vpc_choices)
        if getconfirmation(): 
            ec2class.deletevpc(vpc_choices)
        confirm_or_exit('VPC')
    
    


def confirm_or_exit(service):
    if getconfirmation():
        gotoservice(str(service))
    else:
        sys.exit()



########################## START HERE###################


def main():
    os.system('cls')
    service=getservice()
    print(service)
    gotoservice(service)

if __name__ == '__main__':
    main()

    
    

  



