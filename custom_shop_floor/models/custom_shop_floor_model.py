from odoo import models, fields, api


class CustomShopFloor(models.Model):
    _inherit = 'mrp.workorder'

    x_record = fields.Char(string="Record Field", store=True)

class CustomMrpProduction(models.Model):
    _inherit = 'mrp.production'

    # Define a One2many field to link to multiple mrp.workorder records
    x_record_production = fields.One2many(
        'mrp.workorder',
        'x_record',  # Field in mrp.workorder that links back to mrp.production
        string='Test Record'
    )