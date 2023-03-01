# -*- coding: utf-8 -*-
{
    'name': "Digifact Integration",

    'summary': "Integrate the validation of electronic invoices with Digifact",

    'description': "Allow the validation of Electronic Invoices with SAT in the Purchase, Sale, PoS and Billing modules having Digifact as an intermediary.",

    'author': "Somos Moa",
    'website': "https://somosmoa.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.5',

    # any module necessary for this one to work correctly
    'depends': ['account', 'sale_management', 'report_xlsx'],

    # always loaded
    'data': [
        'views/digifact_button.xml',
        'views/sale_inherit'
    ],
    
    'external_dependencies': {
        'python': ['requests'],
        'python': ['elementpath'],
    },
}
