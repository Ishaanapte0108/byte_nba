import frappe
from frappe.model.document import Document
import bytenba.form_validation as validation
import re

pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'
doctype = 'Exam related work'

class Examrelatedwork(Document):

	"""method to autoname your document"""
	def autoname(self):
		self.name = f'AI1_{self.owner}_{self.academic_year}_{self.semester}'
	def before_save(self):
		self.self_appraisal_score = compute_marks(self)		

	def validate(self):
		validation.standard_validation(self)	

		
def compute_marks(self):
		
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
		
		sum = self.chief_conductor + self.cap_incharge + self.senior_supervisor + self.paper_setting + self.paper_solutions + self.vigilance_squad_member + self.design_of_curriculum + self.invigilation + self.paper_assessment

		if sum >=100:
			self.self_appraisal_score = 100
		else:
			self.self_appraisal_score = sum

		return round(sum)	