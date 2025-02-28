from odoo import models, fields, api

class LichSuCongTac(models.Model):
    _name = 'lien_he'
    _description = 'Liên hệ'

    ma_lien_he = fields.Char("Mã liên hệ", required=True)
    ma_khach_hang = fields.Many2one("khach_hang", string="Khách hàng", required=True)
    email = fields.Char("Email", required=True)
    so_dien_thoai = fields.Char("Số điện thoại", required=True)
    chuc_vu = fields.Selection(
        [
            ("Lãnh đạo & quản lý cấp cao", "Lãnh đạo & quản lý cấp cao"),
            ("Quản lý & trưởng bộ phận", "Quản lý & trưởng bộ phận"),
            ("Nhân viên & người thực hiện", "Nhân viên & người thực hiện"),
            ("Chủ hộ kinh doanh", "Chủ hộ kinh doanh"),
            ("Khách hàng tư nhân", "Khách hàng tư nhân"),
        ],
        string="Chức vụ"
    )
