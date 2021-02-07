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
  default     = "/usr/local/bin/pip"
  description = "Path to your pip installation"
}

variable "python_version" {
  type = string
  default = "python3.8"
  description = "Python version"

}
