# Copyright (c) 2023, byte_team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.document import Document
import re

pattern = re.compile(r'^\d{4}-\d{4}$')
doctype = 'Grades in preceding sem preview'

class Examrelatedwork(Document):
	def before_save(self):
		sum = self.chief_conductor + self.cap_incharge + self.senior_supervisor + self.paper_setting + self.paper_solutions + self.vigilance_squad_member + self.design_of_curriculum + self.invigilation + self.paper_assessment
		if sum >=100:
			self.self_appraisal_score = 100
		else:
			self.self_appraisal_score = sum

	"""method to autoname your document"""
	def autoname(self):
		base_name = f'AI12_{self.academic_year}_{self.professor}'
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
		
		"""Validation for scores"""
		if self.chief_conductor<0 or self.chief_conductor >50:
			frappe.throw('Score for cheif conductor should be between 0 & 50')
		if self.cap_incharge<0 or self.cap_incharge >50:
			frappe.throw('Score for cap incharge should be between 0 & 50')
		if self.senior_supervisor<0 or self.senior_supervisor >30:
			frappe.throw('Score for senior supervisor should be between 0 & 30')
		if self.paper_setting<0 or self.paper_setting >20:
			frappe.throw('Score for paper setting should be between 0 & 20')
		if self.paper_solutions<0 or self.paper_solutions >20:
			frappe.throw('Score for paper solutions should be between 0 & 20')
		if self.vigilance_squad_member<0 or self.vigilance_squad_member >20:
			frappe.throw('Score for vigilance squad member should be between 0 & 20')
		if self.design_of_curriculum<0 or self.design_of_curriculum >10:
			frappe.throw('Score for design of curriculum should be between 0 & 10')
		if self.invigilation<0 or self.invigilation >5:
			frappe.throw('Score for invigilation should be between 0 & 5')
		if self.paper_assessment<0 or self.paper_assessment >10:
			frappe.throw('Score for paper assessment should be between 0 & 10')
		

def renameDoc(base_name, academic_year):
	dict = {'name_value': None}
	filters = {
		"name": ["like", base_name + "%"]
	}
	field = 'name'
	similar_docs = frappe.get_list("Exam related work", filters= filters, pluck = field)
	dict['name_value'] = base_name
	return dict
