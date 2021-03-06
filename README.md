# Covid cases

This application extracts the daily covid cases from the source url https://api.coronavirus.data.gov.uk/v1/data?filters=areaType=nation;areaName=england&structure={%22date%22:%22date%22,%22newCases%22:%22newCasesByPublishDate%22} and creates a csv file for the reporting purpose.

- Code is handled using python3.8 version
- Deployment is automated with two different ways
  - Terraform
  - The Serverless framework

- The below steps details how to deploy the aws lambdas with both the approaches.

- Unit testing is done using pytest, Moto, boto3 frameworks.

Clone the project
- git clone https://github.com/NagaBushan/covidcases.git
- git fetch origin

# Terraform steps
Pre-requisites
- An active AWS account
- aws_access_key_id and aws_secret_access_key has to be generated
- python 3.8
- pip 21.01
- Terrform v0.13.5

Deployment of AWS lambda using terraform scripts.

- git checkout -b feature/terraform origin/feature/terraform
- cd to <Base_dir>/covidcases/application/lambdas
-  pip install -r requirements.txt -t ./lib 
- cd to the folder <Base_dir>/covidcases/infrastructure
- tf init
- tf apply
	- copy and paste access_key, secret_key

Testing
-
- After successfully deploying AWS lambda, testing can be done using AWS lambda consle.
- Search for Lambda in AWS console and select
- There is test button available on console and click on it
- Create a new event, name the event as you like
- Then click again on test button
- The logs output will appear on the screen
- When test is success it will display as "Covid data extracted successfully into S3 bucket"
- Then the resport in the csv format can be seen in s3 bucket, s3: //ttf-covid-cases//tmp/covid.csv

>Please note, the s3 tf-covid-cases bucket needs to be manually deleted. Terraform destroy is not handled to delete it.


# Serverless framework

Pre-requisites
- Make sure you have serverless framework installed , follow the steps mentioned in the below link for installation, https://www.serverless.com/framework/docs/providers/aws/guide/installation/
	The below are the recommended version of the Serverless framework
	- Framework Core: 2.22.0
	- Plugin: 4.4.2
	- SDK: 2.3.2
	- Components: 3.6.3
	
-  An active AWS account
- aws_access_key_id and aws_secret_access_key has to be generated and available in the ./aws/credentials
- python 3.8
- pip 21.01

Steps
-
- git checkout main
- cd <Base_dir>/application/lambdas
- npm install --save serverless-python-requirements
- sls deploy (This command will package and deploy into the aws)
- After successful deployment use the following comand to test it locally
	- sls invoke -f covid-cases ( this will invoke the lambda in aws account, the logs are displayed in the console)
	- The resport in the csv format can be seen in s3 bucket, s3: //sls-covid-cases//tmp/covid.csv
>Please note, the s3 sls-covid-cases bucket needs to be manually deleted. Terraform destroy is not handled to delete it.
>While running sls deploy, serverless expects python3 on path variables so make sure python3 is available

- sls remove, to delete the stack
	- This command will not delete the s3 bucket and aws stack when the bucket is not empty. So please delete the bucket and stack manually 

# Unit testing
- Navigate to ../covidcases/application/lambdas
- pytest -s
