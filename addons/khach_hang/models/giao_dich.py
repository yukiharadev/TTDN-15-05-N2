from odoo import models, fields


class GiaoDich(models.Model):
    _name = 'giao_dich'
    _description = 'Giao dịch'

    amount = fields.Float( string='Số tiền', required=True)
    payment_method = fields.Selection(
        [('cash', 'Tiền mặt'), ('bank', 'Chuyển khoản'),('credit_card', 'Thẻ tín dụng')],
    )
    khach_hang_id = fields.Many2one('khach_hang', string='Khách hàng')

