
import os

from azure.storage.blob import BlobServiceClient

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

# Create the BlobServiceClient object which will be used to create a container client
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# Create a unique name for the container
container_name = 'cebd1160container286ca9fd-cbca-4a8f-bbc6-dc6bbeb32e3d'

blob_client = blob_service_client.get_blob_client(container=container_name, blob='10-script.py')

# Download the blob to a local file
with open('local_file.txt', "wb") as download_file:
    download_file.write(blob_client.download_blob().readall())