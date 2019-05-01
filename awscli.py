
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
############ progress bar ##########################
from time import sleep
import sys

from progress.bar import FillingCirclesBar
from termcolor import colored, cprint

### initialize service clients #############
s3 = boto3.client('s3')
iam = boto3.client('iam')
ec2 = boto3.client('ec2')

f = Figlet(font='big')


################### progress bar function #########
def progressbar(title):
    # for i in range(21):
    #     sys.stdout.write('\r')
    #     # the exact output you're looking for:
    #     sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
    #     sys.stdout.flush()
    #     sleep(0.05)
    text = colored(str(title), 'red', attrs=['reverse', 'blink'])
    print(text)
    bar = FillingCirclesBar('Processing', max=100)
    for i in range(100):
        # Do some work
        sleep(0.025)
        bar.next()
    bar.finish()


def getconfirmation():
    confirmation = prompt(confirmquestions, style=custom_style_2) # initialize questions

    pprint(confirmation)

    return confirmation['continue']

 ##########################getters#########################   
 # s3    
def getbuckets(show):
    bucketlist=[]
    buckets=s3.list_buckets()
    for i in buckets['Buckets']:
        bucket= i['Name']
        if show:
            print("> " +bucket)
        bucketlist.append({'name':bucket})
    #print(bucketlist)
    return bucketlist


# iam
def getusers(show):
    users=iam.list_users()
    userlist=[]
    
    for user in users['Users']:
        name=user['UserName']
        if show:
            print("> "+name)
        userlist.append({"name":name})
    return userlist

def getgroups(show):
    groups=iam.list_groups()
    grouplist=[]
        
    for group in groups['Groups']:
        name=group['GroupName']
        if show:
            print("> "+name)
        grouplist.append({"name":name})

    return grouplist

def getaccesskeys(show):
    accesskeys=iam.list_access_keys()
    accesskeylist=[]
        
    for accesskey in accesskeys['AccessKeyMetadata']:
        name=accesskey['UserName']
        accesskeyid=accesskey['AccessKeyId']
        if show:
            print("> "+name)
        accesskeylist.append({"name":accesskeyid})

    return accesskeylist
# ec2
def getinstances(show):
    serverlist=[]
    count=0
    servers=ec2.describe_instances()
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
    securitygroups=ec2.describe_security_groups()
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
    keypairs=ec2.describe_key_pairs()
    for keypair in keypairs['KeyPairs']:
        name=keypair['KeyName']
        
        if show:
            print("name: "+name)
        keypairlist.append({ "name":name})
    return keypairlist

def getvpcs(show):
    vpclist=[]
    count=0
    vpcs=ec2.describe_vpcs()
    for vpc in vpcs['Vpcs']:
        name=vpc['VpcId']
        cidr=vpc['CidrBlock']
        if show:
            print("VPC Id:  "+name+"           CIDR: "+cidr)
        vpclist.append({ "name":name})
    return vpclist


##########################option loaders###########################

def bucket_list(bucket_choices):
    bucketlist=getbuckets(False)
    return bucketlist

def user_list(bucket_choices):
    userlist=getusers(False)
    return userlist

def group_list(bucket_choices):
    grouplist=getgroups(False)
    return grouplist


def accesskey_list(accesskey_choices):
    accesskeylist=getaccesskeys(False)
    return accesskeylist

    
def instance_list(instance_choices):
    instancelist=getinstances(False)
    return instancelist

def securitygroup_list(securitygroup_choices):
    securitygrouplist=getsecuritygroups(False)
    return securitygrouplist

def keypair_list(keypair_choices):
    keypairlist=getkeypairs(False)
    return keypairlist

def vpc_list(vpc_choices):
    vpclist=getvpcs(False)
    return vpclist



########  SUB QUESTIONS ###############################




