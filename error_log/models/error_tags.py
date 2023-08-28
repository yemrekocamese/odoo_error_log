from odoo import api, fields, models


class Error_tags(models.Model):
    _name = "error_tags.error"
    _description = "Error tags"
    _order = "name"

    name = fields.Char(string="Error Tags")
    tags = fields.Char(string="Error Tags")
    color = fields.Integer(string='Color')
