from odoo import _, api, fields, models

class LichSuCongTac(models.Model):
    _name = 'lich_su_cong_tac'
    _description = 'Lịch sử công tác'

    nhan_vien_id = fields.Many2one('nhan_vien', string='Nhân viên', required=True)
    phong_ban_id = fields.Many2one('phong_ban', string='Phòng ban', required=True)
    chuc_vu_id = fields.Many2one('chuc_vu', string='Chức vụ', required=True)
    loai_cv = fields.Selection(
        [('Chính', 'Chính'), ('Kiêm nhiệm', 'Kiêm nhiệm')],
        string="Loại công tác", default='Chính'
    )