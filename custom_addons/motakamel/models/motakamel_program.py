# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class MotakamelProgram(models.Model):
    _name = 'motakamel.program'
    _description = 'Training Program'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'website.seo.metadata', 'website.published.mixin']
    _order = 'display_order, program_code, id desc'
    _rec_name = 'program_name'

    # ========================================================
    # BASIC INFORMATION
    # ========================================================
    
    program_id = fields.Char(
        string='Program ID',
        required=True,
        copy=False,
        readonly=True,
        index=True,
        default=lambda self: _('New'),
        help="Unique identifier for the program"
    )
    
    program_name = fields.Char(
        string='Program Name (English)',
        required=True,
        translate=True,
        tracking=True,
        help="Official program name in English"
    )
    
    program_name_ar = fields.Char(
        string='Program Name (Arabic)',
        required=True,
        translate=True,
        tracking=True,
        help="Official program name in Arabic"
    )
    
    program_code = fields.Char(
        string='Program Code',
        required=True,
        copy=False,
        index=True,
        tracking=True,
        help="Short code for the program (e.g., PMP, CBAP, ITIL)"
    )
    
    program_category = fields.Selection([
        ('professional', 'Professional Certification'),
        ('technical', 'Technical Training'),
        ('management', 'Management & Leadership'),
        ('it', 'Information Technology'),
        ('finance', 'Finance & Accounting'),
        ('hr', 'Human Resources'),
        ('marketing', 'Marketing & Sales'),
        ('healthcare', 'Healthcare'),
        ('engineering', 'Engineering'),
        ('legal', 'Legal & Compliance'),
        ('other', 'Other'),
    ], string='Program Category', required=True, tracking=True, default='professional')
    
    program_level = fields.Selection([
        ('foundation', 'Foundation'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
        ('master', 'Master'),
    ], string='Program Level', required=True, default='intermediate', tracking=True)
    
    provider_name = fields.Char(
        string='Provider Name',
        required=True,
        tracking=True,
        help="Name of the training provider or certification body"
    )
    
    provider_type = fields.Selection([
        ('internal', 'Internal'),
        ('external', 'External Partner'),
        ('accredited', 'Accredited Body'),
        ('university', 'University'),
        ('vendor', 'Vendor Authorized'),
    ], string='Provider Type', required=True, default='external', tracking=True)
    
    description_en = fields.Html(
<<<<<<< HEAD
        string='Description (English)',
        translate=True,
        help="Detailed program description in English"
    )
    
    description_ar = fields.Html(
        string='Description (Arabic)',
        translate=True,
        help="Detailed program description in Arabic"
=======











        string='Description',
        translate=True,
        help="Detailed program description (use Odoo translations for multiple languages)"
>>>>>>> 959f060 (Motakamel integration: academic operations menus, program smart buttons, courses link, chatter, and marketing media)
    )
    
    program_objective = fields.Text(
        string='Program Objectives',
        translate=True,
        help="Learning objectives and outcomes"
    )
    
    career_outcome = fields.Text(
        string='Career Outcomes',
        translate=True,
        help="Expected career benefits and opportunities"
    )
    
    status = fields.Selection([
        ('draft', 'Draft'),
        ('review', 'Under Review'),
        ('approved', 'Approved'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ], string='Status', default='draft', required=True, tracking=True)
    
    active = fields.Boolean(
        string='Active',
        default=True,
        help="Set to false to archive the program without deleting it"
    )
    
    # ========================================================
    # RELATED MODELS (One2many relationships)
    # ========================================================
    
    accreditation_ids = fields.One2many(
        'motakamel.accreditation',
        'program_id',
        string='Accreditations',
        help="International and local accreditations"
    )
    
    audience_ids = fields.One2many(
        'motakamel.audience',
        'program_id',
        string='Target Audience',
        help="Target sectors and eligible participants"
    )
    
    delivery_ids = fields.One2many(
        'motakamel.delivery',
        'program_id',
        string='Delivery Options',
        help="Training delivery modes and schedules"
    )
    
    pricing_ids = fields.One2many(
        'motakamel.pricing',
        'program_id',
        string='Pricing Plans',
        help="Pricing options and discounts"
    )
    
    credential_ids = fields.One2many(
        'motakamel.credential',
        'program_id',
        string='Credentials',
        help="Certificate and credential information"
    )
    
    marketing_ids = fields.One2many(
        'motakamel.marketing',
        'program_id',
        string='Marketing Materials',
        help="SEO, landing pages, and promotional content"
    )
    
    # ========================================================
    # ADMINISTRATIVE FIELDS
    # ========================================================
    
    created_by = fields.Many2one(
        'res.users',
        string='Created By',
        default=lambda self: self.env.user,
        readonly=True,
        tracking=True
    )
    
    approved_by = fields.Many2one(
        'res.users',
        string='Approved By',
        readonly=True,
        tracking=True
    )
    
    created_date = fields.Datetime(
        string='Created Date',
        default=fields.Datetime.now,
        readonly=True
    )
    
    last_updated = fields.Datetime(
        string='Last Updated',
        readonly=True,
        compute='_compute_last_updated',
        store=True
    )
    
    internal_notes = fields.Text(
        string='Internal Notes',
        help="Internal notes for administrators"
    )
    
    display_order = fields.Integer(
        string='Display Order',
        default=10,
        help="Order for displaying programs (lower numbers appear first)"
    )
    
    visibility_scope = fields.Selection([
        ('public', 'Public'),
        ('registered', 'Registered Users Only'),
        ('corporate', 'Corporate Clients Only'),
        ('internal', 'Internal Only'),
    ], string='Visibility Scope', default='public', required=True)
<<<<<<< HEAD
=======

    # ========================================================
    # RELATED OPENEDUCAT COURSES
    # ========================================================

    course_ids = fields.Many2many(
        'op.course',
        string='Related Courses',
        compute='_compute_related_courses',
        help="OpenEduCat courses whose name or code match this program"
    )

    course_count = fields.Integer(
        string='Courses',
        compute='_compute_related_courses'
    )
>>>>>>> 959f060 (Motakamel integration: academic operations menus, program smart buttons, courses link, chatter, and marketing media)
    
    # ========================================================
    # COMPUTED FIELDS
    # ========================================================
    
    @api.depends('write_date')
    def _compute_last_updated(self):
        for record in self:
            record.last_updated = record.write_date or record.create_date
    
    accreditation_count = fields.Integer(
        string='Accreditations',
        compute='_compute_counts'
    )
    
    delivery_count = fields.Integer(
        string='Delivery Options',
        compute='_compute_counts'
    )
    
    pricing_count = fields.Integer(
        string='Pricing Plans',
        compute='_compute_counts'
    )
<<<<<<< HEAD
    
    @api.depends('accreditation_ids', 'delivery_ids', 'pricing_ids')
=======

    marketing_count = fields.Integer(
        string='Marketing',
        compute='_compute_counts',
        help="Number of marketing/media records for this program"
    )
    
    @api.depends('accreditation_ids', 'delivery_ids', 'pricing_ids', 'marketing_ids')
>>>>>>> 959f060 (Motakamel integration: academic operations menus, program smart buttons, courses link, chatter, and marketing media)
    def _compute_counts(self):
        for record in self:
            record.accreditation_count = len(record.accreditation_ids)
            record.delivery_count = len(record.delivery_ids)
            record.pricing_count = len(record.pricing_ids)
<<<<<<< HEAD
=======
            record.marketing_count = len(record.marketing_ids)

    @api.depends('program_name', 'program_code')
    def _compute_related_courses(self):
        """Link OpenEduCat courses based on matching name/code."""
        Course = self.env['op.course']
        for record in self:
            if not record.program_name and not record.program_code:
                record.course_ids = False
                record.course_count = 0
                continue

            domain = []
            if record.program_name:
                domain.append(('name', 'ilike', record.program_name))
            if record.program_code:
                domain.append(('code', 'ilike', record.program_code))

            if len(domain) == 2:
                search_domain = ['|'] + domain
            elif len(domain) == 1:
                search_domain = domain
            else:
                search_domain = []

            courses = Course.search(search_domain) if search_domain else Course.browse()
            record.course_ids = courses
            record.course_count = len(courses)
>>>>>>> 959f060 (Motakamel integration: academic operations menus, program smart buttons, courses link, chatter, and marketing media)
    
    # ========================================================
    # CONSTRAINTS
    # ========================================================
    
    _sql_constraints = [
        ('program_code_unique', 'UNIQUE(program_code)', 'Program code must be unique!'),
    ]
    
    @api.constrains('program_code')
    def _check_program_code(self):
        for record in self:
            if record.program_code:
                if not record.program_code.replace('_', '').replace('-', '').isalnum():
                    raise ValidationError(_('Program code must contain only letters, numbers, hyphens, and underscores.'))
    
    # ========================================================
    # CRUD OPERATIONS
    # ========================================================
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('program_id', _('New')) == _('New'):
                vals['program_id'] = self.env['ir.sequence'].next_by_code('motakamel.program') or _('New')
        return super().create(vals_list)
    
    def write(self, vals):
        if vals.get('status') == 'approved' and not self.approved_by:
            vals['approved_by'] = self.env.user.id
        return super().write(vals)
    
    # ========================================================
    # ACTIONS
    # ========================================================
    
    def action_submit_for_review(self):
        self.write({'status': 'review'})
    
    def action_approve(self):
        self.write({'status': 'approved', 'approved_by': self.env.user.id})
    
    def action_publish(self):
        self.write({'status': 'published', 'is_published': True})
    
    def action_archive_program(self):
        self.write({'status': 'archived', 'active': False})
    
    def action_view_accreditations(self):
        return {
            'name': _('Accreditations'),
            'type': 'ir.actions.act_window',
            'res_model': 'motakamel.accreditation',
            'view_mode': 'list,form',
            'domain': [('program_id', '=', self.id)],
            'context': {'default_program_id': self.id},
        }
    
    def action_view_delivery(self):
        return {
            'name': _('Delivery Options'),
            'type': 'ir.actions.act_window',
            'res_model': 'motakamel.delivery',
            'view_mode': 'list,form',
            'domain': [('program_id', '=', self.id)],
            'context': {'default_program_id': self.id},
        }
    
    def action_view_pricing(self):
        return {
            'name': _('Pricing Plans'),
            'type': 'ir.actions.act_window',
            'res_model': 'motakamel.pricing',
            'view_mode': 'list,form',
            'domain': [('program_id', '=', self.id)],
            'context': {'default_program_id': self.id},
        }
<<<<<<< HEAD
=======

    def action_view_marketing(self):
        """Open marketing/media records for this program."""
        self.ensure_one()
        return {
            'name': _('Marketing & Media - %s') % self.program_name,
            'type': 'ir.actions.act_window',
            'res_model': 'motakamel.marketing',
            'view_mode': 'list,form',
            'domain': [('program_id', '=', self.id)],
            'context': {'default_program_id': self.id},
        }

    def action_view_courses(self):
        """View OpenEduCat courses linked to this program."""
        self.ensure_one()
        return {
            'name': _('Courses - %s') % self.program_name,
            'type': 'ir.actions.act_window',
            'res_model': 'op.course',
            'view_mode': 'list,form',
            'domain': [('id', 'in', self.course_ids.ids)],
            'context': {
                'default_name': self.program_name,
                'default_code': self.program_code,
            },
        }
>>>>>>> 959f060 (Motakamel integration: academic operations menus, program smart buttons, courses link, chatter, and marketing media)
    
    # ========================================================
    # WEBSITE METHODS
    # ========================================================
    
    def _compute_website_url(self):
        for record in self:
            record.website_url = '/programs/%s' % record.id

