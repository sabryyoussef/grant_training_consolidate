# -*- coding: utf-8 -*-
{
    'name': 'Grants Training Suite V1',
    'version': '18.0.1.0.0',
    'category': 'Education',
    'summary': 'Basic training center management system',
    'description': """
        Grants Training Suite V1
        =======================
        
        The original, stable version of the training center management system that provides:
        - Basic student management
        - Simple enrollment workflows
        - Basic progress tracking
        - Core functionality for training centers
        
        This is the stable, production-ready version.
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'license': 'OEEL-1',
    'depends': [
        'base',
        'mail',
        'portal',
        'contacts',
        'sale',
        'crm',
        'website',
        'survey',
        'website_slides',
        'documents',
        'certificate',
    ],
    'data': [
        # Security
        'security/grants_training_groups.xml',
        'security/ir.model.access.csv',
        
        # Data
        'data/sequence.xml',
        'data/cron_jobs.xml',
        'data/phase3_cron_jobs.xml',
        'data/email_templates.xml',
        
        # Views
        'views/intake_batch_views.xml',
        'views/intake_batch_mapping_wizard_views.xml',
        'views/intake_batch_correction_wizard_views.xml',
        'views/session_template_views.xml',
        'views/enrollment_wizard_views.xml',
        'views/homework_grade_history_views.xml',
        'views/homework_attempt_enhanced_views.xml',
        'views/student_views.xml',
        'views/assignment_views.xml',
        'views/document_request_views.xml',
        'views/course_session_views.xml',
        'views/homework_attempt_views.xml',
        'views/certificate_views.xml',
        'views/certificate_template_views.xml',
        'views/certificate_automation_wizard_views.xml',
        'views/course_integration_views.xml',
        'views/training_program_views.xml',
        'views/progress_tracker_views.xml',
        'views/integration_reports.xml',
        'views/training_dashboard_views.xml',
        'views/notification_system_views.xml',
        'views/certificate_automation_views.xml',
        'views/menu_views.xml',
    ],
    'demo': [
        'demo/simple_demo_data.xml',
        'demo/intake_batch_demo.xml',
        'demo/student_demo.xml',
        'demo/assignment_demo.xml',
        'demo/document_request_demo.xml',
        'demo/course_session_demo.xml',
        'demo/homework_attempt_demo.xml',
        'demo/certificate_demo.xml',
        'demo/elearning_courses_demo.xml',
        'demo/training_programs_demo.xml',
        'demo/course_integrations_demo.xml',
        'demo/certificate_templates_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}