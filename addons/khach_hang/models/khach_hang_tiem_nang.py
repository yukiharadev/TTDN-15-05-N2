
from odoo import _, api, fields, models

class KhachHangTiemNang(models.Model):
    _name = 'khach_hang_tiem_nang'
    _description = 'Khách hàng tiềm năng'

    giai_doan = fields.Selection([
        ('1', 'Giai đoạn 1'),
        ('2', 'Giai đoạn 2'),
        ('3', 'Giai đoạn 3'),
        ('4', 'Giai đoạn 4'),
        ('5', 'Giai đoạn 5'),
    ], string='Giai đoạn', required=True)
    doanh_thu_tiem_nang = fields.Float(string='Doanh thu tiềm năng')
    ngay_du_kien_ky_hop_dong = fields.Date(string='Ngày dự kiến ký hợp đồng')
    ngay_tao = fields.Date(string='Ngày tạo', default=fields.Date.today())
    ngay_cap_nhat = fields.Date(string='Ngày cập nhật', default=fields.Date.today())
    hoat_dong_ids = fields.One2many('hoat_dong', 'khach_hang_tiem_nang_id', string='Hoạt động')
    hop_dong_ids = fields.One2many('hop_dong','khach_hang_tiem_nang_id', string='Hợp đồng')

    # Mối quan hệ với khách hàng
    khach_hang_id = fields.Many2one('khach_hang', string='Khách hàng')