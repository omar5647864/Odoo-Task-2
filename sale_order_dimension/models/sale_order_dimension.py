# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime


class sale_order_dimension(models.Model):
    _inherit = 'sale.order.line'

    dimension = fields.Char("Dimension")
    dimension1 = fields.Char("Test")

    def _prepare_invoice_line(self,**optional_values):
        res = super(sale_order_dimension, self)._prepare_invoice_line(**optional_values)
        res.update({'dimension': self.dimension1})
        return res












