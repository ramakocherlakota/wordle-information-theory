if [ ! -f ./env.sh ]
then
   echo "Create env.sh based on env-template.sh, filling in the necessary data"
   exit 1
fi

source env.sh

$(aws s3api head-bucket --bucket "$CODE_BUCKET" 2>/dev/null)
if [ $? != 0 ]
then
    echo "creating code bucket s3://$CODE_BUCKET"
    aws s3 mb "s3://$CODE_BUCKET"
fi

sam build -t ./template.yaml \
  --parameter-overrides "ParameterKey=LambdaMemorySizeMb,ParameterValue=$LAMBDA_MEMORY_SIZE_MB ParameterKey=LambdaFunctionName,ParameterValue=$LAMBDA_FUNCTION_NAME ParameterKey=LambdaRuntime,ParameterValue=$LAMBDA_RUNTIME ParameterKey=LambdaUrlAuthType,ParameterValue=$LAMBDA_URL_AUTH_TYPE ParameterKey=LambdaUrlCorsOrigin,ParameterValue=$LAMBDA_URL_CORS_ORIGIN ParameterKey=SubnetIds,ParameterValue=$SUBNET_IDS ParameterKey=SecurityGroupIds,ParameterValue=$SECURITY_GROUP_IDS ParameterKey=EfsMountPoint,ParameterValue=$EFS_MOUNT_POINT ParameterKey=EfsAccessPointArn,ParameterValue=$EFS_ACCESS_POINT_ARN " && \
    sam package --s3-bucket $CODE_BUCKET --output-template-file packaged.yaml && \
    aws cloudformation deploy --template-file packaged.yaml --stack-name $STACK_NAME --capabilities CAPABILITY_IAM \
  --parameter-overrides LambdaMemorySizeMb=$LAMBDA_MEMORY_SIZE_MB LambdaRuntime=$LAMBDA_RUNTIME LambdaUrlAuthType=$LAMBDA_URL_AUTH_TYPE LambdaFunctionName=$LAMBDA_FUNCTION_NAME LambdaUrlCorsOrigin=$LAMBDA_URL_CORS_ORIGIN SubnetIds=$SUBNET_IDS SecurityGroupIds=$SECURITY_GROUP_IDS EfsMountPoint=$EFS_MOUNT_POINT EfsAccessPointArn=$EFS_ACCESS_POINT_ARN && \
    echo "Function URL=`aws lambda list-function-url-configs --function-name $LAMBDA_FUNCTION_NAME | jq '.FunctionUrlConfigs[].FunctionUrl '`"

