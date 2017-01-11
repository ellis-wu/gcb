import sys
import json
from googleapiclient import errors
from gcp import bucket as gcpbucket


def list(project_id):
    try:
        gcp_bucket_list = gcpbucket.list(project_id)
        print "{name:<40} \t {created:<25}".format(
            name='BUCKET NAME',
            created='CREATED TIME',
        )
        if 'items' in gcp_bucket_list.keys():
            for value in gcp_bucket_list['items']:
                print "{name:<40} \t {created:<25}".format(
                    name=value['name'],
                    created=value['timeCreated'],
                )
        else:
            print '(empty)'
    except errors.HttpError, e:
        print "[ERROR] GCP Bucket list fail, %s" % json.loads(e.content)['error']['message']


def get(bucket_name):
    try:
        gcp_bucket_get = gcpbucket.get(bucket_name)
        print "{title_name:<40} \t {title_created:<25}\n{bucket_name:<40} \t {bucket_created:<25}".format(
            title_name='BUCKET NAME',
            title_created='CREATED TIME',
            bucket_name=gcp_bucket_get['name'],
            bucket_created=gcp_bucket_get['timeCreated'],
        )
    except errors.HttpError, e:
        print "[ERROR] GCP Bucket list fail, %s" % json.loads(e.content)['error']['message']


def create(project_id, bucket_name):
    try:
        gcp_bucket_create = gcpbucket.create(project_id, bucket_name)
        print "[GCP] CREATED %s SUCCESS !" % gcp_bucket_create['name']
    except errors.HttpError, e:
        print "[ERROR] GCP Bucket create fail, %s" % json.loads(e.content)['error']['message']


def delete(bucket_name):
    try:
        gcpbucket.delete(bucket_name)
        print "[GCP] DELETE %s SUCCESS !" % bucket_name
    except errors.HttpError, e:
        print "[ERROR] GCP Bucket delete fail, %s" % json.loads(e.content)['error']['message']


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


def bucket_cli():
    if len(sys.argv) < 4:
        message_alert(
            "Usage: gcb gcp bucket [-D]",
            list="List user all Bucket in GCP",
            get="Get a specified Bucket in GCP",
            create="Create a Bucket in GCP",
            delete="Delete a Bucket in GCP"
        )
    else:
        if sys.argv[3] == 'list':
            if len(sys.argv) != 5:
                message_alert(
                    "Usage: gcb gcp bucket list [project_id]",
                    none="none"
                )
            else:
                list(sys.argv[4])
        elif sys.argv[3] == 'get':
            if len(sys.argv) != 5:
                message_alert(
                    "Usage: gcb gcp bucket get [bucket_name]",
                    none="none"
                )
            else:
                get(sys.argv[4])
        elif sys.argv[3] == 'create':
            if len(sys.argv) != 6:
                message_alert(
                    "Usage: gcb gcp bucket create [project_id] [bucket_name]",
                    none="none"
                )
            else:
                create(sys.argv[4], sys.argv[5])
        elif sys.argv[3] == 'delete':
            if len(sys.argv) != 5:
                message_alert(
                    "Usage: gcb gcp bucket list [bucket_name]",
                    none="none"
                )
            else:
                delete(sys.argv[4])
        else:
            message_alert(
                "Usage: gcb gcp bucket [-D]",
                list="List user all Bucket in GCP",
                get="Get a specified Bucket in GCP",
                create="Create a Bucket in GCP",
                delete="Delete a Bucket in GCP"
            )
