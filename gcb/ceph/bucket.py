import connection


def list():
    response = connection.connection().get_all_buckets()
    return response


def create(bucket_name):
    response = connection.connection().create_bucket(bucket_name)
    return response


def delete(bucket_name):
    response = connection.connection().delete_bucket(bucket_name)
    return response
