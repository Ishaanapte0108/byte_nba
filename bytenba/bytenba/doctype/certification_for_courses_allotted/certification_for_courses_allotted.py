import frappe
from frappe.model.document import Document
import bytenba.form_validation as validation
import re

Doctype = 'Certification for courses allotted'
pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'

class Certificationforcoursesallotted(Document):
	
	"""method to autoname your document"""
	def autoname(self):
		self.name = f'AI1_{self.owner}_{self.academic_year}_{self.semester}'
	
	def before_save(self):
		self.self_appraisal_score = compute_marks(self)

	def validate(self):
		validation.standard_validation(self)


def compute_marks(self):
	
	match = re.search(pattern_for_wtg, self.platform_type)
	if match:
		val1 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')

	match = re.search(pattern_for_wtg, self.assessment_outcome)
	if match:
		val2 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')

	match = re.search(pattern_for_wtg, self.date_of_cerftification)
	if match:
		val3 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')

	match = re.search(pattern_for_wtg, self.number_of_hours)
	if match:
		val4 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')
		
	product_of_wts = val1*val2*val3*val4
	return product_of_wts*100