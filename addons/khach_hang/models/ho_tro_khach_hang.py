from odoo import _, api, fields, models

class HoTroKhachHang(models.Model):
    _name = 'ho_tro_khach_hang'
    _description = 'Hỗ trợ khách hàng'

    chu_de=fields.Char('Chủ đề', required=True)
    noi_dung=fields.Text('Nội dung', required=True)
    muc_do = fields.Selection([
        ('thap', 'Thấp'),
        ('trung_binh', 'Trung bình'),
        ('cao', 'Cao')
    ], default='thap', required=True)
    trang_thai = fields.Selection([
        ('moi', 'Mới'),
        ('dang_xu_ly', 'Đang xử lý'),
        ('da_xu_ly', 'Đã xử lý')
    ], default='moi', required=True)
    ngay_tao = fields.Datetime('Ngày tạo', default=fields.Datetime.now)
    ngay_giai_quyet = fields.Datetime('Ngày giải quyết')
    nguoi_tao = fields.Many2one('khach_hang', 'Người tạo', inverse_name='ho_tro_ids')

    phan_cong_cong_viec_ids = fields.One2many('phan_cong_cong_viec', 'ho_tro_khach_hang_id', string='Phân công công việc')

