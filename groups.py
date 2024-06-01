from pulumi_aws import iam


group = iam.Group("S3BucketReadOnlyListerGroup",
    name="S3BucketReadOnlyListerGroup")


