# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class StudentLifecycleStage(models.Model):
    _name = 'student.lifecycle.stage'
    _description = 'Student Lifecycle Stage'
    _order = 'sequence, name'

    name = fields.Char(string='Stage Name', required=True)
    dashboard_id = fields.Many2one('student.lifecycle.dashboard', string='Dashboard', required=True, ondelete='cascade')
    sequence = fields.Integer(string='Sequence', default=10)
    description = fields.Text(string='Description')
    icon = fields.Char(string='Icon Class')
    color = fields.Char(string='Color Code')
    button_label = fields.Char(string='Button Label', default='Open')
    action_method = fields.Char(string='Action Method')
    technical_name = fields.Char(string='Technical Name', help="Technical name of the related module")
    menu_xmlid = fields.Char(string='Menu XML ID', help='XML ID of the menu to open')
    
    # Statistics
    record_count = fields.Integer(string='Record Count', compute='_compute_record_count')
    
    @api.depends('action_method', 'technical_name')
    def _compute_record_count(self):
        """Compute the number of records in this stage"""
        for stage in self:
            count = 0
            try:
                if stage.action_method:
                    # Map action methods to models
                    model_mapping = {
                        'action_open_portal_registrations': 'student.registration',
                        'action_open_batch_intake': 'batch.intake',
                        'action_open_contact_pool': 'contact.pool',
                        'action_open_admissions': 'op.admission',
                        'action_open_students': 'op.student',
                        'action_open_enrollments': 'op.student.course',
                        'action_open_attendance': 'op.attendance.sheet',
                        'action_open_assignments': 'op.assignment',
                        'action_open_exams': 'op.exam',
                    }
                    model_name = model_mapping.get(stage.action_method)
                    if model_name and self.env['ir.model'].search([('model', '=', model_name)]):
                        count = self.env[model_name].search_count([])
            except Exception as e:
                _logger.warning(f"Error computing record count for stage {stage.name}: {e}")
            stage.record_count = count

    def action_execute_stage(self):
        """Execute the stage action"""
        self.ensure_one()
        
        _logger.info(f"Executing stage: {self.name}, Action: {self.action_method}")
        
        # Map action methods to specific module actions
        action_mapping = {
            # Registration Sources
            'action_open_portal_registrations': {
                'type': 'ir.actions.act_window',
                'name': 'Portal Registrations',
                'res_model': 'student.registration',
                'view_mode': 'list,form',
                'target': 'current',
            },
            'action_open_batch_intake': {
                'type': 'ir.actions.act_window',
                'name': 'Batch Intake',
                'res_model': 'batch.intake',
                'view_mode': 'list,form',
                'target': 'current',
            },
            'action_open_contact_pool': {
                'type': 'ir.actions.act_window',
                'name': 'Contact Pool',
                'res_model': 'contact.pool',
                'view_mode': 'list,form',
                'target': 'current',
            },
            
            # Admission Process
            'action_open_admissions': {
                'type': 'ir.actions.act_window',
                'name': 'Admissions',
                'res_model': 'op.admission',
                'view_mode': 'list,form',
                'target': 'current',
            },
            
            # Enrollment & Students
            'action_open_students': {
                'type': 'ir.actions.act_window',
                'name': 'Students',
                'res_model': 'op.student',
                'view_mode': 'list,form',
                'target': 'current',
            },
            'action_open_enrollments': {
                'type': 'ir.actions.act_window',
                'name': 'Student Enrollments',
                'res_model': 'op.student.course',
                'view_mode': 'list,form',
                'target': 'current',
            },
            
            # Academic
            'action_open_attendance': {
                'type': 'ir.actions.act_window',
                'name': 'Attendance Sheets',
                'res_model': 'op.attendance.sheet',
                'view_mode': 'list,form',
                'target': 'current',
            },
            'action_open_assignments': {
                'type': 'ir.actions.act_window',
                'name': 'Assignments',
                'res_model': 'op.assignment',
                'view_mode': 'list,form',
                'target': 'current',
            },
            'action_open_exams': {
                'type': 'ir.actions.act_window',
                'name': 'Exams',
                'res_model': 'op.exam',
                'view_mode': 'list,form',
                'target': 'current',
            },
        }
        
        if self.action_method and self.action_method in action_mapping:
            return action_mapping[self.action_method]
        
        # Fallback: try to open menu if menu_xmlid is set
        if self.menu_xmlid:
            try:
                menu = self.env.ref(self.menu_xmlid, raise_if_not_found=False)
                if menu and menu.action:
                    return menu.action.read()[0]
            except Exception as e:
                _logger.warning(f"Failed to open menu {self.menu_xmlid}: {e}")
        
        # Default fallback
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Stage Action',
                'message': f'Opening {self.name} - {self.button_label}',
                'type': 'info',
                'sticky': False,
            }
        }


