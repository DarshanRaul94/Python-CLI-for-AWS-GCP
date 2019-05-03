
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



# iam

# ec2



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



########  SUB QUESTIONS ###############################




def take_action(mainanswers):
    options=[]
    
    if mainanswers['service'] == 'S3':
        ######################## S3 #########################
        if mainanswers['action'] == 'Create Bucket':
            bucket_name=input("What is the name of the bucket you want to create ( Use comma if you want to create multiple buckets): ")###Need to add this functionality later (from mobile app script)
            #location=input("In which region do you want to create the bucket")
            #confirmation = prompt(confirmquestions, style=custom_style_2) # initialize questions

            #pprint(confirmation)
            if getconfirmation():

                progressbar("Creating Bucket")
                try:
                    s3.create_bucket(Bucket=str(bucket_name), CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})
                    print("\n \n Bucket " +bucket_name +" has been created \n \n")
                except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while creating Bucket: \n\n\n")
                    print(e)

                
            options.extend(['Create more buckets','Exit'])
        if mainanswers['action'] == 'Delete Bucket':
            
            bucket_choices = prompt(bucket_choice, style=custom_style_2)
            pprint(bucket_choices)
            if getconfirmation():
                
                s3class.deletebucket(bucket_choices)
                
            options.extend(['Delete more buckets','Exit'])


    if mainanswers['service'] == 'IAM':
        ######################## IAM #######################
        if mainanswers['action'] == 'Create User':
            username=input("What is the name of the user you want to create: ")
            if getconfirmation():
                try:
                    print("Creating user")
                    iam.create_user( UserName=str(username))
                except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while creating user: \n\n\n")
                    print(e)
            options.extend(['Create More users','Exit'])
        if mainanswers['action'] == 'Create Group':
            groupname=input("What is the name of the group you want to create: ")
            if getconfirmation():
                try:
                    print("Creating group")
                    iam.create_group(GroupName=str(groupname))
                except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while creating group: \n\n\n")
                    print(e)
            options.extend(['Create More Groups','Exit']) 
        if mainanswers['action'] == 'Delete User':
            
            user_choices = prompt(user_choice, style=custom_style_2)
            pprint(user_choices)
            if getconfirmation():

                iamclass.deleteuser(user_choices)
            
            #pprint(bucket_choices) 
            #deletebucket(bucket_choices)
            options.extend(['Delete more users','Exit'])
        if mainanswers['action'] == 'Delete Group':
            print("Make sure that the Group is empty before you delete it")
            group_choices = prompt(group_choice, style=custom_style_2)
            pprint(group_choices)
            if getconfirmation():

                iamclass.deletegroup(group_choices)
            options.extend(['Delete more groups','Exit'])
        
        if mainanswers['action'] == 'Add User to Group':
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
            
            options.extend(['Continue','Exit'])  

        if mainanswers['action'] == 'List Access Keys':
            
            iamclass.getaccesskeys(True)
            
            options.extend(['Continue','Exit'])   

        if mainanswers['action'] == 'Create Access Key':
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
            options.extend(['Create More accesskeys','Exit'])

        if mainanswers['action'] == 'Delete Access Key':
            
            accesskey_choices = prompt(accesskey_choice, style=custom_style_2)
            pprint(accesskey_choices)
            if getconfirmation():

                deleteaccesskey(accesskey_choices)
            options.extend(['Delete more accesskeys','Exit'])

    if mainanswers['service'] == 'EC2':

        ############################INSTANCE ########################
        if mainanswers['action'] == 'Run Instances': ######### Will need to add more features here like ami id according to region
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
            options.extend(['Run more servers','Exit'])
        if mainanswers['action'] == 'Start Instances':
            instance_choices = prompt(instance_choice, style=custom_style_2)
            pprint(instance_choices)
            if getconfirmation(): 
                startinstance(instance_choices)
            options.extend(['Start more servers','Exit'])
        if mainanswers['action'] == 'Stop Instances':
            instance_choices = prompt(instance_choice, style=custom_style_2)
            pprint(instance_choices)
            if getconfirmation(): 
                stopinstance(instance_choices)
            options.extend(['Stop more servers','Exit'])
        if mainanswers['action'] == 'Terminate Instances':
            instance_choices = prompt(instance_choice, style=custom_style_2)
            pprint(instance_choices) 
            if getconfirmation():

                terminateinstance(instance_choices)
            options.extend(['Terminate more servers','Exit'])


        #########################SECURITY GROUP ################################
        if mainanswers['action'] == 'Create Security Groups':
            
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
            options.extend(['Start more servers','Exit'])
        if mainanswers['action'] == 'List Security Groups':
            ec2class.getsecuritygroups(True)
            
            options.extend(['Create Security Groups','Delete Security Groups','Exit'])
        if mainanswers['action'] == 'Delete Security Groups':
            securitygroup_choices = prompt(securitygroup_choice, style=custom_style_2)
            pprint(securitygroup_choices) 
            if getconfirmation():
                deletesecuritygroup(securitygroup_choices)
            options.extend(['Delete more securitygroups','Exit'])

        #########################KEYPAIRS ################################
        if mainanswers['action'] == 'Create Keypairs':
            keyname=input("What is the name of the keypair you want to create? ")
            #path=input("Whre do you want to save the keypair? ")
            if getconfirmation():
                try:
                    key=ec2.create_key_pair(
                    KeyName=str(keyname)
                    )
                except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while creating keypair: \n\n\n")
                    print(e)
            #key.save(str(path))
            options.extend(['Create more keypairs','Exit'])
        if mainanswers['action'] == 'List Keypairs':
            ec2class.getkeypairs(True)
            
            options.extend(['Create Keypairs','Delete Keypairs','Exit'])
        if mainanswers['action'] == 'Delete Keypairs':
            keypair_choices = prompt(keypair_choice, style=custom_style_2)
            pprint(keypair_choices)
            if getconfirmation(): 
                deletekeypair(keypair_choices)
            options.extend(['Delete more Keypairs','Exit'])



    ###########################VPCS################################

    if mainanswers['service'] == 'VPC':
        if mainanswers['action'] == 'Create VPC':
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
            options.extend(['Create more VPC\'s','Exit'])
       
        if mainanswers['action'] == 'Delete VPC':
            vpc_choices = prompt(vpc_choice, style=custom_style_2)
            pprint(vpc_choices)
            if getconfirmation(): 
                deletevpc(vpc_choices)
            options.extend(['Delete more VPC\'s','Exit'])

    if mainanswers['action'] == 'Go Back':
        mainanswers = prompt(mainquestions, style=custom_style_2) # initialize questions
        print("incoming")
        pprint(mainanswers)
        get_service_data(mainanswers)

    return options


