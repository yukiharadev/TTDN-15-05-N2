from odoo import fields, models, api
from odoo.exceptions import ValidationError
from datetime import date

class HoatDong(models.Model):
    _name = 'hoat_dong'
    _description = 'Hoạt động'

    loai_hoat_dong = fields.Char(string='Loại hoạt động', required=True)
    chu_de = fields.Char(string='Chủ đề', required=True)
    ngay_thuc_hien = fields.Date(string='Ngày thực hiện', required=True)
    trang_thai = fields.Selection([
        ('moi', 'Mới'),
        ('dang_thuc_hien', 'Đang thực hiện'),
        ('hoan_thanh', 'Hoàn thành'),
        ('huy', 'Hủy'),
    ], string='Trạng thái', default='moi')

    khach_hang_tiem_nang_id = fields.Many2one('khach_hang_tiem_nang', string='Khách hàng tiềm năng')
    phan_cong_cong_viec_ids = fields.One2many('phan_cong_cong_viec', 'hoat_dong_id', string='Phân công công việc')

    @api.constrains('loai_hoat_dong', 'chu_de')
    def _check_text_fields(self):
        """Kiểm tra loại hoạt động và chủ đề có hợp lệ không."""
        for record in self:
            if len(record.loai_hoat_dong.strip()) < 3:
                raise ValidationError("Loại hoạt động phải có ít nhất 3 ký tự.")
            if len(record.chu_de.strip()) < 3:
                raise ValidationError("Chủ đề phải có ít nhất 3 ký tự.")

    @api.constrains('ngay_thuc_hien')
    def _check_ngay_thuc_hien(self):
        """Kiểm tra ngày thực hiện không được lớn hơn ngày hiện tại."""
        for record in self:
            if record.ngay_thuc_hien and record.ngay_thuc_hien > date.today():
                raise ValidationError("Ngày thực hiện không hợp lệ! Không thể lớn hơn ngày hiện tại.")

    @api.constrains('trang_thai')
    def _check_trang_thai(self):
        """Kiểm tra trạng thái hoạt động hợp lệ."""
        valid_status = ['moi', 'dang_thuc_hien', 'hoan_thanh', 'huy']
        for record in self:
            if record.trang_thai not in valid_status:
                raise ValidationError("Trạng thái hoạt động không hợp lệ!")
