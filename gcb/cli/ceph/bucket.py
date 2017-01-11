import sys
from ceph import bucket as cephbucket
from boto.exception import S3ResponseError


def list():
    ceph_bucket_list = cephbucket.list()
    print "{name:<40} \t {created:<25}".format(
        name='BUCKET NAME',
        created='CREATED TIME',
    )
    if len(ceph_bucket_list) != 0:
        for bucket in ceph_bucket_list:
            print "{name:<40} \t {created:<20}".format(
                name=bucket.name,
                created=bucket.creation_date
            )
    else:
        print '(empty)'


def create(bucket_name):
    try:
        if bool([(bucket.name) for bucket in cephbucket.list() if bucket_name == bucket.name]):
            print "[ERROR] Your Bucket name is existing"
        else:
            if cephbucket.create(bucket_name):
                print "[CEPH] CREATED %s SUCCESS !" % bucket_name
    except S3ResponseError, error:
        print "[ERROR] CEPH Bucket create fail, %s" % error.error_code


def delete(bucket_name):
    try:
        cephbucket.delete(bucket_name)
        print "[CEPH] DELETE %s SUCCESS !" % bucket_name
    except S3ResponseError, error:
        print "[ERROR] CEPH Bucket delete fail, %s" % error.error_code


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
            list="List all Bucket in CEPH",
            create="Create a Bucket in CEPH",
            delete="Delete a Bucket in CEPH"
        )
    else:
        if sys.argv[3] == 'list':
            if len(sys.argv) != 4:
                message_alert(
                    "Usage: gcb ceph bucket list",
                    none="none"
                )
            else:
                list()
        elif sys.argv[3] == 'create':
            if len(sys.argv) != 5:
                message_alert(
                    "Usage: gcb ceph bucket create [bucket_name]",
                    none="none"
                )
            else:
                create(sys.argv[4])
        elif sys.argv[3] == 'delete':
            if len(sys.argv) != 5:
                message_alert(
                    "Usage: gcb ceph bucket delete [bucket_name]",
                    none="none"
                )
            else:
                delete(sys.argv[4])
        else:
            message_alert(
                "Usage: gcb gcp bucket [-D]",
                list="List all Bucket in CEPH",
                create="Create a Bucket in CEPH",
                delete="Delete a Bucket in CEPH"
            )
