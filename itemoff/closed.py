# # your_app/api.py
# import frappe

# @frappe.whitelist()
# def get_existing_purchase_orders(material_request, items):
#     existing_po_items = {}

#     purchase_orders = frappe.db.sql("""
#         SELECT poi.item_code, SUM(poi.qty) as qty
#         FROM `tabPurchase Order Item` poi
#         JOIN `tabPurchase Order` po ON po.name = poi.parent
#         WHERE po.docstatus < 2 AND poi.material_request = %s AND poi.item_code IN %s
#         GROUP BY poi.item_code
#     """, (material_request, tuple(items)), as_dict=True)

#     for po_item in purchase_orders:
#         existing_po_items[po_item.item_code] = po_item.qty

#     return existing_po_items
