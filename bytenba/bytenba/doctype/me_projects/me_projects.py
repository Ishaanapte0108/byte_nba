import frappe
from frappe.model.document import Document
import bytenba.form_validation as validation
import re


Doctype = 'ME Projects'
pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'

class MEProjects(Document):	
	
	def autoname(self):
		self.name = f'AI10Engg_{self.owner}_{self.academic_year}_{self.semester}'
	
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

	"""get industry prj"""
	match = re.search(pattern_for_wtg, self.industry_projects)
	if match:
		val2 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')

	"""get live prj"""
	match = re.search(pattern_for_wtg, self.live_projects)
	if match:
		val3 = float(match.group(1).strip())
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

	"""funding"""
	match = re.search(pattern_for_wtg, self.funding_required)
	if match:
		val7 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')

	"""quality_of_university"""
	match = re.search(pattern_for_wtg, self.quality_of_university)
	if match:
		val8 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')
	
	product_of_wts = round(val1*val2*val3*val4*val5*val6*val7*val8*100)
	return product_of_wts