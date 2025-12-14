# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class MotakamelMarketing(models.Model):
    _name = 'motakamel.marketing'
    _description = 'Program Marketing & SEO'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'program_id, id desc'
    _rec_name = 'campaign_name'

    # ========================================================
    # RELATIONSHIP
    # ========================================================
    
    program_id = fields.Many2one(
        'motakamel.program',
        string='Program',
        required=True,
        ondelete='cascade',
        index=True,
        tracking=True
    )
    
    campaign_name = fields.Char(
        string='Campaign Name',
        required=True,
        help="Name of this marketing campaign"
    )
    
    # ========================================================
    # WEBSITE VISIBILITY
    # ========================================================
    
    featured_on_homepage = fields.Boolean(
        string='Featured on Homepage',
        default=False,
        tracking=True,
        help="Display this program prominently on the homepage"
    )
    
    featured_priority = fields.Integer(
        string='Featured Priority',
        default=10,
        help="Priority for featured programs (lower = higher priority)"
    )
    
    show_on_catalog = fields.Boolean(
        string='Show on Catalog',
        default=True,
        help="Display in public course catalog"
    )
    
    # ========================================================
    # SEO OPTIMIZATION
    # ========================================================
    
    seo_title = fields.Char(
        string='SEO Title',
        translate=True,
        help="Page title for search engines (50-60 characters recommended)"
    )
    
    seo_description = fields.Text(
        string='SEO Meta Description',
        translate=True,
        help="Meta description for search engines (150-160 characters recommended)"
    )
    
    seo_keywords = fields.Char(
        string='SEO Keywords',
        help="Comma-separated keywords for SEO"
    )
    
    canonical_url = fields.Char(
        string='Canonical URL',
        help="Canonical URL for this program page"
    )
    
    og_image = fields.Binary(
        string='Open Graph Image',
        attachment=True,
        help="Image for social media sharing (1200x630px recommended)"
    )
    
    og_image_filename = fields.Char(
        string='OG Image Filename'
    )
    
    # ========================================================
    # LANDING PAGE
    # ========================================================
    
    landing_page_url = fields.Char(
        string='Landing Page URL',
        help="Custom landing page URL for this program"
    )
    
    landing_page_template = fields.Selection([
        ('default', 'Default Template'),
        ('modern', 'Modern Template'),
        ('minimal', 'Minimal Template'),
        ('corporate', 'Corporate Template'),
        ('custom', 'Custom Template'),
    ], string='Landing Page Template', default='default')
    
    call_to_action_text = fields.Char(
        string='CTA Button Text',
        default='Enroll Now',
        help="Text for the call-to-action button"
    )
    
    call_to_action_url = fields.Char(
        string='CTA URL',
        help="URL for the call-to-action button"
    )
    
    # ========================================================
    # PROMOTIONAL MATERIALS
    # ========================================================
    
    brochure_pdf = fields.Binary(
        string='Program Brochure (PDF)',
        attachment=True,
        help="Downloadable program brochure"
    )
    
    brochure_pdf_filename = fields.Char(
        string='Brochure Filename'
    )
    
    promo_video_url = fields.Char(
        string='Promotional Video URL',
        help="YouTube, Vimeo, or direct video URL"
    )
    
    promo_images = fields.Many2many(
        'ir.attachment',
        'motakamel_marketing_image_rel',
        'marketing_id',
        'attachment_id',
        string='Promotional Images',
        help="Gallery of promotional images"
    )
    
    testimonial_video_url = fields.Char(
        string='Testimonial Video URL',
        help="Video testimonials from past participants"
    )
    
    # ========================================================
    # LEAD GENERATION
    # ========================================================
    
    whatsapp_lead_link = fields.Char(
        string='WhatsApp Lead Link',
        help="WhatsApp link for direct inquiries (e.g., wa.me/1234567890)"
    )
    
    lead_form_enabled = fields.Boolean(
        string='Lead Form Enabled',
        default=True,
        help="Enable lead capture form on program page"
    )
    
    lead_magnet_type = fields.Selection([
        ('brochure', 'Download Brochure'),
        ('sample', 'Free Sample Lesson'),
        ('consultation', 'Free Consultation'),
        ('webinar', 'Free Webinar'),
        ('ebook', 'Free E-Book'),
        ('none', 'None'),
    ], string='Lead Magnet', default='brochure')
    
    lead_magnet_file = fields.Binary(
        string='Lead Magnet File',
        attachment=True,
        help="File to be sent to leads"
    )
    
    lead_magnet_filename = fields.Char(
        string='Lead Magnet Filename'
    )
    
    # ========================================================
    # EMAIL MARKETING
    # ========================================================
    
    email_campaign_active = fields.Boolean(
        string='Email Campaign Active',
        default=False,
        help="Whether email marketing campaign is active"
    )
    
    email_template_id = fields.Many2one(
        'mail.template',
        string='Email Template',
        help="Email template for this program"
    )
    
    drip_campaign_enabled = fields.Boolean(
        string='Drip Campaign Enabled',
        default=False,
        help="Enable automated drip email campaign"
    )
    
    # ========================================================
    # SOCIAL MEDIA
    # ========================================================
    
    facebook_post_text = fields.Text(
        string='Facebook Post',
        help="Pre-written Facebook post for sharing"
    )
    
    twitter_post_text = fields.Char(
        string='Twitter/X Post',
        help="Pre-written tweet (280 characters max)"
    )
    
    linkedin_post_text = fields.Text(
        string='LinkedIn Post',
        help="Pre-written LinkedIn post for sharing"
    )
    
    instagram_caption = fields.Text(
        string='Instagram Caption',
        help="Caption for Instagram posts"
    )
    
    hashtags = fields.Char(
        string='Hashtags',
        help="Recommended hashtags for social media"
    )
    
    # ========================================================
    # ANALYTICS & TRACKING
    # ========================================================
    
    utm_source = fields.Char(
        string='UTM Source',
        help="UTM source parameter for tracking"
    )
    
    utm_medium = fields.Char(
        string='UTM Medium',
        help="UTM medium parameter for tracking"
    )
    
    utm_campaign = fields.Char(
        string='UTM Campaign',
        help="UTM campaign parameter for tracking"
    )
    
    google_analytics_id = fields.Char(
        string='Google Analytics ID',
        help="Specific GA tracking ID for this program"
    )
    
    facebook_pixel_id = fields.Char(
        string='Facebook Pixel ID',
        help="Facebook Pixel ID for conversion tracking"
    )
    
    # ========================================================
    # CAMPAIGN PERFORMANCE
    # ========================================================
    
    campaign_start_date = fields.Date(
        string='Campaign Start Date'
    )
    
    campaign_end_date = fields.Date(
        string='Campaign End Date'
    )
    
    campaign_budget = fields.Monetary(
        string='Campaign Budget',
        currency_field='currency_id'
    )
    
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        default=lambda self: self.env.company.currency_id
    )
    
    leads_generated = fields.Integer(
        string='Leads Generated',
        default=0,
        help="Number of leads generated from this campaign"
    )
    
    conversions = fields.Integer(
        string='Conversions',
        default=0,
        help="Number of enrollments from this campaign"
    )
    
    conversion_rate = fields.Float(
        string='Conversion Rate (%)',
        compute='_compute_conversion_rate',
        store=True
    )
    
    @api.depends('leads_generated', 'conversions')
    def _compute_conversion_rate(self):
        for record in self:
            if record.leads_generated:
                record.conversion_rate = (record.conversions / record.leads_generated) * 100
            else:
                record.conversion_rate = 0.0
    
    # ========================================================
    # ENROLLMENT TRACKING
    # ========================================================
    
    delivery_ids = fields.Many2many(
        'motakamel.delivery',
        string='Deliveries',
        readonly=True,
        compute='_compute_delivery_ids',
        store=False,
        help="All delivery schedules for this program"
    )
    
    @api.depends('program_id.delivery_ids')
    def _compute_delivery_ids(self):
        for record in self:
            record.delivery_ids = record.program_id.delivery_ids if record.program_id else False
    
    total_capacity = fields.Integer(
        string='Total Capacity',
        compute='_compute_enrollment_stats',
        help="Total maximum capacity across all deliveries"
    )
    
    total_enrolled = fields.Integer(
        string='Total Enrolled',
        compute='_compute_enrollment_stats',
        help="Total current enrollments across all deliveries"
    )
    
    total_available = fields.Integer(
        string='Total Available Seats',
        compute='_compute_enrollment_stats',
        help="Total available seats across all deliveries"
    )
    
    enrollment_rate = fields.Float(
        string='Enrollment Fill Rate (%)',
        compute='_compute_enrollment_stats',
        help="Percentage of capacity filled"
    )
    
    @api.depends('program_id.delivery_ids.max_participants', 
                 'program_id.delivery_ids.current_enrollments')
    def _compute_enrollment_stats(self):
        for record in self:
            deliveries = record.program_id.delivery_ids.filtered(
                lambda d: d.delivery_status in ['open', 'in_progress']
            )
            
            total_cap = sum(d.max_participants for d in deliveries if d.max_participants)
            total_enr = sum(d.current_enrollments for d in deliveries)
            
            record.total_capacity = total_cap
            record.total_enrolled = total_enr
            record.total_available = max(0, total_cap - total_enr)
            record.enrollment_rate = (total_enr / total_cap * 100) if total_cap else 0.0
    
    # ========================================================
    # STUDENTS & LEADS TRACKING
    # ========================================================
    
    enrolled_student_ids = fields.Many2many(
        'op.student',
        compute='_compute_students_and_leads',
        string='Enrolled Students',
        help="Students currently enrolled in courses for this program"
    )
    
    enrolled_count = fields.Integer(
        string='Enrolled Count',
        compute='_compute_students_and_leads'
    )
    
    enrollment_request_ids = fields.One2many(
        'course.enrollment.request',
        compute='_compute_students_and_leads',
        string='Enrollment Requests',
        help="Pending enrollment requests for this program"
    )
    
    pending_request_count = fields.Integer(
        string='Pending Requests',
        compute='_compute_students_and_leads'
    )
    
    lead_ids = fields.One2many(
        'crm.lead',
        compute='_compute_students_and_leads',
        string='Interested Leads',
        help="CRM leads interested in this program"
    )
    
    lead_count = fields.Integer(
        string='Lead Count',
        compute='_compute_students_and_leads'
    )
    
    @api.depends('program_id')
    def _compute_students_and_leads(self):
        """Compute enrolled students, enrollment requests, and leads"""
        for record in self:
            # Get enrolled students from batch intakes related to this program
            batch_intakes = self.env['batch.intake'].search([
                '|',
                ('course_id.name', 'ilike', record.program_id.program_name if record.program_id else ''),
                ('name', 'ilike', record.program_id.program_name if record.program_id else '')
            ])
            enrolled_students = batch_intakes.mapped('openeducat_student_ids')
            record.enrolled_student_ids = enrolled_students
            record.enrolled_count = len(enrolled_students)
            
            # Get enrollment requests for courses matching this program
            if record.program_id:
                courses = self.env['op.course'].search([
                    '|',
                    ('name', 'ilike', record.program_id.program_name),
                    ('code', 'ilike', record.program_id.program_code)
                ])
                requests = self.env['course.enrollment.request'].search([
                    ('course_id', 'in', courses.ids),
                    ('state', 'in', ['draft', 'submitted', 'pending'])
                ])
                record.enrollment_request_ids = requests
                record.pending_request_count = len(requests)
            else:
                record.enrollment_request_ids = False
                record.pending_request_count = 0
            
            # Get CRM leads related to this program
            if record.program_id:
                leads = self.env['crm.lead'].search([
                    '|', '|',
                    ('name', 'ilike', record.program_id.program_name),
                    ('description', 'ilike', record.program_id.program_name),
                    ('description', 'ilike', record.campaign_name)
                ])
                record.lead_ids = leads
                record.lead_count = len(leads)
            else:
                record.lead_ids = False
                record.lead_count = 0
    
    # ========================================================
    # COURSE REQUIREMENTS & ACADEMIC MANAGEMENT
    # ========================================================
    
    course_ids = fields.Many2many(
        'op.course',
        compute='_compute_course_resources',
        string='Related Courses',
        help="OpenEduCat courses related to this program"
    )
    
    exam_ids = fields.One2many(
        'op.exam',
        compute='_compute_course_resources',
        string='Exams',
        help="Exams scheduled for this program"
    )
    
    exam_count = fields.Integer(
        string='Exam Count',
        compute='_compute_course_resources'
    )
    
    assignment_ids = fields.One2many(
        'op.assignment',
        compute='_compute_course_resources',
        string='Assignments',
        help="Assignments for this program"
    )
    
    assignment_count = fields.Integer(
        string='Assignment Count',
        compute='_compute_course_resources'
    )
    
    classroom_ids = fields.Many2many(
        'op.classroom',
        compute='_compute_course_resources',
        string='Classrooms',
        help="Classrooms allocated for this program"
    )
    
    classroom_count = fields.Integer(
        string='Classroom Count',
        compute='_compute_course_resources'
    )
    
    timetable_ids = fields.One2many(
        'op.session',
        compute='_compute_course_resources',
        string='Timetables',
        help="Class schedules for this program"
    )
    
    timetable_count = fields.Integer(
        string='Timetable Count',
        compute='_compute_course_resources'
    )
    
    attendance_sheet_ids = fields.One2many(
        'op.attendance.sheet',
        compute='_compute_course_resources',
        string='Attendance Sheets',
        help="Attendance records for this program"
    )
    
    attendance_count = fields.Integer(
        string='Attendance Count',
        compute='_compute_course_resources'
    )
    
    @api.depends('program_id')
    def _compute_course_resources(self):
        """Compute related course resources (exams, assignments, classes, etc.)"""
        for record in self:
            if not record.program_id:
                record.course_ids = False
                record.exam_ids = False
                record.exam_count = 0
                record.assignment_ids = False
                record.assignment_count = 0
                record.classroom_ids = False
                record.classroom_count = 0
                record.timetable_ids = False
                record.timetable_count = 0
                record.attendance_sheet_ids = False
                record.attendance_count = 0
                continue
                
            # Find related courses
            courses = self.env['op.course'].search([
                '|',
                ('name', 'ilike', record.program_id.program_name),
                ('code', 'ilike', record.program_id.program_code)
            ])
            record.course_ids = courses
            
            # Find exams for these courses
            exams = self.env['op.exam'].search([
                ('course_id', 'in', courses.ids)
            ])
            record.exam_ids = exams
            record.exam_count = len(exams)
            
            # Find assignments
            assignments = self.env['op.assignment'].search([
                ('course_id', 'in', courses.ids)
            ])
            record.assignment_ids = assignments
            record.assignment_count = len(assignments)
            
            # Find classrooms
            classrooms = self.env['op.classroom'].search([
                ('course_id', 'in', courses.ids)
            ])
            record.classroom_ids = classrooms
            record.classroom_count = len(classrooms)
            
            # Find timetables
            timetables = self.env['op.session'].search([
                ('course_id', 'in', courses.ids)
            ])
            record.timetable_ids = timetables
            record.timetable_count = len(timetables)
            
            # Find attendance sheets
            attendance_sheets = self.env['op.attendance.sheet'].search([
                ('course_id', 'in', courses.ids)
            ])
            record.attendance_sheet_ids = attendance_sheets
            record.attendance_count = len(attendance_sheets)
    
    # ========================================================
    # STATUS
    # ========================================================
    
    active = fields.Boolean(
        string='Active',
        default=True
    )
    
    campaign_status = fields.Selection([
        ('draft', 'Draft'),
        ('scheduled', 'Scheduled'),
        ('active', 'Active'),
        ('paused', 'Paused'),
        ('completed', 'Completed'),
    ], string='Campaign Status', default='draft', tracking=True)
    
    notes = fields.Text(
        string='Notes'
    )
    
    # ========================================================
    # METHODS
    # ========================================================
    
    def action_view_enrollments(self):
        """View all deliveries with enrollment details"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Enrollment Details - %s') % self.program_id.program_name,
            'res_model': 'motakamel.delivery',
            'view_mode': 'tree,form',
            'domain': [('program_id', '=', self.program_id.id)],
            'context': {
                'default_program_id': self.program_id.id,
                'group_by': 'venue_city',
            }
        }
    
    def action_view_enrolled_students(self):
        """View enrolled students"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Enrolled Students - %s') % self.program_id.program_name,
            'res_model': 'op.student',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', self.enrolled_student_ids.ids)],
            'context': {'create': False}
        }
    
    def action_view_enrollment_requests(self):
        """View pending enrollment requests"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Enrollment Requests - %s') % self.program_id.program_name,
            'res_model': 'course.enrollment.request',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', self.enrollment_request_ids.ids)],
            'context': {
                'create': False,
                'default_state': 'pending'
            }
        }
    
    def action_view_leads(self):
        """View interested leads"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Interested Leads - %s') % self.program_id.program_name,
            'res_model': 'crm.lead',
            'view_mode': 'tree,form,kanban',
            'domain': [('id', 'in', self.lead_ids.ids)],
            'context': {
                'default_name': self.program_id.program_name,
                'default_description': f'Interested in {self.campaign_name}'
            }
        }
    
    # Course Requirements Actions
    
    def action_view_exams(self):
        """View or create exams"""
        self.ensure_one()
        action = {
            'type': 'ir.actions.act_window',
            'name': _('Exams - %s') % self.program_id.program_name,
            'res_model': 'op.exam',
            'view_mode': 'tree,form,calendar',
            'domain': [('id', 'in', self.exam_ids.ids)],
            'context': {
                'default_course_id': self.course_ids[0].id if self.course_ids else False,
            }
        }
        return action
    
    def action_create_exam(self):
        """Create new exam"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Create Exam - %s') % self.program_id.program_name,
            'res_model': 'op.exam',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_course_id': self.course_ids[0].id if self.course_ids else False,
            }
        }
    
    def action_view_assignments(self):
        """View or create assignments"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Assignments - %s') % self.program_id.program_name,
            'res_model': 'op.assignment',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', self.assignment_ids.ids)],
            'context': {
                'default_course_id': self.course_ids[0].id if self.course_ids else False,
            }
        }
    
    def action_create_assignment(self):
        """Create new assignment"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Create Assignment - %s') % self.program_id.program_name,
            'res_model': 'op.assignment',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_course_id': self.course_ids[0].id if self.course_ids else False,
            }
        }
    
    def action_view_classrooms(self):
        """View or create classrooms"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Classrooms - %s') % self.program_id.program_name,
            'res_model': 'op.classroom',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', self.classroom_ids.ids)],
            'context': {
                'default_course_id': self.course_ids[0].id if self.course_ids else False,
            }
        }
    
    def action_create_classroom(self):
        """Create new classroom"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Create Classroom - %s') % self.program_id.program_name,
            'res_model': 'op.classroom',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_course_id': self.course_ids[0].id if self.course_ids else False,
            }
        }
    
    def action_view_timetables(self):
        """View or create timetables"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Timetables - %s') % self.program_id.program_name,
            'res_model': 'op.session',
            'view_mode': 'tree,form,calendar',
            'domain': [('id', 'in', self.timetable_ids.ids)],
            'context': {
                'default_course_id': self.course_ids[0].id if self.course_ids else False,
            }
        }
    
    def action_create_timetable(self):
        """Create new timetable"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Create Timetable - %s') % self.program_id.program_name,
            'res_model': 'op.session',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_course_id': self.course_ids[0].id if self.course_ids else False,
            }
        }
    
    def action_view_attendance(self):
        """View or create attendance sheets"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Attendance - %s') % self.program_id.program_name,
            'res_model': 'op.attendance.sheet',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', self.attendance_sheet_ids.ids)],
            'context': {
                'default_course_id': self.course_ids[0].id if self.course_ids else False,
            }
        }
    
    def action_create_attendance(self):
        """Create new attendance sheet"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Create Attendance Sheet - %s') % self.program_id.program_name,
            'res_model': 'op.attendance.sheet',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_course_id': self.course_ids[0].id if self.course_ids else False,
            }
        }
    
    def action_activate_campaign(self):
        self.write({'campaign_status': 'active', 'campaign_start_date': fields.Date.today()})
    
    def action_pause_campaign(self):
        self.write({'campaign_status': 'paused'})
    
    def action_complete_campaign(self):
        self.write({'campaign_status': 'completed', 'campaign_end_date': fields.Date.today()})
    
    def name_get(self):
        result = []
        for record in self:
            name = record.campaign_name
            if record.campaign_status:
                status = dict(self._fields['campaign_status'].selection).get(record.campaign_status)
                name = f"{name} ({status})"
            result.append((record.id, name))
        return result

