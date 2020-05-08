# -*- coding: utf-8 -*-
# from odoo import http


# class Wikiapp(http.Controller):
#     @http.route('/wikiapp/wikiapp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wikiapp/wikiapp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('wikiapp.listing', {
#             'root': '/wikiapp/wikiapp',
#             'objects': http.request.env['wikiapp.wikiapp'].search([]),
#         })

#     @http.route('/wikiapp/wikiapp/objects/<model("wikiapp.wikiapp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wikiapp.object', {
#             'object': obj
#         })
