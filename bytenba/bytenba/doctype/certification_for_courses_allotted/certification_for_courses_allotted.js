const DocType = "Certification for courses allotted"

frappe.ui.form.on(DocType, {

  refresh: function(frm) {
		
		$("#navbar-breadcrumbs").css({'visibility':'hidden'});
		$(".btn.btn-xs.btn-secondary.action-btn").css({'visibility':'hidden'});
		$(".btn.btn-default.icon-btn").hide();
		$(".col-lg-2.layout-side-section").hide();




		if (frm.is_new()){
			
					frappe.call({
					method: 'bytenba.custom_utilities.get_user_info',
					args: {
							'session_user': frappe.session.user
					},
					callback: function(response) {
						if (response) {
							frm.set_value('reviewer', response.message[0]);
							frm.set_value('professor', response.message[1]);
							frm.set_value('department', response.message[2]);
							frm.set_value('designation', response.message[3]);
							// frm.set_df_property('academic_year', 'options', response.message[4]);
							frm.set_value('academic_year',frappe.datetime.nowdate().split("-")[0]);
							}
					}
				});
			
		}

		if (frappe.user.has_role('Administrator') || frappe.user.has_role('reviewer'))
		{
		frm.add_custom_button(__(frm.doc.approved == 1 ? "Revoke" : "Approve"), () => {
				if (frm.doc.approved == 0){
				let d = new frappe.ui.Dialog({
					title: 'Approve self appraisal score',
					fields: [
							{
									label: 'Self Appraisal Score',
									fieldname: 'sapc',
									fieldtype: 'Read Only',
									default: frm.doc.self_appraisal_score

							},
							{
									label: 'Reviewer Score',
									fieldname: 'rsc',
									fieldtype: 'Int',
									default: frm.doc.self_appraisal_score
							},
					],
					size: 'small', // small, large, extra-large 
					primary_action_label: 'Approve',
					primary_action(values) {
						frappe.utils.play_sound("click");
						frappe.call({
							method: 'bytenba.approveScore.approve',
							args: {
									
									'session_user': frappe.session.user,
									'owner': frm.doc.owner,
									'doctype': frm.doc.doctype,
									'name': frm.doc.name,
									'rsc': values.rsc

							},					
							callback: function(response) {
									if (response) {
											if (response.message == 'ok'){
												frm.free
												frm.refresh()
												}
										}
								}
						});
							d.hide();
					}
			});
			d.show();
			}
			
			if (frm.doc.approved == 1){
				frappe.confirm(
					'Are you sure you want to revoke approval on this form?',
					function(){
						frappe.utils.play_sound("click");
						frappe.call({
							method: 'bytenba.approveScore.revoke',
							args: {
									'session_user': frappe.session.user,
									'owner': frm.doc.owner,
									'doctype': frm.doc.doctype,
									'name': frm.doc.name,
							},
							callback: function(response) {
									if (response) {
											if (response.message == 'ok'){
												frm.refresh()												
												}
										}
								}
						});
					},
					function(){
							frappe.msgprint('Approval NOT revoked')
					}
				)
			}
		}).css({'color':'white','font-weight': 'normal', background: frm.doc.approved == 1 ? "#000000" : "#2490ef"});
		}
		
		//if form approved and user is not administrator 
		if(frm.doc.approved == 1 && frappe.user.has_role('Administrator') != 1){
			frm.disable_save();
			$.each(frm.fields_dict, function(fieldname, field) {
	      frm.set_df_property(fieldname, "read_only", 1)	
	    });
			frm.dashboard.hide()
		}
  }

});


