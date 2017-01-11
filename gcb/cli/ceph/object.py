import sys
from ceph import object as cephobject
from boto.exception import S3ResponseError


def list(bucket_name):
    ceph_object_list = cephobject.list(bucket_name)
    print "{name:<30} \t {size:<10} \t {modified:<25}".format(
        name='OBJECT NAME',
        size='SIZE',
        modified='MODIFIED',
    )
    for key in ceph_object_list:
        print "{name:<30} \t {size:<10} \t {modified:<25}".format(
            name=key.name,
            size=key.size,
            modified=key.last_modified
        )


def upload(bucket_name, file_path, file_name):
    try:
        cephobject.upload(bucket_name, file_path, file_name)
        print "[CEPH] UPLOAD %s SUCCESS !" % file_name
    except S3ResponseError, error:
        print "[ERROR] CEPH Object upload fail, %s" % error.error_code


def delete(bucket_name, file_name):
    if cephobject.list(bucket_name).get_key(file_name):
        try:
            cephobject.delete(bucket_name, file_name)
            print "[CEPH] DELETE %s SUCCESS !" % file_name
        except S3ResponseError, error:
            print "[ERROR CEPH Object deletet fail, %s]" % error.error_code
    else:
        print "[ERROR] %s NOT IN %s" % (file_name, bucket_name)


def download(bucket_name, file_name):
    if cephobject.list(bucket_name).get_key(file_name):
        try:
            cephobject.download(bucket_name, file_name)
            print "[CEPH] DOWDLOAD %s SUCCESS !" % file_name
        except S3ResponseError, error:
            print "[ERROR CEPH Object deletet fail, %s]" % error.error_code
    else:
        print "[ERROR] %s NOT IN %s" % (file_name, bucket_name)


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
            "Usage: gcb gcp bucket [-D]",
            list="List all Bucket in CEPH",
            upload="Upload a file to CEPH Bucket",
            delete="Delete a Bucket in CEPH",
            download="Download a file in CEPH Bucket"
        )
    else:
        if sys.argv[3] == 'list':
            if len(sys.argv) != 5:
                message_alert(
                    "Usage: gcb ceph object list [bucket_name]",
                    none="none"
                )
            else:
                list(sys.argv[4])
        elif sys.argv[3] == 'upload':
            if len(sys.argv) != 7:
                message_alert(
                    "Usage: gcb ceph object upload [bucket_name] [file_name]",
                    none="none"
                )
            else:
                upload(sys.argv[4], sys.argv[5], sys.argv[6])
        elif sys.argv[3] == 'delete':
            if len(sys.argv) != 6:
                message_alert(
                    "Usage: gcb ceph object delete [bucket_name] [file_path] [file_name]",
                    none="none"
                )
            else:
                delete(sys.argv[4], sys.argv[5])
        elif sys.argv[3] == 'download':
            if len(sys.argv) != 6:
                message_alert(
                    "Usage: gcb ceph object download [bucket_name] [file_path] [file_name]",
                    none="none"
                )
            else:
                download(sys.argv[4], sys.argv[5])