################################DELETE FUNCTIONS   ##############################


    
    



def deleteaccesskey(accesskey_choices):
    #print("deleting group")
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


def startinstance(instance_choices):
    #print("Starting Instance")
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
    #print("deleting vpc")
    progressbar("Deleting VPC")
    vpcname=vpc_choices['vpc'][0]
    try:
        ec2.delete_vpc(VpcId=str(vpcname))
        print("\n \n vpc " +vpcname +" has been deleted \n \n")
    except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while deleting vpc: \n\n\n")
                    print(e)    

def deletesecuritygroup(securitygroup_choices):
    #print("deleting securitygroup")
    progressbar("Deleting Security Group")
    securitygroupname=securitygroup_choices['securitygroup'][0]
    try:

        print("\n \n securitygroup " +securitygroupname +" has been deleted \n \n")
        ec2.delete_security_group(GroupId=str(securitygroupname))
    except botocore.exceptions.ClientError as e:
                    coloredtext("There was an error while deleting security group: \n\n\n")
                    print(e)    



################# MAIN QUESTIONS ###############################



def get_service_data(mainanswers):
    options = []
    if mainanswers['service'] == 'S3':
        text = colored("\n #############Buckets############ ", 'green', attrs=['reverse', 'blink'])
        print(text +'\n')
        #print()
        s3class.getbuckets(True)
        options.extend(['Create Bucket','Delete Bucket','List Bucket Objects','Upload file to Bucket','Go Back'])
        

    
    elif mainanswers['service'] == 'EC2':
        print("\n #############Instances############ \n ")
        ec2class.getinstances(True)
        options.extend(['Run Instances','Start Instances','Stop Instances','Terminate Instances',
        Separator('---------Keypairs---------'),'List Keypairs','Create Keypair','Delete Keypairs',
        Separator('---------Security Groups---------'),'List Security Groups','Create Security Groups','Delete Security Groups','Go Back'])

    elif mainanswers['service'] == 'IAM':
        print("\n #############Users############ \n ")
        iamclass.getusers(True)
        print("\n #############Groups############ \n ")
        iamclass.getgroups(True)
        options.extend(['Create User','Create Group','Add User to Group','Delete User','Delete Group',
        Separator('---------Keys---------'),'List Access Keys','Create Access Key','Delete Access Key',
        Separator('---------Roles---------'),'List Roles','Create Roles','Delete Roles',
        Separator('---------Policy---------'),'List Policies','Create Policies','Delete Policies','Go Back'])
             
    elif mainanswers['service'] == 'VPC':
        print("\n #############VPC's############ \n ")
        ec2class.getvpcs(True)
        
        options.extend(['Create VPC','Delete VPC','Go Back'])
    elif mainanswers['service'] == 'Exit':
        sys.exit()
        
        #options.extend(['Create VPC','Delete VPC','Go Back'])
    

    return options



######################## STATIC MAIN OPTIONS #################
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

########################## CONFIRMATION QUESTIONS #############
confirmquestions = [
    {
        'type': 'confirm',
        'message': 'Do you want to continue?',
        'name': 'continue',
        'default': True,
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



########################## START HERE###################




    
    
# print (f.renderText('AWS CLI'))
# print('A small little CLI to interact with AWS Services')
# print('Made with <3 by Darshan Raul \n')   

mainanswers = prompt(mainquestions, style=custom_style_2) # initialize questions

pprint(mainanswers) # print questions
  



