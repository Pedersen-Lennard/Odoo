# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Custom Shop Floor View',
    'summary': 'This is a custom view that modifies the shop order',
    'depends': ['base', 'account', 'sale', 'product', 'purchase', 'stock', 'mrp_workorder', 'web'],
    'assets': {
        'web.assets_backend': [
            'custom_shop_floor/static/src/components/*/*.js',
            'custom_shop_floor/static/src/components/*/*.xml',
            'custom_shop_floor/static/src/components/*/*.scss',
        ]
    },
    'data': [
    ],
}
