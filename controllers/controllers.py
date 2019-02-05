# -*- coding: utf-8 -*-
from odoo import http

# class Crevisoft(http.Controller):
#     @http.route('/crevisoft/crevisoft/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crevisoft/crevisoft/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('crevisoft.listing', {
#             'root': '/crevisoft/crevisoft',
#             'objects': http.request.env['crevisoft.crevisoft'].search([]),
#         })

#     @http.route('/crevisoft/crevisoft/objects/<model("crevisoft.crevisoft"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crevisoft.object', {
#             'object': obj
#         })