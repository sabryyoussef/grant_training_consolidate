# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class MotakamelPricing(models.Model):
    _name = 'motakamel.pricing'
    _description = 'Program Pricing'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'program_id, list_price'
    _rec_name = 'pricing_name'

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
    
    pricing_name = fields.Char(
        string='Pricing Plan Name',
        required=True,
        help="Name of this pricing plan (e.g., Standard, Early Bird, Corporate)"
    )
    
    # ========================================================
    # PRICING
    # ========================================================
    
    list_price = fields.Monetary(
        string='List Price',
        required=True,
        currency_field='currency_id',
        tracking=True,
        help="Standard/regular price"
    )
    
    discount_price = fields.Monetary(
        string='Discounted Price',
        currency_field='currency_id',
        tracking=True,
        help="Promotional or discounted price"
    )
    
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        required=True,
        default=lambda self: self.env.company.currency_id
    )
    
    discount_percentage = fields.Float(
        string='Discount %',
        compute='_compute_discount_percentage',
        store=True
    )
    
    @api.depends('list_price', 'discount_price')
    def _compute_discount_percentage(self):
        for record in self:
            if record.list_price and record.discount_price:
                record.discount_percentage = ((record.list_price - record.discount_price) / record.list_price) * 100
            else:
                record.discount_percentage = 0.0
    
    final_price = fields.Monetary(
        string='Final Price',
        compute='_compute_final_price',
        store=True,
        currency_field='currency_id'
    )
    
    @api.depends('list_price', 'discount_price')
    def _compute_final_price(self):
        for record in self:
            record.final_price = record.discount_price if record.discount_price else record.list_price
    
    # ========================================================
    # INSTALLMENTS
    # ========================================================
    
    installments_allowed = fields.Boolean(
        string='Installments Allowed',
        default=False,
        help="Whether payment can be made in installments"
    )
    
    installment_terms = fields.Text(
        string='Installment Terms',
        help="Detailed terms for installment payments (number of payments, schedule, etc.)"
    )
    
    number_of_installments = fields.Integer(
        string='Number of Installments',
        help="How many installment payments are allowed"
    )
    
    installment_amount = fields.Monetary(
        string='Installment Amount',
        compute='_compute_installment_amount',
        currency_field='currency_id'
    )
    
    @api.depends('final_price', 'number_of_installments')
    def _compute_installment_amount(self):
        for record in self:
            if record.number_of_installments and record.number_of_installments > 0:
                record.installment_amount = record.final_price / record.number_of_installments
            else:
                record.installment_amount = 0.0
    
    # ========================================================
    # BULK & CORPORATE PRICING
    # ========================================================
    
    corporate_bulk_discount = fields.Float(
        string='Corporate Bulk Discount (%)',
        help="Additional discount for corporate bulk purchases"
    )
    
    min_bulk_quantity = fields.Integer(
        string='Minimum Bulk Quantity',
        help="Minimum number of participants for bulk discount"
    )
    
    bulk_price = fields.Monetary(
        string='Bulk Price Per Person',
        currency_field='currency_id',
        help="Price per person for bulk purchases"
    )
    
    # ========================================================
    # PRICING TYPE & VALIDITY
    # ========================================================
    
    pricing_type = fields.Selection([
        ('standard', 'Standard'),
        ('early_bird', 'Early Bird'),
        ('corporate', 'Corporate'),
        ('government', 'Government'),
        ('student', 'Student'),
        ('group', 'Group Discount'),
        ('promotional', 'Promotional'),
    ], string='Pricing Type', required=True, default='standard')
    
    valid_from = fields.Date(
        string='Valid From',
        default=fields.Date.today
    )
    
    valid_to = fields.Date(
        string='Valid To',
        help="Leave empty for no expiry"
    )
    
    is_active_pricing = fields.Boolean(
        string='Is Active',
        compute='_compute_is_active_pricing',
        store=True
    )
    
    @api.depends('valid_from', 'valid_to', 'active')
    def _compute_is_active_pricing(self):
        today = fields.Date.today()
        for record in self:
            if not record.active:
                record.is_active_pricing = False
            elif not record.valid_to:
                record.is_active_pricing = record.valid_from <= today
            else:
                record.is_active_pricing = record.valid_from <= today <= record.valid_to
    
    # ========================================================
    # TAX & REFUND
    # ========================================================
    
    tax_applicable = fields.Boolean(
        string='Tax Applicable',
        default=True,
        help="Whether tax/VAT is applicable to this price"
    )
    
    tax_ids = fields.Many2many(
        'account.tax',
        'motakamel_pricing_tax_rel',
        'pricing_id',
        'tax_id',
        string='Taxes',
        help="Applicable taxes"
    )
    
    refund_policy = fields.Selection([
        ('full', 'Full Refund'),
        ('partial', 'Partial Refund'),
        ('no_refund', 'No Refund'),
        ('conditional', 'Conditional Refund'),
    ], string='Refund Policy', default='conditional')
    
    refund_policy_details = fields.Text(
        string='Refund Policy Details',
        help="Detailed refund terms and conditions"
    )
    
    # ========================================================
    # WHAT'S INCLUDED
    # ========================================================
    
    includes_exam_fee = fields.Boolean(
        string='Includes Exam Fee',
        default=True
    )
    
    includes_materials = fields.Boolean(
        string='Includes Materials',
        default=True
    )
    
    includes_certificate = fields.Boolean(
        string='Includes Certificate',
        default=True
    )
    
    additional_inclusions = fields.Text(
        string='Additional Inclusions',
        help="Other items included in the price"
    )
    
    # ========================================================
    # STATUS
    # ========================================================
    
    active = fields.Boolean(
        string='Active',
        default=True
    )
    
    is_default = fields.Boolean(
        string='Default Pricing',
        default=False,
        help="Mark as default pricing for this program"
    )
    
    notes = fields.Text(
        string='Notes'
    )
    
    # ========================================================
    # CONSTRAINTS
    # ========================================================
    
    @api.constrains('list_price', 'discount_price')
    def _check_prices(self):
        for record in self:
            if record.list_price < 0:
                raise ValidationError(_('List price cannot be negative.'))
            if record.discount_price and record.discount_price > record.list_price:
                raise ValidationError(_('Discount price cannot exceed list price.'))
    
    @api.constrains('valid_from', 'valid_to')
    def _check_validity_dates(self):
        for record in self:
            if record.valid_to and record.valid_from:
                if record.valid_to < record.valid_from:
                    raise ValidationError(_('Valid To date must be after Valid From date.'))
    
    @api.constrains('is_default')
    def _check_default_pricing(self):
        for record in self:
            if record.is_default:
                # Ensure only one default pricing per program
                other_default = self.search([
                    ('program_id', '=', record.program_id.id),
                    ('is_default', '=', True),
                    ('id', '!=', record.id)
                ])
                if other_default:
                    raise ValidationError(_('Only one default pricing is allowed per program.'))
    
    # ========================================================
    # METHODS
    # ========================================================
    
    def name_get(self):
        result = []
        for record in self:
            name = f"{record.pricing_name} - {record.currency_id.symbol}{record.final_price:,.2f}"
            result.append((record.id, name))
        return result

