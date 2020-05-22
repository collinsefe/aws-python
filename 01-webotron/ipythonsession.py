In [1]: import boto3

In [3]: session = boto3.Session(profile_name='default')

In [4]: s3 = session.resource('s3')
