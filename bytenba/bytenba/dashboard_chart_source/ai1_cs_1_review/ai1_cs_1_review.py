import frappe
from frappe import _
from frappe.utils.dashboard import cache_source


@frappe.whitelist()
@cache_source
def get(**kwargs):  
	
	session_user = frappe.session.user
  #delete leter
	if session_user == 'Administrator':
		session_user = 'arjun.singh@appraisepro.awsapps.com'
		
	document_types = ['Certification for courses allotted' , 'Courses taught', 'BSA guest lecture','BSA industrial visit', 'BSA-Co-curricular', 'Laboratory Work Or Case Studies', 'Course-lab outcome attainment', 'ME Projects','Exam related work',  'BSA-Mini Prj', 'Innovation in TLP','Contribution in learning resources development', 'Subject head-mini project','BE Projects', 'PhD', 'Grades in preceding semester preview', 'Grades in preceding semester review']

	data = []

	metadata = frappe.get_doc('Academic meta data')
	year = metadata.year
	sem = metadata.sem
	completed = 0
	incomplete = 0
    
	for doc in document_types:
			posCount = 0
			negCount = 0
			totalCount = 0
			
			data = frappe.db.get_all(doc, filters={"reviewer": session_user, 'academic_year': year, 'semester': sem}, fields = ['name','approved'])
			
			for tuple in data:
				totalCount+=1
				if tuple['approved'] == 1:
					posCount+=1
				elif tuple['approved'] == 0:
					negCount+=1
			if posCount+negCount == totalCount:
				completed+=posCount
				incomplete+= negCount
		
	return {
		"labels": ['Approved','Approvals Pending'],
		"datasets": [{"values": [completed, incomplete]}]
	}

	