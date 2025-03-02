from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

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

    khach_hang_id = fields.Many2one('khach_hang', string="Khách hàng")
    ten_khach_hang = fields.Char(related='khach_hang_id.full_name', string='Khách hàng', store=True)

    @api.constrains('ngay_bat_dau', 'ngay_ket_thuc')
    def _check_ngay_hop_dong(self):
        """Kiểm tra ngày kết thúc phải sau hoặc bằng ngày bắt đầu."""
        for record in self:
            if record.ngay_ket_thuc and record.ngay_bat_dau and record.ngay_ket_thuc <= record.ngay_bat_dau:
                raise ValidationError(_("Ngày kết thúc không thể trước ngày bắt đầu."))

    @api.constrains('gia_tri_hop_dong')
    def _check_gia_tri_hop_dong(self):
        """Kiểm tra giá trị hợp đồng phải lớn hơn 0."""
        for record in self:
            if record.gia_tri_hop_dong <= 0:
                raise ValidationError(_("Giá trị hợp đồng phải lớn hơn 0."))

    @api.constrains('ten')
    def _check_ten_hop_dong(self):
        """Kiểm tra tên hợp đồng không được quá ngắn."""
        for record in self:
            if len(record.ten.strip()) < 3:
                raise ValidationError(_("Tên hợp đồng phải có ít nhất 3 ký tự."))

    @api.constrains('trang_thai')
    def _check_trang_thai(self):
        """Kiểm tra trạng thái hợp đồng hợp lệ."""
        valid_status = ['moi', 'hoan_thanh', 'huy']
        for record in self:
            if record.trang_thai not in valid_status:
                raise ValidationError(_("Trạng thái hợp đồng không hợp lệ!"))
