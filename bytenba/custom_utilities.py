import pandas as pd
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

@frappe.whitelist()
def get_progress(session_user, buttonValue):

	buttonValue = int(buttonValue)	
	if session_user == 'Administrator':
		session_user = 'aarav.patel@appraisepro.awsapps.com'


	document_types = [{"name": "Certification for courses allotted", "number": "Academic Involvement 1", "description": "KPI assesses faculty course completion", "urlEnd": "/app/certification-for-courses-allotted"}, {"name": "Courses taught", "number": "Academic Involvement 2", "description": "KPI assesses courses taight by faculty", "urlEnd": "/app/courses-taught"}, {"name": "BSA guest lecture", "number": "Academic Involvement 3.1", "description": "KPI assesses guest lectures conducted", "urlEnd": "/app/bsa-guest-lecture"}, {"name": "BSA industrial visit", "number": "Academic Involvement 3.2", "description": "KPI assesses industrial visits arranged by faculty", "urlEnd": "/app/bsa-industrial-visit"}, {"name": "BSA-Co-curricular", "number": "Academic Involvement 3.3", "description": "KPI assesses co-curricular activites by the faculty", "urlEnd": "/app/bsa-co-curricular"}, {"name": "BSA-Mini Prj", "number": "Academic Involvement 3.4", "description": "KPI assesses mini project progress subject wise", "urlEnd": "/app/bsa-mini-prj"}, {"name": "Laboratory Work Or Case Studies", "number": "Academic Involvement 4", "description": "KPI assesses case studies by faculty", "urlEnd": "/app/laboratory-work-or-case-studies"}, {"name": "Course-lab outcome attainment", "number": "Academic Involvement 5", "description": "KPI assesses outcomes generated by faculty", "urlEnd": "/app/course-lab-outcome-attainment"}, {"name": "Innovation in TLP", "number": "Academic Involvement 6", "description": "KPI assesses new achievement in teaching learning process by faculty", "urlEnd": "/app/innovation-in-tlp"}, {"name": "Contribution in learning resources development", "number": "Academic Involvement 7", "description": "KPI assesses resources utilized in TLP", "urlEnd": "/app/contribution-in-learning-resources-development"}, {"name": "Subject head-mini project", "number": "Academic Involvement 8", "description": "KPI assesses mini project criteria", "urlEnd": "/app/subject-head-mini-project"}, {"name": "BE Projects", "number": "Academic Involvement 9", "description": "KPI assesses detailed information about BE projects", "urlEnd": "/app/be-projects"}, {"name": "ME Projects", "number": "Academic Involvement 10", "description": "KPI assesses detailed information about ME projects", "urlEnd": "/app/me-projects"}, {"name": "PhD", "number": "Academic Involvement 11", "description": "KPI assesses phd status of a faculty", "urlEnd": "/app/phd"}, {"name": "Exam related work", "number": "Academic Involvement 12", "description": "KPI assesses roles carried by professor in exams", "urlEnd": "/app/exam-related-work"}, {"name": "Grades in preceding semester preview", "number": "Academic Involvement 13", "description": "KPI assesses grades preview", "urlEnd": "/app/grades-in-preceding-semester-preview"}, {"name": "Grades in preceding semester review", "number": "Academic Involvement 14", "description": "KPI assesses grades review", "urlEnd": "/app/grades-in-preceding-semester-review"}]

	data = []

	metadata = frappe.get_doc('Academic meta data')
	year = metadata.year
	sem = metadata.sem

	for dict in document_types:

			data_tuple = frappe.db.get_all(dict['name'], filters={"owner": session_user, 'academic_year': year, 'semester': sem}, pluck = 'approved')

			if data_tuple:
				if data_tuple[0] == 1:
					dict['status'] = 2
					data.append(dict)
				else:
					dict['status'] = 1
					data.append(dict)
			else:
					dict['status'] = 0
					data.append(dict)
	
	filteredData = []
	
	for tuple in data:
		if tuple['status'] == buttonValue:
			filteredData.append(tuple)
	
	return filteredData
	

