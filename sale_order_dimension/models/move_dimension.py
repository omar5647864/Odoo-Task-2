from odoo import models, fields, api

class move_dimension(models.Model):

    _inherit = 'stock.move'
    dimension = fields.Char(compute='get_data',readonly=False)
    dimension1 = fields.Char(string="dimension")
    #dimension_holder = fields.Char(compute='get_data1',readonly=False)
    trigger = fields.Boolean(defualt="False")

    def get_data(self):
        for move in self:
            if not (move.picking_id and move.picking_id.group_id):
                continue
            picking = move.picking_id
            sale_order = self.env['sale.order'].sudo().search([
                ('procurement_group_id', '=', picking.group_id.id)], limit=1)
            for line in sale_order.order_line:
                if line.product_id.id != move.product_id.id:
                    continue
                move.update({
                    'dimension': line.dimension,
                })
                line.update({
                    'dimension1': move.dimension1,
                })
            if move.trigger == False:
                move.update({
                    'dimension1': move.dimension,
                })
                move.trigger = True
















