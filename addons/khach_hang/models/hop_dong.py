
from odoo import _, api, fields, models

class HopDong(models.Model):
    _name = "hop_dong"
    _description = "Hợp đồng"

    ten = fields.Char(string="Tên hợp đồng", required=True)
    ngay_bat_dau = fields.Date(string="Ngày bắt đầu", required=True)
    ngay_ket_thuc = fields.Date(string="Ngày kết thúc", required=True)
    gia_tri_hop_dong = fields.Float(string="Giá trị hợp đồng", required=True)
    trang_thai = fields.Selection([
        ('moi', 'Mới'),
        ('hoan_thanh', 'Hoàn thành'),
        ('huy', 'Hủy')
    ], string="Trạng thái", default='moi')

    khach_hang_tiem_nang_id = fields.Many2one('khach_hang_tiem_nang', string="Khách hàng tiềm năng")