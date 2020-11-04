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

# Commands on ec2

1. install mount helper `sudo yum install -y amazon-efs-utils`
2. mount filesystem
   a. create efs directory `sudo mkdir efs`
   b. mount efs with file system id `sudo mount -t efs -o tls fs-2226b27a:/ efs`

3) install python `sudo yum install python3 -y`

4. install requirements `sudo pip3 --no-cache-dir install -t efs/lib torch torchvision numpy`
   -> aktuelles Problem MemoryError aber funktioniert
