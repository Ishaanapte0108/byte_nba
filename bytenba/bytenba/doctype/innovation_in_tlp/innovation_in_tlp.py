import frappe
from frappe.model.document import Document
import bytenba.form_validation as validation
import re

Doctype = 'Innovation in TLP	'
pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'

class InnovationinTLP(Document):

	def autoname(self):
		self.name = f'AI6_{self.owner}_{self.academic_year}_{self.semester}'

	def before_save(self):
		
		self.self_appraisal_score = compute_marks(self)

	def autoname(self):
		self.name = f'AI6_{self.academic_year}_{self.professor}'

	def validate(self):
		
		validation.standard_validation(self)

		# no of participants		
		enrolled = self.no_of_enrollments
		participants=self.no_of_participants
		if participants > enrolled:
			frappe.throw('Number of participants should be less than number of students enrolled')
		
		# clusters
		no1 = self.quality_of_assignments
		no2 = self.quality_of_tests
		no3 = self.quality_of_experiment
		no4 = self.activities_done_outside_the_classroom
		no5 = self.activities_for_slow_learners
		no6 = self.activities_for_advance_learners
		list1={no1,no2,no3,no4,no5,no6}
		for x in list1:
			if int(x)<0 or int(x)>1:
				frappe.throw('All fields under the cluster should be between 0 to 1.')

		# assessment(term work)
		activities = self.no_of_activities
		if activities < 4:
			frappe.throw('Minimum nunmber of activities considered for term work should be 4')


def compute_marks(self):

		"""get mark1"""
		participants_int = self.no_of_participants
		enrolled_int = self.no_of_enrollments
		mark1 = participants_int / enrolled_int

		"""get mapping"""
		match = re.search(pattern_for_wtg, self.mapping)
		if match:
			mark4 = float(match.group(1).strip())
		else:
			frappe.throw('Error Fetching Field Weightages')


		"""get number of activities"""
		mark3 = self.no_of_activities*0.25
		
		"""get mark2 cluster"""
		no1 = self.quality_of_assignments
		no2 = self.quality_of_tests
		no3 = self.quality_of_experiment
		no4 = self.activities_done_outside_the_classroom
		no5 = self.activities_for_slow_learners
		no6 = self.activities_for_advance_learners
		sum1 = no1+no2+no3+no4+no5+no6
		mark2 = round(sum1/6)		

		product_of_wtg = mark1*mark2*mark3*mark4
		marks = round(product_of_wtg*150)

		return marks	