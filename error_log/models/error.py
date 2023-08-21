from odoo import api, fields, models


class Error(models.Model):
    _name = "error"
    _description = "Error Logs"
    _order = "name"

    stacktrace = fields.Text(required=True)
    assigned = fields.Many2one("res.users", required=True, )
    is_ok = fields.Boolean()
    summary = fields.Char()
    active = fields.Boolean(default=True)
    comment = fields.Text()
    error_type = fields.Selection(
        selection=[
            ("xml", "Xml"),
            ("python", "Python"),
            ("javascript", "Javascript"),
            ("atama", "Atama"),
        ],
        required=True,
    )
