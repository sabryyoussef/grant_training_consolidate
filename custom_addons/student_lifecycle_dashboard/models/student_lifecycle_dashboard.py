# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)


class StudentLifecycleDashboard(models.Model):
    _name = 'student.lifecycle.dashboard'
    _description = 'Student Lifecycle Dashboard'
    _order = 'sequence, name'

    name = fields.Char(string='Workflow Name', required=True)
    description = fields.Text(string='Description')
    sequence = fields.Integer(string='Sequence', default=10)
    icon = fields.Char(string='Icon Class', default='fa-graduation-cap')
    color = fields.Char(string='Color Code', default='#3498db')
    is_active = fields.Boolean(string='Active', default=True)
    stage_ids = fields.One2many('student.lifecycle.stage', 'dashboard_id', string='Stages')
    
    # Statistics fields
    total_registrations = fields.Integer(string='Total Registrations', compute='_compute_statistics')
    total_admissions = fields.Integer(string='Total Admissions', compute='_compute_statistics')
    total_enrollments = fields.Integer(string='Total Enrollments', compute='_compute_statistics')
    total_students = fields.Integer(string='Total Students', compute='_compute_statistics')
    
    # Source breakdown
    portal_registrations = fields.Integer(string='Portal Registrations', compute='_compute_statistics')
    batch_intake_count = fields.Integer(string='Batch Intake', compute='_compute_statistics')
    contact_pool_count = fields.Integer(string='Contact Pool', compute='_compute_statistics')
    stage_count = fields.Integer(string='Stage Count', compute='_compute_stage_count')
    
    @api.depends('stage_ids')
    def _compute_stage_count(self):
        """Compute the number of stages"""
        for dashboard in self:
            dashboard.stage_count = len(dashboard.stage_ids)
    
    @api.depends('stage_ids')
    def _compute_statistics(self):
        """Compute statistics for the dashboard"""
        for dashboard in self:
            # Count portal registrations
            portal_count = self.env['student.registration'].search_count([
                ('state', 'in', ['draft', 'submitted', 'under_review', 'approved'])
            ])
            
            # Count batch intake records
            batch_count = self.env['batch.intake'].search_count([
                ('state', 'in', ['draft', 'validated', 'processing', 'completed'])
            ])
            
            # Count contact pool records
            # Note: contact.pool model doesn't have a state field, so we count all pools
            contact_count = self.env['contact.pool'].search_count([])
            
            # Count admissions
            admission_count = self.env['op.admission'].search_count([
                ('state', 'in', ['draft', 'submit', 'confirm', 'admit'])
            ])
            
            # Count enrolled students
            enrollment_count = self.env['op.student.course'].search_count([
                ('state', '=', 'active')
            ])
            
            # Count total students
            student_count = self.env['op.student'].search_count([
                ('active', '=', True)
            ])
            
            dashboard.total_registrations = portal_count + batch_count + contact_count
            dashboard.portal_registrations = portal_count
            dashboard.batch_intake_count = batch_count
            dashboard.contact_pool_count = contact_count
            dashboard.total_admissions = admission_count
            dashboard.total_enrollments = enrollment_count
            dashboard.total_students = student_count

    def action_open_dashboard(self):
        """Open the dashboard view"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': f'{self.name} Dashboard',
            'res_model': 'student.lifecycle.dashboard',
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'current',
        }


