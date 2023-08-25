from odoo import api, fields, models


class Tags(models.Model):
    _name = "error.tags" # TODO: isim değişicek
    _description = "Error tags"
    _order = "name"

    name = fields.Char(string="Error Tags")
    tags = fields.Char(string="Error Tags")
    # TODO: color  eklenecek ömer