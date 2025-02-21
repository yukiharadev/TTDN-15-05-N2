from odoo import models, fields

class ChucVu(models.Model):
    _name = 'chuc_vu'
    _description = 'Bảng chứa thông tin chức vụ'

    ma_dinh_danh = fields.Char("Mã định danh", required=True)
    ten_chuc_vu = fields.Char("Tên chức vụ")
    mo_ta = fields.Text("Mô tả")
    luong_co_ban = fields.Float("Lương cơ bản")
    phu_cap = fields.Float("Phụ cấp")
    phong_ban_id = fields.Many2one("phong_ban", string="Phòng ban")
    phong_ban_ten = fields.Char(string="Tên phòng ban", related="phong_ban_id.ten_phong_ban", store=True)
