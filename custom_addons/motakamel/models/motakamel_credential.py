# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class MotakamelCredential(models.Model):
    _name = 'motakamel.credential'
    _description = 'Program Credentials & Certificates'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'program_id, id desc'
    _rec_name = 'credential_name'

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
    
    credential_name = fields.Char(
        string='Credential Name',
        required=True,
        help="Name of the certificate/credential"
    )
    
    # ========================================================
    # CERTIFICATE INFORMATION
    # ========================================================
    
    certificate_issued = fields.Boolean(
        string='Certificate Issued',
        default=True,
        help="Whether a certificate is issued upon completion"
    )
    
    certificate_type = fields.Selection([
        ('professional', 'Professional Certification'),
        ('completion', 'Certificate of Completion'),
        ('achievement', 'Certificate of Achievement'),
        ('attendance', 'Certificate of Attendance'),
        ('competency', 'Competency Certificate'),
        ('diploma', 'Diploma'),
        ('micro_credential', 'Micro-Credential'),
        ('digital_badge', 'Digital Badge'),
    ], string='Certificate Type', required=True, default='professional')
    
    certificate_serial_format = fields.Char(
        string='Certificate Serial Format',
        help="Format for certificate serial numbers (e.g., CERT-{YEAR}-{NUMBER})"
    )
    
    # ========================================================
    # ISSUING AUTHORITY
    # ========================================================
    
    issuing_authority = fields.Char(
        string='Issuing Authority',
        required=True,
        help="Organization/body that issues the certificate"
    )
    
    issuing_authority_logo = fields.Binary(
        string='Authority Logo',
        attachment=True
    )
    
    co_branded = fields.Boolean(
        string='Co-Branded Certificate',
        default=False,
        help="Whether certificate is co-branded with partners"
    )
    
    partner_organizations = fields.Text(
        string='Partner Organizations',
        help="List of partner organizations on the certificate"
    )
    
    # ========================================================
    # DELIVERY & TIMELINE
    # ========================================================
    
    certificate_delivery_days = fields.Integer(
        string='Delivery Time (Days)',
        default=7,
        help="Number of days to deliver certificate after completion"
    )
    
    delivery_method = fields.Selection([
        ('digital', 'Digital (Email/Download)'),
        ('physical', 'Physical (Mail)'),
        ('both', 'Both Digital & Physical'),
        ('blockchain', 'Blockchain Verified'),
    ], string='Delivery Method', default='digital')
    
    # ========================================================
    # VALIDITY & RENEWAL
    # ========================================================
    
    renewal_required = fields.Boolean(
        string='Renewal Required',
        default=False,
        help="Whether the certificate needs to be renewed"
    )
    
    renewal_cycle_years = fields.Integer(
        string='Renewal Cycle (Years)',
        help="Number of years before renewal is required"
    )
    
    continuing_education_required = fields.Boolean(
        string='Continuing Education Required',
        default=False,
        help="Whether continuing education is needed for renewal"
    )
    
    ce_hours_required = fields.Float(
        string='CE Hours Required',
        help="Continuing education hours needed for renewal"
    )
    
    # ========================================================
    # VERIFICATION
    # ========================================================
    
    verification_available = fields.Boolean(
        string='Verification Available',
        default=True,
        help="Whether certificate can be verified online"
    )
    
    verification_url = fields.Char(
        string='Verification URL',
        help="URL for online certificate verification"
    )
    
    verification_method = fields.Selection([
        ('qr_code', 'QR Code'),
        ('serial_number', 'Serial Number Lookup'),
        ('blockchain', 'Blockchain'),
        ('api', 'API Integration'),
        ('manual', 'Manual Verification'),
    ], string='Verification Method', default='serial_number')
    
    # ========================================================
    # DIGITAL CREDENTIALS
    # ========================================================
    
    digital_badge_available = fields.Boolean(
        string='Digital Badge Available',
        default=False,
        help="Whether a digital badge is issued (e.g., Open Badges)"
    )
    
    badge_platform = fields.Selection([
        ('credly', 'Credly'),
        ('badgr', 'Badgr'),
        ('accredible', 'Accredible'),
        ('open_badges', 'Open Badges'),
        ('custom', 'Custom Platform'),
    ], string='Badge Platform')
    
    linkedin_integration = fields.Boolean(
        string='LinkedIn Integration',
        default=False,
        help="Can be added to LinkedIn profile"
    )
    
    # ========================================================
    # CERTIFICATE TEMPLATE
    # ========================================================
    
    certificate_template = fields.Binary(
        string='Certificate Template',
        attachment=True,
        help="Upload certificate template file"
    )
    
    certificate_template_filename = fields.Char(
        string='Template Filename'
    )
    
    certificate_sample = fields.Binary(
        string='Certificate Sample',
        attachment=True,
        help="Sample certificate for preview"
    )
    
    certificate_sample_filename = fields.Char(
        string='Sample Filename'
    )
    
    # ========================================================
    # ADDITIONAL INFORMATION
    # ========================================================
    
    transcript_available = fields.Boolean(
        string='Transcript Available',
        default=False,
        help="Whether a transcript of courses/modules is available"
    )
    
    wallet_card_available = fields.Boolean(
        string='Wallet Card Available',
        default=False,
        help="Whether a physical wallet card is provided"
    )
    
    certificate_features = fields.Text(
        string='Certificate Features',
        help="Special features of the certificate (embossed seal, hologram, etc.)"
    )
    
    active = fields.Boolean(
        string='Active',
        default=True
    )
    
    notes = fields.Text(
        string='Notes'
    )
    
    # ========================================================
    # COMPUTED FIELDS
    # ========================================================
    
    validity_period = fields.Char(
        string='Validity Period',
        compute='_compute_validity_period'
    )
    
    @api.depends('renewal_required', 'renewal_cycle_years')
    def _compute_validity_period(self):
        for record in self:
            if record.renewal_required and record.renewal_cycle_years:
                record.validity_period = f"{record.renewal_cycle_years} year(s)"
            elif record.renewal_required:
                record.validity_period = "Renewal Required"
            else:
                record.validity_period = "Lifetime"
    
    # ========================================================
    # METHODS
    # ========================================================
    
    def name_get(self):
        result = []
        for record in self:
            name = record.credential_name
            cert_type = dict(self._fields['certificate_type'].selection).get(record.certificate_type)
            if cert_type:
                name = f"{name} ({cert_type})"
            result.append((record.id, name))
        return result

