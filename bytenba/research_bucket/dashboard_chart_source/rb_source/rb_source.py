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

	
	document_types = ['Aggregate Contribution Score', 'Fellowship received for national or international conference', 'Institute level technical presentations', 'Interaction with entities', 'Papers published in national or international conferences', 'Papers published in national or international journal', 'Participation in events', 'Patents-designs-copyrights-technologies developed', 'Peer reviewed publications', 'Qualification upgradation', 'Special Accolades', 'Special chair in academic events']


	data = []

	metadata = frappe.get_doc('Academic meta data')
	year = metadata.year
	sem = metadata.sem
	

	for doc in document_types:
		try:
			data_tuple = frappe.db.get_all(doc, filters={"owner": session_user, 'academic_year': year, 'semester': sem}, pluck = 'approved')
			if data_tuple:
				if data_tuple[0] == 1:
					data.append({'docType': doc, 'status': 2})
				else:
					data.append({'docType': doc, 'status': 1})
			else:
				data.append({'docType': doc, 'status': 0})
		except:
			pass
	
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