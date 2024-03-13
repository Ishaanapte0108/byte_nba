import frappe
from frappe.model.document import Document
import bytenba.form_validation as validation
import re

Doctype = 'Subject head-mini project'
pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'

class Subjectheadminiproject(Document):
	
	"""method to autoname your document"""
	def autoname(self):
		self.name = f'AI8_{self.owner}_{self.academic_year}_{self.semester}'
	
	def before_save(self):
		self.self_appraisal_score = compute_marks(self)

	def validate(self):
		validation.standard_validation(self)


def compute_marks(self):
	
	match = re.search(pattern_for_wtg, self.col1)
	if match:
		val1 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')

	match = re.search(pattern_for_wtg, self.col2)
	if match:
		val2 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')

	match = re.search(pattern_for_wtg, self.col3)
	if match:
		val3 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')

	match = re.search(pattern_for_wtg, self.col4)
	if match:
		val4 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')

	match = re.search(pattern_for_wtg, self.col5)
	if match:
		val5 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')
		
	product_of_wts = val1*val2*val3*val4*val5
	
	return round(product_of_wts*50)