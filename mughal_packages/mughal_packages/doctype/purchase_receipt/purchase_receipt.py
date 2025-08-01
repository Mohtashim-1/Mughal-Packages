import frappe

def get_secondary_uom_from_item(doc, method):
    """Get unit of measurement from item and get first uom for each item"""
    if doc.items:
        for item in doc.items:
            if item.item_code:
                try:
                    item_doc = frappe.get_doc("Item", item.item_code)
                    if item_doc.uoms:
                        # Get the first UOM from the item's UOM list
                        first_uom = item_doc.uoms[0]
                        if first_uom and hasattr(first_uom, 'uom') and first_uom.uom:
                            item.custom_second_uom = first_uom.uom
                            frappe.msgprint(f"Set second UOM '{first_uom.uom}' for item '{item.item_code}'")
                        else:
                            frappe.msgprint(f"No valid UOM found for item '{item.item_code}'")
                    else:
                        frappe.msgprint(f"No UOMs configured for item '{item.item_code}'")
                except Exception as e:
                    frappe.msgprint(f"Error processing item '{item.item_code}': {str(e)}")
                    frappe.log_error(f"Error in get_secondary_uom_from_item for item {item.item_code}: {str(e)}")

def set_secondary_uom_on_item_add(doc, method):
    """Set secondary UOM when item is added to purchase receipt"""
    if doc.doctype == "Purchase Receipt Item" and doc.item_code:
        try:
            item_doc = frappe.get_doc("Item", doc.item_code)
            if item_doc.uoms:
                first_uom = item_doc.uoms[0]
                if first_uom and hasattr(first_uom, 'uom') and first_uom.uom:
                    doc.custom_second_uom = first_uom.uom
                    frappe.msgprint(f"Set second UOM '{first_uom.uom}' for item '{doc.item_code}'")
        except Exception as e:
            frappe.log_error(f"Error in set_secondary_uom_on_item_add for item {doc.item_code}: {str(e)}")