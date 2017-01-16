import os
import sys
from gcp import bucket as gcpbucket
from gcp import object as gcpobject
from cli.gcp import project as cligcpproject
from cli.gcp import bucket as cligcpbucket
from cli.gcp import object as cligcpobject
from ceph import bucket as cephbucket
from ceph import  object as cephobject
from cli.ceph import bucket as clicephbucket
from cli.ceph import object as clicephobject


def progress(count, total):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))
    percents = round(100.0 * count / float(total), 1)
    bar = '#' * filled_len + ' ' * (bar_len - filled_len)
    sys.stdout.write('[%s] %s%s ... %s/%s\r' % (bar, percents, '%', count, total))
    sys.stdout.flush()
    if count == total:
        print '\n[GCB] Backup finish'


def bucket_backup(ceph_bucket, gcp_project, gcp_bucket):
    cephbuckets = cephbucket.list()
    if bool([(bucket.name) for bucket in cephbuckets if ceph_bucket == bucket.name]):
        gcpbuckets = gcpbucket.list(gcp_project)
        if 'items' in gcpbuckets.keys():
            if bool([(value['name']) for value in gcpbuckets['items'] if gcp_bucket == value['name']]):
                ceph_objects = cephobject.list(ceph_bucket)
                # objects_count = sum(1 for key in ceph_objects)
                # index = 1
                for key in ceph_objects:
                    cephobject.download(ceph_bucket, key.name)
                    gcp_object = gcpobject.upload(gcp_bucket, key.name, key.name)
                    done = None
                    while done is None:
                        status, done = gcp_object.next_chunk()
                        if status:
                            sys.stdout.write("Uploaded %d%%.\r" % int(status.progress() * 100))
                            sys.stdout.flush()
                    os.remove(key.name)
                    print "%s upload complete" % key.name
                    # progress(index, objects_count)
                    # index += 1
            else:
                print "[GCB] %s not in your GCP" % gcp_bucket
    else:
        print "[GCB] %s not in your Ceph" % ceph_bucket


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


def main():
    if len(sys.argv) < 2:
        message_alert(
            "Usage: gcb [-D]",
            gcp="Provides the CLI access to the GCP",
            ceph="Provides the CLI access to the CEPH",
            backup="CEPH Bucket backup to GCP Bucket"
        )
    else:
        if sys.argv[1] == 'gcp':
            if len(sys.argv) > 2:
                if sys.argv[2] == 'project':
                    cligcpproject.project_cli()
                elif sys.argv[2] == 'bucket':
                    cligcpbucket.bucket_cli()
                elif sys.argv[2] == 'object':
                    cligcpobject.object_cli()
                else:
                    message_alert(
                        "Usage: gcb gcp [-D]",
                        project="Provides the project CLI access to the GCP",
                        bucket="Provides the bucket CLI access to the GCP",
                        object="Provides the object CLI access to the GCP",
                    )
            else:
                message_alert(
                    "Usage: gcb gcp [-D]",
                    project="Provides the project CLI access to the GCP",
                    bucket="Provides the bucket CLI access to the GCP",
                    object="Provides the object CLI access to the GCP",
                )
        elif sys.argv[1] == 'ceph':
            if len(sys.argv) > 2:
                if sys.argv[2] == 'bucket':
                    clicephbucket.bucket_cli()
                elif sys.argv[2] == 'object':
                    clicephobject.object_cli()
                else:
                    message_alert(
                        "Usage: gcb ceph [-D]",
                        bucket="Provides the bucket CLI access to the CEPH",
                        object="Provides the object CLI access to the CEPH",
                    )
            else:
                message_alert(
                    "Usage: gcb ceph [-D]",
                    bucket="Provides the bucket CLI access to the CEPH",
                    object="Provides the object CLI access to the CEPH",
                )
        elif sys.argv[1] == 'backup':
            if len(sys.argv) != 5:
                message_alert(
                    "Usage: gcb backup [ceph_bucket] [gcp_project] [gcp_bucket]",
                    none="none"
                )
            else:
                ceph_bucket = sys.argv[2]
                gcp_project = sys.argv[3]
                gcp_bucket = sys.argv[4]
                bucket_backup(ceph_bucket, gcp_project, gcp_bucket)
        else:
            message_alert(
                "Usage: gcb [-D]",
                gcp="Provides the CLI access to the GCP",
                ceph="Provides the CLI access to the CEPH",
                backup="CEPH Bucket backup to GCP Bucket"
            )


if __name__ == '__main__':
    main()
