from datetime import date
from odoo import fields, models

class TopicHoTro(models.Model):
    _name = 'topic_ho_tro'
    _description = 'Topic hỗ trợ'

    ho_tro_khach_hang_id = fields.Many2one('ho_tro_khach_hang', string='Phiếu hỗ trợ')
    nhan_vien_id = fields.Many2one('nhan_vien', string='Mã nhân viên')
    nhan_vien_tra_loi = fields.Char(string='Nhân viên')
    khach_hang_tra_loi = fields.Char(string='Khách hàng')

