import sys
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

def gcp_credential(api):
    try:
        credentials = GoogleCredentials.get_application_default()
        service = discovery.build(api, 'v1', credentials=credentials)
        return service
    except:
        sys.exit("[GCP] Promise Undefined.")
