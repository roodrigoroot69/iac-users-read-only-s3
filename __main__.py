import pulumi
from pulumi_aws import s3
from pulumi_aws import iam

from buckets import bucket_two, bucket_one
from groups import group
from policies import policy
from users import user_one_s3, user_two_s3, user_three_s3




group_policy_attachment = iam.GroupPolicyAttachment("groupPolicyAttachment",
    group=group.name,
    policy_arn=policy.arn)





user_group_membership_one = iam.UserGroupMembership(f"{user_one_s3}UserGroupMembership",
    user=user_one_s3.name,
    groups=[group.name])

user_group_membership_two = iam.UserGroupMembership(f"{user_two_s3}UserGroupMembership",
    user=user_two_s3.name,
    groups=[group.name])

user_group_membership_three = iam.UserGroupMembership(f"{user_three_s3}UserGroupMembership",
    user=user_three_s3.name,
    groups=[group.name])



pulumi.export("group_name", group.name)
pulumi.export("policy_arn", policy.arn)
pulumi.export("Bucket One", bucket_one.id)
pulumi.export("Bucket Two", bucket_two.id)


