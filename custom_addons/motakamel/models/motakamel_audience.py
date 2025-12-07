# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class MotakamelAudience(models.Model):
    _name = 'motakamel.audience'
    _description = 'Program Target Audience'
    _order = 'program_id, id desc'

    # ========================================================
    # RELATIONSHIP
    # ========================================================
    
    program_id = fields.Many2one(
        'motakamel.program',
        string='Program',
        required=True,
        ondelete='cascade',
        index=True
    )
    
    # ========================================================
    # TARGET SECTORS
    # ========================================================
    
    target_sector = fields.Selection([
        ('public', 'Public Sector'),
        ('private', 'Private Sector'),
        ('nonprofit', 'Non-Profit Sector'),
        ('individual', 'Individuals'),
        ('government', 'Government Entities'),
        ('corporate', 'Corporate'),
        ('sme', 'Small & Medium Enterprises'),
        ('startup', 'Startups'),
        ('education', 'Educational Institutions'),
        ('healthcare', 'Healthcare'),
        ('all', 'All Sectors'),
    ], string='Target Sector', required=True, default='all')
    
    # ========================================================
    # ELIGIBLE PARTICIPANTS
    # ========================================================
    
    eligible_job_titles = fields.Text(
        string='Eligible Job Titles',
        help="List of job titles suitable for this program (one per line)"
    )
    
    career_level = fields.Selection([
        ('entry', 'Entry Level'),
        ('junior', 'Junior (1-3 years)'),
        ('mid', 'Mid-Level (3-5 years)'),
        ('senior', 'Senior (5-10 years)'),
        ('lead', 'Lead/Principal (10+ years)'),
        ('executive', 'Executive/C-Level'),
        ('all', 'All Levels'),
    ], string='Career Level', default='all')
    
    industry_focus = fields.Many2many(
        'motakamel.industry',
        'motakamel_audience_industry_rel',
        'audience_id',
        'industry_id',
        string='Industry Focus',
        help="Specific industries this program targets"
    )
    
    # ========================================================
    # PREREQUISITES
    # ========================================================
    
    prerequisites_required = fields.Boolean(
        string='Prerequisites Required',
        default=False,
        help="Whether prerequisites are mandatory for enrollment"
    )
    
    prerequisites_description = fields.Text(
        string='Prerequisites Description',
        help="Detailed description of prerequisites (education, experience, certifications)"
    )
    
    min_education_level = fields.Selection([
        ('high_school', 'High School'),
        ('diploma', 'Diploma'),
        ('bachelor', 'Bachelor Degree'),
        ('master', 'Master Degree'),
        ('phd', 'PhD'),
        ('none', 'No Requirement'),
    ], string='Minimum Education Level', default='none')
    
    min_experience_years = fields.Integer(
        string='Minimum Experience (Years)',
        default=0,
        help="Minimum years of professional experience required"
    )
    
    required_certifications = fields.Text(
        string='Required Certifications',
        help="List any prerequisite certifications"
    )
    
    # ========================================================
    # ADDITIONAL INFORMATION
    # ========================================================
    
    age_restriction = fields.Char(
        string='Age Restriction',
        help="Age requirements if any (e.g., 18+, 21+)"
    )
    
    language_requirements = fields.Char(
        string='Language Requirements',
        help="Required language proficiency (e.g., English B2, Arabic Native)"
    )
    
    technical_requirements = fields.Text(
        string='Technical Requirements',
        help="Technical skills or equipment needed"
    )
    
    active = fields.Boolean(
        string='Active',
        default=True
    )
    
    notes = fields.Text(
        string='Notes'
    )
    
    # ========================================================
    # METHODS
    # ========================================================
    
    def name_get(self):
        result = []
        for record in self:
            name = dict(self._fields['target_sector'].selection).get(record.target_sector)
            if record.career_level and record.career_level != 'all':
                career = dict(self._fields['career_level'].selection).get(record.career_level)
                name = f"{name} - {career}"
            result.append((record.id, name))
        return result


class MotakamelIndustry(models.Model):
    _name = 'motakamel.industry'
    _description = 'Industry Category'
    _order = 'name'

    name = fields.Char(
        string='Industry Name',
        required=True,
        translate=True
    )
    
    code = fields.Char(
        string='Industry Code',
        help="Short code for the industry"
    )
    
    description = fields.Text(
        string='Description',
        translate=True
    )
    
    active = fields.Boolean(
        string='Active',
        default=True
    )
    
    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Industry name must be unique!'),
    ]

