# Here's an example of how to use Boto3 to interact with AWS CloudFormation:

# Using AWS CLI Commands:

#You can also execute AWS CLI commands directly from Python using the subprocess module. This allows you to leverage the full power of the AWS CLI within your Python scripts.

#Here's an example of executing an AWS CLI command to create a CloudFormation stack:

import boto3


# Create a CloudFormation client
cf_client = boto3.client('cloudformation')

# Create a stack
stack_name = 'MyStack'
template_body = '''
{
  "Resources": {
    "MyEC2Instance": {
      "Type": "AWS::EC2::Instance",
      "Properties": {
        "ImageId": "ami-12345678",
        "InstanceType": "t2.micro"
      }
    }
  }
}
'''
response = cf_client.create_stack(StackName=stack_name, TemplateBody=template_body)
print(response)

import subprocess

stack_name = 'MyStack'
template_body = '''
{
  "Resources": {
    "MyEC2Instance": {
      "Type": "AWS::EC2::Instance",
      "Properties": {
        "ImageId": "ami-12345678",
        "InstanceType": "t2.micro"
      }
    }
  }
}
'''

# Execute AWS CLI command to create a stack
subprocess.run(['aws', 'cloudformation', 'create-stack', '--stack-name', stack_name, '--template-body', template_body])
