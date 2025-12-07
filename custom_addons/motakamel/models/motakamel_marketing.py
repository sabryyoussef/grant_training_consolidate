# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class MotakamelMarketing(models.Model):
    _name = 'motakamel.marketing'
    _description = 'Program Marketing & SEO'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'program_id, id desc'
    _rec_name = 'campaign_name'

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
    
    campaign_name = fields.Char(
        string='Campaign Name',
        required=True,
        help="Name of this marketing campaign"
    )
    
    # ========================================================
    # WEBSITE VISIBILITY
    # ========================================================
    
    featured_on_homepage = fields.Boolean(
        string='Featured on Homepage',
        default=False,
        tracking=True,
        help="Display this program prominently on the homepage"
    )
    
    featured_priority = fields.Integer(
        string='Featured Priority',
        default=10,
        help="Priority for featured programs (lower = higher priority)"
    )
    
    show_on_catalog = fields.Boolean(
        string='Show on Catalog',
        default=True,
        help="Display in public course catalog"
    )
    
    # ========================================================
    # SEO OPTIMIZATION
    # ========================================================
    
    seo_title = fields.Char(
        string='SEO Title',
        translate=True,
        help="Page title for search engines (50-60 characters recommended)"
    )
    
    seo_description = fields.Text(
        string='SEO Meta Description',
        translate=True,
        help="Meta description for search engines (150-160 characters recommended)"
    )
    
    seo_keywords = fields.Char(
        string='SEO Keywords',
        help="Comma-separated keywords for SEO"
    )
    
    canonical_url = fields.Char(
        string='Canonical URL',
        help="Canonical URL for this program page"
    )
    
    og_image = fields.Binary(
        string='Open Graph Image',
        attachment=True,
        help="Image for social media sharing (1200x630px recommended)"
    )
    
    og_image_filename = fields.Char(
        string='OG Image Filename'
    )
    
    # ========================================================
    # LANDING PAGE
    # ========================================================
    
    landing_page_url = fields.Char(
        string='Landing Page URL',
        help="Custom landing page URL for this program"
    )
    
    landing_page_template = fields.Selection([
        ('default', 'Default Template'),
        ('modern', 'Modern Template'),
        ('minimal', 'Minimal Template'),
        ('corporate', 'Corporate Template'),
        ('custom', 'Custom Template'),
    ], string='Landing Page Template', default='default')
    
    call_to_action_text = fields.Char(
        string='CTA Button Text',
        default='Enroll Now',
        help="Text for the call-to-action button"
    )
    
    call_to_action_url = fields.Char(
        string='CTA URL',
        help="URL for the call-to-action button"
    )
    
    # ========================================================
    # PROMOTIONAL MATERIALS
    # ========================================================
    
    brochure_pdf = fields.Binary(
        string='Program Brochure (PDF)',
        attachment=True,
        help="Downloadable program brochure"
    )
    
    brochure_pdf_filename = fields.Char(
        string='Brochure Filename'
    )
    
    promo_video_url = fields.Char(
        string='Promotional Video URL',
        help="YouTube, Vimeo, or direct video URL"
    )
    
    promo_images = fields.Many2many(
        'ir.attachment',
        'motakamel_marketing_image_rel',
        'marketing_id',
        'attachment_id',
        string='Promotional Images',
        help="Gallery of promotional images"
    )
    
    testimonial_video_url = fields.Char(
        string='Testimonial Video URL',
        help="Video testimonials from past participants"
    )
    
    # ========================================================
    # LEAD GENERATION
    # ========================================================
    
    whatsapp_lead_link = fields.Char(
        string='WhatsApp Lead Link',
        help="WhatsApp link for direct inquiries (e.g., wa.me/1234567890)"
    )
    
    lead_form_enabled = fields.Boolean(
        string='Lead Form Enabled',
        default=True,
        help="Enable lead capture form on program page"
    )
    
    lead_magnet_type = fields.Selection([
        ('brochure', 'Download Brochure'),
        ('sample', 'Free Sample Lesson'),
        ('consultation', 'Free Consultation'),
        ('webinar', 'Free Webinar'),
        ('ebook', 'Free E-Book'),
        ('none', 'None'),
    ], string='Lead Magnet', default='brochure')
    
    lead_magnet_file = fields.Binary(
        string='Lead Magnet File',
        attachment=True,
        help="File to be sent to leads"
    )
    
    lead_magnet_filename = fields.Char(
        string='Lead Magnet Filename'
    )
    
    # ========================================================
    # EMAIL MARKETING
    # ========================================================
    
    email_campaign_active = fields.Boolean(
        string='Email Campaign Active',
        default=False,
        help="Whether email marketing campaign is active"
    )
    
    email_template_id = fields.Many2one(
        'mail.template',
        string='Email Template',
        help="Email template for this program"
    )
    
    drip_campaign_enabled = fields.Boolean(
        string='Drip Campaign Enabled',
        default=False,
        help="Enable automated drip email campaign"
    )
    
    # ========================================================
    # SOCIAL MEDIA
    # ========================================================
    
    facebook_post_text = fields.Text(
        string='Facebook Post',
        help="Pre-written Facebook post for sharing"
    )
    
    twitter_post_text = fields.Char(
        string='Twitter/X Post',
        help="Pre-written tweet (280 characters max)"
    )
    
    linkedin_post_text = fields.Text(
        string='LinkedIn Post',
        help="Pre-written LinkedIn post for sharing"
    )
    
    instagram_caption = fields.Text(
        string='Instagram Caption',
        help="Caption for Instagram posts"
    )
    
    hashtags = fields.Char(
        string='Hashtags',
        help="Recommended hashtags for social media"
    )
    
    # ========================================================
    # ANALYTICS & TRACKING
    # ========================================================
    
    utm_source = fields.Char(
        string='UTM Source',
        help="UTM source parameter for tracking"
    )
    
    utm_medium = fields.Char(
        string='UTM Medium',
        help="UTM medium parameter for tracking"
    )
    
    utm_campaign = fields.Char(
        string='UTM Campaign',
        help="UTM campaign parameter for tracking"
    )
    
    google_analytics_id = fields.Char(
        string='Google Analytics ID',
        help="Specific GA tracking ID for this program"
    )
    
    facebook_pixel_id = fields.Char(
        string='Facebook Pixel ID',
        help="Facebook Pixel ID for conversion tracking"
    )
    
    # ========================================================
    # CAMPAIGN PERFORMANCE
    # ========================================================
    
    campaign_start_date = fields.Date(
        string='Campaign Start Date'
    )
    
    campaign_end_date = fields.Date(
        string='Campaign End Date'
    )
    
    campaign_budget = fields.Monetary(
        string='Campaign Budget',
        currency_field='currency_id'
    )
    
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        default=lambda self: self.env.company.currency_id
    )
    
    leads_generated = fields.Integer(
        string='Leads Generated',
        default=0,
        help="Number of leads generated from this campaign"
    )
    
    conversions = fields.Integer(
        string='Conversions',
        default=0,
        help="Number of enrollments from this campaign"
    )
    
    conversion_rate = fields.Float(
        string='Conversion Rate (%)',
        compute='_compute_conversion_rate',
        store=True
    )
    
    @api.depends('leads_generated', 'conversions')
    def _compute_conversion_rate(self):
        for record in self:
            if record.leads_generated:
                record.conversion_rate = (record.conversions / record.leads_generated) * 100
            else:
                record.conversion_rate = 0.0
    
    # ========================================================
    # STATUS
    # ========================================================
    
    active = fields.Boolean(
        string='Active',
        default=True
    )
    
    campaign_status = fields.Selection([
        ('draft', 'Draft'),
        ('scheduled', 'Scheduled'),
        ('active', 'Active'),
        ('paused', 'Paused'),
        ('completed', 'Completed'),
    ], string='Campaign Status', default='draft', tracking=True)
    
    notes = fields.Text(
        string='Notes'
    )
    
    # ========================================================
    # METHODS
    # ========================================================
    
    def action_activate_campaign(self):
        self.write({'campaign_status': 'active', 'campaign_start_date': fields.Date.today()})
    
    def action_pause_campaign(self):
        self.write({'campaign_status': 'paused'})
    
    def action_complete_campaign(self):
        self.write({'campaign_status': 'completed', 'campaign_end_date': fields.Date.today()})
    
    def name_get(self):
        result = []
        for record in self:
            name = record.campaign_name
            if record.campaign_status:
                status = dict(self._fields['campaign_status'].selection).get(record.campaign_status)
                name = f"{name} ({status})"
            result.append((record.id, name))
        return result

