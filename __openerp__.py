# -*- coding: utf-8 -*-
{
    'name': 'Sales Order Confirmation Datetime',
    'summary': 'Convert "Confirmation Date" to datetime field',
    'description': """

        Initially, the old confirmation dates will be set in local time (UTC -4 for us), so the dates had to be manually adjusted +4 hours to prevent orders from appearing like they had been ordered a day before they actually were.

        UPDATE sale_order
        SET date_confirm = date_confirm + interval '4h';

        It is also worth considering setting old orders to have a confirmation date if they don't already have one set.

        UPDATE sale_order
        SET date_confirm = date_order
        WHERE state NOT IN ('draft','cancel')
        AND date_confirm IS NULL;
    """,
    'category': 'Sales Management',
    'version': '1.0',
    'website': 'https://github.com/travs-w',
    'author': 'Travis Waelbroeck',
    'depends': ['base','sale'],
    'data': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
