# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, api

class Employer(models.Model):
    _inherit = 'hr.employee'

    @api.one
    @api.depends('decharge_ids')
    def _nbr_decharge(self):
        decharges = self.env['decharge'].search([('employer_id', '=', self.ids)])
        self.nbr_decharge =len(decharges)

    decharge_ids = fields.One2many('decharge', 'employer_id', 'employer_decharge')
    nbr_decharge = fields.Integer(string="Décharge", compute="_nbr_decharge")