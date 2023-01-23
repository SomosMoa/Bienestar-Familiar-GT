# -*- coding: utf-8 -*-
from odoo import http

class BillsDigifact(http.Controller):
          
    @http.route('/bills_digifact/bills_digifact/', auth='public')
    def index(self, **kw):
        return "Hello, World"
        
    @http.route('/bills_digifact/bills_digifact/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('bills_digifact.listing', {
            'root': '/bills_digifact/bills_digifact',
            'objects': http.request.env['bills_digifact.bills_digifact'].search([]),            
        })
        
    @http.route('/bills_digifact/bills_digifact/objects/<model("bills_digifact.bills_digifact"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('bills_digifact.object', {
            'object': obj            
        })