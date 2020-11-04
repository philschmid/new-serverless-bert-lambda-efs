https://github.com/serverless/serverless/issues/7848

https://aws.amazon.com/de/blogs/aws/new-a-shared-file-system-for-your-lambda-functions/

https://aws.amazon.com/de/blogs/aws/new-for-amazon-efs-iam-authorization-and-access-points/

```yaml
functions:
  write-post:
    handler: handler.writePost

resources:
  extensions:
    WriteDashPostLambdaFunction:
      Properties:
        FileSystemConfigs:
          - Arn: arn:aws:elasticfilesystem:us-east-1:111111111111:access-point/fsap-abc123xyz45glhfjk
            LocalMountPath: /mnt/bigLibs
```

# Local Set up for testing

**1. install pip packages into local directory**

```bash
pip install -r requirements.txt --target ./lib
```

**2. set env for path so local packages will be used**

```
LOCAL_PIP_PATH_SL="$(pwd)/lib"
```
