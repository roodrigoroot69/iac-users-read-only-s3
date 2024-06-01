from pulumi_aws import iam


policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:ListAllMyBuckets",
            "Resource": "*"
        }
    ]
}

policy = iam.Policy("listS3BucketsPolicy",
    description="Policy to allow listing all S3 buckets",
    policy=policy_document)