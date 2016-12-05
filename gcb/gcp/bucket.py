import json
import sys
import credential


def list(project):
    try:
        request = credential.gcp_credential('storage').buckets()
        response = request.list(project=project).execute()
        encodedjson = json.dumps(response, sort_keys=True, indent=4)
        print encodedjson
    except:
        sys.exit('list bucket fail.')


def get(bucket):
    try:
        request = credential.gcp_credential('storage').buckets()
        response = request.get(bucket=bucket).execute()
        encodedjson = json.dumps(response, sort_keys=True, indent=4)
        print encodedjson
    except:
        sys.exit('get bucket fail')


def create(project, bucket):
    try:
        config = {
            'name': bucket
        }
        request = credential.gcp_credential('storage').buckets()
        response = request.insert(project=project, body=config).execute()
        print("create [%s] bucket success" % bucket)
        encodedjson = json.dumps(response, sort_keys=True, indent=4)
        print encodedjson
    except:
        sys.exit('create bucket fail')


def delete(bucket):
    try:
        request = credential.gcp_credential('storage').buckets()
        request.delete(bucket=bucket).execute()
        print("delete [%s] bucket success" % bucket)
    except:
        sys.exit('delete bucket fail')
