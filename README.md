# Odoo-Task-2

# 1 - Sale Module
Create a new char field (Dimension:) in sale order line to allow salesperson to add the product dimension (e.g 4cm * 12 cm)


# 2 - Inventory
When confirm sale order system by default create a delivery order to all sortable product,Please create a new char field (Dimension:) in stock move that read from sale order line also make this field editable (user can edit this field and this will NOT reflect the sale order line)

# 3 - Invoicing
When create invoice to this sale order please add a new char field (Dimension:) in account invoice line that read from stock move dimension NOT the dimension of sale order line and this field should be readonly
