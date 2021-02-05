provider "aws" {
  region = var.region
  access_key = var.access_key
  secret_key = var.secret_key
}

resource "aws_lambda_function" "covid-cases" {
  function_name = "covid-cases"

  filename = "covid-new-cases.zip"
  source_code_hash = "${data.archive_file.lambda_zip.output_base64sha256}"
  handler = "handler.handle"
  runtime = "python3.8"
  environment {
    variables = {
      "COVID_CASES_API"= "https://api.coronavirus.data.gov.uk/v1/data?filters=areaType=nation;areaName=england&structure={%22date%22:%22date%22,%22newCases%22:%22newCasesByPublishDate%22}"
    }
  }

  role = aws_iam_role.lambda_exec.arn
}

resource "aws_iam_role" "lambda_exec" {
  name = "serverless-covid-lambda"

  assume_role_policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Action": "sts:AssumeRole",
        "Principal": {
          "Service": "lambda.amazonaws.com"
        },
        "Effect": "Allow",
        "Sid": ""
      }
    ]
}
EOF
}

resource "aws_cloudwatch_event_rule" "every_five_minutes" {
    name = "covid-scheduler"
    description = " Covid scheduler"
    schedule_expression = "rate(5 minutes)"
}

resource "aws_cloudwatch_event_target" "check_covid_cases_every_five_minute" {
  rule      = "${aws_cloudwatch_event_rule.every_five_minutes.name}"
  target_id = "covid-cases"
  arn       = "${aws_lambda_function.covid-cases.arn}"
}


resource "aws_lambda_permission" "allow_cloudwatch_to_call_check_foo" {
  statement_id  = "AllowExecutionFromCloudWatch"
  action        = "lambda:InvokeFunction"
  function_name = "${aws_lambda_function.covid-cases.function_name}"
  principal     = "events.amazonaws.com"
  source_arn    = "${aws_cloudwatch_event_rule.every_five_minutes.arn}"
}
resource "aws_lambda_permission" "allow_log_groups_to_log" {
  statement_id = "AllowToWriteLogs"
  action        = "lambda:InvokeFunction"
  function_name = "${aws_lambda_function.covid-cases.function_name}"
  principal     = "logs.amazonaws.com"
  source_arn = "${aws_cloudwatch_log_group.covid-cases.arn}"
}

resource "aws_cloudwatch_log_group" "covid-cases" {
  name = "/aws/lambda/covid-cases"
  retention_in_days = 90
}

data "archive_file" "lambda_zip" {
  type = "zip"
  source_dir = "../application/lambdas"
  output_path = "covid-new-cases.zip"
}
