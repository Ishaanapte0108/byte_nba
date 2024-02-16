import frappe
from frappe.model.document import Document
import bytenba.form_validation as validation
import re

Doctype = 'Contribution in learning resources development'
pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'


class Contributioninlearningresourcesdevelopment(Document):	

	def autoname(self):
		self.name = f'AI7_{self.owner}_{self.academic_year}_{self.semester}'

	def before_save(self):
		self.self_appraisal_score = compute_marks(self)

	def validate(self):
		validation.standard_validation(self)
			

def compute_marks(self):

	counter = 0

	pas = [[],[],[],[]]

	for item in self.criteria_table:
		
		if counter > 2:
			frappe.throw('Can only have three entries in the table')

		else:
			counter +=1

			if not 0<=item.benchmark_1<=1:
				frappe.throw('All benchmark quality factors must be between 0 and 1')
			if not 0<=item.benchmark_2<=1:
				frappe.throw('All benchmark quality factors must be between 0 and 1')
			if not 0<=item.benchmark_3<=1:
				frappe.throw('All benchmark quality factors must be between 0 and 1')
			if not 0<=item.benchmark_4<=1:
				frappe.throw('All benchmark quality factors must be between 0 and 1')

			val1 = item.benchmark_1*40
			val2 = item.benchmark_2*30
			val3 = item.benchmark_3*20
			val4 = item.benchmark_4*10
			
			pas[0].append(val1)
			pas[1].append(val2)
			pas[2].append(val3)
			pas[3].append(val4)	

	new_pas = []
	
	for i in pas:
		if not i:
			new_pas.append(0)
		else:
			new_pas.append(sum(i)/len(i))

	self.avg_benchmark_1 = new_pas[0]
	self.avg_benchmark_2 = new_pas[1]
	self.avg_benchmark_3 = new_pas[2]
	self.avg_benchmark_4 = new_pas[3]

	return round(sum(new_pas))
