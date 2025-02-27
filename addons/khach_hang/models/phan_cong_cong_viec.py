
from odoo import _, api, fields, models

class PhanCongCongViec(models.Model):
    _name = 'phan_cong_cong_viec'
    _description = 'Phân công công việc'

    nhan_vien_id = fields.Many2one('nhan_vien', string='Mã nhân viên')
    hoat_dong_id = fields.Many2one('hoat_dong', string='Hoạt động')
    ho_tro_khach_hang_id = fields.Many2one('ho_tro_khach_hang', string='Hỗ trợ khách hàng')
    ngay_phan_cong = fields.Date(string='Ngày phân công')
    trang_thai = fields.Selection([
        ('moi', 'Mới'),
        ('dang_thuc_hien', 'Đang thực hiện'),
        ('hoan_thanh', 'Hoàn thành'),
        ('huy', 'Hủy')
    ], string='Trạng thái', default='moi')