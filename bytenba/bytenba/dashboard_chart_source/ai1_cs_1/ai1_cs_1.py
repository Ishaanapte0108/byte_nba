import frappe
from frappe import _
from frappe.utils.dashboard import cache_source

@frappe.whitelist()
@cache_source
def get():
	
	return {
		"labels": ["SD-1", "SD-2", "SD-3", "SD-4", "SD-5"],
		
		"datasets": [
		{
			"name": "Completed",
			"values": [1,2,1,2,2]
		},
		{
			"name": "Required",
			"values": [1,1,2,2,1]
		}
	],
	"type": "pie",
	}

