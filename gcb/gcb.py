#!/usr/bin/env python
from gcp import project
from gcp import bucket
from gcp import object


def main():
    project.list()
    # project.create('gcb-test1', 'ellis-gcb-test1')
    # project.delete('ellis-gcb-test1')

    bucket.list('gcb-project')
    # bucket.get('gcb-test-bucket1')
    # bucket.create('gcb-project', 'gcb-test-bucket2')
    # bucket.delete('gcb-test-bucket2')

    object.list('gcb-test-bucket1')
    # object.upload('gcb-test-bucket1', 'gcb.py', 'gcb.py')
    # object.delete('gcb-test-bucket1', 'gcb.py')

if __name__ == '__main__':
    main()
