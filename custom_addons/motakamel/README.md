# Motakamel - Enterprise Training & Certification Platform

## Overview

**Motakamel** is a comprehensive, production-ready Odoo 19 module for managing professional certifications and training programs. It provides a unified platform for courses, certifications, accreditations, pricing, delivery, credentials, and marketing.

## Features

### 📚 Program Management
- Complete training program lifecycle
- Multi-language support (Arabic & English)
- Program categorization and leveling
- Provider management
- Approval workflows
- Website publishing

### 🏆 Accreditation Tracking
- International & local accreditations
- Validity period tracking
- Certificate type management
- Verification URL support
- Sample certificate uploads
- Primary accreditation designation

### 👥 Target Audience Management
- Sector targeting (public, private, non-profit, etc.)
- Career level specification
- Industry focus
- Prerequisites management
- Education and experience requirements

### 📅 Delivery Management
- Multiple training modes (online, on-site, hybrid)
- Scheduling and duration tracking
- Exam management
- Study materials tracking
- Venue management
- Capacity and enrollment tracking
- Registration status management

### 💰 Flexible Pricing
- Multiple pricing plans per program
- Discount management
- Installment support
- Corporate bulk pricing
- Validity periods
- Tax configuration
- Refund policies

### 📜 Credential System
- Certificate issuance management
- Multiple certificate types
- Issuing authority tracking
- Delivery timeline management
- Renewal management
- Digital badge support
- Verification system
- LinkedIn integration

### 📢 Marketing & SEO
- Homepage featuring
- SEO optimization (title, description, keywords)
- Landing page management
- Promotional materials (brochures, videos)
- Lead generation tools
- WhatsApp integration
- Email campaigns
- Social media content
- UTM tracking
- Campaign performance analytics

## Technical Specifications

### Requirements
- Odoo 19.0 (compatible with 16-19)
- Python 3.8+
- PostgreSQL 12+

### Dependencies
- `base`
- `website`
- `crm`
- `sale`
- `website_sale`

### Architecture
- Clean ORM design
- Upgrade-safe structure
- Full referential integrity
- Comprehensive access control
- Website-ready templates
- CRM-ready integration

## Installation

1. **Copy Module**
   ```bash
   cp -r motakamel /path/to/odoo/addons/
   ```

2. **Update Apps List**
   - Go to Apps menu
   - Click "Update Apps List"

3. **Install Module**
   - Search for "Motakamel"
   - Click "Install"

4. **Configure Access Rights**
   - Go to Settings → Users & Companies → Users
   - Assign appropriate Motakamel roles:
     - **Administrator**: Full access
     - **Manager**: Create, edit, approve programs
     - **Sales**: View programs, create leads
     - **User**: View programs

## Usage

### Creating a Program

1. Go to **Motakamel → Programs**
2. Click **Create**
3. Fill in program details:
   - Program Name (English & Arabic)
   - Program Code
   - Category and Level
   - Provider Information
4. Add descriptions and objectives
5. Click **Save**

### Adding Accreditations

1. Open a program
2. Go to **Accreditations** tab
3. Click **Add a line**
4. Fill in accreditation details
5. Upload certificate sample

### Setting Up Delivery

1. Open a program
2. Go to **Delivery** tab
3. Click **Add a line**
4. Configure:
   - Training mode
   - Schedule
   - Duration
   - Capacity

### Configuring Pricing

1. Open a program
2. Go to **Pricing** tab
3. Click **Add a line**
4. Set:
   - Pricing plan name
   - List and discount prices
   - Installment options
   - Validity period

### Publishing to Website

1. Complete program setup
2. Click **Submit for Review**
3. Manager clicks **Approve**
4. Click **Publish**
5. Program appears on `/programs`

## Access Control

### User Groups

| Group | Permissions |
|-------|-------------|
| **Public** | View published programs on website |
| **Portal** | View published programs (registered users) |
| **User** | View all active programs |
| **Sales** | View programs, create leads |
| **Manager** | Create, edit, approve programs |
| **Administrator** | Full access, delete programs |

### Record Rules

- Public: Only published, public-scope programs
- Portal: Published programs (public + registered scope)
- Users: All active programs
- Managers: All programs (no delete)
- Admins: Full access

## Data Models

### Core Models

1. **motakamel.program** - Main program model
2. **motakamel.accreditation** - Accreditations
3. **motakamel.audience** - Target audience
4. **motakamel.delivery** - Delivery options
5. **motakamel.pricing** - Pricing plans
6. **motakamel.credential** - Credentials
7. **motakamel.marketing** - Marketing campaigns
8. **motakamel.industry** - Industry categories

### Relationships

```
motakamel.program (1) → (Many) motakamel.accreditation
motakamel.program (1) → (Many) motakamel.audience
motakamel.program (1) → (Many) motakamel.delivery
motakamel.program (1) → (Many) motakamel.pricing
motakamel.program (1) → (Many) motakamel.credential
motakamel.program (1) → (Many) motakamel.marketing
```

## API / Integration

### Website Routes

- `/programs` - Program catalog
- `/programs/<id>` - Program detail
- `/programs/category/<category>` - Filter by category

### CRM Integration

Programs are ready for CRM lead integration:
- Lead capture forms
- WhatsApp links
- Email campaigns
- Conversion tracking

## Customization

### Adding Custom Fields

```python
from odoo import models, fields

class MotakamelProgramCustom(models.Model):
    _inherit = 'motakamel.program'
    
    custom_field = fields.Char(string='Custom Field')
```

### Extending Views

```xml
<record id="view_program_form_custom" model="ir.ui.view">
    <field name="name">motakamel.program.form.custom</field>
    <field name="model">motakamel.program</field>
    <field name="inherit_id" ref="motakamel.view_motakamel_program_form"/>
    <field name="arch" type="xml">
        <xpath expr="//field[@name='program_code']" position="after">
            <field name="custom_field"/>
        </xpath>
    </field>
</record>
```

## Troubleshooting

### Module Won't Install
- Check dependencies are installed
- Verify Odoo version compatibility
- Check server logs for errors

### Access Denied Errors
- Verify user has appropriate group membership
- Check record rules
- Ensure security CSV is loaded

### Website Pages Not Showing
- Verify program status is "Published"
- Check visibility_scope is "public"
- Clear browser cache

## Upgrade Guide

### From Draft to Production
1. Review all program data
2. Test approval workflows
3. Configure access rights
4. Test website publishing
5. Train users

### Migration Safety
- Module uses standard Odoo ORM
- No external dependencies
- Clean upgrade path
- Backward compatible

## Support & Contribution

### Getting Help
- Check documentation
- Review code comments
- Contact your Odoo partner

### Contributing
- Follow Odoo coding guidelines
- Add unit tests
- Update documentation
- Submit pull requests

## License

LGPL-3

## Credits

**Author**: Your Company  
**Version**: 19.0.1.0.0  
**Category**: Education  

---

**Motakamel** - متكامل - Complete Training & Certification Solution

