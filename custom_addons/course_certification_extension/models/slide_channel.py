# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SlideChannel(models.Model):
    _inherit = 'slide.channel'

    # Certification Information
    is_internationally_certified = fields.Boolean(
        string='Internationally Certified',
        default=False,
        help='Check if this course is internationally certified'
    )
    
    has_local_accreditation = fields.Boolean(
        string='Has Local Accreditation',
        default=False,
        help='Check if this course has local accreditation'
    )
    
    certification_body = fields.Char(
        string='Certification Body',
        help='Name of the international certification body (e.g., IBTA)'
    )
    
    course_name_arabic = fields.Char(
        string='Course Name (Arabic)',
        help='Arabic name of the course'
    )
    
    course_name_english = fields.Char(
        string='Course Name (English)',
        help='English name of the course'
    )
    
    # Target Beneficiaries
    target_public_sector = fields.Boolean(
        string='Public Sector',
        default=False,
        help='This course targets public sector organizations'
    )
    
    target_private_sector = fields.Boolean(
        string='Private Sector',
        default=False,
        help='This course targets private sector organizations'
    )
    
    target_individuals = fields.Boolean(
        string='Individuals',
        default=False,
        help='This course targets individuals'
    )
    
    target_nonprofit = fields.Boolean(
        string='Non-Profit Sector',
        default=False,
        help='This course targets non-profit organizations'
    )
    
    # Accreditation Bodies
    accreditation_body_ids = fields.Many2many(
        'course.accreditation.body',
        string='Local Accreditation Bodies',
        help='Local bodies that accredit this course'
    )
    
    # Enhanced Description
    certification_description = fields.Html(
        string='Certification Description',
        help='Detailed description of the certification program'
    )
    
    # Course Image (already exists in slide.channel as 'image_1920', but we can add more)
    certificate_image = fields.Image(
        string='Certificate Sample',
        max_width=1920,
        max_height=1920,
        help='Sample image of the certificate'
    )
    
    @api.onchange('course_name_arabic', 'course_name_english')
    def _onchange_course_names(self):
        """Update the main name field if not set"""
        if self.course_name_english and not self.name:
            self.name = self.course_name_english

