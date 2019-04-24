

from __future__ import print_function, unicode_literals

from pprint import pprint

from PyInquirer import style_from_dict, Token, prompt, Separator

from examples import custom_style_2

from pyfiglet import Figlet
import boto3

s3 = boto3.client('s3')
f = Figlet(font='big')

def getbuckets():
    bucketlist=[]
    buckets=s3.list_buckets()
    for i in buckets['Buckets']:
        bucket= i['Name']
        print("> " +bucket)
        bucketlist.append({'name':bucket})
    #print(bucketlist)
    return bucketlist


def bucket_list(bucket_choices):
    bucketlist=getbuckets()
    return bucketlist

def take_action(mainanswers):
    options=[]
    
    if mainanswers['service'] == 'S3':
        if mainanswers['action'] == 'Create Bucket':
            bucket_name=input("What is the name of the bucket you want to create ( Use comma if you want to create multiple buckets)")###Need to add this functionality later (from mobile app script)
            location=input("In which region do you want to create the bucket")
            s3.create_bucket(Bucket=str(bucket_name), CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})
            options.extend(['Create more buckets','Exit'])
        if mainanswers['action'] == 'Delete Bucket':
            print("delete me aa")
            bucket_choices = prompt(bucket_choice, style=custom_style_2)
            pprint(bucket_choices) 
            options.extend(['Create more buckets','Exit'])
    return options


def get_service_data(mainanswers):
    options = []
    if mainanswers['service'] == 'S3':
        print("\n #############Buckets############ \n ")
        getbuckets()
        options.extend(['Create Bucket','Delete Bucket','List Bucket Objects','Upload file to Bucket'])
        

    
    if mainanswers['service'] == 'EC2':
        print("\n #############Instances############ \n ")
        options.extend(['Start Instance','Stop Instance'])
             
        
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
            Separator(),
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
        'name': 'delivery',
        'message': 'Which vehicle you want to use for delivery?',
        'choices': take_action
    },
]


bucket_choice=[{
        'type': 'checkbox',
        'qmark': '😃',
        'message': 'Select Buckets',
        'name': 'buckets',
        #'choices': ['test1','test2'],
        'choices': bucket_list
}
        ]

print (f.renderText('AWS API'))
print('A small little CLI to interact with AWS Services')
print('Made with <3 by Darshan Raul \n')
mainanswers = prompt(mainquestions, style=custom_style_2)

pprint(mainanswers)