def take_action(mainanswers):
    options=[]
    
    if mainanswers['service'] == 'S3':
        ######################## S3 #########################
        if mainanswers['action'] == 'Create Bucket':
            bucket_name=input("What is the name of the bucket you want to create ( Use comma if you want to create multiple buckets): ")###Need to add this functionality later (from mobile app script)
            location=input("In which region do you want to create the bucket")
            #confirmation = prompt(confirmquestions, style=custom_style_2) # initialize questions

            #pprint(confirmation)
            if getconfirmation():

                progressbar("Creating Bucket")
                s3.create_bucket(Bucket=str(bucket_name), CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})
                print("\n \n Bucket " +bucket_name +" has been created \n \n")
            options.extend(['Create more buckets','Exit'])
        if mainanswers['action'] == 'Delete Bucket':
            
            bucket_choices = prompt(bucket_choice, style=custom_style_2)
            pprint(bucket_choices)
            if getconfirmation():

                deletebucket(bucket_choices)
            options.extend(['Delete more buckets','Exit'])


    if mainanswers['service'] == 'IAM':
        ######################## IAM #######################
        if mainanswers['action'] == 'Create User':
            username=input("What is the name of the user you want to create: ")
            if getconfirmation():
                print("Creating user")
                iam.create_user( UserName=str(username))
            options.extend(['Create More users','Exit'])
        if mainanswers['action'] == 'Create Group':
            groupname=input("What is the name of the group you want to create: ")
            if getconfirmation():
                print("Creating group")
                iam.create_group(GroupName=str(groupname))
            options.extend(['Create More Groups','Exit']) 
        if mainanswers['action'] == 'Delete User':
            
            user_choices = prompt(user_choice, style=custom_style_2)
            pprint(user_choices)
            if getconfirmation():

                deleteuser(user_choices)
            
            #pprint(bucket_choices) 
            #deletebucket(bucket_choices)
            options.extend(['Delete more users','Exit'])
        if mainanswers['action'] == 'Delete Group':
            print("Make sure that the Group is empty before you delete it")
            group_choices = prompt(group_choice, style=custom_style_2)
            pprint(group_choices)
            if getconfirmation():

                deletegroup(group_choices)
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

                iam.add_user_to_group(
                GroupName=str(groupid),
                UserName=str(userid)
                )
            
            options.extend(['Continue','Exit'])  

        if mainanswers['action'] == 'List Access Keys':
            
            getaccesskeys(True)
            
            options.extend(['Continue','Exit'])   

        if mainanswers['action'] == 'Create Access Key':
            print("Select the user you want to create accesskey for")
            user_choices = prompt(user_choice, style=custom_style_2)
            pprint(user_choices)
            userid=user_choices['user'][0]
            if getconfirmation():

                iam.create_access_key(
                UserName=str(userid)
                )
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
                ec2.run_instances( ImageId=str(os),
                InstanceType=str(instance_type),MaxCount=int(count),
                MinCount=int(count),KeyName=str(keyname))
                print("Running instances now")
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
                ec2.create_security_group(
                Description=str(description),
                GroupName=str(groupname),
                VpcId=str(vpcid)
            
                )
            options.extend(['Start more servers','Exit'])
        if mainanswers['action'] == 'List Security Groups':
            getsecuritygroups(True)
            
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
                key=ec2.create_key_pair(
                KeyName=str(keyname)
                )
            #key.save(str(path))
            options.extend(['Create more keypairs','Exit'])
        if mainanswers['action'] == 'List Keypairs':
            getkeypairs(True)
            
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
                ec2.create_vpc(
                CidrBlock=str(cidrblock))
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

def deletebucket(bucket_choices):
    #print("deleting bucket")
    progressbar("Deleting Bucket")
    
    bucketname=bucket_choices['bucket'][0]
    print("\n \n Bucket " +bucketname +" has been deleted \n \n")
    s3.delete_bucket(  Bucket=str(bucketname))

def deleteuser(user_choices):
    #print("deleting user")
    progressbar("Deleting user")
    username=user_choices['user'][0]
    print("\n \n User " +username +" has been deleted \n \n")
    iam.delete_user( UserName=str(username))

