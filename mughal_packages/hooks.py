app_name = "mughal_packages"
app_title = "Mughal Packages"
app_publisher = "mohtashim"
app_description = "app for mughal packages"
app_email = "shoaibmohtashim973@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "mughal_packages",
# 		"logo": "/assets/mughal_packages/logo.png",
# 		"title": "Mughal Packages",
# 		"route": "/mughal_packages",
# 		"has_permission": "mughal_packages.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mughal_packages/css/mughal_packages.css"
app_include_js = "/assets/mughal_packages/js/workflow_rejection.js"

# include js, css files in header of web template
# web_include_css = "/assets/mughal_packages/css/mughal_packages.css"
# web_include_js = "/assets/mughal_packages/js/mughal_packages.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "mughal_packages/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "mughal_packages/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "mughal_packages.utils.jinja_methods",
# 	"filters": "mughal_packages.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "mughal_packages.install.before_install"
# after_install = "mughal_packages.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "mughal_packages.uninstall.before_uninstall"
# after_uninstall = "mughal_packages.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "mughal_packages.utils.before_app_install"
# after_app_install = "mughal_packages.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "mughal_packages.utils.before_app_uninstall"
# after_app_uninstall = "mughal_packages.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mughal_packages.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Workflow": {
		"validate": "mughal_packages.mughal_packages.doctype.custom_workflow.custom_workflow.validate_workflow",
        "on_update": "mughal_packages.mughal_packages.doctype.custom_workflow.custom_workflow.check_workflow_rejection_required"
	},
    "Purchase Receipt": {
        "validate": "mughal_packages.mughal_packages.doctype.purchase_receipt.purchase_receipt.get_secondary_uom_from_item"
    },
    "Purchase Receipt Item": {
        "validate": "mughal_packages.mughal_packages.doctype.purchase_receipt.purchase_receipt.set_secondary_uom_on_item_add"
    },
    "Delivery Note": {
        "validate": "mughal_packages.mughal_packages.doctype.delivery_note.delivery_note.get_secondary_uom_from_item"
    },
    "Delivery Note Item": {
        "validate": "mughal_packages.mughal_packages.doctype.delivery_note.delivery_note.set_secondary_uom_on_item_add"
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"mughal_packages.tasks.all"
# 	],
# 	"daily": [
# 		"mughal_packages.tasks.daily"
# 	],
# 	"hourly": [
# 		"mughal_packages.tasks.hourly"
# 	],
# 	"weekly": [
# 		"mughal_packages.tasks.weekly"
# 	],
# 	"monthly": [
# 		"mughal_packages.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "mughal_packages.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "mughal_packages.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "mughal_packages.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["mughal_packages.utils.before_request"]
# after_request = ["mughal_packages.utils.after_request"]

# Job Events
# ----------
# before_job = ["mughal_packages.utils.before_job"]
# after_job = ["mughal_packages.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"mughal_packages.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

