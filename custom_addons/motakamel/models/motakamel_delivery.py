# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class MotakamelDelivery(models.Model):
    _name = 'motakamel.delivery'
    _description = 'Program Delivery Options'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'start_date desc, program_id'
    _rec_name = 'delivery_name'

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
    
    delivery_name = fields.Char(
        string='Delivery Name',
        compute='_compute_delivery_name',
        store=True
    )
    
    @api.depends('training_mode', 'start_date', 'program_id.program_name')
    def _compute_delivery_name(self):
        for record in self:
            mode = dict(self._fields['training_mode'].selection).get(record.training_mode, '')
            if record.start_date:
                record.delivery_name = f"{record.program_id.program_name} - {mode} - {record.start_date}"
            else:
                record.delivery_name = f"{record.program_id.program_name} - {mode}"
    
    # ========================================================
    # DELIVERY MODE
    # ========================================================
    
    training_mode = fields.Selection([
        ('online_live', 'Online Live (Virtual Classroom)'),
        ('online_self', 'Online Self-Paced'),
        ('onsite', 'On-Site (In-Person)'),
        ('hybrid', 'Hybrid (Online + On-Site)'),
        ('blended', 'Blended Learning'),
        ('workshop', 'Workshop'),
        ('bootcamp', 'Bootcamp'),
    ], string='Training Mode', required=True, default='online_live', tracking=True)
    
    training_language = fields.Selection([
        ('en', 'English'),
        ('ar', 'Arabic'),
        ('bilingual', 'Bilingual (English & Arabic)'),
        ('other', 'Other'),
    ], string='Training Language', required=True, default='bilingual')
    
    # ========================================================
    # DURATION & SCHEDULE
    # ========================================================
    
    total_training_hours = fields.Float(
        string='Total Training Hours',
        required=True,
        help="Total number of training hours"
    )
    
    daily_training_hours = fields.Float(
        string='Daily Training Hours',
        help="Number of hours per training day"
    )
    
    program_duration_days = fields.Integer(
        string='Program Duration (Days)',
        required=True,
        help="Total number of days the program runs"
    )
    
    start_date = fields.Date(
        string='Start Date',
        tracking=True
    )
    
    end_date = fields.Date(
        string='End Date',
        tracking=True
    )
    
    schedule_details = fields.Text(
        string='Schedule Details',
        help="Detailed schedule information (days, times, breaks)"
    )
    
    # ========================================================
    # EXAM & MATERIALS
    # ========================================================
    
    exam_included = fields.Boolean(
        string='Exam Included',
        default=True,
        help="Whether certification exam is included"
    )
    
    exam_format = fields.Selection([
        ('online', 'Online Exam'),
        ('onsite', 'On-Site Exam'),
        ('proctored', 'Proctored Online'),
        ('paper', 'Paper-Based'),
        ('practical', 'Practical Assessment'),
        ('none', 'No Exam'),
    ], string='Exam Format', default='online')
    
    exam_date = fields.Date(
        string='Exam Date',
        help="Scheduled exam date (if applicable)"
    )
    
    study_material_included = fields.Boolean(
        string='Study Materials Included',
        default=True,
        help="Whether study materials are provided"
    )
    
    study_material_details = fields.Text(
        string='Study Material Details',
        help="Description of included study materials"
    )
    
    mock_exam_included = fields.Boolean(
        string='Mock Exam Included',
        default=False,
        help="Whether practice/mock exams are included"
    )
    
    # ========================================================
    # LOCATION & CAPACITY
    # ========================================================
    
    venue_name = fields.Char(
        string='Venue Name',
        help="Name of training venue (for on-site training)"
    )
    
    venue_address = fields.Text(
        string='Venue Address',
        help="Full address of training location"
    )
    
    venue_city = fields.Char(
        string='City'
    )
    
    venue_country_id = fields.Many2one(
        'res.country',
        string='Country'
    )
    
    online_platform = fields.Char(
        string='Online Platform',
        help="Platform used for online delivery (e.g., Zoom, Teams, Moodle)"
    )
    
    max_participants = fields.Integer(
        string='Maximum Participants',
        help="Maximum number of participants allowed"
    )
    
    min_participants = fields.Integer(
        string='Minimum Participants',
        help="Minimum number of participants to run the program"
    )
    
    current_enrollments = fields.Integer(
        string='Current Enrollments',
        default=0,
        help="Number of currently enrolled participants"
    )
    
    # ========================================================
    # STATUS
    # ========================================================
    
    delivery_status = fields.Selection([
        ('planned', 'Planned'),
        ('open', 'Open for Registration'),
        ('full', 'Fully Booked'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ], string='Delivery Status', default='planned', tracking=True)
    
    active = fields.Boolean(
        string='Active',
        default=True
    )
    
    # ========================================================
    # COMPUTED FIELDS
    # ========================================================
    
    seats_available = fields.Integer(
        string='Seats Available',
        compute='_compute_seats_available'
    )
    
    @api.depends('max_participants', 'current_enrollments')
    def _compute_seats_available(self):
        for record in self:
            if record.max_participants:
                record.seats_available = record.max_participants - record.current_enrollments
            else:
                record.seats_available = 0
    
    is_full = fields.Boolean(
        string='Is Full',
        compute='_compute_is_full'
    )
    
    @api.depends('seats_available')
    def _compute_is_full(self):
        for record in self:
            record.is_full = record.seats_available <= 0 if record.max_participants else False
    
    # ========================================================
    # CONSTRAINTS
    # ========================================================
    
    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.start_date and record.end_date:
                if record.end_date < record.start_date:
                    raise ValidationError(_('End date must be after start date.'))
    
    @api.constrains('min_participants', 'max_participants')
    def _check_participants(self):
        for record in self:
            if record.min_participants and record.max_participants:
                if record.min_participants > record.max_participants:
                    raise ValidationError(_('Minimum participants cannot exceed maximum participants.'))
    
    @api.constrains('current_enrollments', 'max_participants')
    def _check_enrollments(self):
        for record in self:
            if record.max_participants and record.current_enrollments > record.max_participants:
                raise ValidationError(_('Current enrollments cannot exceed maximum participants.'))
    
    # ========================================================
    # METHODS
    # ========================================================
    
    def action_open_registration(self):
        self.write({'delivery_status': 'open'})
    
    def action_close_registration(self):
        self.write({'delivery_status': 'full'})
    
    def action_start_program(self):
        self.write({'delivery_status': 'in_progress'})
    
    def action_complete_program(self):
        self.write({'delivery_status': 'completed'})
    
    def action_cancel_program(self):
        self.write({'delivery_status': 'cancelled'})

