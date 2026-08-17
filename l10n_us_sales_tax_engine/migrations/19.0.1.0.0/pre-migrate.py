# Copyright 2026 Binhex - Carlos R. Rodriguez.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
"""Prepare Odoo 18 security groups for the Odoo 19 privilege model."""


UPDATEABLE_SECURITY_XMLIDS = (
    "module_category_us_sales_tax",
    "group_us_tax_user",
    "group_us_tax_manager",
    "group_us_tax_technical",
)


def migrate(cr, version):
    """Allow the data loader to assign the new privilege to existing groups."""
    if not version:
        return

    cr.execute(
        """
        UPDATE ir_model_data
           SET noupdate = FALSE
         WHERE module = 'l10n_us_sales_tax_engine'
           AND name IN %s
        """,
        (UPDATEABLE_SECURITY_XMLIDS,),
    )
