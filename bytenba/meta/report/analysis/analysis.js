// Copyright (c) 2024, byte_team and contributors
// For license information, please see license.txt

frappe.query_reports["Analysis"] = {
	"filters": [
		{
			"fieldname": "academic_year",
			"fieldtype": "Select",
			"label": "Academic Year",
			"mandatory": 0,
			"wildcard_filter": 0,
			"options": "2024\n2025\n2026\n2027\n2028\n2029\n2030\n2031\n2032\n2033\n2034\n2035"
		},
		{
			"fieldname": "semester",
			"fieldtype": "Select",
			"label": "Semester",
			"mandatory": 0,
			"options": "Odd\nEven",
			"wildcard_filter": 0
		},
		{   
		"fieldname": "department",
		"fieldtype": "Link",
		"label": "Department",
		"mandatory": 0,
		"options": "Department",
		"wildcard_filter": 0
		},
		{   
		"fieldname": "designation",
		"fieldtype": "Select",
		"label": "Designation",
		"mandatory": 0,
		"options": "\nProfessor\nAssistant Professor\nAssociate Professor",
		"wildcard_filter": 0
		},
		{
			"fieldname": "bucket",
			"fieldtype": "Select",
			"label": "Bucket",
			"mandatory": 0,
			"options": "\nAcademic Involvement\nStudent Development\nAdministration\nResearch\nConsultancy and Corporate Training\nProduct Development",
			"wildcard_filter": 0
		 }
	],
	"formatter": function(value, row, column, data, default_formatter) {
		
		value = default_formatter(value, row, column, data);
		
    if (column['id'] === "Courses taught" && data['Designation']=== "Professor") {
        
        if (value < 100) {
            value = '<b style="color: red;">' + value + '</b>';
        }
				if (value >= 100){
					value = '<b style="color: green;">' + value + '</b>';
				}
    }
    return value;
	},
};
