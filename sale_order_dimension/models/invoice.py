from odoo import models, fields, api

class invoice_dimension(models.Model):
    _inherit = 'account.move.line'
    dimension = fields.Char(readonly='True')


