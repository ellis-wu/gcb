import sys
import json
from googleapiclient import errors
from gcp import project as gcpproject


def list():
    try:
        gcp_project_list = gcpproject.list()
        print "{name:<15} \t {projectid:<20} \t {state:10} \t {created:<25}".format(
            name='PROJECT NAME',
            projectid='PROJECT ID',
            state='STATE',
            created='CREATED TIME',
        )
        for value in gcp_project_list['projects']:
            print "{name:<15} \t {projectid:<20} \t {stat:10} \t {created:<25}".format(
                name=value['name'],
                projectid=value['projectId'],
                stat=value['lifecycleState'],
                created=value['createTime'],
            )
    except errors.HttpError, e:
        print "[ERROR] GCP Bucket create fail, %s" % json.loads(e.content)['error']['message']


def message_alert(usage, **kwargs):
    print "{usage:<70}".format(
        usage=usage,
    )
    if "none" not in kwargs:
        print "\nAvailable commands:"
        for command, descript in kwargs.iteritems():
            print "  {command:<10} \t {description:<50}".format(
                command=command,
                description=descript
            )


def project_cli():
    if len(sys.argv) < 4:
        message_alert(
            "Usage: gcb gcp project [-D]",
            list="List user all projects in GCP"
        )
    elif len(sys.argv) > 4:
        message_alert(
            "Usage: gcb gcp project list",
            none="none"
        )
    else:
        if sys.argv[3] == 'list':
            list()
