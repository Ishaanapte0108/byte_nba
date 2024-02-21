import frappe
from frappe.model.document import Document
import bytenba.form_validation as validation
import re


Doctype = 'Average Student Attendance'
pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'

class AverageStudentAttendance(Document):
	"""method to autoname your document"""
	def autoname(self):
		self.name = f'SD1_{self.owner}_{self.academic_year}_{self.semester}'
	
	def before_save(self):
		computemarks(self)

	def validate(self):
			validation.standard_validation(self)
			
def computemarks(self):
		sum = 0
		count = 0
		for item in self.course_attendance_table:
			if item.attendance_percent < 0 or item.attendance_percent > 100:
				frappe.throw('Attendance percentage entered incorrectly')
			else:
				count +=1
				if item.attendance_percent >= 80:
					temp_marks = 300
				elif 70 <= item.attendance_percent < 80:
					temp_marks = 225
				elif 60 <= item.attendance_percent < 70:
					temp_marks = 150
				elif 50 <= item.attendance_percent < 60:
					temp_marks = 105
				elif 40 <= item.attendance_percent < 50:
					temp_marks = 70
				elif item.attendance_percent < 40:
					temp_marks = 0
				else:
					frappe.throw('Something went wrong')
				sum+= temp_marks
				item.marks_obtained = temp_marks
		
		self.self_appraisal_score = sum // count