from odoo import models, fields



class AlterEmployee(models.Model):
    _inherit = "hr.employee"

    hiring_date = fields.Date(string="Hiring Date", default=fields.Date.today)
    company_name = fields.Char(string="Company Name")
    employee_signature = fields.Image(string="Upload Signature")
    date = fields.Date(default=fields.Date.today)
