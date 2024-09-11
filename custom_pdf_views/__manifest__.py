# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Custom PDF Views',
    'summary': 'These are custom views for the pdf invoices and quotations',
    'depends': ['base', 'account', 'sale', 'product', 'purchase', 'stock', 'mrp_workorder', 'web'],
    'assets': {
        'web.assets_backend': [
            'custom_pdf_views/static/src/components/*/*.js',
            'custom_pdf_views/static/src/components/*/*.xml',
            # 'custom_pdf_views/static/src/components/*/*.scss',
        ]
    },
    'data': [
        'views/custom_address_template.xml',
        'views/custom_invoice.xml',
        'views/custom_quotations.xml',
        'views/custom_template.xml'
    ],
}
