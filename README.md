# python_streaming
This project is a file streaming using a google cloud storage to read and write files by streaming

## Getting Started
### Prerequisites
* Python 2.7+
* google-resumable-media
* google-auth
Installing python and pip
Debian
```
sudo apt-get install python python-pip
```
CentOS
```
sudo yum install python python-pip
```
Install libs
```
pip install google-resumable-media google-auth
```
Now you need to change this var in code for your informations
```
bucket = 'source_bucket_name'
bucket_upload = 'destiny_bucket_name'
blob_name = 'source_filename'
blob_name_upload = 'destiny_filename'
```

After complet this requisites you need to execute the code
```
python python_streaming.py
```
