from setuptools import setup, find_packages

setup(
    name="script-to-auto-upload-file-to-s3",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A script to automatically upload files to an AWS S3 bucket using Boto3.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/script-to-auto-upload-file-to-s3",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'boto3',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)