import credential


def list():
    request = credential.gcp_credential('cloudresourcemanager').projects()
    response = request.list().execute()
    print response


def create(project_name, project_id):
    config = {
        'project_id': project_id,
        'name': project_name
     }
    request = credential.gcp_credential('cloudresourcemanager').projects()
    response = request.create(body=config).execute()
    print response


def delete(project_id):
    request = credential.gcp_credential('cloudresourcemanager').projects()
    response = request.delete(projectId=project_id).execute()
    print response
