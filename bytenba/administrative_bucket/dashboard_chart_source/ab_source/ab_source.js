frappe.provide('frappe.dashboards.chart_sources');


frappe.dashboards.chart_sources["Ab Source"] = {
	
	method: "bytenba.research_bucket.dashboard_chart_source.rb_source.rb_source.get",
	
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