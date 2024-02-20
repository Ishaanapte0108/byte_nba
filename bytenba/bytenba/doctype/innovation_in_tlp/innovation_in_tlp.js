// // Copyright (c) 2023, byte_team and contributors
// // For license information, please see license.txt

// frappe.ui.form.on('Innovation in TLP', {
// 	refresh: function(frm) {
// 		// Get the current user's username
// 		var currentUser = frappe.session.user;
  
// 		// Set the value of the "Professor" field
// 		frm.set_value('professor', currentUser);
  
// 		// Make the "Professor" field read-only (optional)
// 		// frm.set_df_property('professor', 'read_only', 1);
// 	}
// });

let templateString = frappe.boot.my_global_template
let modifiedString = templateString.replace("{{DocType}}", "Innovation in TLP");
eval(modifiedString);
