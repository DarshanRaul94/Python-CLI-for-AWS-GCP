# Python-CLI-for-AWS




<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="/images/awskonsole.png" alt="Project logo"></a>
</p>

<h3 align="center">Python-CLI-for-AWS</h3>

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]() 
 
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Interactive CLI created using Python 3. Trying to leverage the PyInquirer(https://pypi.org/project/PyInquirer/) Package to make a very User-Friendly CLI application with many more custom options compared to AWS CLI offers 
    <br> 
</p>

## 📝 Table of Contents
- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Built Using](#built_using)
- [TODO](#todo)


## 🧐 About <a name = "about"></a>
- This is part of a bigger project of creating a unified platform to interact with AWS services from a various interfaces (WEB,MOBILE,CLI,VOICE) 
- Interactive CLI created using Python 3.
- Still in the works. Should be completed by year end as I am commiting consistently but once a week.


## Demo:
![demo](https://github.com/darshan-raul/Python-CLI-for-AWS/blob/master/img/demo.gif)
![Main terminal](https://github.com/darshan-raul/Python-CLI-for-AWS/blob/master/img/cli%20main.png)
![s3 terminal](https://github.com/darshan-raul/Python-CLI-for-AWS/blob/master/img/cli%20s3.png)
## 🏁 Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites
What things you need to install the software and how to install them.

- Python 3
- Pip
- Virtualenv


### Installing
A step by step series of examples that tell you how to get a development env running.

- Clone the project
    ```
    git clone https://github.com/darshan-raul/Python-CLI-for-AWS.git pyawscli
    ```
- Change the directory to project directory
    ```
    cd pyawscli
    ```
- Install all the required dependencies
    ```
    pip install -r requirements.txt
    ```
- Run locally
    ```
    python ./awscli.py
    ```


## 🚀 Deployment <a name = "deployment"></a>

If you want to create a pip package out of the code.
[Here are the steps ](https://cloudforte.wordpress.com/2019/05/19/220/)

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) 
- [PyInquirer](https://github.com/CITGuru/PyInquirer) 

# TODO:
- [x] Create another branch for testing packaging features
- [x] Find alternatives for relative imports beyond top level package
- [ ] Use rebase to limit the commits that go to remote
- [x] Add regions choices 
- [x] Add requirements.txt for python modules
- [x] Add excpetion handling
    - [ ] create a base class for exceptions defined by this cli
    - [ ] Add finally clauses wherever needed
    - [x] Make exceptions appear in red
- [x] Create different classes for different AWS services:
    - [x] S3
    - [x] IAM
    - [x] EC2        
- [x] Add docstring to all functions
- [ ] Use Spinx or Read the docs to create documentation for the package
- [x] Use the comment tags to filter TODO,Bugs etc in code (https://realpython.com/documenting-python-code/)
- [x] Have a look at other CLI offerings and look how you can do something different
- [x] Add confirmation before taking actions
- [x] Add loop to go back to main menu if back is pressed
    - [ ] Create fucntion which creates options maybe and then loop around
- [ ] Integrate pytest to check if code is working
    - [x] Try on single aws s3 service
    - [ ] Replicate on other services
    - [ ] Use parametrize to create multiple scenarios
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
- [x] Add test's using pytest by creating small scenarios 
- [x] Add exit to main menu
- [x] Add keyboard shortcuts for commiting in vscode
- [x] FINAL : Package the whole thing and post on pypi

# References/Inspiration:

https://github.com/donnemartin/awesome-aws#cli


# BUGFIXES:

- [ ] create bucket locationconstraint error
