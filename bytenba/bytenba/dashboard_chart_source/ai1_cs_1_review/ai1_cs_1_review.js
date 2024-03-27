frappe.provide('frappe.dashboards.chart_sources');


frappe.dashboards.chart_sources["AI1 CS 1 Review"] = {
	
	method: "bytenba.bytenba.dashboard_chart_source.ai1_cs_1_review.ai1_cs_1_review.get",
	
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