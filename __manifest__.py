# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Gestion de Dotation',
    'version': '0.1',
    'author': 'reda mekhezzem & meriah nesrine',
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
             'views/article_dotation.xml'
             ],
    'website' :'https://www.redamekhezzem.meriahnesrine.co.uk',
    'license' : 'GPL-2',
}
