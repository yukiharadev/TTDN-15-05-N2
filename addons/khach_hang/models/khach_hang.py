from odoo import fields, models, api
from odoo.exceptions import ValidationError
import re

class KhachHang(models.Model):
    _name = 'khach_hang'
    _description = 'Khách hàng'

    ma_khach_hang = fields.Char("Mã khách hàng", required=True)
    ho_ten_dem = fields.Char("Họ tên đệm", required=True)
    ten = fields.Char("Tên", required=True)
    ho_va_ten = fields.Char("Họ và tên", compute="_compute_ho_va_ten", store=True)
    email = fields.Char("Email")
    so_dien_thoai = fields.Char("Số điện thoại")
    dia_chi = fields.Char("Địa chỉ")
    ngay_tao = fields.Date("Ngày tạo", default=fields.Date.context_today, readonly=True)

    @api.depends("ho_ten_dem", "ten")
    def _compute_ho_va_ten(self):
        for item in self:
            if item.ho_ten_dem and item.ten:
                item.ho_va_ten = item.ho_ten_dem + ' ' + item.ten

    @api.constrains('so_dien_thoai')
    def _check_so_dien_thoai(self):
        phone_regex = r'^\d{10}$'
        for item in self:
            if item.so_dien_thoai and not re.match(phone_regex, item.so_dien_thoai):
                raise ValidationError("Số điện thoại không hợp lệ!")
            
    @api.constrains('email')
    def _check_email(self):
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        for item in self:
            if item.email and not re.match(email_regex, item.email):
                raise ValidationError("Email không hợp lệ!")
