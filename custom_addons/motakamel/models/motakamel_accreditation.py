# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class MotakamelAccreditation(models.Model):
    _name = 'motakamel.accreditation'
    _description = 'Program Accreditation'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'program_id, id desc'
    _rec_name = 'accreditation_code'

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
    
    # ========================================================
    # ACCREDITATION INFORMATION
    # ========================================================
    
    international_accreditation_body = fields.Char(
        string='International Accreditation Body',
        help="Name of international accreditation organization (e.g., PMI, IIBA, AXELOS)"
    )
    
    local_accreditation_body = fields.Char(
        string='Local Accreditation Body',
        help="Name of local/national accreditation organization"
    )
    
    accreditation_code = fields.Char(
        string='Accreditation Code',
        required=True,
        help="Unique accreditation identifier/code"
    )
    
    accreditation_valid_from = fields.Date(
        string='Valid From',
        required=True,
        default=fields.Date.today,
        tracking=True
    )
    
    accreditation_valid_to = fields.Date(
        string='Valid To',
        tracking=True,
        help="Expiry date of accreditation (leave empty if perpetual)"
    )
    
    certificate_type = fields.Selection([
        ('professional', 'Professional Certification'),
        ('completion', 'Certificate of Completion'),
        ('achievement', 'Certificate of Achievement'),
        ('attendance', 'Certificate of Attendance'),
        ('competency', 'Competency Certificate'),
        ('diploma', 'Diploma'),
        ('degree', 'Degree'),
    ], string='Certificate Type', required=True, default='professional')
    
    verification_url = fields.Char(
        string='Verification URL',
        help="URL for online certificate verification"
    )
    
    certificate_sample_file = fields.Binary(
        string='Certificate Sample',
        attachment=True,
        help="Upload a sample certificate image/PDF"
    )
    
    certificate_sample_filename = fields.Char(
        string='Certificate Sample Filename'
    )
    
    # ========================================================
    # ADDITIONAL INFORMATION
    # ========================================================
    
    accreditation_level = fields.Selection([
        ('international', 'International'),
        ('regional', 'Regional'),
        ('national', 'National'),
        ('local', 'Local'),
    ], string='Accreditation Level', default='national')
    
    is_primary = fields.Boolean(
        string='Primary Accreditation',
        default=False,
        help="Mark as the main accreditation for this program"
    )
    
    active = fields.Boolean(
        string='Active',
        default=True
    )
    
    notes = fields.Text(
        string='Notes',
        help="Additional notes about this accreditation"
    )
    
    # ========================================================
    # COMPUTED FIELDS
    # ========================================================
    
    is_valid = fields.Boolean(
        string='Is Valid',
        compute='_compute_is_valid',
        store=True,
        help="Whether the accreditation is currently valid"
    )
    
    @api.depends('accreditation_valid_from', 'accreditation_valid_to')
    def _compute_is_valid(self):
        today = fields.Date.today()
        for record in self:
            if not record.accreditation_valid_to:
                # Perpetual accreditation
                record.is_valid = record.accreditation_valid_from <= today
            else:
                record.is_valid = record.accreditation_valid_from <= today <= record.accreditation_valid_to
    
    days_until_expiry = fields.Integer(
        string='Days Until Expiry',
        compute='_compute_days_until_expiry'
    )
    
    @api.depends('accreditation_valid_to')
    def _compute_days_until_expiry(self):
        today = fields.Date.today()
        for record in self:
            if record.accreditation_valid_to:
                delta = record.accreditation_valid_to - today
                record.days_until_expiry = delta.days
            else:
                record.days_until_expiry = 0
    
    # ========================================================
    # CONSTRAINTS
    # ========================================================
    
    @api.constrains('accreditation_valid_from', 'accreditation_valid_to')
    def _check_validity_dates(self):
        for record in self:
            if record.accreditation_valid_to and record.accreditation_valid_from:
                if record.accreditation_valid_to < record.accreditation_valid_from:
                    raise ValidationError(_('Valid To date must be after Valid From date.'))
    
    @api.constrains('is_primary')
    def _check_primary_accreditation(self):
        for record in self:
            if record.is_primary:
                # Ensure only one primary accreditation per program
                other_primary = self.search([
                    ('program_id', '=', record.program_id.id),
                    ('is_primary', '=', True),
                    ('id', '!=', record.id)
                ])
                if other_primary:
                    raise ValidationError(_('Only one primary accreditation is allowed per program.'))
    
    # ========================================================
    # METHODS
    # ========================================================
    
    def name_get(self):
        result = []
        for record in self:
            name = record.accreditation_code
            if record.international_accreditation_body:
                name = f"{record.international_accreditation_body} - {name}"
            elif record.local_accreditation_body:
                name = f"{record.local_accreditation_body} - {name}"
            result.append((record.id, name))
        return result

