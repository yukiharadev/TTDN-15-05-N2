
from odoo import _, api, fields, models

class KhachHangTiemNang(models.Model):
    _name = 'khach_hang_tiem_nang'
    _description = 'Khách hàng tiềm năng'

    giai_doan = fields.Selection([
        ('1', 'Tiếp cận'),
        ('2', 'Đàm phán'),
        ('3', 'ký hợp đồng'),
        ('4', 'Thất bại'),
    ], string='Giai đoạn', required=True)
    doanh_thu_tiem_nang = fields.Float(string='Doanh thu tiềm năng')
    ngay_du_kien_ky_hop_dong = fields.Date(string='Ngày dự kiến ký hợp đồng')
    ngay_tao = fields.Date(string='Ngày tạo', default=fields.Date.today())
    ngay_cap_nhat = fields.Date(string='Ngày cập nhật', default=fields.Date.today())

    khach_hang_id = fields.Many2one('khach_hang', string='Khách hàng')