import json
import sys
import gcpcredential


def list():
    try:
        request = gcpcredential.gcp_credential('cloudresourcemanager')
        response = request.projects().list().execute()
        encodedjson = json.dumps(response['projects'], sort_keys=True, indent=4)
        print encodedjson
    except:
        sys.exit("get project list fail.")


def create(project_name, project_id):
    try:
        config = {
            'project_id': project_id,
            'name': project_name
        }
        request = gcpcredential.gcp_credential('cloudresourcemanager')
        response = request.projects().create(body=config).execute()
        print("create [%s] project success" % project_name)
        encodedjson = json.dumps(response, sort_keys=True, indent=4)
        print encodedjson
    except:
        sys.exit("create project fail.")


def delete(project_id):
    try:
        request = gcpcredential.gcp_credential('cloudresourcemanager').projects()
        response = request.delete(projectId=project_id).execute()
        print("delete [%s] success" % project_id)
        encodedjson = json.dumps(response, sort_keys=True, indent=4)
        print encodedjson
    except:
        sys.exit("delete prject fail")
