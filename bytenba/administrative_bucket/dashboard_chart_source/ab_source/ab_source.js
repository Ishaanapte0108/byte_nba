frappe.provide('frappe.dashboards.chart_sources');


frappe.dashboards.chart_sources["Ab Source"] = {
	
	method: "bytenba.administrative_bucket.dashboard_chart_source.ab_source.ab_source.get",
	
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