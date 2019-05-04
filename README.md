# Python-CLI-for-AWS


![demo](https://github.com/darshan-raul/Python-CLI-for-AWS/blob/master/img/demo.gif)
![Main terminal](https://github.com/darshan-raul/Python-CLI-for-AWS/blob/master/img/cli%20main.png)
![s3 terminal](https://github.com/darshan-raul/Python-CLI-for-AWS/blob/master/img/cli%20s3.png)


# TODO:
- [x] Create another branch for testing packaging features
- [ ] Find alternatives for relative imports beyond top level package
- [ ] Use rebase to limit the commits that go to remote
- [ ] Add regions choices 
- [ ] Add requirements.txt for python modules
- [x] Add excpetion handling
    - [ ] create a base class for exceptions defined by this cli
    - [ ] Add finally clauses wherever needed
    - [x] Make exceptions appear in red
- [ ] Use a class/package based approach
    - [ ] Create seperate classes for different questions
    - [ ] Create modules for:
            - [ ] get functions
            - [ ] Choice arrays
            - [ ] Action functions 
    - [x] Create different classes for different AWS services:
            - [x] S3
            - [x] IAM
            - [x] EC2
- [ ] Add docstring to all functions
- [ ] Use Spinx or Read the docs to create documentation for the package
- [ ] Use the comment tags to filter TODO,Bugs etc in code (https://realpython.com/documenting-python-code/)
- [x] Have a look at other CLI offerings and look how you can do something different
- [x] Add confirmation before taking actions
- [ ] Replace the if statements with switch ## using dictionary or lambda
- [x] Add loop to go back to main menu if back is pressed
    - [ ] Create fucntion which creates options maybe and then loop around
- [ ] Integrate pytest to check if code is working
- [x] Create Group function 
- [x] Delete User function
- [x] Delete Group function
- [ ] Try to package the choice arrays and then import in main file 
- [x] Comment the code till now (After making packages so u can comment import statements)
- [x] Start instance
- [x] Stop instance 
- [x] Terminate instance 
- [x] Run instances # Lot more scope here
- [x] Create security groups
- [x] Delete security groups
- [x] Create VPC with CIDR
- [x] View the VPC networks
- [ ] Run instances by chosing options
- [x] Dont print values when doing operations
- [x] Create keypairs
- [X] Delete Keypairs
- [x] Add progress bar when creating/deleting things
- [ ] RDS create
- [ ] RDS delete
 - [ ] IAM
    - [ ] Create policy by providing json policy
    - [x] Add user to group
    - [x] delete access key
    - [x] create access keys
    - [x] list access keys
    - [ ] list roles
	- [ ] Delete roles
- [ ] Add test's using pytest by creating small scenarios 
- [x] Add exit to main menu
- [x] Add keyboard shortcuts for commiting in vscode
- [ ] FINAL : Package the whole thing and post on pypi

# References/Inspiration:

https://github.com/donnemartin/awesome-aws#cli