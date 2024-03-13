let templateString = frappe.boot.my_global_template
let modifiedString = templateString.replace("{{DocType}}", "Subject head-mini project");
eval(modifiedString);