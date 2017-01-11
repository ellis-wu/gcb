import sys
import boto
import boto.s3.connection
from boto.exception import S3ResponseError
from boto.s3.connection import S3Connection


ACCESS_KEY = 'XCCUR6083YYW9U8NZ0OZ'
SECRET_KEY = '2xZOUNzrqCmOvkTf0cOaOafvoSpQUb0BXj6nlbg7'
S3_HOST = '127.0.0.1'
S3_PORT = '8080'


def connection():
    if ACCESS_KEY is None and SECRET_KEY is None and S3_HOST is None and S3_PORT is None:
        sys.exit("ERROR : You must setting S3_ACCESS_KEY, S3_SECRET_KEY, S3_HOST and S3_PORT in config")

    try:
        if S3_HOST != 's3.amazonaws.com':
            s3_connect = boto.connect_s3(
                aws_access_key_id=ACCESS_KEY,
                aws_secret_access_key=SECRET_KEY,
                host=S3_HOST,
                port=int(S3_PORT),
                is_secure=False,
                calling_format=boto.s3.connection.OrdinaryCallingFormat(),
            )
            return s3_connect
        else:
            s3_connect = S3Connection(ACCESS_KEY, SECRET_KEY)
            return s3_connect
    except S3ResponseError, error:
        sys.exit("[CEPH] Promise Undefined.")
