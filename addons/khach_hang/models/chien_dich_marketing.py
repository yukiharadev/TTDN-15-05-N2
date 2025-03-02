from datetime import date
from odoo import fields, models, api
from odoo.exceptions import ValidationError

class ChienDichMarketing(models.Model):
    _name = 'chien_dich_marketing'
    _description = 'Chiến dịch Marketing'

    ma_chien_dich = fields.Char(string="Mã chiến dịch", required=True)
    ten_chien_dich = fields.Char(string="Tên chiến dịch", required=True)
    mo_ta = fields.Char(string="Mô tả", required=True)
    ngay_bat_dau = fields.Date(string="Ngày bắt đầu", required=True)
    ngay_ket_thuc = fields.Date(string="Ngày kết thúc", required=True)
    ngan_sach = fields.Float(string="Ngân sách", required=True)
    giai_doan_trien_khai = fields.Selection([
        ('Ý tưởng', 'Ý tưởng'),
        ('Đang triển khai', 'Đang triển khai'),
        ('Kết thúc', 'Kết thúc')
    ], string='Trạng thái', default='Ý tưởng')

    bao_cao_mkt_ids = fields.One2many('bao_cao_marketing', inverse_name='chien_dich_mkt_id', string='Báo cáo Marketing')

    @api.constrains('ngay_bat_dau', 'ngay_ket_thuc')
    def _check_ngay_hop_dong(self):
        """Kiểm tra ngày kết thúc phải sau hoặc bằng ngày bắt đầu."""
        for record in self:
            if record.ngay_ket_thuc and record.ngay_bat_dau and record.ngay_ket_thuc <= record.ngay_bat_dau:
                raise ValidationError(_("Ngày kết thúc không thể trước ngày bắt đầu."))