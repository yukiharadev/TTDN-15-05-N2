from datetime import date
from odoo import fields, models

class BaoCaoMarketing(models.Model):
    _name = 'bao_cao_marketing'
    _description = 'Báo cáo Marketing'

    ma_bao_cao_mkt = fields.Char(string="Mã báo cáo marketing", required=True)
    muc_do_tuong_tac = fields.Selection([
        ('Tốt', 'Tốt'),
        ('Ít tương tác', 'Ít tương tác'),
        ('Không hứng thú', 'Không hứng thú')
    ], string='Mức độ tương tác', required=True)

    khach_hang_id = fields.Many2one("khach_hang", string="Khách hàng", required=True)
    khach_hang_tham_gia = fields.Char(related="khach_hang_id.full_name", string="Khách hàng tham gia", store=True)
    chien_dich_mkt_id = fields.Many2one("chien_dich_marketing", string="Chiến dịch Marketing", required=True)