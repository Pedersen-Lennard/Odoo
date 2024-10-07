from odoo import models, fields, api
import re


class CustomPurchaseQuotation(models.Model):
    _inherit = 'purchase.order.line'

    product_id = fields.Many2one('product.product', string='Product')
    default_code = fields.Char(string="Item Code", compute='_compute_default_code', store="True")
    clean_name = fields.Char(string="Clean Product Name", compute='_compute_clean_name', store=True)

    @api.depends('name')
    def _compute_clean_name(self):
        for line in self:
            # Remove text within brackets and the brackets themselves
            line.clean_name = re.sub(r'\[.*?\]', '', line.name)

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
    display_product_name = fields.Char(string="Product Name", compute='_compute_display_product_name', store="True")

    @api.depends('product_id', 'product_template_id')
    def _compute_display_product_name(self):
        for line in self:
            description_sale = line.product_template_id.description_sale or ''
            product_variant = line.product_id.product_template_variant_value_ids or ''
            variants = []
            if description_sale == False or description_sale == '':
                line.display_product_name = line.product_template_id.name
            else:
                if product_variant:
                    for value in product_variant:
                        variants.append(value.name)
                    string_variants = ', '.join(variants)
                if len(variants) > 0:
                    line.display_product_name = f"{description_sale} ({string_variants})"
                else:
                    line.display_product_name = description_sale

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

class AccountMove(models.Model):
    _inherit = 'account.move'

    x_partner_invoice_id = fields.Many2one(
        comodel_name='res.partner',
        string='Invoice Address',
        compute='_compute_partner_invoice_id', store=True, readonly=False, precompute=True,
        check_company=True,
    )

    @api.depends('partner_id')
    def _compute_partner_invoice_id(self):
        for move in self:
            if move.is_invoice(include_receipts=True):
                addr = move.partner_id.address_get(['invoice'])  # Get the invoice address
                move.x_partner_invoice_id = addr and addr.get('invoice')  # Set the invoice address
            else:
                move.x_partner_invoice_id = False