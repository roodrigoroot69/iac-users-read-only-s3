from pulumi_aws import iam


user_one_s3 = iam.User("user_one_s3",
    name="user_one_s3")

user_two_s3 = iam.User("user_two_s3",
    name="user_two_s3")

user_three_s3 = iam.User("user_three_s3",
    name="user_three_s3")

login_profile_one = iam.UserLoginProfile(f"{user_one_s3}LoginProfile",
        user=user_one_s3.name,
        password_reset_required=True)


login_profile_two = iam.UserLoginProfile(f"{user_two_s3}LoginProfile",
        user=user_two_s3.name,
        password_reset_required=True)

login_profile_three = iam.UserLoginProfile(f"{user_three_s3}LoginProfile",
        user=user_three_s3.name,
        password_reset_required=True)
