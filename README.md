# Script to Auto Upload File to S3

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Boto3](https://img.shields.io/badge/boto3-latest-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A robust Python utility that simplifies file uploads to Amazon S3 buckets using the Boto3 SDK. Built with error handling and automation in mind.

## 🚀 Features

- Simple file upload to AWS S3 buckets
- Comprehensive error handling
- Environment variable support for secure credential management
- Boolean return values for easy automation integration
- Lightweight and dependency minimal

## 📋 Prerequisites

- Python 3.8 or higher
- AWS account with S3 access
- Boto3 library

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/script-to-auto-upload-file-to-s3.git
   cd script-to-auto-upload-file-to-s3
   ```

2. Set up a virtual environment (recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🔑 Configuration

Configure AWS credentials using environment variables (recommended):

```bash
# Windows (PowerShell)
$env:AWS_ACCESS_KEY_ID="your_access_key"
$env:AWS_SECRET_ACCESS_KEY="your_secret_key"
$env:AWS_REGION="your_region"  # e.g., us-east-1
$env:S3_BUCKET="your_bucket_name"
```

## 📝 Usage

### Basic Usage

```python
from src.upload_to_s3 import upload_to_aws

# Upload a file
success = upload_to_aws('local_file.txt', 's3_filename.txt')
if success:
    print("Upload completed successfully!")
```

### Error Handling

The script handles common scenarios:
- Missing files
- Invalid credentials
- AWS service errors
- Network issues

## 🧪 Testing

Run the test suite:

```bash
python -m unittest discover tests
```

## 🔒 Security Best Practices

- Never commit AWS credentials to version control
- Use environment variables or AWS credentials file
- Implement least-privilege access policies
- Regularly rotate access keys

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📬 Contact

For questions or feedback, please open an issue in the GitHub repository.

---
Made by vijitha shetty using Python and Boto3