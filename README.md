# Python-CLI-for-AWS


![demo](https://github.com/darshan-raul/Python-CLI-for-AWS/blob/master/img/demo.gif)
![Main terminal](https://github.com/darshan-raul/Python-CLI-for-AWS/blob/master/img/cli%20main.png)
![s3 terminal](https://github.com/darshan-raul/Python-CLI-for-AWS/blob/master/img/cli%20s3.png)


# TODO:
- [x] Add excpetion handling
        - [ ] create a base class for exceptions defined by this cli
        - [ ] Add finally clauses wherever needed
        - [x] Make exceptions appear in red
- [ ] Use a class/package based approach
        - [ ] Create seperate classes for different questions
        - [ ] Create different classes for different AWS services:
                - [ ] S3
                - [ ] IAM
                - [ ] EC2
- [ ] Use the comment tags to filter TODO,Bugs etc in code (https://realpython.com/documenting-python-code/)
- [x] Have a look at other CLI offerings and look how you can do something different
- [x] Add confirmation before taking actions
- [ ] Add regions choices 
- [ ] Replace the if statements with switch ## using dictionary or lambda
- [x] Add loop to go back to main menu if back is pressed
        * [ ] Create fucntion which creates options maybe and then loop around
- [ ] Integrate pytest to check if code is working
- [x] Create Group function 
- [x] Delete User function
- [x] Delete Group function
- [ ] Try to package the choice arrays and then import in main file [Can skip if not feasible today]
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
- [ ] Add keyboard shortcuts for commiting in vscode
- [ ] FINAL : Package the whole thing and post on pypi

# References/Inspiration:

https://github.com/donnemartin/awesome-aws#cli