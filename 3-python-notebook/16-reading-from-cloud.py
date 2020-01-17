#!/usr/bin/env python3

# pip install --upgrade google-cloud-storage
from google.cloud import storage


def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    # bucket_name = "your-bucket-name"
    # source_blob_name = "storage-object-name"
    # destination_file_name = "local/path/to/file"

    # go to https://console.cloud.google.com/apis/credentials/serviceaccountkey to generate this file
    storage_client = storage.Client.from_service_account_json('cebd1160-59355d33122c.json')

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    print(f"Blob {source_blob_name} downloaded to {destination_file_name}.")


download_blob('cebd1160-el', 'world-cup-2018-tweets.zip', './downloaded-file.zip')
