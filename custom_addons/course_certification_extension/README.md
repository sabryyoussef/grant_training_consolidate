# Course Certification Extension

## Overview

This module extends the Odoo eLearning (website_slides) module to add comprehensive certification and accreditation management features for training courses.

## Features

### 1. Certification Information
- **International Certification Badge**: Mark courses as internationally certified
- **Local Accreditation Badge**: Indicate local accreditation status
- **Certification Body**: Specify the certifying organization (e.g., IBTA)
- **Bilingual Course Names**: Support for both Arabic and English course names

### 2. Target Beneficiaries
Track which sectors can benefit from the course:
- Public Sector (القطاع العام)
- Private Sector (القطاع الخاص)
- Individuals (الأفراد)
- Non-Profit Sector (القطاع غير الربحي)

### 3. Accreditation Bodies Management
- Create and manage local accreditation bodies
- Add logos for each accreditation body
- Link multiple accreditation bodies to courses
- Display accreditation body information

### 4. Enhanced Course Details
- **Certification Description**: Rich text field for detailed certification information
- **Certificate Sample**: Upload sample certificate images

## Installation

1. Copy the module to your Odoo addons directory
2. Update the apps list in Odoo
3. Install the "Course Certification Extension" module

## Dependencies

- `website_slides` (Odoo eLearning module)

## Usage

### Adding Certification Information to a Course

1. Go to **eLearning → Courses**
2. Open or create a course
3. Navigate to the **"Certification & Accreditation"** tab
4. Fill in the certification details:
   - Check "Internationally Certified" if applicable
   - Enter the certification body name (e.g., IBTA)
   - Add Arabic and English course names
   - Select target beneficiaries
   - Add local accreditation bodies
   - Write a detailed certification description
   - Upload a certificate sample image

### Managing Accreditation Bodies

1. Go to **eLearning → Configuration → Accreditation Bodies**
2. Create new accreditation bodies with:
   - Name (English and Arabic)
   - Logo
   - Website
   - Description
3. Link them to courses

## Technical Details

### Models

#### slide.channel (inherited)
New fields added:
- `is_internationally_certified`: Boolean
- `has_local_accreditation`: Boolean
- `certification_body`: Char
- `course_name_arabic`: Char
- `course_name_english`: Char
- `target_public_sector`: Boolean
- `target_private_sector`: Boolean
- `target_individuals`: Boolean
- `target_nonprofit`: Boolean
- `accreditation_body_ids`: Many2many
- `certification_description`: Html
- `certificate_image`: Image

#### course.accreditation.body (new)
Fields:
- `name`: Char (required)
- `name_arabic`: Char
- `logo`: Image
- `website`: Char
- `description`: Text
- `active`: Boolean
- `sequence`: Integer
- `course_ids`: Many2many

### Views

- Extended course form view with new "Certification & Accreditation" tab
- Accreditation body form and tree views
- Menu item under eLearning Configuration

## Matching the HTML Design

This module provides the backend structure to support the course display shown in `course_1.html`:

- ✅ معتمدة دوليًا → `is_internationally_certified`
- 🏛 جهة الاعتماد المحلية → `has_local_accreditation`
- Course titles (Arabic/English) → `course_name_arabic`, `course_name_english`
- IBTA → `certification_body`
- Target sectors → `target_*` fields
- Accreditation logos → `accreditation_body_ids` with logos
- Description → `certification_description`

## Future Enhancements

- Frontend template to display certification information
- Certificate generation
- Accreditation expiry tracking
- Multi-language support for all fields

## Support

For issues or questions, please contact your system administrator.

## License

LGPL-3

## Version

19.0.1.0.0

