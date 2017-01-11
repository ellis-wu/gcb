import credential


def list(project_id):
    request = credential.gcp_credential('storage').buckets()
    response = request.list(project=project_id).execute()
    return response


def get(bucket_name):
    request = credential.gcp_credential('storage').buckets()
    response = request.get(bucket=bucket_name).execute()
    return response


def create(project_id, bucket_name):
    config = {
        'name': bucket_name
    }
    request = credential.gcp_credential('storage').buckets()
    response = request.insert(project=project_id, body=config).execute()
    return response


def delete(bucket_name):
    request = credential.gcp_credential('storage').buckets()
    response = request.delete(bucket=bucket_name).execute()
    return response
