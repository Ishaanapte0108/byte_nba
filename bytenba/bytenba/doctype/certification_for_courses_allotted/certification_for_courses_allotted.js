let templateString = frappe.boot.my_global_template
let modifiedString = templateString.replace("{{DocType}}", "Certification for courses allotted");
eval(modifiedString);
