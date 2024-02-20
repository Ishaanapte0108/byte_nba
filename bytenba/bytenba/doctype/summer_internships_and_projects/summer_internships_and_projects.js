// Copyright (c) 2024, byte_team and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Summer internships and projects", {
// 	refresh(frm) {

// 	},
// });
let templateString = frappe.boot.my_global_template
let modifiedString = templateString.replace("{{DocType}}", "Summer internships and projects");
eval(modifiedString);
