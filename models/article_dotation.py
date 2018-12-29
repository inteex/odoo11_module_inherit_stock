# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models

class Article_dotation(models.Model):
    _inherit = 'product.template'

    dotation_ok = fields.Boolean(string="dotation")

