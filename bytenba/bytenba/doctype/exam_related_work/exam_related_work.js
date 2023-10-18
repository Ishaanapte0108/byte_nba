// Copyright (c) 2023, byte_team and contributors
// For license information, please see license.txt

frappe.ui.form.on("Exam related work", {
  refresh: function (frm) {
    var currentUser = frappe.session.user;
    frm.set_value("professor", currentUser);
  },
});
