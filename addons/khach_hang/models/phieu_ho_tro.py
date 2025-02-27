from odoo import models, fields, api


class PhieuHoTro(models.Model):
    _name = "phieu_ho_tro"
    _description = "Phiếu hỗ trợ"

    tieu_de = fields.Char(string="Tiêu đề", required=True)
    description = fields.Text(string="Description")
    trang_thai = fields.Selection(
        [("moi", "Mới"), ("dang_xu_ly", "Đang xử lý"), ("da_xu_ly", "Đã xử lý")],
        default="moi",
    )
    muc_do = fields.Selection(
        [("thap", "Thấp"), ("trung_binh", "Trung bình"), ("cao", "Cao")],
        default="thap",
    )

    ngay_tao = fields.Date(string="Ngày tạo", default=fields.Date.today)
    ngay_xu_ly = fields.Date(string="Ngày xử lý")
    khach_hang_id = fields.Many2one("khach_hang", string="Khách hàng")
