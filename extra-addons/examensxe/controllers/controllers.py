# -*- coding: utf-8 -*-
# from odoo import http


# class Examensxe(http.Controller):
#     @http.route('/examensxe/examensxe', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/examensxe/examensxe/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('examensxe.listing', {
#             'root': '/examensxe/examensxe',
#             'objects': http.request.env['examensxe.examensxe'].search([]),
#         })

#     @http.route('/examensxe/examensxe/objects/<model("examensxe.examensxe"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('examensxe.object', {
#             'object': obj
#         })
