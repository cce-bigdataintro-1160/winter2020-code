import os
import uuid

from azure.storage.blob import BlobServiceClient

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

# Create the BlobServiceClient object which will be used to create a container client
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# Create a unique name for the container
container_name = "cebd1160container" + str(uuid.uuid4())

# Create the container
container_client = blob_service_client.create_container(container_name)

# Create a blob client using the local file name as the name for the blob
blob_client = blob_service_client.get_blob_client(container=container_name, blob='10-script.py')

# Upload the created file
with open('10-script.py', "rb") as data:
    blob_client.upload_blob(data)
