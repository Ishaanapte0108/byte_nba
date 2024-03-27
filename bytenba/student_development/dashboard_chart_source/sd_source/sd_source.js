frappe.provide('frappe.dashboards.chart_sources');


frappe.dashboards.chart_sources["Sd source"] = {
	
  method: "bytenba.student_development.dashboard_chart_source.sd_source.sd_source.get",
	
	filters: [
		{
			// fieldname: "type",
			// label: __("Analysis Type"),
			// fieldtype: "Select",
			// options: "Overview\nSubmitted\nApproved",
			// default: "Overview"
		},
	],
	
};