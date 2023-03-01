from odoo import models, fields, api

class sale_inherit(models.Model):
    _inherit='sale.order'

    operation_date = fields.Datetime(string = 'Fecha de Operacion')
    invoice_fel= fields.char(string='Factura FEL')
    invoice_code = fields.Char(string='Referencia Interna')

    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['validation_code'] = self.invoice_fel
        invoice_vals['invoice_code'] = self.invoice_code
        return invoice_vals
