// Copyright (c) 2024, byte_team and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Mini project as a subject head", {
// 	refresh(frm) {

// 	},
// });
let templateString = frappe.boot.my_global_template
let modifiedString = templateString.replace("{{DocType}}", "Mini project as a subject head");
eval(modifiedString);
