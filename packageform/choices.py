
class choices:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.mainquestions = [
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


        self.confirmquestions = [
            {
                'type': 'confirm',
                'message': 'Do you want to continue?',
                'name': 'continue',
                'default': True,
            },
            
        ]
 
 
    def printMembers(self):
        print('Printing members of the Mammals class')
        for member in self.mainquestions:
            print('\t%s ' % member)

        for member in self.confirmquestions:
            print('\t%s ' % member)