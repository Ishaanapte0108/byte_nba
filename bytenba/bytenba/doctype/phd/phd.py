import frappe
from frappe.model.document import Document
import bytenba.form_validation as validation
import re


Doctype = 'PhD'
pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'

class PhD(Document):
	
	def autoname(self):
		self.name = f'AI11_{self.owner}_{self.academic_year}_{self.semester}'
	
	def before_save(self):
		self.self_appraisal_score = compute_marks(self)

	def validate(self):
		validation.standard_validation(self)


		
def compute_marks(self):
	
	"""get num prj guided"""
	match = re.search(pattern_for_wtg, self.col1)
	if match:
		val1 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')

	"""get industry prj"""
	match = re.search(pattern_for_wtg, self.col2)
	if match:
		val2 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')

	"""get live prj"""
	match = re.search(pattern_for_wtg, self.col3)
	if match:
		val3 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')

	"""get participation in competitions"""
	match = re.search(pattern_for_wtg, self.col4)
	if match:
		val4 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')
	
	"""get awards"""
	match = re.search(pattern_for_wtg, self.col5)
	if match:
		val5 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')
	
	"""publications"""
	match = re.search(pattern_for_wtg, self.col6)
	if match:
		val6 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')
	
	product_of_wts = round(val1*val2*val3*val4*val5*val6*150)
	return product_of_wts