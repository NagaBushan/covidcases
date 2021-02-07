# Covid cases

# Terraform steps
Pre-requisites
- An active AWS account
- aws_access_key_id and aws_secret_access_key has to be generated

Deployment of AWS lambda using terraform scripts.
- cd to the folder <Base_dir>/covidcases/infrastructure
- tf init
- tf plan
	- cat ~/.aws/credentials
	- copy and past access_key, secret_key
- tf apply
	- copy and past access_key, secret_key

Testing
-
- After successfully deploying AWS lambda, testing can be done using AWS lambda consle.
- Search for Lambda in AWS console and select
- There is test button available on console and click on it and mention a name for the test
- Then click again on test button
- The logs output will be displayed on the screen
-  For success messsage it will display as "Covid data extracted successfully into S3 bucket"
- Then the resport in the csv format can be seen in s3 bucket, s3: tf-covid-cases/./tmp/covid.csv

>Please note, the s3 tf-covid-cases bucket needs to be manually deleted. Terraform destroy is not handled to delete it.


# Serverless framework

Pre-requisites
- Make sure you have serverless framework installed , follow these steps mentioned in the below link installed, https://www.serverless.com/framework/docs/providers/aws/guide/installation/
-  An active AWS account
- aws_access_key_id and aws_secret_access_key has to be generated

Steps
-
- npm install --save serverless-python-requirements
- sls deploy (This command will package and deploy into the aws)
- After successful deployment use the following comand to test it locally
	- sls invoke -f covid-cases ( this will invoke the lambda in aws account, the logs are displayed in the console)
>Please note, the s3 sls-covid-cases bucket needs to be manually deleted. Terraform destroy is not handled to delete it.


# Unit testing
- Navigate to ../covidcases/application/lambdas
- pytest -s
