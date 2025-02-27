from datetime import date

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class KhachHang(models.Model):
    _name = 'khach_hang'
    _description = 'Khach Hang'

    first_name = fields.Char(string='Tên', required=True)
    last_name = fields.Char(string='Họ và tên đệm', required=True)
    full_name = fields.Char(string='Họ và tên', compute='_compute_full_name', store=True)
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Số điện thoại', required=True)
    address = fields.Char(string='Địa chỉ', required=True)
    birthday = fields.Date(string='Ngày sinh', required=True)
    loai_khach_hang = fields.Selection([
        ('doanh_nghiep', 'Doanh nghiệp'),
        ('ca_nhan', 'Cá nhân')
    ], default='ca_nhan')
    phieu_ho_tro_ids = fields.One2many('phieu_ho_tro', 'khach_hang_id', string='Phiếu hỗ trợ')
    giao_dich_ids = fields.One2many('giao_dich', 'khach_hang_id', string='Giao dịch')

    @api.depends('first_name', 'last_name')
    def _compute_full_name(self):
        for hang in self:
            hang.full_name = f"{hang.last_name} {hang.first_name}"


    @api.constrains('birthday')
    def _check_birthday(self):
        """Kiểm tra ngày sinh không được lớn hơn ngày hiện tại."""
        for record in self:
            if record.birthday and record.birthday > date.today():
                raise ValidationError("Ngày sinh không hợp lệ! Ngày sinh không thể lớn hơn ngày hiện tại.")