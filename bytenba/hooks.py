from . import __version__ as app_version

app_name = "bytenba"
app_title = "bytenba"
app_publisher = "byte_team"
app_description = "ERP for Clg"
app_email = "ishaanmapte@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/bytenba/css/bytenba.css"
# app_include_js = "/assets/bytenba/js/bytenba.js"

# include js, css files in header of web template
# web_include_css = "/assets/bytenba/css/bytenba.css"
# web_include_js = "/assets/bytenba/js/bytenba.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "bytenba/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}

doctype_list_js = {
  "Certification for courses allotted": "bytenba/bytenba/doctype/certification_for_courses_allotted/certification_for_courses_allotted_list.js",
  "ME Projects": "bytenba/bytenba/doctype/me_projects/me_projects_list.js",
  "MMS FY Projects": "bytenba/bytenba/doctype/mms_fy_projects/mms_fy_projects_list.js",
  "BSA guest lecture":"bytenba/bytenba/doctype/bsa_guest_lecture/bsa_guest_lecture_list.js",
  "BSA-Co-curricular":"bytenba/bytenba/doctype/bsa_co_curricular/bsa_co_curricular_list.js",
  "BSA-Mini Prj":"bytenba/bytenba/doctype/bsa_mini_prj/bsa_mini_prj_list.js",
  "BSA industrial visit":"bytenba/bytenba/doctype/bsa_industrial_visit/bsa_industrial_visit_list.js",
  "Course_Lab outcome attainment" : "bytenba/bytenba/doctype/course_lab_outcome_attainment/course_lab_outcome_attainment_list.js",
  "Internal revenue generation": "bytenba/consultancy_and_corporate_training_bucket/doctype/internal_revenue_generation/internal_revenue_generation_list.js"
}

extend_bootinfo = "bytenba.controller.boot_session"

# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

doctype_js = {
    # "Certification for courses allotted": "public/js/custom_cert_courses.js",
    # "Courses taught": "public/js/custom_cert_courses.js",
    # "Course_Lab outcome attainment":"public/js/custom_cert_courses.js",
    # "BSA industrial visit":"public/js/custom_cert_courses.js",
    # "Innovation in TLP":"public/js/custom_cert_courses.js",
    # "BSA industrial visit":"public/js/custom_cert_courses.js",
    # "BSA guest lecture": "public/js/custom_cert_courses.js",
    # "BSA-Mini Prj":"public/js/custom_cert_courses.js",
    # "BSA-Co-curricular":"public/js/custom_cert_courses.js"
    # "Professors":"public/js/custom_cert_courses.js",
    # "Course-lab outcome attainment": "public/js/custom_cert_courses.js",
}


sounds = [
	{"name": "email", "src": "/assets/frappe/sounds/email.mp3", "volume": 0.1},
	{"name": "submit", "src": "/assets/frappe/sounds/submit.mp3", "volume": 0.1},
	{"name": "cancel", "src": "/assets/frappe/sounds/cancel.mp3", "volume": 0.1},
	{"name": "delete", "src": "/assets/frappe/sounds/delete.mp3", "volume": 0.05},
	{"name": "click", "src": "/assets/frappe/sounds/click.mp3", "volume": 0.05},
	{"name": "error", "src": "/assets/frappe/sounds/error.mp3", "volume": 0.1},
	{"name": "alert", "src": "/assets/frappe/sounds/alert.mp3", "volume": 0.2},
	# {"name": "chime", "src": "/assets/frappe/sounds/chime.mp3"},
]
# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "index"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "bytenba.utils.jinja_methods",
#	"filters": "bytenba.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "bytenba.install.before_install"
# after_install = "bytenba.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "bytenba.uninstall.before_uninstall"
# after_uninstall = "bytenba.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "bytenba.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events
doc_events = {
    # "File": {
    #     "after_insert": "bytenba.controller.file_upload_to_s3",
    #     "on_trash": "bytenba.controller.delete_from_cloud"
    # }

    # "Certification for courses allotted": {
    #   "on_trash": "bytenba.form_validation.validate_delete"
    # }
}


# doc_events = {

    # "BSA-Co-curricular": {
    #     "on_update":"bytenba.bytenba.doctype.bsa_co_curricular.bsa_co_curricular.sumDocs"
    # },
    # "Certification for courses allotted": {
    #   "on_update": "bytenba.bytenba.doctype.certification_for_courses_allotted.certification_for_courses_allotted.rankDocs",
    # },
    # "BSA guest lecture":{
    #   "on_update":"bytenba.bytenba.doctype.bsa_guest_lecture.bsa_guest_lecture.addDocs"
    # }
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"bytenba.tasks.all"
#	],
#	"daily": [
#		"bytenba.tasks.daily"
#	],
#	"hourly": [
#		"bytenba.tasks.hourly"
#	],
#	"weekly": [
#		"bytenba.tasks.weekly"
#	],
#	"monthly": [
#		"bytenba.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "bytenba.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "bytenba.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "bytenba.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["bytenba.utils.before_request"]
# after_request = ["bytenba.utils.after_request"]

# Job Events
# ----------
# before_job = ["bytenba.utils.before_job"]
# after_job = ["bytenba.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"bytenba.auth.validate"
# ]
