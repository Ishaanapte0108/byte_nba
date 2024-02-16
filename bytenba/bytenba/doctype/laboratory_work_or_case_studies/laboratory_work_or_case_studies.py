# Copyright (c) 2023, byte_team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import bytenba.form_validation as validation
import re

pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'
Doctype = "Laboratory Work Or Case Studies"

class LaboratoryWorkOrCaseStudies(Document):

	"""method to autoname your document"""
	def autoname(self):
		self.name = f'AI4_{self.owner}_{self.academic_year}_{self.semester}'
	
	def before_save(self):
		self.self_appraisal_score = compute_marks(self)

	def validate(self):
		validation.standard_validation(self)


def compute_marks(self):
	
	counter = 0
	pas = []
	
	match = re.search(pattern_for_wtg, self.mapping)
	if match:
		val5 = float(match.group(1).strip())
	else:
		frappe.throw('Error Fetching Field Weightages')

	for item in self.engg_table:
		if counter > 1:
			frappe.throw('Can only have two entries in the table')

		else:
			counter +=1

			match = re.search(pattern_for_wtg, item.engg_a)
			if match:
				val1 = float(match.group(1).strip())
			else:
				frappe.throw('Error Fetching Field Weightages')

			match = re.search(pattern_for_wtg, item.engg_b)
			if match:
				val2 = float(match.group(1).strip())
			else:
				frappe.throw('Error Fetching Field Weightages')
			
			match = re.search(pattern_for_wtg, item.engg_c)
			if match:
				val3 = float(match.group(1).strip())
			else:
				frappe.throw('Error Fetching Field Weightages')				

			match = re.search(pattern_for_wtg, item.engg_d)
			if match:
				val4 = float(match.group(1).strip())
			else:
				frappe.throw('Error Fetching Field Weightages')			

			pow = val1*val2*val3*val4*val5*100
			
			item.app_engg_wt = round(pow)

			pas.append(round(pow))
	
	return sum(pas)