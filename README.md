# Log Analysis Project
This is a project for Udacity's [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)
## Project Description:
Building an informative summary from logs by sql database queries. Interacting with a live database both from the command line and from the python code.

### The output of this project is to answer three questions:

1. **What are the most popular three articles of all time?** 
2. **Who are the most popular article authors of all time?** 
3. **On which days did more than 1% of requests lead to errors?**

## PreRequisites:
1. Install [Vagrant](https://www.vagrantup.com/)
1. Install [VirtualBox](https://www.virtualbox.org/)
1. install [Python3](https://www.python.org)
1. Download the vagrant setup files from [Udacity's Github](https://github.com/udacity/fullstack-nanodegree-vm)
These files configure the virtual machine and install all the tools needed to run this project.
1. Download the database setup: [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

## Installation:
Once you get the above software installed, follow the insturctions detailed below:
1. Open Terminal and navigate to the project folders we setup above.
1. run  ``` cd vagrant ```  
1. Run ``` vagrant up ``` to build the VM for the first time.
1. Once it is built, run ``` vagrant ssh ``` to connect.
1. cd into the correct project directory: ``` cd /vagrant ```
1. run  ``` mkdir log-analysis-project ```  to create the dirictory.
1. run  ``` cd log-analysis-project ```
1. Load the data using the following command: ``` psql -d news -f newsdata.sql ```
1. run ```pip install flask ```
1. run ``` pip install psycopg2 ```
1. ``` python3 newsdata.py```  to run the reporting tool.


## Helpful Resources:
1. Install [Vagrant](https://www.vagrantup.com/)
1. Install [VirtualBox](https://www.virtualbox.org/)
1. install [Python3](https://www.python.org)
