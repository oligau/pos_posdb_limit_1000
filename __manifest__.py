# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'pos_posdb_limit_1000',
    'version': '1.0',
    'category': 'Sales/Point of Sale',
    'sequence': 6,
    'summary': 'Override PosDB.limit value to 1000',
    'description': """

PosDB.limit value is hard coded to 100 in point_of_sale module. This module
override this limit to 1000 to allow display more than 100 products in POS
product view.
""",
    'depends': ['point_of_sale'],
    'installable': True,
    'assets': {
        'point_of_sale.assets': [
            'pos_posdb_limit_1000/static/src/js/**/*',
        ],
    },
    'license': 'LGPL-3',
}
