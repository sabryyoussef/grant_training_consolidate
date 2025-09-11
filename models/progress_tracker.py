# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)


class ProgressTracker(models.Model):
    _name = 'gr.progress.tracker'
    _description = 'Unified Progress Tracking'
    _order = 'student_id, course_integration_id'

    student_id = fields.Many2one(
        'gr.student',
        string='Student',
        required=True,
        help='The student being tracked'
    )
    
    course_integration_id = fields.Many2one(
        'gr.course.integration',
        string='Course Integration',
        required=True,
        help='The course integration being tracked'
    )
    
    # eLearning Progress
    elearning_progress = fields.Float(
        string='eLearning Progress (%)',
        default=0.0,
        help='Progress percentage in the eLearning course'
    )
    
    elearning_enrollment_id = fields.Many2one(
        'slide.channel.partner',
        string='eLearning Enrollment',
        help='The eLearning enrollment record'
    )
    
    # Custom Training Progress
    custom_sessions_completed = fields.Integer(
        string='Custom Sessions Completed',
        default=0,
        help='Number of custom training sessions completed'
    )
    
    homework_submissions = fields.Integer(
        string='Homework Submissions',
        default=0,
        help='Number of homework submissions'
    )
    
    # Overall Progress
    overall_progress = fields.Float(
        string='Overall Progress (%)',
        compute='_compute_overall_progress',
        store=True,
        help='Overall progress combining eLearning and custom training'
    )
    
    # Status
    status = fields.Selection([
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('certified', 'Certified')
    ], string='Status', default='not_started', tracking=True)
    
    # Dates
    enrollment_date = fields.Datetime(
        string='Enrollment Date',
        default=fields.Datetime.now,
        tracking=True
    )
    
    start_date = fields.Datetime(
        string='Start Date',
        help='When the student started the course'
    )
    
    completion_date = fields.Datetime(
        string='Completion Date',
        help='When the student completed the course'
    )
    
    # Computed fields
    days_to_complete = fields.Integer(
        string='Days to Complete',
        compute='_compute_days_to_complete',
        store=True,
        help='Number of days taken to complete the course'
    )
    
    @api.depends('elearning_progress', 'custom_sessions_completed', 'homework_submissions')
    def _compute_overall_progress(self):
        """Compute overall progress percentage."""
        for record in self:
            # Weighted calculation: 70% eLearning, 30% custom training
            elearning_weight = 0.7
            custom_weight = 0.3
            
            # eLearning progress (0-100%)
            elearning_score = record.elearning_progress
            
            # Custom training score (based on sessions and homework)
            # This is a simplified calculation - can be enhanced
            custom_score = min(100.0, (record.custom_sessions_completed * 10) + (record.homework_submissions * 5))
            
            # Calculate overall progress
            record.overall_progress = (elearning_score * elearning_weight) + (custom_score * custom_weight)
    
    @api.depends('start_date', 'completion_date')
    def _compute_days_to_complete(self):
        """Compute days taken to complete the course."""
        for record in self:
            if record.start_date and record.completion_date:
                delta = record.completion_date - record.start_date
                record.days_to_complete = delta.days
            else:
                record.days_to_complete = 0
    
    @api.constrains('elearning_progress')
    def _check_elearning_progress(self):
        """Validate eLearning progress."""
        for record in self:
            if record.elearning_progress < 0 or record.elearning_progress > 100:
                raise ValidationError(_('eLearning progress must be between 0 and 100.'))
    
    @api.constrains('student_id', 'course_integration_id')
    def _check_unique_enrollment(self):
        """Ensure unique enrollment per student per course."""
        for record in self:
            existing = self.search([
                ('student_id', '=', record.student_id.id),
                ('course_integration_id', '=', record.course_integration_id.id),
                ('id', '!=', record.id)
            ])
            if existing:
                raise ValidationError(_('Student is already enrolled in this course.'))
    
    def action_start_course(self):
        """Mark the course as started."""
        for record in self:
            if record.status == 'not_started':
                record.status = 'in_progress'
                record.start_date = fields.Datetime.now()
                _logger.info('Course started for student %s: %s', record.student_id.name, record.course_integration_id.name)
    
    def action_complete_course(self):
        """Mark the course as completed."""
        for record in self:
            if record.status == 'in_progress':
                # Check if completion threshold is met
                course = record.course_integration_id
                if record.overall_progress >= course.completion_threshold:
                    record.status = 'completed'
                    record.completion_date = fields.Datetime.now()
                    _logger.info('Course completed for student %s: %s', record.student_id.name, record.course_integration_id.name)
                else:
                    raise ValidationError(_('Overall progress must be at least %s%% to complete the course.') % course.completion_threshold)
    
    def action_certify(self):
        """Mark the course as certified."""
        for record in self:
            if record.status == 'completed':
                record.status = 'certified'
                _logger.info('Course certified for student %s: %s', record.student_id.name, record.course_integration_id.name)
    
    def action_update_elearning_progress(self, progress_value):
        """Update eLearning progress from external source."""
        for record in self:
            if 0 <= progress_value <= 100:
                record.elearning_progress = progress_value
                _logger.info('Updated eLearning progress for student %s: %s%%', record.student_id.name, progress_value)
                
                # Auto-start if not started and progress > 0
                if record.status == 'not_started' and progress_value > 0:
                    record.action_start_course()
                
                # Auto-complete if threshold met
                if record.status == 'in_progress' and record.overall_progress >= record.course_integration_id.completion_threshold:
                    record.action_complete_course()
            else:
                raise ValidationError(_('Progress value must be between 0 and 100.'))
    
    def action_sync_with_elearning(self):
        """Synchronize progress with eLearning system."""
        for record in self:
            if record.elearning_enrollment_id:
                # Get progress from eLearning enrollment
                elearning_progress = record.elearning_enrollment_id.completion
                record.action_update_elearning_progress(elearning_progress)
                _logger.info('Synchronized progress for student %s: %s%%', record.student_id.name, elearning_progress)
    
    def name_get(self):
        """Custom name display."""
        result = []
        for record in self:
            name = f"{record.student_id.name} - {record.course_integration_id.name}"
            result.append((record.id, name))
        return result
