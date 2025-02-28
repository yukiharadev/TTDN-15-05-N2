# -*- coding: utf-8 -*-
{
    'name': "khach_hang",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','nhan_su'],

    'data': [
        'security/ir.model.access.csv',
        'views/khach_hang.xml',
        'views/ho_tro_khach_hang.xml',
        'views/khach_hang_tiem_nang.xml',
        'views/hoat_dong.xml',
        'views/hop_dong.xml',
        'views/phan_cong_cong_viec.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
