# Problem statement

We need to write code that will query the meta data of an instance within AWS and provide a json formatted output. The choice of language and implementation is up to you.
Bonus Points
The code allows for a particular data key to be retrieved individually

# Approach
In Azure inorder to retrieve meta data information. On a linux terminal
>curl -H Metadata:true --noproxy "*"  "http://ip-address/metadata/instance?api-version=2020-09-01"

Would give the JSON output of metadata


# Assumptions

- The machine that is running this service is configured with right access keys and permissions in IAM.  

# Testing

  

  

I am going to use Mocha javascript testing framework to do the unit testing
  

  

# Bonus Points

  

The code allows for a particular data key to be retrieved individually

  

  

# Prerequisites

  

  

Create an EC2 Linux instance on AWS

  

SSH into the instance

  

  

# Installation

  

  

Install Python 3 and git on your instance

  

>sudo yum install python3 git

  

Clone this repository

  

>git clone https://github.com/senthilkm/challenges

  
  

Install pipenv

  

>sudo pip3 install pipenv

  

Go to directory **challenge2**

  

>cd challenge2

  

Install project dependancies

  

>pipenv install

  

  

# Running

  

  

Open the src folder

  

>cd challenges/challenge2/src

  

Run whichever script you need:

  

>python3 metadata.py

  

>python3 querymetadata.py

  

  

Examples for the key ami-id or vpc-id