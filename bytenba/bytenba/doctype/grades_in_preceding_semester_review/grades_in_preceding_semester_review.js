let templateString = frappe.boot.my_global_template
let modifiedString = templateString.replace("{{DocType}}", "Grades in preceding semester review");
eval(modifiedString);