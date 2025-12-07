# -*- coding: utf-8 -*-
{
    'name': 'Course Certification Extension',
    'version': '19.0.1.0.0',
    'category': 'Website/eLearning',
    'summary': 'Extends eLearning courses with certification and accreditation fields',
    'description': """
        Course Certification Extension
        ===============================
        
        This module extends the website_slides (eLearning) module to add:
        - International certification badges
        - Local accreditation information
        - Target beneficiaries (Public/Private/Individuals/Non-profit sectors)
        - Accreditation body logos
        - IBTA certification support
        - Enhanced course details for certification programs
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'license': 'LGPL-3',
    'depends': [
        'website_slides',  # eLearning module
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/slide_channel_views.xml',
        'views/portal/course_portal_template.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'course_certification_extension/static/src/css/course_certification.css',
        ],
        'web.assets_frontend': [
            'course_certification_extension/static/src/css/course_portal.css',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}

