from odoo import api, fields, models


class Error(models.Model):
    _name = "error_log.error"
    _description = "Error Logs"
    _order = "name"

    stacktrace = fields.Text(required=True)
    name = fields.Char()
    assigned = fields.Many2one("res.partner", required=True, domain="[('category_id.name', 'in',['developer'])]")
    is_ok = fields.Boolean()
    summary = fields.Char(string="aciklama")
    active = fields.Boolean(default=True)
    comment = fields.Text()
    tags = fields.Many2many("error_tags.error", required=True)

    error_type = fields.Selection(
        selection=[
            ("xml", "Xml"),
            ("python", "Python"),
            ("javascript", "Javascript"),
            ("atama", "Atama"),
        ],
        required=True,
    )
