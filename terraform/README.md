# Deploy AWS-Infrastructure

All CLI-Commands need to be executed in `./aws/ressources`

## intialize Terraform

`terraform init`

# Dev Environment

## Load Workspace

`terraform workspace select dev`

## Plan Dev Environment

`terraform plan -var-file="main.dev.tfvars"`

## Deploy Dev Environment

`terraform apply -var-file="main.dev.tfvars"`

# Prod Environment

## Load Workspace

`terraform workspace select prod`

## Plan Prod Environment

`terraform plan -var-file="main.prod.tfvars"`

## Deploy Prod Environment

`terraform apply -var-file="main.prod.tfvars"`

aws_api_gateway_rest_api-id = 52hnb7wjvc
aws_api_gateway_rest_api-root-id = 2hg9n8x6q0
