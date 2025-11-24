# -*- coding: utf-8 -*-
{
    'name': 'Notification Manager',
    'version': '19.0.1.0.0',
    'category': 'Tools',
    'summary': 'Flexible notification system for progress tracking and alerts',
    'description': """
        Notification Manager
        ===================
        
        A standalone, flexible notification system that provides:
        
        - Multi-channel notifications (Email, SMS, In-App)
        - Progress milestone tracking
        - Automated notification triggers
        - Custom notification types
        - Notification templates
        - Status tracking and archiving
        
        Can work standalone or integrate with other modules like grants_training_suite_v19.
    """,
    'author': 'Edafa',
    'website': 'https://www.edafa.sa',
    'license': 'OEEL-1',
    'depends': [
        'base',
        'mail',              # For mail.thread, mail.activity, mail.mail
        'openeducat_core',   # For op.student model
    ],
    'external_dependencies': {},
    'data': [
        # Security
        'security/ir.model.access.csv',
        
        # Data
        'data/email_templates.xml',
        'data/cron_jobs.xml',
        
        # Views
        'views/notification_views.xml',
        'views/menu_views.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}

