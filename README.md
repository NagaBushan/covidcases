# covidcases


GEtting the covid data from website,https://api.coronavirus.data.gov.uk/v1/data?filters=areaType=nation;areaName=england&structure={%22date%22:%22date%22,%22newCases%22:%22newCasesByPublishDate%22}

creating a CSV file with headers as Date, New cases
publishing into S3 bucket
Using AWS lambda for the implementation
Terraform scripts to deploy the code into AWS
