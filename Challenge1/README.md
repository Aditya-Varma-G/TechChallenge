#Challenge #1

A 3-tier environment is a common setup.

#Problem statement

A three-tier architecture is a software architecture pattern where the application is broken down into three logical tiers: the presentation layer(front end of the application), the business logic layer(middleware) and the data storage layer(DB storage).

#What is achived 
One virtual network tied in three subnets.
Each subnet will have one virtual machine.
First virtual machine -> allow inbound traffic from internet only.
Second virtual machine -> entertain traffic from first virtual machine only and can reply the same virtual machine again.
App can connect to database and database can connect to app but database cannot connect to web.

#For the solution, we have created and used five modules:

resourcegroup - creating resourcegroup
networking - creating azure virtual network and required subnets
securitygroup - creating network security group, setting desired security rules and associating them to subnets
compute - creating availability sets, network interfaces and virtual machines
database - creating database server and database


#Installation
Need to install Terraform.

#Deployment Steps:

terraform init
terraform plan
terraform validate
terraform apply

