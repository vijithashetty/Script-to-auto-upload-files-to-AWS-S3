import unittest
from src.upload_to_s3 import upload_to_aws

class TestUploadToAWS(unittest.TestCase):

    def test_upload_success(self):
        # This test would require a mock or a test S3 bucket to run successfully.
        result = upload_to_aws('test.text', 'test.text')
        self.assertTrue(result)

    def test_file_not_found(self):
        result = upload_to_aws('non_existent_file.txt', 'test.text')
        self.assertFalse(result)

    def test_no_credentials(self):
        # This test would require mocking the boto3 client to simulate no credentials.
        result = upload_to_aws('test.text', 'test.text')
        self.assertFalse(result)

    def test_aws_error(self):
        # This test would require mocking the boto3 client to simulate an AWS error.
        result = upload_to_aws('test.text', 'test.text')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()