# -*-coding: utf-8 -*-
from odoo import models, fields

class Ligne_decharge(models.Model):
	_name="ligne_decharge"

	decharge_id = fields.Many2one('decharge', 'numero de la decharge')
	quantite = fields.Integer()
	article = fields.Many2one('product.template');