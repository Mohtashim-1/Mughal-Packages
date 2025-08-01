import frappe
from frappe.model.document import Document

@frappe.whitelist()
def get_rejection_dialog(workflow_name, doc_name, doc_type):
    """Get rejection dialog for workflow transitions"""
    try:
        # Get the workflow
        workflow = frappe.get_doc("Workflow", workflow_name)
        
        if not workflow.enable_rejection_reason:
            return None
            
        # Get the document
        doc = frappe.get_doc(doc_type, doc_name)
        
        # Check if document has the rejection fields
        has_rejection_reason = hasattr(doc, workflow.rejection_reason_field)
        has_rejection_notes = hasattr(doc, workflow.rejection_notes_field)
        
        return {
            "enable_rejection_reason": workflow.enable_rejection_reason,
            "rejection_reason_field": workflow.rejection_reason_field,
            "rejection_notes_field": workflow.rejection_notes_field,
            "has_rejection_reason": has_rejection_reason,
            "has_rejection_notes": has_rejection_notes,
            "current_rejection_reason": getattr(doc, workflow.rejection_reason_field, ""),
            "current_rejection_notes": getattr(doc, workflow.rejection_notes_field, "")
        }
    except Exception as e:
        frappe.log_error(f"Error getting rejection dialog: {str(e)}")
        return None

@frappe.whitelist()
def save_rejection_reason(workflow_name, doc_name, doc_type, rejection_reason, rejection_notes):
    """Save rejection reason to the document"""
    try:
        # Get the workflow
        workflow = frappe.get_doc("Workflow", workflow_name)
        
        if not workflow.enable_rejection_reason:
            return {"success": False, "message": "Rejection reason not enabled for this workflow"}
            
        # Get the document
        doc = frappe.get_doc(doc_type, doc_name)
        
        # Update rejection fields
        if hasattr(doc, workflow.rejection_reason_field):
            setattr(doc, workflow.rejection_reason_field, rejection_reason)
            
        if hasattr(doc, workflow.rejection_notes_field):
            setattr(doc, workflow.rejection_notes_field, rejection_notes)
        
        # Save the document
        doc.save()
        
        return {"success": True, "message": "Rejection reason saved successfully"}
    except Exception as e:
        frappe.log_error(f"Error saving rejection reason: {str(e)}")
        return {"success": False, "message": f"Error saving rejection reason: {str(e)}"}

@frappe.whitelist()
def check_workflow_rejection_required(workflow_name, from_state, to_state, action=None):
    """Check if rejection reason is required for this transition"""
    try:
        # Get the workflow
        workflow = frappe.get_doc("Workflow", workflow_name)
        
        if not workflow.enable_rejection_reason:
            return False
            
        # Method 1: Check if target state has custom_rejected_remarks checked
        for state in workflow.workflow_states:
            if state.state == to_state and state.custom_rejected_remarks:
                return True
            
        # Method 2: Check if target state is a rejection state (fallback)
        rejected_states = ["Rejected", "Declined", "Cancelled", "Returned", "Denied"]
        if to_state in rejected_states:
            return True
            
        # Method 3: Check if action name indicates rejection (fallback)
        rejection_actions = ["reject", "decline", "cancel", "return", "deny"]
        if action and action.lower() in rejection_actions:
            return True
            
        # Method 4: Check if workflow has custom rejection states configured (fallback)
        if hasattr(workflow, 'rejection_states') and workflow.rejection_states:
            custom_rejection_states = [state.strip() for state in workflow.rejection_states.split('\n')]
            if to_state in custom_rejection_states:
                return True
            
        return False
    except Exception as e:
        frappe.log_error(f"Error checking workflow rejection requirement: {str(e)}")
        return False

# Add validation to the standard workflow doctype
def validate_workflow(doc, method):
    """Validate workflow rejection settings"""
    if hasattr(doc, 'enable_rejection_reason') and doc.enable_rejection_reason:
        if not doc.rejection_reason_field:
            frappe.throw("Rejection Reason Field is required when Enable Rejection Reason is checked")
        if not doc.rejection_notes_field:
            frappe.throw("Rejection Notes Field is required when Enable Rejection Reason is checked") 


