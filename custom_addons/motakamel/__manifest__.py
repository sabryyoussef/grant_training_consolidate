# -*- coding: utf-8 -*-
{
    'name': 'Motakamel - Enterprise Training & Certification Platform',
    'version': '19.0.1.0.0',
    'category': 'Education',
    'summary': 'Professional Certification & Courses Management System',
    'description': """
        Motakamel - Enterprise Training & Certification Platform
        ==========================================================
        
        A unified Courses & Certifications engine inside Odoo that supports:
        
        - Website publishing for courses and programs
        - CRM lead capture and conversion
        - LMS-style training operations
        - Certificate issuance lifecycle management
        - Corporate contracts & public sector programs
        - Multi-accreditation support (international & local)
        - Flexible pricing models with installments
        - Multiple delivery modes (online, in-person, hybrid)
        - SEO-optimized marketing capabilities
        - Full credential management and verification
        
        Key Features:
        -------------
        * Program Management: Complete course/certification lifecycle
        * Accreditation Tracking: International & local certifications
        * Flexible Pricing: Discounts, installments, bulk pricing
        * Delivery Options: Online, in-person, hybrid modes
        * Marketing Tools: SEO, landing pages, promotional materials
        * Credential System: Certificate issuance and verification
        * CRM Integration: Lead capture and conversion tracking
        * Website Publishing: Public course catalog
        * Multi-language: Arabic and English support
        
        Technical:
        ----------
        * Odoo 16-19 compatible
        * Clean ORM architecture
        * Upgrade-safe design
        * Enterprise-grade quality
        * Full access control
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'website',
        'crm',
        'sale',
        'website_sale',
        # OpenEduCat Integration
        'openeducat_core',
        'openeducat_exam',
        'openeducat_assignment',
        'openeducat_classroom',
        'openeducat_timetable',
        'openeducat_attendance',
        # Custom Modules
        'batch_intake',
        'student_enrollment_portal',
    ],
    'data': [
        # Security
        'security/motakamel_security.xml',
        'security/ir.model.access.csv',
        
        # Data
        'data/motakamel_data.xml',
        
        # Views - Programs (main)
        'views/motakamel_program_views.xml',
        
        # Views - Related models
        'views/motakamel_accreditation_views.xml',
        'views/motakamel_audience_views.xml',
        'views/motakamel_delivery_views.xml',
        'views/motakamel_pricing_views.xml',
        'views/motakamel_credential_views.xml',
        'views/motakamel_marketing_views.xml',
        
        # Menus
        'views/motakamel_menus.xml',
        
        # Website
        'views/website_templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'motakamel/static/src/css/motakamel_backend.css',
        ],
        'website.assets_frontend': [
            'motakamel/static/src/css/motakamel_frontend.css',
        ],
    },
    'demo': [
        'data/motakamel_program_demo.xml',
        'data/motakamel_accreditation_demo.xml',
        'data/motakamel_audience_demo.xml',
        'data/motakamel_delivery_demo.xml',
        'data/motakamel_pricing_demo.xml',
        'data/motakamel_credential_demo.xml',
        'data/motakamel_marketing_demo.xml',
    ],
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': True,
    'auto_install': False,
}

