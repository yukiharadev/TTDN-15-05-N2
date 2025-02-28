import re
from datetime import date
from odoo import fields, models, api
from odoo.exceptions import ValidationError


class KhachHang(models.Model):
    _name = 'khach_hang'
    _description = 'Khách Hàng'

    first_name = fields.Char(string='Tên', required=True)
    last_name = fields.Char(string='Họ và tên đệm', required=True)
    full_name = fields.Char(string='Họ và tên', compute='_compute_full_name', store=True)
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Số điện thoại', required=True)
    address = fields.Char(string='Địa chỉ', required=True)
    birthday = fields.Date(string='Ngày sinh', required=True)


    ho_tro_ids = fields.One2many('ho_tro_khach_hang', 'nguoi_tao', string='Hỗ trợ khách hàng')
    khach_hang_tiem_nang_ids = fields.One2many('khach_hang_tiem_nang', 'khach_hang_id', string='Khách hàng tiềm năng')

    @api.depends('first_name', 'last_name')
    def _compute_full_name(self):
        for record in self:
            if(record.first_name and record.last_name):
                record.full_name = f"{record.last_name.strip()} {record.first_name.strip()}"

    @api.constrains('birthday')
    def _check_birthday(self):
        """Ngày sinh không thể lớn hơn ngày hiện tại."""
        for record in self:
            if record.birthday and record.birthday > date.today():
                raise ValidationError("Ngày sinh không hợp lệ! Không thể lớn hơn ngày hiện tại.")

    @api.constrains('email')
    def _check_email(self):
        """Kiểm tra email có hợp lệ không."""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        for record in self:
            if not re.match(email_regex, record.email.strip()):
                raise ValidationError("Địa chỉ email không hợp lệ!")

    @api.constrains('phone')
    def _check_phone(self):
        """Kiểm tra số điện thoại luôn có đúng 10 số."""
        phone_regex = r'^\d{10}$'
        for record in self:
            if not re.match(phone_regex, record.phone.strip()):
                raise ValidationError("Số điện thoại không hợp lệ! Phải có đúng 10 chữ số.")

    @api.constrains('first_name', 'last_name')
    def _check_name(self):
        """Kiểm tra tên không chứa ký tự đặc biệt và không quá ngắn."""
        name_regex = r'^[\p{L}\s]+$'  # Chỉ chấp nhận chữ cái & khoảng trắng (Unicode)
        for record in self:
            first_name_clean = record.first_name.strip()
            last_name_clean = record.last_name.strip()

            if len(first_name_clean) < 2 or len(last_name_clean) < 2:
                raise ValidationError("Tên và họ không hợp lệ! Phải có ít nhất 2 ký tự.")

            if not re.match(name_regex, first_name_clean) or not re.match(name_regex, last_name_clean):
                raise ValidationError("Tên không được chứa ký tự đặc biệt hoặc số!")

