from openerp import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    in_box_qty = fields.Float(
        string="m/m2",
        digits='Product Unit of Measure',
    )
    prod_in_box = fields.Float(
        string="m2 x caja",
        related="product_id.product_tmpl_id.prod_in_box",
        readonly=True
    )
    prod_in_box_uom = fields.Selection(
        related="product_id.product_tmpl_id.prod_in_box_uom",
        help="Campo tecnico para mostrar u ocultar metros por caja en la linea de "
             "presupuesto"
    )

    @api.onchange('quantity')
    def onchange_quantity(self):
        for rec in self:
            if rec.prod_in_box_uom != 'na':
                rec.in_box_qty = rec.quantity * rec.prod_in_box
            else:
                rec.in_box_qty = 0

    @api.onchange('in_box_qty')
    def onchange_in_box_qty(self):
        for rec in self:
            if rec.prod_in_box_uom != 'na':
                qty = rec.in_box_qty / rec.prod_in_box if rec.prod_in_box else 0
                frac = qty - int(qty)
                if frac != 0:
                    qty += 1
                rec.quantity = int(qty)
            else:
                rec.quantity = 1
