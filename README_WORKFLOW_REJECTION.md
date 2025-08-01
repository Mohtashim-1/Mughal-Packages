# Workflow Rejection Reason Extension

This extension adds rejection reason functionality to the standard Frappe Workflow doctype.

## Features

- Extends the standard Workflow doctype with rejection reason fields
- **NEW**: Checkbox in workflow states to mark specific states as rejection states
- Requires users to provide a reason when rejecting documents
- Supports both rejection reason (dropdown) and rejection notes (text)
- Works with any document type that has workflow enabled

## Setup Instructions

### 1. Install the App

```bash
bench --site your-site.com install-app mughal_packages
```

### 2. Add Rejection Fields to Your Document

Add these fields to your document's custom fields:

```json
{
  "fieldname": "rejection_reason",
  "fieldtype": "Select",
  "label": "Rejection Reason",
  "options": "Incomplete Information\nIncorrect Data\nMissing Documents\nPolicy Violation\nOther",
  "read_only": 1
},
{
  "fieldname": "rejection_notes",
  "fieldtype": "Text",
  "label": "Rejection Notes",
  "read_only": 1
}
```

### 3. Configure Workflow

1. Go to **Setup > Workflow**
2. Create or edit a workflow
3. In the **Rejection Settings** section:
   - ✅ Check **Enable Rejection Reason**
   - Set **Rejection Reason Field** to `rejection_reason`
   - Set **Rejection Notes Field** to `rejection_notes`

### 4. Configure Workflow States

**NEW METHOD (Recommended):**
1. In the **States** section, for each rejection state:
   - ✅ Check **"Require Rejection Remarks"** checkbox
   - This will automatically trigger rejection dialog when transitioning to this state

**Example Workflow States:**
```
State: Draft
State: Pending  
State: Approved
State: Rejected    ← Check "Require Rejection Remarks"
State: Declined    ← Check "Require Rejection Remarks"
```

### 5. Configure Transitions

Set up your transitions normally:
```
From: Pending → To: Approved (Action: Approve)
From: Pending → To: Rejected (Action: Reject)
From: Pending → To: Declined (Action: Decline)
```

## How It Works

### **Primary Method: State-Level Configuration**
1. When creating workflow states, check **"Require Rejection Remarks"** for rejection states
2. When user tries to transition to a state with this checkbox checked
3. System automatically shows rejection dialog
4. User must provide rejection reason and notes
5. Information is saved to the document
6. Workflow transition proceeds

### **Fallback Methods:**
If no states have the checkbox checked, the system falls back to:
- State name detection: "Rejected", "Declined", "Cancelled", "Returned", "Denied"
- Action name detection: "reject", "decline", "cancel", "return", "deny"

## Example Usage

### **For Purchase Order:**

1. **Add rejection fields to Purchase Order custom fields**
2. **Create workflow with states:**
   ```
   Draft → Pending → Approved/Rejected
   ```
3. **In workflow configuration:**
   - Enable rejection reason
   - Set rejection fields
   - **Check "Require Rejection Remarks" for "Rejected" state**
4. **Result:** When rejecting, users must provide reason

### **For Sales Invoice:**

1. **Add rejection fields to Sales Invoice custom fields**
2. **Create workflow with states:**
   ```
   Draft → Pending → Approved/Rejected
   ```
3. **In workflow configuration:**
   - Enable rejection reason
   - Set rejection fields
   - **Check "Require Rejection Remarks" for "Rejected" state**
4. **Result:** When rejecting, users must provide reason

## Files Created

- `custom/workflow.json` - Extends standard workflow doctype
- `custom/workflow_state.json` - Extends workflow state doctype with checkbox
- `custom/sales_invoice.json` - Example for Sales Invoice
- `doctype/custom_workflow/custom_workflow.py` - Python controller
- `public/js/workflow_rejection.js` - Frontend JavaScript
- `hooks.py` - App configuration

## Troubleshooting

1. **Rejection dialog not appearing**: 
   - Check if rejection reason is enabled in workflow settings
   - Check if target state has "Require Rejection Remarks" checked
2. **Fields not saving**: Ensure the rejection fields exist in your document
3. **JavaScript errors**: Check browser console for any JavaScript errors 