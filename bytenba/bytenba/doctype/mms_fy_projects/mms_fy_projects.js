let templateString = frappe.boot.my_global_template
let modifiedString = templateString.replace("{{DocType}}", "MMS FY Projects");
eval(modifiedString);