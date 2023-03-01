from odoo import models, fields, api, _
import logging

class Book_Report_Xlsx(models.AbstractModel):
    _name = 'report.x_libro_de_compras.purchase_book_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data):
        format1 = workbook.add_format({'font_size':13, 'align': 'vcenter', 'bold':True})
        format2= workbook.add_format({'font_size':10, 'align': 'vcenter'})
        sheet = workbook.add_worksheet('Libro de Compra')
        sheet.write(2,2, 'Contactos', format1)
        sheet.write(2,3, self.x_studio_fecha, format2)

