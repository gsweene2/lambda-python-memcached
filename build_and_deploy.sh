#!/bin/bash

# Rm previous package
rm -rf package

# Install Dependencies
pipenv run pip install -r <(pipenv lock -r) --target package/

# Copy code to dir
cp src/* package/

# Create a deployment package out of the files in package
cd package && zip -r my-deployment-package.zip ./*

# Update Function Code
aws lambda update-function-code --function-name lambda-python-memcached --zip-file fileb://my-deployment-package.zip --region us-east-2
