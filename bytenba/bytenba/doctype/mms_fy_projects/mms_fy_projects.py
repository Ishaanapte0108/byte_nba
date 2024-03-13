import frappe
from frappe.model.document import Document
import bytenba.form_validation as validation
import re

Doctype = 'MMS FY Projects'
pattern_for_wtg = r'\((\s*(?:\d+\.\d+|\d+)\s*)\)'

class MMSFYProjects(Document):
  
  def autoname(self):
    self.name = f'AI10MMS_{self.owner}_{self.semester}_{self.professor}'
  
  def before_save(self):
    self.self_appraisal_score = compute_marks(self)

  def validate(self):
    validation.standard_validation(self)

def compute_marks(self):

  match = re.search(pattern_for_wtg, self.number_of_projects_guided)
  if match:
    val1 = float(match.group(1).strip())
  else:
    frappe.throw('Error Fetching Field Weightages')

  match = re.search(pattern_for_wtg, self.live_or_industry_projects)
  if match:
    val2 = float(match.group(1).strip())
  else:
    frappe.throw('Error Fetching Field Weightages')

  match = re.search(pattern_for_wtg, self.participation_in_competitions)
  if match:
    val3 = float(match.group(1).strip())
  else:
    frappe.throw('Error Fetching Field Weightages')

  match = re.search(pattern_for_wtg, self.awards)
  if match:
    val4 = float(match.group(1).strip())
  else:
    frappe.throw('Error Fetching Field Weightages')
  
  match = re.search(pattern_for_wtg, self.publications)
  if match:
    val5 = float(match.group(1).strip())
  else:
    frappe.throw('Error Fetching Field Weightages')
    
  product_of_wts = val1*val2*val3*val4*val5
  return product_of_wts*100
