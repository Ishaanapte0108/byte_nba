import datetime
import os
import random
import re
import string
import time
import boto3
from botocore.client import Config
from botocore.exceptions import ClientError
import frappe
import threading


AWS_ACCESS_KEY = 'AKIA2BMG37DHUNDSWJWC'
AWS_SECRET_KEY = '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'
AWS_S3_BUCKET_NAME = 'appraiseprofilestorage'
AWS_REGION = 'us-west-2'
# LOCAL_FILE = '11evidence.pdf'
# OBJECT_KEY = 'fromAppNEW.pdf'
CONTENT_TYPE = 'application/pdf'

s3_client = boto3.client(service_name='s3',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

def boot_session(bootinfo):
    bootinfo.my_global_template = """frappe.ui.form.on('{{DocType}}', {

	refresh: function(frm) {

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

});"""


@frappe.whitelist()
def file_upload_to_s3(doc, method):

    def metaData(doc):

        #get file path in dir
        path = doc.file_url
        #get file name
        doc_name = doc.file_name
        
        #check for valid extensions
        match = re.search(r'^(.+)\.([^.]+)$', doc_name)
        if match:
            extension = match.group(2)
            if extension not in ['jpeg', 'txt', 'pdf', 'png']:
                frappe.throw('Entered file format not accepted')
        else:
            frappe.throw('File name improper')

        #get parent doctype
        parent_doctype = doc.attached_to_doctype or 'File'
            
        if not doc.is_private:
            
            #get full file path
            file_path = frappe.utils.get_site_path() + '/public' + path

            #generate a custom name
            OBJECT_KEY = str(int(time.time())) + '_' + doc_name
            
            regex = re.compile('[^0-9a-zA-Z._-]')
            OBJECT_KEY = regex.sub('_', OBJECT_KEY)

            return {'LOCAL_FILE' : file_path, 'OBJECT_KEY': OBJECT_KEY, 'PARENT_DOCTYPE': parent_doctype, 'DOCNAME': doc.name, 'ATTACHED_TO_NAME': doc.attached_to_name}

        if doc.is_private:
            return False

    def upload_to_container(LOCAL_FILE, OBJECT_KEY):
        try:
            response = s3_client.upload_file(LOCAL_FILE, AWS_S3_BUCKET_NAME, OBJECT_KEY, ExtraArgs={'ContentType': 'application/pdf'})
            return True
        except Exception as e:
            return False
        

    
    def preSignedUrlGenerate(OBJECT_KEY):
        try:
            response = s3_client.generate_presigned_url('get_object', Params={'Bucket': AWS_S3_BUCKET_NAME,
            'Key': OBJECT_KEY}, ExpiresIn= 100)
            return response
        except Exception as e:
            return False


    info = metaData(doc)
    if info:
        success = upload_to_container(info['LOCAL_FILE'], info['OBJECT_KEY'])
        if success:
            psu = preSignedUrlGenerate(info['OBJECT_KEY'])
            if psu:
                try:
                    r1 = frappe.db.sql("""UPDATE `tabFile` SET file_name = %s, file_url=%s WHERE name=%s""", (
                    info['OBJECT_KEY'], psu, info['DOCNAME']))
                        
                except Exception as e:
                    frappe.throw(r1, e)

                try:
                    p_doc = frappe.get_last_doc(info['PARENT_DOCTYPE'])
                    # query = """UPDATE `{parent_name}` SET attach_evidence = "{signed_url}" WHERE name = '{p_doc_name}'""".format(parent_name = "tab" + info['PARENT_DOCTYPE'], signed_url = psu, p_doc_name = p_doc.name)
                    # r2 = frappe.db.sql(query)
                    # print(query)
                    frappe.db.set_value(info['PARENT_DOCTYPE'], p_doc.name, "attach_evidence", psu)
                    frappe.msgprint('here')
                except Exception as e:
                    frappe.throw(e)

                frappe.db.commit()
                os.remove(info['LOCAL_FILE'])
        else:
            frappe.throw("Could not upload to cloud")
    else:
        frappe.msgprint('Private files will not be uploaded to cloud')


@frappe.whitelist()
def delete_from_cloud(doc, method):
    """Delete file from s3"""
    # s3 = S3Operations()
    # s3.delete_from_s3(doc.content_hash)
    frappe.msgprint('now here')
