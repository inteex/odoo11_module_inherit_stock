# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Gestion de Dotation',
    'version': '0.1',
    'author': 'reda mekhezzem',
    'category': 'Article',
    'description': "automatisation de la gestion des dotations",
    'depends': [
                'stock',
                'hr',
                'product'
                ],
    'installable': True,
    'application': True,
    'data': [
             'views/article_dotation.xml',
             'views/decharge_view.xml',
             'views/ligne_decharge_view.xml',
             'views/employer_view.xml',
             'report/decharge_report.xml'
    ],
    'website' :'https://www.redamekhezzem.co.uk',
    'license' : 'GPL-2',
}
