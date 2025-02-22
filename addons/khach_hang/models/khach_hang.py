from odoo import fields, models

class KhachHang(models.Model):
    _name = 'khach_hang'
    _description = 'Khach Hang'

    first_name = fields.Char(string='FirstName', required=True)
    last_name = fields.Char(string='LastName', required=True)
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Phone', required=True)
    address = fields.Char(string='Address', required=True)
    birthday = fields.Date(string='Birthday', required=True)
