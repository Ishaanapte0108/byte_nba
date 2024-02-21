let templateString = frappe.boot.my_global_template
let modifiedString = templateString.replace("{{DocType}}", "Average Student Attendance");
eval(modifiedString);