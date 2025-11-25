# -*- coding: utf-8 -*-
{
    'name': 'Student Lifecycle Dashboard',
    'version': '19.0.1.0.0',
    'category': 'Education',
    'summary': 'Comprehensive dashboard for student lifecycle management from registration to completion',
    'description': """
        Student Lifecycle Dashboard
        ===========================
        
        A comprehensive workflow dashboard that tracks and manages the complete student journey:
        
        * Registration Sources
          - Portal Registrations (student_enrollment_portal)
          - Batch Intake Processing (batch_intake)
          - Contact Pool Management (contact_pool_manager)
        
        * Admission Process
          - Admission creation and tracking
          - Multi-source integration
        
        * Enrollment & Academic
          - Course enrollment
          - Academic progress tracking
          - Attendance and assignments
        
        * Completion & Reporting
          - Graduation tracking
          - Performance analytics
        
        Features:
        - Visual workflow representation
        - Stage-based navigation
        - Real-time statistics
        - Quick access to related modules
        - Manager-friendly interface
    """,
    'author': 'Edafa',
    'website': 'https://www.edafa.sa',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'web',
        'mail',
        'openeducat_core',
        'openeducat_admission',
        'openeducat_attendance',
        'openeducat_assignment',
        'openeducat_exam',
        'student_enrollment_portal',
        'batch_intake',
        'contact_pool_manager',
        'admission_integration',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/student_lifecycle_data.xml',
        'views/student_lifecycle_dashboard_views.xml',
        'views/student_lifecycle_menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'student_lifecycle_dashboard/static/src/css/dashboard.css',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
    'sequence': 1,
}


