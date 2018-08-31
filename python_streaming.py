from google.resumable_media.requests import ChunkedDownload
from google.resumable_media.requests import ResumableUpload
import google.auth
import google.auth.transport.requests as tr_requests
import io
from StringIO import StringIO

ro_scope = u'https://www.googleapis.com/auth/devstorage.read_only'
credentials, _ = google.auth.default(scopes=(ro_scope,))
transport = tr_requests.AuthorizedSession(credentials)
bucket = 'source_bucket_name'
bucket_upload = 'destiny_bucket_name'
blob_name = 'source_filename'
blob_name_upload = 'destiny_filename'
content_type = u'text/plain'

url_template = (
    u'https://www.googleapis.com/download/storage/v1/b/'
    u'{bucket}/o/{blob_name}?alt=media')

url_template_upload = (
     u'https://www.googleapis.com/upload/storage/v1/b/{bucket}/o?'
     u'uploadType=resumable')

upload_url = url_template_upload.format(bucket=bucket_upload)

media_url = url_template.format(
    bucket=bucket, blob_name=blob_name)

chunk_size = 1 * 1024 * 1024
stream = io.BytesIO()

download = ChunkedDownload(media_url, chunk_size, stream)
upload = ResumableUpload(upload_url, chunk_size)

while download.finished != True:
	response = download.consume_next_chunk(transport)
	data = response.content.decode("utf-8").replace(',','|')
	stream_upload = io.BytesIO(bytes(data, 'UTF-8'))
	metadata = {u'name': blob_name_upload}
	reponse_upload = upload.initiate(transport, stream_upload, metadata, content_type)
