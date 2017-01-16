import credential
import magic
from googleapiclient import http


def list(bucket_name):
    request = credential.gcp_credential('storage').objects()
    response = request.list(bucket=bucket_name).execute()
    return response


def upload(bucket_name, file_path, file_name):
    body = {
        'name': file_name,
    }
    mime = magic.Magic(mime=True)
    fileType = mime.from_file(file_path)
    chunk_size = 5 * 1024 * 1024
    with open(file_path, 'rb') as f:
        media = http.MediaFileUpload(file_path,
                                     mimetype=fileType,
                                     chunksize=chunk_size,
                                     resumable=True)
        request = credential.gcp_credential('storage').objects()
        response = request.insert(bucket=bucket_name,
                                  body=body,
                                  media_body=media)
        return response


def delete(bucket_name, object_name):
    request = credential.gcp_credential('storage').objects()
    request.delete(bucket=bucket_name, object=object_name).execute()
