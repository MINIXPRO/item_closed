import frappe
import pymysql

@frappe.whitelist()
def update_material_request(item_code, qty):
    """
    Updates the custom_purchase_order_generated field for Material Request Items.

    Args:
        item_code (str): The item code to filter Material Request Items.
        qty (int): The quantity to filter Material Request Items.

    Returns:
        bool: True if the update is successful, False otherwise.
    """
    if not item_code or not qty:
        frappe.throw("Item code and quantity are required parameters.")
    
    try:
        material_request_items = frappe.get_all(
            'Material Request Item', 
            filters={'item_code': item_code, 'qty': qty},
            fields=['name']
        )
        
        if not material_request_items:
            frappe.log("No Material Request Items found for item_code: {0} and qty: {1}".format(item_code, qty))
            return False

        for item in material_request_items:
            frappe.db.set_value('Material Request Item', item['name'], 'custom_purchase_order_generated', 1)
        
        frappe.db.commit()  # Ensure changes are committed to the database
        return True

    except pymysql.err.OperationalError as e:
        if e.args[0] == 1305:
            frappe.log_error(frappe.get_traceback(), "OperationalError: Function or procedure does not exist.")
        else:
            frappe.log_error(frappe.get_traceback(), f"OperationalError: {str(e)}")
        return False
    
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), f"Error in update_material_request: {str(e)}")
        return False
