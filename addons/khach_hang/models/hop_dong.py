from odoo import fields, models, api

class KhachHang(models.Model):
    _name = 'hop_dong'
    _description = 'Hợp đồng'

    ma_hop_dong = fields.Char("Mã hợp đồng", required=True)
    ma_khach_hang_tiem_nang_ids = fields.One2many("khach_hang_tiem_nang", inverse_name="ma_khach_hang_tiem_nang", string="Khách hàng kí hợp đồng")
    ten_hop_dong = fields.Char("Tên hợp đồng", required=True)
    ngay_bat_dau = fields.Date("Ngày bắt đầu", default=fields.Date.context_today, required=True)
    ngay_ket_thuc = fields.Date("Ngày kết thúc", default=lambda self: fields.Date.add(fields.Date.context_today(self), months=6), required=True)
    gia_tri_hop_dong = fields.Monetary("Giá trị hợp đồng", currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string="Currency")
    trang_thai = fields.Selection(
        [
            ("Đang hiệu lực", "Đang hiệu lực"),
            ("Hết hạn", "Hết hạn")
        ],
        string="Trạng thái", default="Đang hiệu lực", readonly=True
    )
