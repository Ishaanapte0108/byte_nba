let templateString = frappe.boot.my_global_template
let modifiedString = templateString.replace("{{DocType}}", "Contribution in learning resources development");
console.log(modifiedString)
eval(modifiedString);