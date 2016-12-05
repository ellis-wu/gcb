# GCB
GCB is Google Ceph backup. The goal is to back up Ceph's object storage data to Google Cloud Storage(GCS).

> Reference :
> * [Ceph Documentation](http://docs.ceph.com/docs/master/)
> * [Google Cloud Platform - GCP](https://cloud.google.com/products/)
> * [Google Cloud Storage - GCS](https://cloud.google.com/storage/)

## TO DO
- [ ] Create GCP Project
- [ ] Create GCS bucket
- [ ] GCS export/import APIs
- [ ] Ceph object storage export to GCS bucket

## How to use

### Before running
1. If not already done, enable the Compute Engine API and check the quota for your project at [https://console.developers.google.com/apis/api/compute](https://console.developers.google.com/apis/api/compute)

2. This sample uses Application Default Credentials for authentication. If not already done, install the gcloud CLI from [https://cloud.google.com/sdk/](https://cloud.google.com/sdk/) and run
  ```sh
  $ gcloud beta auth application-default login
  ```

3. Install the Python client library for Google APIs by running
  ```sh
  $ pip install --upgrade google-api-python-client
  ```

4. Install the Python library Magic
  ```sh
  $ pip install python-magic
  ```

(TBD)
