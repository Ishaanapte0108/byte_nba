# Copyright (c) 2023, byte_team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import re

pattern = re.compile(r'^\d{4}-\d{4}$')
doctype = 'Grades in preceding sem preview'

class GradesinprecedingsempreviewAI13(Document):
	def before_save(self):
		if self.precd_sem_grade=="A":
			self.self_appraisal_score = 100
		elif self.precd_sem_grade=="B":
			self.self_appraisal_score = 50
		elif self.precd_sem_grade=="C":
			self.self_appraisal_score = 25
		else:
			self.self_appraisal_score = 0

	"""method to autoname your document"""
	def autoname(self):
		base_name = f'AI13_{self.academic_year}_{self.professor}'
		data = renameDoc(base_name, self.academic_year)
		if data['name_value']:
			self.name = data['name_value']
		else:
			frappe.throw("Failed to generate a unique name.")
	
	def validate(self):
		"""Validation for academic year"""
		academic_yr_str = self.academic_year
		if not re.match(pattern, academic_yr_str):
			frappe.throw('Academic year must be of the form like 2022-2023')
		else:
			yr_end_1 = int(academic_yr_str[2:4])
			yr_end_2 = int(academic_yr_str[7:9])
			if yr_end_2 != yr_end_1 + 1:
				frappe.throw('Academic Date entered improperly')
		

def renameDoc(base_name, academic_year):
	dict = {'name_value': None}
	filters = {
		"name": ["like", base_name + "%"]
	}
	field = 'name'
	similar_docs = frappe.get_list("Grades in preceding sem preview AI13", filters= filters, pluck = field)
	dict['name_value'] = base_name
	return dict