# -*- coding: utf-8 -*-
from odoo import http

# class ImageCompressor(http.Controller):
#     @http.route('/image_compressor/image_compressor/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/image_compressor/image_compressor/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('image_compressor.listing', {
#             'root': '/image_compressor/image_compressor',
#             'objects': http.request.env['image_compressor.image_compressor'].search([]),
#         })

#     @http.route('/image_compressor/image_compressor/objects/<model("image_compressor.image_compressor"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('image_compressor.object', {
#             'object': obj
#         })