from odoo import api, fields, models


class Error(models.Model):
    _name = "error_log.error" # TODO: isim değişicek selim
    _description = "Error Logs"
    _order = "name" # TODO: sıralama düzeltilecek. yunus

    stacktrace = fields.Text(required=True)
    # TODO: state eklenecek. yunus
    name = fields.Char()
    assigned = fields.Many2one("res.partner", required=True, domain="[('category_id.name', 'in',['developer'])]")
    is_ok = fields.Boolean()
    summary = fields.Char(string="aciklama") # TODO: aciklama a--A. ömer
    active = fields.Boolean(default=True)
    comment = fields.Text()
    tags = fields.Many2many("error.tags", required=True)
    error_type = fields.Selection(
        selection=[
            ("xml", "Xml"),
            ("python", "Python"),
            ("javascript", "Javascript"),
            ("atama", "Atama"),
        ],
        required=True,
    )
    # TODO: chatter eklenecek. yunus eklem
    # TODO: required değişecek. ömer