def deletegroup(group_choices):
    #print("deleting group")
    progressbar("Deleting Group")
    groupname=group_choices['group'][0]
    print("\n \n Group " +groupname +" has been deleted \n \n")
    iam.delete_group( GroupName=str(groupname))


def deleteaccesskey(accesskey_choices):
    #print("deleting group")
    progressbar("Deleting Access Key")
    accesskeyname=accesskey_choices['accesskey'][0]
    print("\n \n Accesskey " +accesskeyname +" has been deleted \n \n")
    iam.delete_access_key(
    AccessKeyId=str(accesskeyname)
    )


def startinstance(instance_choices):
    #print("Starting Instance")
    progressbar(" Starting Instance")
    instancename=instance_choices['instance'][0]
    print("\n \n Instance " +instancename +" has been started \n \n")
    ec2.start_instances( InstanceIds=[
        str(instancename),
    ])    

def stopinstance(instance_choices):
    #print("Stopping Instance")
    progressbar("Stopping Instances")
    instancename=instance_choices['instance'][0]
    print("\n \n Instance " +instancename +" has been stopped \n \n")
    ec2.stop_instances( InstanceIds=[
        str(instancename),
    ])
def terminateinstance(instance_choices):
    #print("Terminating Instance")
    progressbar("Terminating Instance")
    instancename=instance_choices['instance'][0]
    print("\n \n Instance " +instancename +" has been terminated \n \n")
    ec2.terminate_instances( InstanceIds=[
        str(instancename),
    ]) 


def deletekeypair(keypair_choices):
    #print("deleting keypair")
    progressbar("Deleting Keypair")
    keypairname=keypair_choices['keypair'][0]
    print("\n \n Keypair " +keypairname +" has been deleted \n \n")
    ec2.delete_key_pair(KeyName=str(keypairname))    


def deletevpc(vpc_choices):
    #print("deleting vpc")
    progressbar("Deleting VPC")
    vpcname=vpc_choices['vpc'][0]
    print("\n \n vpc " +vpcname +" has been deleted \n \n")
    ec2.delete_vpc(VpcId=str(vpcname))    

def deletesecuritygroup(securitygroup_choices):
    #print("deleting securitygroup")
    progressbar("Deleting Security Group")
    securitygroupname=securitygroup_choices['securitygroup'][0]
    print("\n \n securitygroup " +securitygroupname +" has been deleted \n \n")
    ec2.delete_security_group(GroupId=str(securitygroupname))    



################# MAIN QUESTIONS ###############################



def get_service_data(mainanswers):
    options = []
    if mainanswers['service'] == 'S3':
        text = colored("\n #############Buckets############ ", 'green', attrs=['reverse', 'blink'])
        print(text +'\n')
        #print()
        getbuckets(True)
        options.extend(['Create Bucket','Delete Bucket','List Bucket Objects','Upload file to Bucket','Go Back'])
        

    
    elif mainanswers['service'] == 'EC2':
        print("\n #############Instances############ \n ")
        getinstances(True)
        options.extend(['Run Instances','Start Instances','Stop Instances','Terminate Instances',
        Separator('---------Keypairs---------'),'List Keypairs','Create Keypair','Delete Keypairs',
        Separator('---------Security Groups---------'),'List Security Groups','Create Security Groups','Delete Security Groups','Go Back'])

    elif mainanswers['service'] == 'IAM':
        print("\n #############Users############ \n ")
        getusers(True)
        print("\n #############Groups############ \n ")
        getgroups(True)
        options.extend(['Create User','Create Group','Add User to Group','Delete User','Delete Group',
        Separator('---------Keys---------'),'List Access Keys','Create Access Key','Delete Access Key',
        Separator('---------Roles---------'),'List Roles','Create Roles','Delete Roles',
        Separator('---------Policy---------'),'List Policies','Create Policies','Delete Policies','Go Back'])
             
    elif mainanswers['service'] == 'VPC':
        print("\n #############VPC's############ \n ")
        getvpcs(True)
        
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
  



