
import boto3
from botocore.exceptions import NoCredentialsError, ClientError

ACCESS_KEY = "your access-key"
SECRET_KEY = "your secret-key"
BUCKET_NAME = "your-bucket-name"

def upload_to_aws(local_file, s3_file):
    s3 = boto3.client(
        's3',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        region_name='ap-south-1'
    )

    try:
        s3.upload_file(local_file, BUCKET_NAME, s3_file)
        print(f"✅ Upload Successful: {s3_file}")
        return True
    except FileNotFoundError:
        print("❌ The file was not found")
        return False
    except NoCredentialsError:
        print("❌ Credentials not available")
        return False
    except ClientError as e:
        print(f"❌ AWS Error: {e}")
        return False

if __name__ == "__main__":
    upload_to_aws('test.text', 'test.text')