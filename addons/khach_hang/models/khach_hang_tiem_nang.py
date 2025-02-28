from odoo import fields, models, api
from odoo.exceptions import ValidationError
import re

class KhachHang(models.Model):
    _name = 'khach_hang_tiem_nang'
    _description = 'Khách hàng tiềm năng'

    ma_khach_hang_tiem_nang = fields.Char("Mã khách hàng tiềm năng", required=True)
    ma_hop_dong = fields.Many2one("hop_dong", string="Hợp đồng")
    doanh_thu_tiem_nang = fields.Monetary("Doanh thu tiềm năng", currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string="Currency")
    giai_doan = fields.Selection(
        [
            ("Tiếp cận", "Tiếp cận"),
            ("Đàm phán", "Tiếp cận"),
            ("Chốt đơn", "Chốt đơn"),
            ("Thất bại", "Thất bại"),
        ],
        string="Giai đoạn", default="Tiếp cận"
    )
    ngay_du_kien_ky_hop_dong = fields.Date("Ngày dự kiến ký hợp đồng")
