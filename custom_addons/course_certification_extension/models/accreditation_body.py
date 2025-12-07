# -*- coding: utf-8 -*-

from odoo import models, fields


class AccreditationBody(models.Model):
    _name = 'course.accreditation.body'
    _description = 'Course Accreditation Body'
    _order = 'sequence, name'

    name = fields.Char(
        string='Name',
        required=True,
        help='Name of the accreditation body'
    )
    
    name_arabic = fields.Char(
        string='Name (Arabic)',
        help='Arabic name of the accreditation body'
    )
    
    logo = fields.Image(
        string='Logo',
        max_width=512,
        max_height=512,
        help='Logo of the accreditation body'
    )
    
    website = fields.Char(
        string='Website',
        help='Official website URL'
    )
    
    description = fields.Text(
        string='Description',
        help='Description of the accreditation body'
    )
    
    active = fields.Boolean(
        string='Active',
        default=True
    )
    
    sequence = fields.Integer(
        string='Sequence',
        default=10,
        help='Used to order accreditation bodies'
    )
    
    course_ids = fields.Many2many(
        'slide.channel',
        string='Courses',
        help='Courses accredited by this body'
    )

