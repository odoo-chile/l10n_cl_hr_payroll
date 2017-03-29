from odoo import models, fields, api


UPDATE_PARTNER_FIELDS = ['name', 'user_id', 'address_home_id']


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    firstname = fields.Char("Firstname")
    last_name = fields.Char("Last Name")
    middle_name = fields.Char("'Second Name", help='Second employee name')
    mothers_name = fields.Char("'Second Last Name", help='Second employee last name')





    @api.multi
    @api.onchange('firstname', 'last_name')
    def get_name(self):
        for employee in self:
            if employee.firstname and employee.last_name:
                employee.name = u" ".join((p for p in (self.last_name, self.firstname) if p))



    @api.model
    def _get_computed_name(self, last_name, firstname):
        """Compute the 'name' field according to splitted data.
        You can override this method to change the order of lastname and
        firstname the computed name"""
        return u" ".join((p for p in (last_name, firstname) if p))


