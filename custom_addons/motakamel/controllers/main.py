# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class MotakamelController(http.Controller):
    
    @http.route(['/', '/home'], type='http', auth='public', website=True, sitemap=False)
    def homepage(self, **kwargs):
        """Override homepage to show programs catalog"""
        Program = request.env['motakamel.program'].sudo()
        
        # Get published programs visible to public
        domain = [
            ('status', '=', 'published'),
            ('visibility_scope', '=', 'public'),
            ('active', '=', True)
        ]
        
        programs = Program.search(domain, order='display_order, program_name')
        
        # Check if student_enrollment_portal module is installed
        # Try to access the student.registration model - if it exists, module is installed
        has_enrollment = False
        try:
            request.env['student.registration'].sudo().search([], limit=1)
            has_enrollment = True
        except (KeyError, AttributeError):
            has_enrollment = False
        
        values = {
            'programs': programs,
            'page_name': 'home',
            'has_enrollment_module': has_enrollment,
        }
        
        return request.render('motakamel.programs_catalog', values)
    
    @http.route(['/programs', '/programs/page/<int:page>'], type='http', auth='public', website=True, sitemap=True)
    def programs_catalog(self, page=1, **kwargs):
        """Display public catalog of training programs"""
        Program = request.env['motakamel.program'].sudo()
        
        # Get published programs visible to public
        domain = [
            ('status', '=', 'published'),
            ('visibility_scope', '=', 'public'),
            ('active', '=', True)
        ]
        
        programs = Program.search(domain, order='display_order, program_name')
        
        # Check if student_enrollment_portal module is installed
        # Try to access the student.registration model - if it exists, module is installed
        has_enrollment = False
        try:
            request.env['student.registration'].sudo().search([], limit=1)
            has_enrollment = True
        except (KeyError, AttributeError):
            has_enrollment = False
        
        values = {
            'programs': programs,
            'page_name': 'programs',
            'has_enrollment_module': has_enrollment,
        }
        
        return request.render('motakamel.programs_catalog', values)
    
    @http.route(['/programs/<int:program_id>'], type='http', auth='public', website=True, sitemap=True)
    def program_detail(self, program_id, **kwargs):
        """Display program detail page"""
        Program = request.env['motakamel.program'].sudo()
        
        program = Program.browse(program_id)
        
        # Check if program exists and is accessible
        if not program.exists() or program.status != 'published' or program.visibility_scope != 'public':
            return request.render('website.404')
        
        # Check if student_enrollment_portal module is installed
        # Try to access the student.registration model - if it exists, module is installed
        has_enrollment = False
        try:
            request.env['student.registration'].sudo().search([], limit=1)
            has_enrollment = True
        except (KeyError, AttributeError):
            has_enrollment = False
        
        values = {
            'program': program,
            'page_name': 'program_detail',
            'has_enrollment_module': has_enrollment,
        }
        
        return request.render('motakamel.program_detail', values)
    
    @http.route(['/programs/category/<string:category>'], type='http', auth='public', website=True, sitemap=False)
    def programs_by_category(self, category, **kwargs):
        """Filter programs by category"""
        Program = request.env['motakamel.program'].sudo()
        
        domain = [
            ('status', '=', 'published'),
            ('visibility_scope', '=', 'public'),
            ('active', '=', True),
            ('program_category', '=', category)
        ]
        
        programs = Program.search(domain, order='display_order, program_name')
        
        values = {
            'programs': programs,
            'category': category,
            'page_name': 'programs_category',
        }
        
        return request.render('motakamel.programs_catalog', values)

