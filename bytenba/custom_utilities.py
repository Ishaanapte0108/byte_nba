import datetime
from io import BytesIO
import frappe
import re
import os, uuid
import boto3, requests
from frappe.utils import today

def validate_delete(doc, method):
	if doc.approved == 1 and not doc.modified_by == "Administrator":
		frappe.throw('Cannot delete document post approval')

@frappe.whitelist()
def evidenceUpload(fileData):
	AWS_ACCESS_KEY = 'AKIA2BMG37DHUNDSWJWC'
	AWS_SECRET_KEY = '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'
	AWS_S3_BUCKET_NAME = 'appraiseprofilestorage'
	AWS_REGION = 'us-west-2'
	LOCAL_FILE = fileData
	OBJECT_KEY = 'fromAppNEW.pdf'
	CONTENT_TYPE = 'application/pdf'

	# Assuming 'file' is the key containing the uploaded file in FormData
	fileData = {'file': '...'}

	# Get the file from the FormData
	file_content = fileData.get('file')  # Adjust accordingly if different key name

	if file_content:
			# Convert base64 data to bytes
			file_content = file_content.encode()

			# Create an in-memory stream with BytesIO
			file_stream = BytesIO(file_content)

			s3_client = boto3.client(
					service_name='s3',
					region_name=AWS_REGION,
					aws_access_key_id=AWS_ACCESS_KEY,
					aws_secret_access_key=AWS_SECRET_KEY
			)

			try:
					response = s3_client.upload_fileobj(
							file_stream,
							AWS_S3_BUCKET_NAME,
							OBJECT_KEY,
							ExtraArgs={'ContentType': CONTENT_TYPE}
					)
					print("File uploaded successfully to AWS S3")
			except Exception as e:
					print("Error uploading file to AWS S3:", e)
	else:
			print("File content not found in FormData")


@frappe.whitelist()
def uploadToBlob(file, filename):
		
		try:

			connect_str = "DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;AccountName=appraiseteststorage;AccountKey=sxAY187MXRIf5voMhZcIGH4R48KZukd58HrEmKyp+4coax/i4CaIp4qr2ULgtWU6qwdGXzPU9Fau+ASttKoLSA==;BlobEndpoint=https://appraiseteststorage.blob.core.windows.net/;FileEndpoint=https://appraiseteststorage.file.core.windows.net/;QueueEndpoint=https://appraiseteststorage.queue.core.windows.net/;TableEndpoint=https://appraiseteststorage.table.core.windows.net/"
			# Create BlobServiceClient
			blob_service_client = BlobServiceClient.from_connection_string(connect_str)

			name = filename.strip().lower()

			# Replace invalid characters with a hyphen (-)
			name = re.sub(r'[^a-zA-Z0-9\-]', '-', name)

			# Remove consecutive hyphens
			name = re.sub(r'\-+', '-', name)

			# Remove leading/trailing hyphens
			name = name.strip('-')

			# Limit the length of the name (Azure Blob name limit is 1024 characters)
			formatted_blob_name = name = name[:1024]

			# Blob client with formatted name
			blob_client = blob_service_client.get_blob_client(container="firsttestcontainer", blob=formatted_blob_name)

			blob_client.upload_blob(file)

			return "success"

		except Exception as e:
			return str(e)
		

import frappe

@frappe.whitelist()
def get_user_info(session_user):
		if session_user == "Administrator":
			return ["Not Applicable", "Administrator", "Not Applicable", "Not Applicable"]
		
		data = frappe.db.get_list('Professors', fields = ["select_reviewer", "full_name", "department", "faculty_designation"], filters={'name': ['=', session_user]}, as_list=True, ignore_permissions = True)

		current_year = datetime.datetime.now().year
		previous_years = [current_year - i for i in range(5)]

		data = data[0] + (previous_years,)
		
		return data


@frappe.whitelist()
def get_reviewer_names(doctype, txt, searchfield, start, page_len, filters):
		data = frappe.db.get_list('Has Role', start=start, page_length= page_len, fields=["parent"], filters = {'role': ['=', 'reviewer']}, as_list=True)
		return data

@frappe.whitelist()
def get_roles(session_user):
		roles = frappe.get_roles(session_user)
		return roles

# @frappe.whitelist()
# def get_progress(session_user):
# 	#get academic year and semester
# 	session_user = "aarav.patel@appraisepro.awsapps.com"
# 	year = today()[0:4]
# 	month = int(today()[5:7])
# 	if 1 <= month <= 6:
# 		sem = 'Even'
# 	else:
# 		sem = 'Odd'
# 	partial_name = session_user + '_' + year + '_' + sem
# 	doc_list = [['Certification for courses allotted','AI1_'], ['Courses taught', 'AI2_']]
# 	success = {}
# 	for ele in doc_list:
# 		doc = ele[0]
# 		instnace_name = ele[1] + partial_name
# 		print(instnace_name)
# 		if frappe.db.exists(doc, instnace_name):
# 			doc = 'success-'+ doc.replace(' ', '-')
# 			success[doc] = True
# 	if not success:
# 		return None
# 	else:
# 		return success
		
	