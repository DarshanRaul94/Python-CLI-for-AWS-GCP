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
