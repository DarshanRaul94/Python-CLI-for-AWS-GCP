

from __future__ import print_function, unicode_literals

from pprint import pprint

from PyInquirer import style_from_dict, Token, prompt, Separator

from examples import custom_style_2

from pyfiglet import Figlet
import boto3

s3 = boto3.client('s3')
f = Figlet(font='big')


def get_delivery_options(answers):
    options = ['bike', 'car', 'truck']
    if answers['size'] == 'jumbo':
        options.append('helicopter')
    return options

def get_service_data(answers):
    options = []
    if answers['service'] == 'S3':
        print("Buckets:")
        options.append('Create Bucket')
        buckets=s3.list_buckets()
        bucketlist=[]
        for i in buckets['Buckets']:
            bucket= i['Name']
            print(bucket)
            bucketlist.append(bucket)
        
        
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
            'RDS'
        ]
    },
    {
        'type': 'list',
        'name': 'size',
        'message': 'Actions',
        'choices': get_service_data
        
    },
    {
        'type': 'list',
        'name': 'delivery',
        'message': 'Which vehicle you want to use for delivery?',
        'choices': get_delivery_options,
    },
]





def main():
    print (f.renderText('AWS API'))
    print('A small little CLI to interact with AWS Services')
    print('Made with <3 by Darshan Raul ')
    answers = prompt(questions, style=custom_style_2)
    pprint(answers)





if __name__ == '__main__':
    main()
