#!/usr/bin/env python
import gcpproject
import gcpbucket


def main():
    # gcpproject.list()
    # gcpproject.create('gcb-test1', 'ellis-gcb-test1')
    # gcpproject.delete('ellis-gcb-test1')

    # gcpbucket.list('gcb-project')
    # gcpbucket.get('gcb-test-bucket1')
    # gcpbucket.create('gcb-project', 'gcb-test-bucket2')
    gcpbucket.delete('gcb-test-bucket2')


if __name__ == '__main__':
    main()