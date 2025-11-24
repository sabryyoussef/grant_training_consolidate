# -*- coding: utf-8 -*-
{
    'name': 'Contact Pool Manager',
    'version': '19.0.1.0.0',
    'category': 'Sales/CRM',
    'summary': 'Manage contact pools for distribution and tracking',
    'description': """
        Contact Pool Manager
        ====================
        
        Organize contacts into pools for efficient distribution,
        tracking, and management. Features include:
        
        - Pool creation and management
        - Contact assignment and tracking
        - Sales person distribution
        - Activity tracking
        - Lead conversion metrics (with CRM)
        - Batch operations
        - Distribution wizards (manual & round-robin)
    """,
    'author': 'Edafa',
    'website': 'https://www.edafa.sa',
    'license': 'OEEL-1',
    'depends': ['base', 'mail', 'contacts', 'sales_team'],
    'external_dependencies': {},
    'data': [
        # Security
        'security/ir.model.access.csv',
        'security/ir.rule.xml',
        
        # Data
        'data/sequences.xml',
        'data/contact_pool_data.xml',
        
        # Views
        'views/contact_pool_views.xml',
        'views/res_partner_views.xml',
        'views/menu_views.xml',
        # Optional: CRM views (will fail gracefully if CRM not installed)
        # 'views/crm_lead_views.xml',
    ],
    'demo': ['data/contact_pool_demo.xml'],
    'installable': True,
    'application': True,
}
