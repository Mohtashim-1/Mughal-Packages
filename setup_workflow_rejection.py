#!/usr/bin/env python3
import frappe
import json

def setup_workflow_rejection():
    """Setup workflow rejection fields"""
    
    # Add custom fields to Workflow doctype
    add_workflow_custom_fields()
    
    # Add custom fields to Workflow State doctype
    add_workflow_state_custom_fields()
    
    print("✅ Workflow rejection fields setup completed!")

def add_workflow_custom_fields():
    """Add custom fields to Workflow doctype"""
    
    # Check if custom field already exists
    existing = frappe.db.exists("Custom Field", {
        "dt": "Workflow",
        "fieldname": "rejection_section"
    })
    
    if not existing:
        # Add Section Break
        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Workflow",
            "fieldname": "rejection_section",
            "fieldtype": "Section Break",
            "label": "Rejection Settings",
            "insert_after": "transitions"
        }).insert()
    
    # Check if enable_rejection_reason exists
    existing = frappe.db.exists("Custom Field", {
        "dt": "Workflow",
        "fieldname": "enable_rejection_reason"
    })
    
    if not existing:
        # Add Enable Rejection Reason
        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Workflow",
            "fieldname": "enable_rejection_reason",
            "fieldtype": "Check",
            "label": "Enable Rejection Reason",
            "description": "When enabled, users will be required to provide a reason when rejecting documents",
            "default": "0",
            "insert_after": "rejection_section"
        }).insert()
    
    # Check if rejection_reason_field exists
    existing = frappe.db.exists("Custom Field", {
        "dt": "Workflow",
        "fieldname": "rejection_reason_field"
    })
    
    if not existing:
        # Add Rejection Reason Field
        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Workflow",
            "fieldname": "rejection_reason_field",
            "fieldtype": "Data",
            "label": "Rejection Reason Field",
            "description": "Field name in the document where rejection reason will be stored (e.g., 'rejection_reason')",
            "depends_on": "eval:doc.enable_rejection_reason==1",
            "insert_after": "enable_rejection_reason"
        }).insert()
    
    # Check if rejection_notes_field exists
    existing = frappe.db.exists("Custom Field", {
        "dt": "Workflow",
        "fieldname": "rejection_notes_field"
    })
    
    if not existing:
        # Add Rejection Notes Field
        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Workflow",
            "fieldname": "rejection_notes_field",
            "fieldtype": "Data",
            "label": "Rejection Notes Field",
            "description": "Field name in the document where rejection notes will be stored (e.g., 'rejection_notes')",
            "depends_on": "eval:doc.enable_rejection_reason==1",
            "insert_after": "rejection_reason_field"
        }).insert()
    
    print("✅ Workflow custom fields added!")

def add_workflow_state_custom_fields():
    """Add custom fields to Workflow State doctype"""
    
    # Check if custom_rejected_remarks exists
    existing = frappe.db.exists("Custom Field", {
        "dt": "Workflow State",
        "fieldname": "custom_rejected_remarks"
    })
    
    if not existing:
        # Add Custom Rejected Remarks
        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Workflow State",
            "fieldname": "custom_rejected_remarks",
            "fieldtype": "Check",
            "label": "Require Rejection Remarks",
            "description": "If checked, users must provide rejection reason when transitioning to this state",
            "insert_after": "allow_edit"
        }).insert()
    
    print("✅ Workflow State custom fields added!")

if __name__ == "__main__":
    setup_workflow_rejection() 