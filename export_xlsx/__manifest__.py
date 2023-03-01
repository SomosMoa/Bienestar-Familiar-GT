# -*- coding: utf-8 -*-
{
    'name': "XLSX",

    'summary': "Integrate the validation of electronic invoices with Digifact",

    'description': "Allow the validation of Electronic Invoices with SAT in the Purchase, Sale, PoS and Billing modules having Digifact as an intermediary.",

    'author': "Somos Moa",
    'website': "https://somosmoa.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report_xlsx'],

    # always loaded
    'data': [
        'reports/purcharse_book.xml',
    ],
    
    'external_dependencies': {
    },
}