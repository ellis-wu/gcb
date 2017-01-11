import connection
from boto.s3.key import Key


def list(bucket_name):
    response = connection.connection().get_bucket(bucket_name)
    return response


def upload(bucket_name, file_path, file_name):
    bucket = connection.connection().get_bucket(bucket_name)
    key = Key(bucket)
    key.name = file_name
    key.set_contents_from_filename(file_path)


def delete(bucket_name, file_name):
    bucket = connection.connection().get_bucket(bucket_name)
    bucket.delete_key(file_name)


def download(bucket_name, file_name):
    bucket = connection.connection().get_bucket(bucket_name)
    key = bucket.get_key(file_name)
    key.get_contents_to_filename('./%s' % file_name)
