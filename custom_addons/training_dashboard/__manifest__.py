# -*- coding: utf-8 -*-
{
    'name': 'Training Dashboard',
    'version': '19.0.1.0.0',
    'category': 'Education',
    'summary': 'Advanced analytics and KPIs dashboard for training programs',
    'description': """
        Training Dashboard
        ==================
        
        A comprehensive analytics dashboard that provides:
        
        - KPI Metrics (students, enrollments, completion rates)
        - Progress Analytics (distribution, trends, monthly data)
        - Student Analytics (top performers, struggling students, engagement)
        - Course Analytics (performance, popularity)
        - Integration Analytics (eLearning adoption, status summary)
        - Auto-refresh capabilities
        - Export and scheduling features
        
        Can work standalone or integrate with grants_training_suite_v19.
    """,
    'author': 'Edafa',
    'website': 'https://www.edafa.sa',
    'license': 'OEEL-1',
    'depends': [
        'base',
    ],
    'external_dependencies': {},
    'data': [
        # Security
        'security/ir.model.access.csv',
        
        # Data
        'data/cron_jobs.xml',
        
        # Views
        'views/training_dashboard_views.xml',
        'views/menu_views.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}

