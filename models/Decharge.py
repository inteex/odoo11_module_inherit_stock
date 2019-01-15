# -*-coding: utf-8 -*-
from odoo import models, fields

class Decharge(models.Model):
    _name = "decharge"
    _description = "décharge de l'employer"

    employer_id = fields.Many2one('hr.employee', 'decahrge pour l\'employer', ondelete="cascade")
    etat = fields.Selection([('b', 'brouillant'), ('v', 'Validee')],default='b')
    ligne_decharge_ids = fields.One2many('ligne_decharge','decharge_id','les dotations',ondelete="cascade")
