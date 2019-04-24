

from __future__ import print_function, unicode_literals

from pprint import pprint

from PyInquirer import style_from_dict, Token, prompt, Separator

from examples import custom_style_2

from pyfiglet import Figlet
import boto3

s3 = boto3.client('s3')
f = Figlet(font='big')


def take_action(answers):
    options=[]
    if answers['service'] == 'S3':
        if answers['action'] == 'Create Bucket':
            bucket_name=input("What is the name of the bucket you want to create")
            s3.create_bucket(Bucket=str(bucket_name), CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})
    options.extend(['Create more buckets','Exit'])
    return options

def get_service_data(answers):
    options = []
    if answers['service'] == 'S3':
        print("\n #############Buckets############ \n ")
        options.extend(['Create Bucket','Delete Bucket','List Bucket Objects','Upload file to Bucket'])
        buckets=s3.list_buckets()
        bucketlist=[]
        for i in buckets['Buckets']:
            bucket= i['Name']
            print("> " +bucket)
            bucketlist.append(bucket)

    if answers['service'] == 'EC2':
        print("\n #############Instances############ \n ")
        options.extend(['Start Instance','Stop Instance'])
             
        
    return options

questions = [
    {
        'type': 'list',
        'name': 'service',
        'message': 'Which AWS service you want to use ?',
        'choices': [
            Separator(),
            'EC2',
            'Lambda',
            Separator(),
            'S3',
            'RDS',
            Separator(),
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





def main():
    print (f.renderText('AWS API'))
    print('A small little CLI to interact with AWS Services')
    print('Made with <3 by Darshan Raul \n')
    answers = prompt(questions, style=custom_style_2)
    pprint(answers)





if __name__ == '__main__':
    main()
