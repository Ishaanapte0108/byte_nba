import frappe
from frappe.model.document import Document
import bytenba.form_validation as validation
import re

Doctype = 'Summer internships and projects'
pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'

class Summerinternshipsandprojects(Document):
	
	def autoname(self):
		self.name = f'AI9MMS_{self.owner}_{self.academic_year}_{self.semester}'
	
	def before_save(self):
		self.self_appraisal_score = compute_marks(self)

	def validate(self):
		validation.standard_validation(self)

def compute_marks(self):
	
	"""get num prj guided"""
	match = re.search(pattern_for_wtg, self.number_of_projects_guided)
	if match:
		val1 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')


	"""get participation in competitions"""
	match = re.search(pattern_for_wtg, self.participation_in_competitions)
	if match:
		val4 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')
	
	"""get awards"""
	match = re.search(pattern_for_wtg, self.awards)
	if match:
		val5 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')
	
	"""publications"""
	match = re.search(pattern_for_wtg, self.publications)
	if match:
		val6 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')

	
	product_of_wts = val1*val4*val5*val6
	return round(product_of_wts*100)
