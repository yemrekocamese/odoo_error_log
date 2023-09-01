from odoo import api, fields, models


class Error(models.Model):
    _name = "error_log.error"
    _description = "Error Logs"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "name"

    name = fields.Char(string="Summary", compute='_compute_name')
    stacktrace = fields.Text(required=True)
    assigned = fields.Many2one("res.partner", domain="[('category_id.name', 'in',['developer'])]")
    is_ok = fields.Boolean()

    active = fields.Boolean(default=True)
    comment = fields.Text()
    tags = fields.Many2many("error_tags.error")
    error_type = fields.Selection(string="Error Türü",
        selection=[
            ("xml", "Xml"),
            ("python", "Python"),
            ("javascript", "Javascript"),
        ],
    )
    atama = fields.Selection(string="Atama Durumu",
        selection=[
            ("atandı", "Atandı"),
            ("atanmadı", "Atanmadı"),
        ],
    )

    @api.depends('stacktrace')
    def _compute_name(self):
        for rec in self:
            # rec.name = rec.stacktrace and rec.stacktrace[:50] or 'Yeni'
            if rec.stacktrace:
                rec.name = rec.stacktrace[:50]
            else:
                rec.name = 'Yeni'
