variable "region" {
  description = "AWS Region"
  type = string
  default = "eu-west-2"
}

variable "access_key" {
  description = "value"
  type = string
}

variable "secret_key" {
  description = "AWS secret key"
  type = string
}

variable "pip_path" {
  type        = string
  default     = "pip"
  description = "Path to your pip installation"
}

variable "python_version" {
  type = string
  default = "python3.8"
  description = "Python version"

}

variable "covid_cases_bucket" {
  type = string
  default = "ttf-covid-cases"
  description = "covid cases bucket"
}

variable "cron_expression" {
  type = string
  default = "rate(5 minutes)"
  description = "Cron expression"
}
