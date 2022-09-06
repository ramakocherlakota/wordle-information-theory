# This file has the data that you need to build the lambda.  Copy the file to env.sh and
# customize if for your setup.

# SAM build and lambda basic info 
export CODE_BUCKET=
export STACK_NAME=
export LAMBDA_TIMEOUT_SECONDS=
export LAMBDA_MEMORY_SIZE_MB=
export LAMBDA_FUNCTION_NAME=

# This should be some version of python >= 3.9
export LAMBDA_RUNTIME=

export LAMBDA_URL_AUTH_TYPE=
export LAMBDA_URL_CORS_ORIGIN=

# VPC config (you should put the lambda in the same VPC as the EFS volume)
export SUBNET_IDS=
export SECURITY_GROUP_IDS=

export EFS_MOUNT_POINT=
export EFS_ACCESS_POINT_ARN=



