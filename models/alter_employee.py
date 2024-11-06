from odoo import models, fields, api



class AlterEmployee(models.Model):
    _inherit = "hr.employee"

    hiring_date = fields.Date(string="Hiring Date", default=fields.Date.today)
    last_working_date = fields.Date(string="Last Working Date")
    company_name = fields.Char(string="Company Name")
    employee_signature = fields.Image(string="Upload Signature")
    date = fields.Date(default=lambda self: fields.Date.today())
    bank_name = fields.Char(string="Bank Name")
    company_id = fields.Many2one('res.company', store=True, copy=False,
                                 string="Company",
                                 default=lambda self: self.env.user.company_id.id)
    currency_id = fields.Many2one('res.currency', string="Currency",
                                  related='company_id.currency_id',
                                  default=lambda
                                      self: self.env.user.company_id.currency_id.id)
    basic_salary = fields.Monetary(string="Basic Salary", currency_field='currency_id')
    accommodation_allowance =fields.Monetary(string="Accommodation Allowance", currency_field='currency_id')
    transportation_allowance = fields.Monetary(string="Transportation Allowance", currency_field='currency_id')
    other_allowance = fields.Monetary(string="Other Allowance", currency_field='currency_id')
    total_salary = fields.Monetary(string="Total Salary", currency_field='currency_id', compute="_compute_total_salary")

    @api.depends('basic_salary', 'accommodation_allowance', 'transportation_allowance', 'other_allowance')
    def _compute_total_salary(self):
        for record in self:
            record.total_salary = (
                    record.basic_salary +
                    record.accommodation_allowance +
                    record.transportation_allowance +
                    record.other_allowance
            )
