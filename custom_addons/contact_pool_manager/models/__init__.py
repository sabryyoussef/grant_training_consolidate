# -*- coding: utf-8 -*-

from . import contact_pool
from . import res_partner
from . import contact_pool_distribution_wizard
from . import contact_pool_batch_assignment_wizard

# Optional CRM integration
try:
    from odoo.addons.crm.models import crm_lead
    from . import crm_lead as contact_pool_crm_lead
except ImportError:
    # CRM module not installed, skip lead extension
    pass

