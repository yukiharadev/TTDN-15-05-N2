from datetime import date
from odoo import fields, models

class PhanHoiKhachHang(models.Model):
    _name = 'phan_hoi_khach_hang'
    _description = 'Phản hồi khách hàng'

    ma_phan_hoi = fields.Char(string="Mã phản hồi", required=True)
    loai_phan_hoi = fields.Selection([
        ('Tích cực', 'Tích cực'),
        ('Tiêu cực', 'Tiêu cực'),
        ('Đánh giá', 'Đánh giá')
    ], string="Loại phản hồi", required=True)
    noi_dung = fields.Char(string="Nội dung", required=True)
    ngay_danh_gia = fields.Date(string='Ngày tạo', default=fields.Date.today())

    khach_hang_id = fields.Many2one("khach_hang", string="Khách hàng", required=True)
    khach_hang_phan_hoi = fields.Char(related='khach_hang_id.full_name', string='Khách hàng phản hồi', store=True)

