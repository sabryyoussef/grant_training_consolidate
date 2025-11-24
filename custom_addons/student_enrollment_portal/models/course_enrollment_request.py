# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class CourseEnrollmentRequest(models.Model):
    _name = 'course.enrollment.request'
    _description = 'Course Enrollment Request'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc'

    # Basic Information
    name = fields.Char(
        string='Request Number',
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: _('New'),
        tracking=True
    )

    student_id = fields.Many2one(
        'op.student',
        string='Student',
        required=True,
        tracking=True,
        help='Student requesting enrollment'
    )

    course_id = fields.Many2one(
        'op.course',
        string='Course',
        required=True,
        tracking=True,
        help='Course to enroll in'
    )

    batch_id = fields.Many2one(
        'op.batch',
        string='Batch',
        domain="[('course_id', '=', course_id)]",
        tracking=True,
        help='Specific batch to enroll in (optional)'
    )

    # Workflow State
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('pending', 'Pending Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Status', default='draft', required=True, tracking=True)

    # Dates
    request_date = fields.Datetime(
        string='Request Date',
        default=fields.Datetime.now,
        tracking=True,
        help='Date when the request was submitted'
    )

    approval_date = fields.Datetime(
        string='Approval Date',
        tracking=True,
        help='Date when the request was approved'
    )

    rejection_reason = fields.Text(
        string='Rejection Reason',
        tracking=True,
        help='Reason for rejection if request is rejected'
    )

    approved_by = fields.Many2one(
        'res.users',
        string='Approved By',
        tracking=True,
        help='User who approved the request'
    )

    # Related Enrollment
    student_course_id = fields.Many2one(
        'op.student.course',
        string='Student Course Enrollment',
        readonly=True,
        tracking=True,
        help='The enrollment record created when request was approved'
    )

    @api.model_create_multi
    def create(self, vals_list):
        """Generate sequence number for enrollment request"""
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('course.enrollment.request') or _('New')
        return super(CourseEnrollmentRequest, self).create(vals_list)

    @api.constrains('student_id', 'course_id', 'batch_id')
    def _check_duplicate_request(self):
        """Prevent duplicate enrollment requests"""
        for record in self:
            if record.state in ['draft', 'submitted', 'pending']:
                domain = [
                    ('student_id', '=', record.student_id.id),
                    ('course_id', '=', record.course_id.id),
                    ('state', 'in', ['draft', 'submitted', 'pending']),
                ]
                if record.batch_id:
                    domain.append(('batch_id', '=', record.batch_id.id))
                else:
                    domain.append(('batch_id', '=', False))
                
                existing = self.search(domain)
                if len(existing) > 1 or (len(existing) == 1 and existing.id != record.id):
                    raise ValidationError(_('A pending enrollment request already exists for this student, course, and batch combination.'))

    def action_submit(self):
        """Submit request for review"""
        for record in self:
            if record.state != 'draft':
                raise UserError(_('Only draft requests can be submitted.'))
            
            # Check if student is already enrolled
            domain = [
                ('student_id', '=', record.student_id.id),
                ('course_id', '=', record.course_id.id),
            ]
            if record.batch_id:
                domain.append(('batch_id', '=', record.batch_id.id))
            
            existing_enrollment = self.env['op.student.course'].search(domain, limit=1)
            if existing_enrollment:
                raise UserError(_('Student is already enrolled in this course/batch combination.'))
            
            record.write({
                'state': 'submitted',
                'request_date': fields.Datetime.now()
            })
            
            # Send notification to admins
            self._send_submission_notification()
            
            record.message_post(
                body=_('Enrollment request submitted for review.'),
                message_type='notification'
            )
            
            _logger.info(f'Enrollment request {record.name} submitted by student {record.student_id.name}')

    def action_approve(self):
        """Approve request and create enrollment"""
        for record in self:
            if record.state not in ['submitted', 'pending']:
                raise UserError(_('Only submitted or pending requests can be approved.'))
            
            # Check if student is already enrolled
            domain = [
                ('student_id', '=', record.student_id.id),
                ('course_id', '=', record.course_id.id),
            ]
            if record.batch_id:
                domain.append(('batch_id', '=', record.batch_id.id))
            
            existing_enrollment = self.env['op.student.course'].search(domain, limit=1)
            if existing_enrollment:
                raise UserError(_('Student is already enrolled in this course/batch combination.'))
            
            # Create enrollment
            student_course = record._create_student_course()
            
            record.write({
                'state': 'approved',
                'approval_date': fields.Datetime.now(),
                'approved_by': self.env.user.id,
                'student_course_id': student_course.id
            })
            
            # Send approval email
            self._send_approval_email()
            
            record.message_post(
                body=_('Enrollment request approved. Student enrolled in course: %s') % record.course_id.name,
                message_type='notification'
            )
            
            _logger.info(f'Enrollment request {record.name} approved. Created enrollment {student_course.id}')

    def action_reject(self):
        """Reject request with reason"""
        for record in self:
            if record.state not in ['submitted', 'pending']:
                raise UserError(_('Only submitted or pending requests can be rejected.'))
            
            if not record.rejection_reason:
                raise UserError(_('Please provide a rejection reason.'))
            
            record.write({'state': 'rejected'})
            
            # Send rejection email
            self._send_rejection_email()
            
            record.message_post(
                body=_('Enrollment request rejected. Reason: %s') % record.rejection_reason,
                message_type='notification'
            )
            
            _logger.info(f'Enrollment request {record.name} rejected')

    def action_set_pending(self):
        """Set request to pending review"""
        for record in self:
            if record.state != 'submitted':
                raise UserError(_('Only submitted requests can be set to pending.'))
            
            record.write({'state': 'pending'})
            
            record.message_post(
                body=_('Request set to pending review by %s.') % self.env.user.name,
                message_type='notification'
            )

    def _create_student_course(self):
        """Create op.student.course enrollment record"""
        self.ensure_one()
        
        enrollment_vals = {
            'student_id': self.student_id.id,
            'course_id': self.course_id.id,
            'state': 'running',
        }
        
        if self.batch_id:
            enrollment_vals['batch_id'] = self.batch_id.id
        
        student_course = self.env['op.student.course'].create(enrollment_vals)
        
        _logger.info(f'Created student course enrollment {student_course.id} for request {self.name}')
        
        return student_course

    def _send_submission_notification(self):
        """Send notification to admins when request is submitted"""
        self.ensure_one()
        
        try:
            # Get manager and faculty groups
            manager_group = self.env.ref('openeducat_core.group_op_back_office_admin', raise_if_not_found=False)
            faculty_group = self.env.ref('openeducat_core.group_op_faculty', raise_if_not_found=False)
            
            if not manager_group and not faculty_group:
                _logger.warning('Manager or Faculty group not found, skipping admin notification')
                return
            
            # Get all users that belong to these groups
            group_ids = []
            if manager_group:
                group_ids.append(manager_group.id)
            if faculty_group:
                group_ids.append(faculty_group.id)
            
            if group_ids:
                admin_users = self.env['res.users'].search([
                    ('groups_id', 'in', group_ids)
                ])
                
                # Send notification
                if admin_users:
                    partner_ids = admin_users.mapped('partner_id').ids
                    if partner_ids:
                        self.message_subscribe(partner_ids=partner_ids)
                        self.message_post(
                            body=_('New enrollment request submitted: %s - Course: %s') % (
                                self.student_id.name, self.course_id.name
                            ),
                            message_type='notification',
                            partner_ids=partner_ids
                        )
        except Exception as e:
            _logger.error(f'Error sending admin notification: {str(e)}')

    def _send_approval_email(self):
        """Send approval email to student"""
        self.ensure_one()
        
        template = self.env.ref('student_enrollment_portal.email_template_enrollment_request_approved', raise_if_not_found=False)
        if template:
            template.send_mail(self.id, force_send=True)

    def _send_rejection_email(self):
        """Send rejection email to student"""
        self.ensure_one()
        
        template = self.env.ref('student_enrollment_portal.email_template_enrollment_request_rejected', raise_if_not_found=False)
        if template:
            template.send_mail(self.id, force_send=True)

