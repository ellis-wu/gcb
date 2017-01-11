import sys
import json
from googleapiclient import errors
from gcp import object as gcpobject


def list(bucket_name):
    try:
        gcp_object_list = gcpobject.list(bucket_name)
        print "{name:<30} \t {size:<10} \t {type:<15} \t {modified:<25}".format(
            name='OBJECT NAME',
            size='SIZE',
            type='TYPE',
            modified='MODIFIED',
        )
        if 'items' in gcp_object_list.keys():
            for value in gcp_object_list['items']:
                print "{name:<30} \t {size:<10} \t {type:<15} \t {modified:<25}".format(
                    name=value['name'],
                    size=value['size'],
                    type=value['contentType'],
                    modified=value['updated'],
                )
        else:
            print '(empty)'
    except errors.HttpError, e:
        print "[ERROR] GCP Object list fail, %s" % json.loads(e.content)['error']['message']


def upload(bucket_name, file_path, file_name):
    try:
        gcp_object_upload = gcpobject.upload(bucket_name, file_path, file_name)
        print "[GCP] UPLOAD %s SUCCESS !" % gcp_object_upload['name']
    except errors.HttpError, e:
        print "[ERROR] GCP object upload fail, %s" % json.loads(e.content)['error']['message']


def delete(bucket_name, file_name):
    try:
        gcpobject.delete(bucket_name, file_name)
        print "[GCP] DELETE %s SUCCESS !" % bucket_name
    except errors.HttpError, e:
        print "[ERROR] GCP object delete fail, %s" % json.loads(e.content)['error']['message']


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


def object_cli():
    if len(sys.argv) < 4:
        message_alert(
            "Usage: gcb gcp object [-D]",
            list="List user all Objects in GCP Bucket",
            upload="Upload a file to GCP Bucket",
            delete="Delete a Objects in GCP Bucket"
        )
    else:
        if sys.argv[3] == 'list':
            if len(sys.argv) != 5:
                message_alert(
                    "Usage: gcb gcp object list [bucket_name]",
                    none="none"
                )
            else:
                list(sys.argv[4])
        elif sys.argv[3] == 'upload':
            if len(sys.argv) != 7:
                message_alert(
                    "Usage: gcb gcp object upload [bucket_name] [file_path] [file_name]",
                    none="none"
                )
            else:
                upload(sys.argv[4], sys.argv[5], sys.argv[6])
        elif sys.argv[3] == 'delete':
            if len(sys.argv) != 6:
                message_alert(
                    "Usage: gcb gcp object delete [bucket_name] [file_name]",
                    none="none"
                )
            else:
                delete(sys.argv[4], sys.argv[5])
        else:
            message_alert(
                "Usage: gcb gcp object [-D]",
                list="List user all Objects in GCP Bucket",
                upload="Upload a file to GCP Bucket",
                delete="Delete a Objects in GCP Bucket"
            )
