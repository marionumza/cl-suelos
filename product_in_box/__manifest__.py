# -----------------------------------------------------------------------------------
#
#    Copyright (C) 2021  jeo Software  (http://www.jeo-soft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# -----------------------------------------------------------------------------------
{
    "name": "Product In Box",
    "version": "13.0.1.0.0",
    "category": "Tools",
    "summary": "Contabilida cantidad de producto en caja",
    "author": "jeo Software",
    "depends": [
        "product",
        "sale",
        "l10n_ar_ux",
    ],
    "data": [
        "views/product_template_view.xml",
        "views/sale_order_view.xml",
        "views/account_move_view.xml",
        "views/account_invoice_line_report_tree.xml",
    ],
    "test": [],
    "installable": True,
    "application": True,
    "auto_install": False,
    "images": [],
}
