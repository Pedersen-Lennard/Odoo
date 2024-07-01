from odoo import models, fields, api


class CustomPurchaseQuotation(models.Model):
    _inherit = 'purchase.order.line'

    product_id = fields.Many2one('product.product', string='Product')
    default_code = fields.Char(string="Item Code", compute='_compute_default_code', store="True")

    @api.depends('product_id.default_code')
    def _compute_default_code(self):
        for record in self:
            if record.product_id:
                print(record.product_id)
                record.default_code = record.product_id.default_code
            else:
                record.default_code = False


class CustomSaleQuotation(models.Model):
    _inherit = 'sale.order.line'

    # product_id = fields.Many2one('product.product', string='Product')
    x_default_code = fields.Char(string="Item Code", compute='_compute_default_code', store="True")

    @api.depends('product_template_id.default_code')
    def _compute_default_code(self):
        for record in self:
            if record.product_id:
                record.x_default_code = record.product_id.default_code
            else:
                record.x_default_code = False


class CustomInvoice(models.Model):
    # _name = "custom.invoice"
    _inherit = 'account.move.line'

    # product_id = fields.Many2one('product.product', string='Product', domain=[('purchase_ok', '=', True)], change_default=True, index='btree_not_null')
    product_id = fields.Many2one('product.product', string='Product')
    # product_template_id = fields.Many2one('product.template', string='Product')
    # x_default_code = fields.Char(related='product_id.default_code', compute='_compute_default_code', string="Item Code", store="True")
    x_default_code = fields.Char(string="Item Code", compute='_compute_default_code', store=True)

    @api.depends('product_id.default_code')
    def _compute_default_code(self):
        for record in self:
            if record.product_id:
                record.x_default_code = record.product_id.default_code
            else:
                record.x_default_code = False



