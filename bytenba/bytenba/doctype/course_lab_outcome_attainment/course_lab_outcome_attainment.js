let templateString = frappe.boot.my_global_template
let modifiedString = templateString.replace("{{DocType}}", "Course-lab outcome attainment");
eval(modifiedString);