sam build && \
sam package --s3-bucket wordle-lambda-code --output-template-file packaged.yaml && \
aws cloudformation deploy --template-file /Users/rama/work/wordle-information-theory/python/wordle/sam/packaged.yaml --stack-name wordle-lambda-stack --capabilities CAPABILITY_IAM
