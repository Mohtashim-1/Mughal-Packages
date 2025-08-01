// Workflow Rejection Reason Handler
frappe.workflow_rejection = {
    show_rejection_dialog: function(workflow_name, doc_name, doc_type, from_state, to_state, callback) {
        // Check if rejection is required for this transition
        frappe.call({
            method: 'mughal_packages.mughal_packages.doctype.custom_workflow.custom_workflow.check_workflow_rejection_required',
            args: {
                workflow_name: workflow_name,
                from_state: from_state,
                to_state: to_state,
                action: action
            },
            callback: function(r) {
                if (r.message) {
                    // Rejection is required, show dialog
                    frappe.workflow_rejection.create_rejection_dialog(workflow_name, doc_name, doc_type, callback);
                } else {
                    // No rejection required, proceed with normal transition
                    if (callback) callback();
                }
            },
            error: function(r) {
                // On error, proceed with normal transition
                if (callback) callback();
            }
        });
    },

    create_rejection_dialog: function(workflow_name, doc_name, doc_type, callback) {
        // Get rejection dialog configuration
        frappe.call({
            method: 'mughal_packages.mughal_packages.doctype.custom_workflow.custom_workflow.get_rejection_dialog',
            args: {
                workflow_name: workflow_name,
                doc_name: doc_name,
                doc_type: doc_type
            },
            callback: function(r) {
                if (r.message && r.message.enable_rejection_reason) {
                    frappe.workflow_rejection.show_dialog(r.message, workflow_name, doc_name, doc_type, callback);
                } else {
                    // No rejection dialog configured, proceed with normal transition
                    if (callback) callback();
                }
            },
            error: function(r) {
                // On error, proceed with normal transition
                if (callback) callback();
            }
        });
    },

    show_dialog: function(config, workflow_name, doc_name, doc_type, callback) {
        let d = new frappe.ui.Dialog({
            title: __('Rejection Reason Required'),
            fields: [
                {
                    fieldname: 'rejection_reason',
                    fieldtype: 'Select',
                    label: __('Rejection Reason'),
                    options: 'Incomplete Information\nIncorrect Data\nMissing Documents\nPolicy Violation\nOther',
                    reqd: 1,
                    default: config.current_rejection_reason || ''
                },
                {
                    fieldname: 'rejection_notes',
                    fieldtype: 'Text',
                    label: __('Additional Notes'),
                    description: __('Please provide additional details about the rejection'),
                    default: config.current_rejection_notes || ''
                }
            ],
            primary_action_label: __('Submit'),
            primary_action: function(values) {
                // Save rejection reason
                frappe.call({
                    method: 'mughal_packages.mughal_packages.doctype.custom_workflow.custom_workflow.save_rejection_reason',
                    args: {
                        workflow_name: workflow_name,
                        doc_name: doc_name,
                        doc_type: doc_type,
                        rejection_reason: values.rejection_reason,
                        rejection_notes: values.rejection_notes
                    },
                    callback: function(r) {
                        if (r.message && r.message.success) {
                            frappe.show_alert(__('Rejection reason saved successfully'), 'green');
                            d.hide();
                            if (callback) callback();
                        } else {
                            frappe.show_alert(r.message.message || __('Error saving rejection reason'), 'red');
                        }
                    },
                    error: function(r) {
                        frappe.show_alert(__('Error saving rejection reason'), 'red');
                    }
                });
            },
            secondary_action_label: __('Cancel'),
            secondary_action: function() {
                d.hide();
            }
        });
        d.show();
    }
};

// Override the standard workflow transition to include rejection reason
frappe.workflow = frappe.workflow || {};
const original_workflow_transition = frappe.workflow.transition_to;

frappe.workflow.transition_to = function(doc, action, update, callback) {
    // Check if this is a custom workflow with rejection reason enabled
    if (doc.workflow_name) {
        frappe.call({
            method: 'mughal_packages.mughal_packages.doctype.custom_workflow.custom_workflow.check_workflow_rejection_required',
            args: {
                workflow_name: doc.workflow_name,
                from_state: doc.workflow_state,
                to_state: action,
                action: action
            },
            callback: function(r) {
                if (r.message) {
                    // Rejection is required, show dialog
                    frappe.workflow_rejection.show_rejection_dialog(
                        doc.workflow_name, 
                        doc.name, 
                        doc.doctype, 
                        doc.workflow_state, 
                        action, 
                        function() {
                            // After rejection reason is saved, proceed with transition
                            if (original_workflow_transition) {
                                original_workflow_transition(doc, action, update, callback);
                            }
                        }
                    );
                } else {
                    // No rejection required, proceed with normal transition
                    if (original_workflow_transition) {
                        original_workflow_transition(doc, action, update, callback);
                    }
                }
            },
            error: function(r) {
                // On error, proceed with normal transition
                if (original_workflow_transition) {
                    original_workflow_transition(doc, action, update, callback);
                }
            }
        });
    } else {
        // No custom workflow, proceed with normal transition
        if (original_workflow_transition) {
            original_workflow_transition(doc, action, update, callback);
        }
    }
}; 