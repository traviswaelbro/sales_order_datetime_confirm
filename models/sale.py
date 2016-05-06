from openerp.osv import osv, fields
from datetime import datetime

class sale_order(osv.osv):
    _inherit = 'sale.order'

    def action_wait(self, cr, uid, ids, context=None):
        context = context or {}
        for o in self.browse(cr, uid, ids):
            if not any(line.state != 'cancel' for line in o.order_line):
                raise osv.except_osv(_('Error!'),_('You cannot confirm a sales order which has no line.'))
            noprod = self.test_no_product(cr, uid, o, context)
            if (o.order_policy == 'manual') or noprod:
                self.write(cr, uid, [o.id], {'state': 'manual', 'date_confirm': datetime.now()})
            else:
                self.write(cr, uid, [o.id], {'state': 'progress', 'date_confirm': datetime.now()})
            self.pool.get('sale.order.line').button_confirm(cr, uid, [x.id for x in o.order_line if x.state != 'cancel'])
        return True

    _columns = {
            'date_confirm': fields.datetime('Confirmation Date', readonly=True, select=True, help="Date on which sales order is confirmed.", copy=False),
        }

class sale_report(osv.osv):
    _inherit = "sale.report"

    _columns = {
            'date_confirm': fields.datetime('Date Confirm', readonly=True),
        }