import frappe
from frappe.model.document import Document
import bytenba.form_validation as validation
import re

Doctype = 'Certification for courses allotted'
pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'


class Courselaboutcomeattainment(Document):
	
	"""method to autoname your document"""
	def autoname(self):
		self.name = f'AI5_{self.owner}_{self.academic_year}_{self.semester}'
	
	def before_save(self):
		self.self_appraisal_score = compute_marks(self)

	def validate(self):
		validation.standard_validation(self)


def compute_marks(self):

	pas = [item.attainment for item in self.criteria_table]
	avg = sum(pas) // len(pas)
	if avg > 2:
			return 200
	elif avg > 1:
			return 150
	elif avg > 0:
			return 100
	else:
			return 0