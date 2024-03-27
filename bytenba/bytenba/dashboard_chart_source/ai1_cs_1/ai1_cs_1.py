import frappe
from frappe import _
from frappe.utils.dashboard import cache_source


@frappe.whitelist()
@cache_source
def get(**kwargs):  
	
	filters = frappe.parse_json(kwargs['filters'])
	session_user = frappe.session.user
	
	#delete later
	if session_user == 'Administrator':
		session_user = 'aarav.patel@appraisepro.awsapps.com'

	
	document_types = ['Certification for courses allotted' , 'Courses taught', 'BSA guest lecture','BSA industrial visit', 'BSA-Co-curricular', 		'Laboratory Work Or Case Studies', 'Course-lab outcome attainment', 'ME Projects',  'Exam related work',  'BSA-Mini Prj', 'Innovation in TLP','Contribution in learning resources development', 'Subject head-mini project','BE Projects', 'PhD', 'Grades in preceding semester preview', 'Grades in preceding semester review']

	data = []

	metadata = frappe.get_doc('Academic meta data')
	year = metadata.year
	sem = metadata.sem
	

	for doc in document_types:

			data_tuple = frappe.db.get_all(doc, filters={"owner": session_user, 'academic_year': year, 'semester': sem}, pluck = 'approved')

			if data_tuple:
				if data_tuple[0] == 1:
					data.append({'docType': doc, 'status': 2})
				else:
					data.append({'docType': doc, 'status': 1})
			else:
				data.append({'docType': doc, 'status': 0})
	
	submitted = 0
	approved = 0
	pending = 0

	for tuple in data:
		
		if tuple['status'] == 2:
				approved+=1
				submitted+=1
		elif tuple['status'] == 1:
			submitted+=1
		elif tuple['status'] == 0:
			pending+=1

	#note: 0 means pending, 1 means submitted only and 2 means submitted and approved
	return {
		"labels": ['Submitted','Approved','Pending'],
		"datasets": [{"values": [submitted, approved, pending]}]
	}

	# for doc in document_types:

	# 		data_tuple = frappe.db.get_all(doc, filters={"owner": 'aarav.patel@appraisepro.awsapps.com', 'academic_year': year, 'semester': sem}, pluck = 'approved')
	# 		if data_tuple:
	# 			data.append({'docType': doc, 'exists': True, 'approved': data_tuple[0]})
	# 		else:
	# 			data.append({'docType': doc, 'exists': False, 'approved': None})
	

	# if not filters or filters.get('type') == 'Overview':
	# 	submitted = 0
	# 	approved = 0
	# 	pending = 0
	# 	for tuple in data:
			
	# 		if tuple['exists'] == True:
	# 			submitted+=1
	# 			if tuple['approved'] == 1:
	# 				approved+=1
	# 		else:
	# 			pending+=1

	# 	return {
	# 		"labels": ['Submitted','Approved','Pending'],
	# 		"datasets": [{"values": [submitted, approved, pending]}]
	# 	}		
	
	# elif filters.get('type') == 'Submitted':
		
	# 	submitted = 0
	# 	pending = 0

	# 	for tuple in data:
			
	# 		if tuple['exists'] == True:
	# 			submitted+=1
	# 		else:
	# 			pending+=1

	# 	return {
	# 		"labels": ['Submitted','Pending'],
	# 		"datasets": [{"values": [submitted, pending]}]
	# 	}		
	
	# elif filters.get('type') == 'Approved':
		
	# 	approved = 0
	# 	pending = 0

	# 	for tuple in data:
			
	# 		if tuple['exists'] == True and tuple['approved'] == 1:
	# 			approved+=1
	# 		else:
	# 			pending+=1

	# 	return {
	# 		"labels": ['Approved','Pending'],
	# 		"datasets": [{"values": [approved, pending]}]
	# 	}		
