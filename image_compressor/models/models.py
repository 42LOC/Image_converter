# -*- coding: utf-8 -*-
import os
from PIL import Image

from odoo import models, fields, api


class ImageCompressor(models.Model):
    _name = 'image_compressor'

    def image_compressor_cron(self):
        pathfolder = "/var/odoo-data/filestore/DB1"
        size = 1024, 1024
        self.env.cr.execute(
            """SELECT * FROM ir_attachment WHERE file_size > 500000 AND res_model NOT IN ('ir.ui.view', 'res.country');""")
        attachment = self.env.cr.dictfetchall()

        def convert(self, image):
            if image.size[0] > 1024 or image.size[1] > 1024:
                image.thumbnail(size)
                image.save("{}/{}".format(pathfolder, attach['store_fname']), "JPEG")
                file_size = os.path.getsize("{}/{}".format(pathfolder, attach['store_fname']))
                self.env.cr.execute("""UPDATE ir_attachment SET file_size = {} WHERE id = {};""".format(file_size, attach['id']))

        for attach in attachment:
            images = "{}/{}".format(pathfolder, attach['store_fname'])
            try:
                image = Image.open(images)
                try:
                    convert(self, image)
                finally:
                    image.close()
            except (IOError, OSError) as e:
                print("Sorry, but {}".format(e))