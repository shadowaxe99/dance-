```python
import boto3
from botocore.exceptions import NoCredentialsError

class BackendInfrastructure:
    def __init__(self):
        self.s3 = boto3.client('s3')

    def upload_to_aws(self, local_file, bucket, s3_file):
        try:
            self.s3.upload_file(local_file, bucket, s3_file)
            print("Upload Successful")
            return True
        except FileNotFoundError:
            print("The file was not found")
            return False
        except NoCredentialsError:
            print("Credentials not available")
            return False

    def download_from_aws(self, local_file, bucket, s3_file):
        try:
            self.s3.download_file(bucket, s3_file, local_file)
            print("Download Successful")
            return True
        except FileNotFoundError:
            print("The file was not found")
            return False
        except NoCredentialsError:
            print("Credentials not available")
            return False

backend = BackendInfrastructure()

# Example usage:
# backend.upload_to_aws('local_file.txt', 'bucket_name', 's3_file_name.txt')
# backend.download_from_aws('local_file.txt', 'bucket_name', 's3_file_name.txt')
```