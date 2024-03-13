import frappe
import pandas as pd
from frappe.utils import today

def execute(filters=None):

	academic_year = filters.get('academic_year', today()[0:4])
	semester = filters.get('semester', 'Odd')
	department = filters.get('department', '')
	faculty_designation = filters.get('designation', '')
	bucket = filters.get('bucket', 'bytenba')

	# sql = """SELECT p.full_name as Faculty, p.user_id as 'Employee Code', p.department as Department, p.faculty_designation as Designation, COALESCE(c.reviewer_score, "Pending") as "AI 1", COALESCE(co.reviewer_score, "Pending") as "AI 2",  COALESCE(b.reviewer_score, "Pending") as "AI 3.1"
  # FROM `tabProfessors` as p
  # JOIN `tabCertification for courses allotted` as c
  # ON p.name = c.owner
	# JOIN `tabCourses taught` as co
	# ON p.name = co.owner
	# JOIN `tabBSA guest lecture` as b
	# ON p.name = b.owner
	# WHERE p.department like '{department}'
  # AND p.faculty_designation like '{faculty_designation}'
	# AND c.academic_year = '{academic_year}'
	# AND c.semester = '{semester}'
	# AND co.academic_year = '{academic_year}'
	# AND co.semester = '{semester}'
	# AND b.academic_year = '{academic_year}'
	# AND b.semester = '{semester}'
  # """.format(department = department + "%", faculty_designation = faculty_designation + "%", academic_year = academic_year, semester = semester)

	# print(sql)

	# data = frappe.db.sql(sql, as_dict=True)

  # # Convert data to Pandas DataFrame
	# result = [dict(row) for row in data]
	# df = pd.DataFrame(result)
	# column_names = df.columns.tolist()
	

	# """SEND DATA as a report	"""
	# columns = []
	# for name in column_names:
	# 	columns.append({"fieldname": name,"label": name})
	# data_dict = df.to_dict('records')	

	# return columns, data_dict
	
	filters_faculty={'Active': ['=', '1']}
	# filters_doctype = {'module': ['=', 'bytenba']}

	data = frappe.db.get_list("Professors", fields = ['name', 'full_name', 'faculty_designation'], filters = filters_faculty)
	# doctypes = frappe.db.get_list("DocType", pluck= "name", filters = {'module': ['=', 'bytenba'], 'istable': ['!=', 1]})

	doctypes = ['Certification for courses allotted', 'Courses taught', 'BSA guest lecture','BSA industrial visit', 'BSA-Co-curricular', 		'Laboratory Work Or Case Studies', 'Course-lab outcome attainment', 'ME Projects', 'Average Student Attendance',  'Exam related work',  'BSA-Mini Prj', 'Innovation in TLP','Contribution in learning resources development', 'Subject head-mini project','BE Projects', 'PhD', 'Grades in preceding semester preview', 'Grades in preceding semester review']

	#		Excluded temporarily
	#  'Summer internships and projects'
	#  'MMS FY Projects',

	
	for i in data:
		
		for doc in doctypes:

				rs = frappe.db.get_value(doc, filters={'owner': ['=', i['name']], 'academic_year': ['=', '2024'], 'semester': ['=', 'Odd']}, fieldname='reviewer_score') or 'Pending'
				i[doc] = rs
	
	
	column_names = data[0].keys()
	columns = []
	for name in column_names:
		columns.append({"fieldname": name,"label": name})

	return columns, data	


