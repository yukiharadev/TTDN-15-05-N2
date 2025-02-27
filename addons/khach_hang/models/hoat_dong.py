
from odoo import fields, models, api

class HoatDong(models.Model):
    _name = 'hoat_dong'
    _description = 'Hoạt động'

    loai_hoat_dong = fields.Char(string='Loại hoạt động')
    chu_de = fields.Char(string='Chủ đề')
    ngay_thuc_hien = fields.Date(string='Ngày thực hiện')
    trang_thai = fields.Selection([
        ('moi', 'Mới'),
        ('dang_thuc_hien', 'Đang thực hiện'),
        ('hoan_thanh', 'Hoàn thành'),
        ('huy', 'Hủy'),
    ], string='Trạng thái', default='moi')

    khach_hang_tiem_nang_id = fields.Many2one('khach_hang_tiem_nang', string='Khách hàng tiềm năng')
    phan_cong_cong_viec_ids = fields.One2many('phan_cong_cong_viec', 'hoat_dong_id', string='Phân công công việc')
