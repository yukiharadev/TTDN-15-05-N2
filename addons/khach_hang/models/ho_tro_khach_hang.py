from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class HoTroKhachHang(models.Model):
    _name = 'ho_tro_khach_hang'
    _description = 'Hỗ trợ khách hàng'

    chu_de = fields.Char('Chủ đề', required=True)
    noi_dung = fields.Text('Nội dung', required=True)
    muc_do = fields.Selection([
        ('thap', 'Thấp'),
        ('trung_binh', 'Trung bình'),
        ('cao', 'Cao')
    ], string="Mức độ", default='thap', required=True)

    trang_thai = fields.Selection([
        ('moi', 'Mới'),
        ('dang_xu_ly', 'Đang xử lý'),
        ('da_xu_ly', 'Đã xử lý')
    ], string="Trạng thái", default='moi', required=True)

    ngay_tao = fields.Datetime('Ngày tạo', default=fields.Datetime.now)
    ngay_giai_quyet = fields.Datetime('Ngày giải quyết')
    nguoi_tao = fields.Many2one('khach_hang', 'Người tạo', inverse_name='ho_tro_ids')
    ten_nguoi_tao = fields.Char(related='nguoi_tao.full_name', string='KH tạo', store=True)

    phan_cong_cong_viec_ids = fields.One2many('phan_cong_cong_viec', 'ho_tro_khach_hang_id',
                                              string='Phân công công việc')

    @api.constrains('chu_de')
    def _check_chu_de(self):
        """Kiểm tra chủ đề phải có ít nhất 3 ký tự."""
        for record in self:
            if len(record.chu_de.strip()) < 3:
                raise ValidationError(_("Chủ đề phải có ít nhất 3 ký tự."))

    @api.constrains('noi_dung')
    def _check_noi_dung(self):
        """Kiểm tra nội dung không được để trống."""
        for record in self:
            if not record.noi_dung.strip():
                raise ValidationError(_("Nội dung không được để trống."))

    @api.constrains('ngay_tao', 'ngay_giai_quyet')
    def _check_ngay_giai_quyet(self):
        """Kiểm tra ngày giải quyết không được nhỏ hơn ngày tạo."""
        for record in self:
            if record.ngay_giai_quyet and record.ngay_giai_quyet < record.ngay_tao:
                raise ValidationError(_("Ngày giải quyết không được nhỏ hơn ngày tạo."))

    @api.constrains('trang_thai')
    def _check_trang_thai(self):
        """Kiểm tra trạng thái hỗ trợ hợp lệ."""
        valid_status = ['moi', 'dang_xu_ly', 'da_xu_ly']
        for record in self:
            if record.trang_thai not in valid_status:
                raise ValidationError(_("Trạng thái hỗ trợ khách hàng không hợp lệ!"))
