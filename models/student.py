# -*- coding: utf-8 -*-

import logging
from datetime import datetime, date
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)

class Student(models.Model):
    _name = 'gr.student'
    _description = 'Grants Training Student'
    _order = 'create_date desc'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # Basic Information
    name = fields.Char(
        string='Full Name',
        required=True,
        tracking=True,
        help='Student full name'
    )
    
    email = fields.Char(
        string='Email',
        required=True,
        tracking=True,
        help='Student email address'
    )
    
    phone = fields.Char(
        string='Phone',
        tracking=True,
        help='Student phone number'
    )
    
    # Personal Information
    birth_date = fields.Date(
        string='Birth Date',
        tracking=True,
        help='Student birth date'
    )
    
    age = fields.Integer(
        string='Age',
        compute='_compute_age',
        store=True,
        help='Student age calculated from birth date'
    )
    
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender', tracking=True)
    
    nationality = fields.Char(
        string='Nationality',
        help='Student nationality'
    )
    
    # Language Information
    native_language = fields.Char(
        string='Native Language',
        help='Student native language'
    )
    
    english_level = fields.Selection([
        ('beginner', 'Beginner'),
        ('elementary', 'Elementary'),
        ('intermediate', 'Intermediate'),
        ('upper_intermediate', 'Upper Intermediate'),
        ('advanced', 'Advanced'),
        ('proficient', 'Proficient'),
    ], string='English Level', tracking=True, help='Student English proficiency level')
    
    # Eligibility Information
    has_certificate = fields.Boolean(
        string='Has Certificate',
        default=False,
        tracking=True,
        help='Does the student have a required certificate?'
    )
    
    certificate_type = fields.Char(
        string='Certificate Type',
        help='Type of certificate the student has'
    )
    
    certificate_date = fields.Date(
        string='Certificate Date',
        help='Date when certificate was obtained'
    )
    
    # Status and Workflow
    state = fields.Selection([
        ('draft', 'Draft'),
        ('eligible', 'Eligible'),
        ('assigned', 'Assigned to Agent'),
        ('contacted', 'Contacted'),
        ('enrolled', 'Enrolled'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('certified', 'Certified'),
        ('rejected', 'Rejected'),
    ], string='Status', default='draft', tracking=True)
    
    # Intake Information
    intake_batch_id = fields.Many2one(
        'gr.intake.batch',
        string='Intake Batch',
        help='Batch from which this student was imported'
    )
    
    intake_date = fields.Datetime(
        string='Intake Date',
        default=fields.Datetime.now,
        help='Date when student was added to the system'
    )
    
    # Assignment Information
    assigned_agent_id = fields.Many2one(
        'res.users',
        string='Assigned Agent',
        tracking=True,
        help='Agent assigned to this student'
    )
    
    assignment_date = fields.Datetime(
        string='Assignment Date',
        help='Date when student was assigned to an agent'
    )
    
    first_contact_date = fields.Datetime(
        string='First Contact Date',
        help='Date when agent first contacted the student'
    )
    
    # Course Information (will be added when gr.course.session model is created)
    # course_session_ids = fields.One2many(
    #     'gr.course.session',
    #     'student_id',
    #     string='Course Sessions',
    #     help='Course sessions this student is enrolled in'
    # )
    
    # Assessment Information (will be added when gr.homework.attempt model is created)
    # homework_attempt_ids = fields.One2many(
    #     'gr.homework.attempt',
    #     'student_id',
    #     string='Homework Attempts',
    #     help='Homework attempts by this student'
    # )
    
    # Certificate Information (will be added when gr.certificate model is created)
    # certificate_ids = fields.One2many(
    #     'gr.certificate',
    #     'student_id',
    #     string='Certificates',
    #     help='Certificates earned by this student'
    # )
    
    # Computed Fields
    total_sessions = fields.Integer(
        string='Total Sessions',
        compute='_compute_total_sessions',
        store=True,
        help='Total number of course sessions'
    )
    
    completed_sessions = fields.Integer(
        string='Completed Sessions',
        compute='_compute_completed_sessions',
        store=True,
        help='Number of completed sessions'
    )
    
    progress_percentage = fields.Float(
        string='Progress (%)',
        compute='_compute_progress_percentage',
        store=True,
        help='Course completion percentage'
    )
    
    # Eligibility Assessment
    is_eligible = fields.Boolean(
        string='Is Eligible',
        compute='_compute_eligibility',
        store=True,
        help='Whether student meets eligibility criteria'
    )
    
    eligibility_reason = fields.Text(
        string='Eligibility Reason',
        compute='_compute_eligibility',
        store=True,
        help='Reason for eligibility or rejection'
    )
    
    @api.depends('birth_date')
    def _compute_age(self):
        """Compute age from birth date."""
        today = date.today()
        for record in self:
            if record.birth_date:
                age = today.year - record.birth_date.year
                if today.month < record.birth_date.month or \
                   (today.month == record.birth_date.month and today.day < record.birth_date.day):
                    age -= 1
                record.age = age
            else:
                record.age = 0
    
    def _compute_total_sessions(self):
        """Compute total number of course sessions."""
        for record in self:
            # TODO: Implement when course_session_ids field is uncommented
            record.total_sessions = 0
    
    def _compute_completed_sessions(self):
        """Compute number of completed sessions."""
        for record in self:
            # TODO: Implement when course_session_ids field is uncommented
            record.completed_sessions = 0
    
    @api.depends('total_sessions', 'completed_sessions')
    def _compute_progress_percentage(self):
        """Compute course progress percentage."""
        for record in self:
            if record.total_sessions > 0:
                record.progress_percentage = (record.completed_sessions / record.total_sessions) * 100
            else:
                record.progress_percentage = 0.0
    
    @api.depends('age', 'english_level', 'has_certificate')
    def _compute_eligibility(self):
        """Compute eligibility based on criteria."""
        for record in self:
            reasons = []
            eligible = True
            
            # Age requirement (18-65)
            if record.age < 18:
                eligible = False
                reasons.append('Age must be at least 18 years')
            elif record.age > 65:
                eligible = False
                reasons.append('Age must be 65 years or less')
            
            # English level requirement (at least intermediate)
            if record.english_level in ['beginner', 'elementary']:
                eligible = False
                reasons.append('English level must be at least intermediate')
            
            # Certificate requirement
            if not record.has_certificate:
                eligible = False
                reasons.append('Required certificate is missing')
            
            record.is_eligible = eligible
            if eligible:
                record.eligibility_reason = 'Student meets all eligibility criteria'
            else:
                record.eligibility_reason = '; '.join(reasons)
    
    @api.model
    def create(self, vals):
        """Override create to set intake date and assess eligibility."""
        student = super(Student, self).create(vals)
        
        # Assess eligibility after creation
        student._assess_eligibility()
        
        # Log creation
        _logger.info('Student created: %s (%s)', student.name, student.email)
        
        return student
    
    def write(self, vals):
        """Override write to reassess eligibility if relevant fields change."""
        result = super(Student, self).write(vals)
        
        # Reassess eligibility if relevant fields changed
        relevant_fields = ['age', 'english_level', 'has_certificate', 'birth_date']
        if any(field in vals for field in relevant_fields):
            for record in self:
                record._assess_eligibility()
        
        return result
    
    def _assess_eligibility(self):
        """Assess student eligibility and update state."""
        self.ensure_one()
        
        if self.is_eligible:
            if self.state == 'draft':
                self.state = 'eligible'
                _logger.info('Student %s marked as eligible', self.name)
        else:
            if self.state in ['draft', 'eligible']:
                self.state = 'rejected'
                _logger.info('Student %s marked as rejected: %s', self.name, self.eligibility_reason)
    
    def action_assign_agent(self):
        """Action to assign an agent to the student."""
        self.ensure_one()
        
        if self.state != 'eligible':
            raise UserError(_('Only eligible students can be assigned to agents.'))
        
        # Find available agent (round-robin assignment)
        available_agents = self.env['res.users'].search([
            ('groups_id', 'in', [('id', '=', ('grants_training_suite_v2.group_agent', '=', True))]),
            ('active', '=', True)
        ])
        
        if not available_agents:
            raise UserError(_('No available agents found.'))
        
        # Simple round-robin assignment (can be improved)
        agent = available_agents[0]
        
        self.assigned_agent_id = agent
        self.assignment_date = fields.Datetime.now()
        self.state = 'assigned'
        
        # Log assignment
        _logger.info('Student %s assigned to agent %s', self.name, agent.name)
        
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Agent Assigned'),
                'message': _('Student has been assigned to agent %s.') % agent.name,
                'type': 'success',
            }
        }
    
    def action_mark_contacted(self):
        """Action to mark student as contacted by agent."""
        self.ensure_one()
        
        if self.state != 'assigned':
            raise UserError(_('Student must be assigned to an agent first.'))
        
        self.first_contact_date = fields.Datetime.now()
        self.state = 'contacted'
        
        # Log contact
        _logger.info('Student %s marked as contacted by agent %s', self.name, self.assigned_agent_id.name)
        
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Student Contacted'),
                'message': _('Student has been marked as contacted.'),
                'type': 'success',
            }
        }
    
    def action_enroll(self):
        """Action to enroll student in a course."""
        self.ensure_one()
        
        if self.state != 'contacted':
            raise UserError(_('Student must be contacted first before enrollment.'))
        
        self.state = 'enrolled'
        
        # Log enrollment
        _logger.info('Student %s enrolled in course', self.name)
        
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Student Enrolled'),
                'message': _('Student has been enrolled in the course.'),
                'type': 'success',
            }
        }
    
    def action_start_course(self):
        """Action to start the course for the student."""
        self.ensure_one()
        
        if self.state != 'enrolled':
            raise UserError(_('Student must be enrolled first.'))
        
        self.state = 'in_progress'
        
        # Log course start
        _logger.info('Student %s started the course', self.name)
        
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Course Started'),
                'message': _('Student has started the course.'),
                'type': 'success',
            }
        }
    
    def action_complete_course(self):
        """Action to mark course as completed."""
        self.ensure_one()
        
        if self.state != 'in_progress':
            raise UserError(_('Student must be in progress first.'))
        
        self.state = 'completed'
        
        # Log completion
        _logger.info('Student %s completed the course', self.name)
        
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Course Completed'),
                'message': _('Student has completed the course.'),
                'type': 'success',
            }
        }
    
    def action_issue_certificate(self):
        """Action to issue certificate to student."""
        self.ensure_one()
        
        if self.state != 'completed':
            raise UserError(_('Student must complete the course first.'))
        
        self.state = 'certified'
        
        # Log certification
        _logger.info('Student %s received certificate', self.name)
        
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Certificate Issued'),
                'message': _('Certificate has been issued to the student.'),
                'type': 'success',
            }
        }
    
    def action_reset(self):
        """Action to reset student to draft state."""
        self.ensure_one()
        self.state = 'draft'
        self.assigned_agent_id = False
        self.assignment_date = False
        self.first_contact_date = False
        
        # Log reset
        _logger.info('Student %s reset to draft state', self.name)
    
    @api.constrains('email')
    def _check_email(self):
        """Validate email format."""
        for record in self:
            if record.email and '@' not in record.email:
                raise ValidationError(_('Please enter a valid email address.'))
    
    @api.constrains('age')
    def _check_age(self):
        """Validate age range."""
        for record in self:
            if record.age and (record.age < 0 or record.age > 100):
                raise ValidationError(_('Age must be between 0 and 100 years.'))
