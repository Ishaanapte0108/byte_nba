import frappe
from frappe.model.document import Document
import bytenba.form_validation as validation
import re

Doctype = 'Grades in preceding semester review'
pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'

class Gradesinprecedingsemesterreview(Document):

	"""method to autoname your document"""
	def autoname(self):
		self.name = f'AI14_{self.owner}_{self.academic_year}_{self.semester}'
	
	def before_save(self):
		self.self_appraisal_score = compute_marks(self)

	def validate(self):
		validation.standard_validation(self)

def compute_marks(self):
		
	match = re.search(pattern_for_wtg, self.precd_sem_grade)
	if match:
		val = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')
	
	return val
