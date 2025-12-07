# Motakamel - Complete User Manual
## Enterprise Training & Certification Platform

**Version:** 19.0.1.0.0  
**Last Updated:** December 2024  
**Category:** Education

---

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [User Roles & Permissions](#user-roles--permissions)
4. [Program Management](#program-management)
5. [Accreditation Management](#accreditation-management)
6. [Target Audience Configuration](#target-audience-configuration)
7. [Delivery Options Setup](#delivery-options-setup)
8. [Pricing Configuration](#pricing-configuration)
9. [Credential Management](#credential-management)
10. [Marketing & SEO](#marketing--seo)
11. [Website Publishing](#website-publishing)
12. [Workflow Management](#workflow-management)
13. [Integration with Other Modules](#integration-with-other-modules)
14. [Best Practices](#best-practices)
15. [Troubleshooting](#troubleshooting)
16. [FAQ](#faq)

---

## Introduction

### What is Motakamel?

**Motakamel** (متكامل - meaning "Complete" in Arabic) is a comprehensive Odoo 19 module designed for managing professional training programs and certifications. It provides a unified platform for:

- **Course Management**: Create and manage training programs with full lifecycle support
- **Certification Tracking**: Track accreditations, credentials, and certificates
- **Pricing Management**: Flexible pricing models with discounts and installments
- **Delivery Scheduling**: Manage online, on-site, and hybrid training sessions
- **Marketing Tools**: SEO optimization, landing pages, and promotional materials
- **Website Integration**: Publish programs to your public website
- **CRM Integration**: Capture leads and track conversions

### Key Benefits

✅ **Complete Solution**: All training management in one place  
✅ **Multi-language**: Full Arabic and English support  
✅ **Flexible Workflows**: Approval processes and status tracking  
✅ **Website Ready**: Automatic website publishing  
✅ **SEO Optimized**: Built-in SEO tools for better visibility  
✅ **Enterprise Grade**: Production-ready with full security  

---

## Getting Started

### System Requirements

- **Odoo Version**: 19.0 (compatible with 16-19)
- **Python**: 3.8 or higher
- **PostgreSQL**: 12 or higher
- **Required Modules**: `base`, `website`, `crm`, `sale`, `website_sale`

### Installation Steps

#### Step 1: Install the Module

1. **Access Odoo Backend**
   - Log in to your Odoo instance
   - Navigate to **Apps** menu

2. **Update Apps List**
   - Click **Update Apps List** button
   - Wait for the update to complete

3. **Search for Motakamel**
   - In the search bar, type: `Motakamel`
   - Or filter by category: **Education**

4. **Install the Module**
   - Click on the **Motakamel** module card
   - Click the **Install** button
   - Wait for installation to complete (may take 1-2 minutes)

#### Step 2: Configure User Access

1. **Navigate to Users**
   - Go to **Settings → Users & Companies → Users**

2. **Assign User Groups**
   - Select a user
   - Go to **Access Rights** tab
   - Under **Motakamel**, assign appropriate groups:
     - **Motakamel / User**: Basic viewing access
     - **Motakamel / Sales**: View programs and create leads
     - **Motakamel / Manager**: Create, edit, and approve programs
     - **Motakamel / Administrator**: Full access including deletion

3. **Save Changes**
   - Click **Save** button

#### Step 3: Verify Installation

1. **Check Menu**
   - Look for **Motakamel** menu in the main navigation
   - You should see submenus: Programs, Configuration

2. **Access Programs**
   - Click **Motakamel → Programs**
   - You should see an empty list (or demo data if installed)

3. **Test Access**
   - Try creating a new program
   - If you can see the form, installation is successful

---

## User Roles & Permissions

### User Groups Overview

| Group | Permissions | Use Case |
|-------|-------------|----------|
| **Public** | View published programs on website | Website visitors |
| **Portal** | View published programs (registered) | Registered website users |
| **Motakamel / User** | View all active programs | Internal staff viewing |
| **Motakamel / Sales** | View programs, create CRM leads | Sales team |
| **Motakamel / Manager** | Create, edit, approve programs | Program managers |
| **Motakamel / Administrator** | Full access, delete programs | System administrators |

### Detailed Permissions

#### Public Users
- ✅ View published programs on website
- ✅ View program details
- ✅ Access `/programs` page
- ❌ Cannot access backend
- ❌ Cannot view draft programs

#### Portal Users
- ✅ All public permissions
- ✅ View registered-scope programs
- ✅ Access portal features
- ❌ Cannot edit programs

#### Motakamel / User
- ✅ View all active programs in backend
- ✅ View program details
- ✅ Search and filter programs
- ❌ Cannot create or edit
- ❌ Cannot approve or publish

#### Motakamel / Sales
- ✅ All User permissions
- ✅ Create CRM leads from programs
- ✅ View pricing information
- ✅ Access marketing materials
- ❌ Cannot create or edit programs
- ❌ Cannot approve or publish

#### Motakamel / Manager
- ✅ All Sales permissions
- ✅ Create new programs
- ✅ Edit existing programs
- ✅ Submit programs for review
- ✅ Approve programs
- ✅ Publish programs to website
- ✅ Archive programs
- ❌ Cannot delete programs

#### Motakamel / Administrator
- ✅ All Manager permissions
- ✅ Delete programs
- ✅ Configure module settings
- ✅ Full system access

### Record Rules

The module implements record-level security:

- **Public**: Only sees programs with `status='published'` AND `visibility_scope='public'`
- **Portal**: Sees published programs (both public and registered scope)
- **Users**: See all active programs
- **Managers**: See all programs (including archived)
- **Admins**: See all programs (including deleted)

---

## Program Management

### Understanding Programs

A **Program** in Motakamel represents a complete training course or certification. Each program can have:
- Multiple accreditations
- Various target audiences
- Different delivery options
- Multiple pricing plans
- Credential information
- Marketing campaigns

### Creating a New Program

#### Step-by-Step Guide

1. **Navigate to Programs**
   - Go to **Motakamel → Programs**
   - Click **Create** button

2. **Basic Information Tab**

   **Program Names** (Required):
   - **Program Name (English)**: e.g., "Certified Business Professional"
   - **Program Name (Arabic)**: e.g., "محترف أعمال معتمد"
   - Both fields are required and translatable

   **Program Code** (Required):
   - Short unique identifier: e.g., "CBP", "PMP", "ITIL"
   - Used for internal reference and URLs
   - Must be unique

   **Program Category** (Required):
   - Select from: Professional Certification, Technical Training, Management & Leadership, IT, Finance, HR, Marketing, Healthcare, Engineering, Legal, Other

   **Program Level** (Required):
   - Foundation, Intermediate, Advanced, Expert, Master

   **Provider Information**:
   - **Provider Name**: e.g., "IBTA", "PMI", "Microsoft"
   - **Provider Type**: Internal, External Partner, Accredited Body, University, Vendor Authorized

3. **Description Tab**

   **English Description**:
   - Rich HTML editor
   - Detailed program description
   - Learning outcomes
   - Course content overview

   **Arabic Description**:
   - Same as English but in Arabic
   - Supports RTL (Right-to-Left) display

   **Program Objectives**:
   - Learning objectives
   - Skills participants will gain
   - Expected outcomes

   **Career Outcomes**:
   - Career benefits
   - Job opportunities
   - Professional growth

4. **Visibility & Status**

   **Visibility Scope**:
   - **Public**: Visible to everyone on website
   - **Registered**: Only visible to logged-in users
   - **Internal**: Only visible to internal staff

   **Status**:
   - **Draft**: Initial creation, not yet submitted
   - **Under Review**: Submitted for approval
   - **Approved**: Approved by manager, ready to publish
   - **Published**: Live on website
   - **Archived**: Removed from active listings

   **Display Order**:
   - Number for sorting programs
   - Lower numbers appear first

5. **Save the Program**
   - Click **Save** button
   - Program ID is automatically generated

### Editing a Program

1. **Find the Program**
   - Go to **Motakamel → Programs**
   - Use search or filters to find the program
   - Click on the program name

2. **Make Changes**
   - Edit any field as needed
   - Changes are tracked in the chatter

3. **Save Changes**
   - Click **Save** button
   - Changes are immediately saved

### Program Workflow

#### Workflow States

```
Draft → Under Review → Approved → Published
  ↓         ↓            ↓
Archived  Archived    Archived
```

#### Workflow Actions

**1. Submit for Review** (Draft → Under Review)
- Available when status is "Draft"
- Button: **Submit for Review**
- Only Managers can approve

**2. Approve** (Under Review → Approved)
- Available when status is "Under Review"
- Button: **Approve**
- Requires Manager role
- Records who approved and when

**3. Publish** (Approved → Published)
- Available when status is "Approved"
- Button: **Publish**
- Makes program visible on website
- Sets `is_published` flag

**4. Archive** (Any Status → Archived)
- Available from any status
- Button: **Archive**
- Removes from active listings
- Sets `active=False`

### Program Statistics

The program form shows statistics buttons:

- **Accreditations**: Count of linked accreditations
- **Delivery Options**: Count of delivery schedules
- **Pricing Plans**: Count of pricing options

Click any button to view related records.

### Searching and Filtering Programs

#### Search Bar
- Search by program name (English or Arabic)
- Search by program code
- Search by provider name

#### Filters
- **Status**: Draft, Under Review, Approved, Published, Archived
- **Category**: Filter by program category
- **Level**: Filter by program level
- **Provider Type**: Filter by provider type
- **Visibility Scope**: Public, Registered, Internal

#### Grouping
- Group by Status
- Group by Category
- Group by Level
- Group by Provider Type

---

## Accreditation Management

### What are Accreditations?

Accreditations represent certifications or approvals that validate your program. A program can have multiple accreditations (e.g., both international and local).

### Adding Accreditations to a Program

1. **Open the Program**
   - Navigate to **Motakamel → Programs**
   - Open the desired program

2. **Go to Accreditations Tab**
   - Click on **Accreditations** tab
   - You'll see a list of existing accreditations (if any)

3. **Add New Accreditation**
   - Click **Add a line** button
   - Fill in the form:

   **Accreditation Code** (Required):
   - Unique identifier: e.g., "IBTA-CBP-2025"
   - Format: `BODY-CODE-YEAR`

   **Accreditation Type**:
   - **International**: Recognized globally
   - **Local**: Country/region specific

   **Accreditation Body**:
   - **International**: Select from list (PMI, Microsoft, Cisco, etc.)
   - **Local**: Enter local body name

   **Validity Period**:
   - **Valid From**: Start date
   - **Valid To**: End date (optional for perpetual)

   **Certificate Information**:
   - **Certificate Type**: Digital, Physical, Both
   - **Verification URL**: Link to verify certificate
   - **Sample Certificate**: Upload PDF/image

   **Primary Accreditation**:
   - Check if this is the main accreditation
   - Only one primary per program

4. **Save**
   - Click **Save** on the accreditation line
   - Click **Save** on the program form

### Managing Accreditations

#### Editing an Accreditation
- Click on the accreditation line
- Make changes
- Save

#### Removing an Accreditation
- Click **Delete** (trash icon) on the line
- Confirm deletion

#### Setting Primary Accreditation
- Check **Is Primary** checkbox
- Only one can be primary
- System will uncheck others automatically

### Accreditation Categories

**International Bodies** (Predefined):
- PMI (Project Management Institute)
- Microsoft
- Cisco
- Oracle
- IBM
- AWS
- Google
- CompTIA
- ISACA
- (ISC)²

**Local Bodies**:
- Enter custom names
- Examples: "Saudi Commission", "Egyptian Authority"

---

## Target Audience Configuration

### Understanding Target Audience

Target Audience defines who the program is designed for. You can specify:
- Target sectors (public, private, non-profit)
- Career levels
- Industries
- Prerequisites

### Adding Target Audience

1. **Open the Program**
   - Navigate to the program

2. **Go to Target Audience Tab**
   - Click **Target Audience** tab

3. **Add Audience Entry**
   - Click **Add a line**

   **Target Sector** (Required):
   - **Public Sector**: Government employees
   - **Private Sector**: Corporate employees
   - **Non-Profit**: NGO staff
   - **Individual**: Personal development
   - **All Sectors**: Open to everyone

   **Career Level**:
   - Entry Level, Mid-Level, Senior, Executive, All Levels

   **Target Industries**:
   - Select from predefined industries
   - Multiple selection allowed

   **Eligible Job Titles**:
   - Comma-separated list
   - Example: "Manager, Director, Executive"

   **Prerequisites**:
   - Education requirements
   - Experience requirements
   - Certification requirements

   **Minimum Education**:
   - High School, Bachelor's, Master's, PhD, None

   **Minimum Experience**:
   - Years of experience required

4. **Save**
   - Save the audience entry
   - Save the program

### Best Practices for Target Audience

- **Be Specific**: Clear targeting improves conversion
- **Multiple Entries**: Create separate entries for different sectors
- **Realistic Prerequisites**: Don't set unrealistic requirements
- **Update Regularly**: Keep prerequisites current

---

## Delivery Options Setup

### Understanding Delivery Options

Delivery Options define how and when the program is delivered. A program can have multiple delivery options (e.g., online and in-person versions).

### Adding Delivery Options

1. **Open the Program**
   - Navigate to the program

2. **Go to Delivery Tab**
   - Click **Delivery Options** tab

3. **Add Delivery Option**
   - Click **Add a line**

   **Training Mode** (Required):
   - **Online**: Virtual training
   - **On-Site**: Physical location
   - **Hybrid**: Combination of both
   - **Self-Paced**: Independent learning

   **Schedule Information**:
   - **Start Date**: When training begins
   - **End Date**: When training ends
   - **Duration (Days)**: Total training days
   - **Duration (Hours)**: Total training hours

   **Exam Information**:
   - **Has Exam**: Check if program includes exam
   - **Exam Date**: Scheduled exam date
   - **Exam Duration**: Exam length in minutes

   **Location Details**:
   - **Venue Name**: Physical location name
   - **Venue Address**: Full address
   - **Online Platform**: For online training (Zoom, Teams, etc.)
   - **Platform URL**: Link to online platform

   **Capacity & Enrollment**:
   - **Maximum Capacity**: Maximum participants
   - **Current Enrollment**: Current number enrolled
   - **Registration Status**: Open, Full, Closed

   **Study Materials**:
   - **Materials Included**: Description of materials
   - **Materials Cost**: Additional cost (if any)

4. **Save**
   - Save the delivery option
   - Save the program

### Delivery Status Management

**Registration Status Options**:
- **Open**: Accepting registrations
- **Full**: Capacity reached
- **Closed**: Registration closed

**Updating Enrollment**:
- Manually update **Current Enrollment** field
- System calculates available spots

### Multiple Delivery Options

You can create multiple delivery options for the same program:
- Different dates
- Different locations
- Different modes (online vs. on-site)
- Different languages

---

## Pricing Configuration

### Understanding Pricing

Pricing allows you to create multiple pricing plans for the same program. Each plan can have:
- Different prices
- Discounts
- Installment options
- Validity periods
- Corporate rates

### Adding Pricing Plans

1. **Open the Program**
   - Navigate to the program

2. **Go to Pricing Tab**
   - Click **Pricing** tab

3. **Add Pricing Plan**
   - Click **Add a line**

   **Pricing Plan Name** (Required):
   - e.g., "Standard", "Early Bird", "Corporate", "Group Discount"

   **Pricing Details**:
   - **List Price**: Original price
   - **Discount (%)**: Percentage discount
   - **Discount Amount**: Fixed discount amount
   - **Final Price**: Automatically calculated

   **Currency**:
   - Defaults to company currency
   - Can be changed per plan

   **Validity Period**:
   - **Valid From**: When pricing becomes active
   - **Valid To**: When pricing expires (optional)

   **Pricing Type**:
   - **Standard**: Regular pricing
   - **Early Bird**: Limited time discount
   - **Corporate**: Bulk pricing
   - **Group**: Group discount
   - **Student**: Student discount

   **Installment Options**:
   - **Allows Installments**: Check if installments available
   - **Number of Installments**: How many payments
   - **Installment Amount**: Amount per installment

   **Additional Information**:
   - **Tax Included**: Check if tax included in price
   - **Refund Policy**: Refund terms
   - **Payment Terms**: Payment conditions

   **Default Pricing**:
   - Check if this is the default plan
   - Only one default per program

4. **Save**
   - Save the pricing plan
   - Save the program

### Pricing Calculations

**Final Price Formula**:
```
Final Price = List Price - Discount Amount - (List Price × Discount % / 100)
```

**Installment Calculation**:
```
Installment Amount = Final Price / Number of Installments
```

### Pricing Best Practices

- **Clear Naming**: Use descriptive plan names
- **Realistic Discounts**: Don't over-discount
- **Validity Periods**: Set clear expiration dates
- **One Default**: Always have one default pricing plan
- **Update Regularly**: Keep prices current

---

## Credential Management

### Understanding Credentials

Credentials represent certificates or certifications issued upon program completion. You can track:
- Certificate types
- Issuing authorities
- Delivery timelines
- Renewal requirements

### Adding Credentials

1. **Open the Program**
   - Navigate to the program

2. **Go to Credentials Tab**
   - Click **Credentials** tab

3. **Add Credential**
   - Click **Add a line**

   **Credential Type** (Required):
   - **Certificate**: Completion certificate
   - **Certification**: Professional certification
   - **Diploma**: Diploma certificate
   - **Badge**: Digital badge
   - **License**: Professional license

   **Issuing Authority**:
   - Who issues the credential
   - Usually matches accreditation body

   **Delivery Information**:
   - **Delivery Method**: Email, Physical Mail, Digital Download
   - **Delivery Timeline**: Days after completion
   - **Digital Badge**: Check if digital badge available
   - **Badge URL**: Link to digital badge

   **Renewal Information**:
   - **Requires Renewal**: Check if credential expires
   - **Renewal Period**: Years until renewal needed
   - **Renewal Process**: How to renew

   **Verification**:
   - **Verification URL**: Link to verify credential
   - **Verification Code**: Unique verification code format

   **LinkedIn Integration**:
   - **LinkedIn Shareable**: Check if can be shared on LinkedIn
   - **LinkedIn Badge ID**: LinkedIn badge identifier

4. **Save**
   - Save the credential
   - Save the program

### Credential Lifecycle

1. **Program Completion**: Student completes program
2. **Credential Issuance**: Credential is issued
3. **Delivery**: Credential delivered to student
4. **Verification**: Student can verify credential online
5. **Renewal** (if applicable): Credential renewed before expiration

---

## Marketing & SEO

### Understanding Marketing

Marketing features help promote your programs through:
- SEO optimization
- Landing pages
- Promotional materials
- Lead generation
- Social media integration

### Setting Up Marketing

1. **Open the Program**
   - Navigate to the program

2. **Go to Marketing Tab**
   - Click **Marketing** tab

3. **Add Marketing Campaign**
   - Click **Add a line**

   **Campaign Information**:
   - **Campaign Name**: e.g., "Summer 2025 Promotion"
   - **Campaign Type**: SEO, Social Media, Email, Landing Page, General

   **SEO Settings**:
   - **SEO Title**: Optimized page title (50-60 characters)
   - **SEO Description**: Meta description (150-160 characters)
   - **SEO Keywords**: Comma-separated keywords
   - **Canonical URL**: Preferred URL for SEO

   **Homepage Featuring**:
   - **Feature on Homepage**: Check to feature on homepage
   - **Homepage Order**: Display order on homepage

   **Landing Page**:
   - **Landing Page URL**: Custom landing page URL
   - **Landing Page Content**: HTML content for landing page

   **Promotional Materials**:
   - **Brochure**: Upload PDF brochure
   - **Promotional Video**: Video URL (YouTube, Vimeo)
   - **Social Media Content**: Pre-written social posts

   **Lead Generation**:
   - **WhatsApp Link**: Direct WhatsApp contact link
   - **Lead Capture Form**: Form URL
   - **UTM Parameters**: Tracking parameters

   **Campaign Period**:
   - **Start Date**: When campaign starts
   - **End Date**: When campaign ends

   **Performance Tracking**:
   - **Views**: Number of views
   - **Clicks**: Number of clicks
   - **Leads Generated**: Number of leads
   - **Conversions**: Number of conversions

4. **Save**
   - Save the marketing campaign
   - Save the program

### SEO Best Practices

**SEO Title**:
- 50-60 characters
- Include program name and key benefit
- Example: "PMP Certification Training | Project Management Institute"

**SEO Description**:
- 150-160 characters
- Compelling summary
- Include call-to-action
- Example: "Get PMP certified with our comprehensive training. Expert instructors, flexible schedules, 100% pass guarantee. Enroll today!"

**SEO Keywords**:
- 5-10 relevant keywords
- Include program name, category, location
- Example: "PMP, project management, certification, training, PMI"

### Marketing Campaign Types

**SEO Campaign**:
- Focus on search engine optimization
- Optimize titles, descriptions, keywords
- Track organic search performance

**Social Media Campaign**:
- Create social media content
- Schedule posts
- Track engagement

**Email Campaign**:
- Email marketing integration
- Newsletter features
- Automated follow-ups

**Landing Page Campaign**:
- Custom landing pages
- A/B testing
- Conversion optimization

---

## Website Publishing

### Publishing Programs to Website

#### Prerequisites

Before publishing:
1. ✅ Program status must be "Approved"
2. ✅ Visibility scope must be "Public" or "Registered"
3. ✅ Program must be active
4. ✅ At least basic information must be filled

#### Publishing Steps

1. **Complete Program Setup**
   - Fill in all required fields
   - Add descriptions (English and Arabic)
   - Add at least one pricing plan
   - Add delivery options (optional but recommended)

2. **Submit for Review**
   - Click **Submit for Review** button
   - Status changes to "Under Review"
   - Manager receives notification

3. **Manager Approval**
   - Manager reviews the program
   - Clicks **Approve** button
   - Status changes to "Approved"

4. **Publish to Website**
   - Click **Publish** button
   - Status changes to "Published"
   - Program appears on website immediately

### Website Pages

#### Program Catalog Page
- **URL**: `/programs`
- **Content**: List of all published programs
- **Features**: Search, filter, sort
- **Layout**: Card-based grid

#### Program Detail Page
- **URL**: `/programs/<program_id>`
- **Content**: Full program details
- **Features**: 
  - Program information
  - Pricing display
  - Registration button (if enrollment module installed)
  - Contact form

#### Homepage Integration
- Programs can be featured on homepage
- Set in Marketing tab: **Feature on Homepage**
- Control display order with **Homepage Order**

### Website Features

**Multi-language Support**:
- Automatic RTL (Right-to-Left) for Arabic
- Bilingual content display
- Language switching

**Responsive Design**:
- Mobile-friendly
- Tablet optimized
- Desktop layout

**SEO Optimization**:
- Meta tags
- Structured data
- Sitemap integration

### Unpublishing Programs

To remove a program from website:
1. Click **Archive** button
2. Or change status to "Draft"
3. Program is immediately removed from website

---

## Workflow Management

### Understanding Workflows

Motakamel uses a status-based workflow to manage program lifecycle:

```
┌─────────┐   Submit    ┌──────────────┐   Approve   ┌──────────┐   Publish   ┌───────────┐
│  Draft  │ ──────────> │ Under Review │ ──────────> │ Approved │ ──────────> │ Published │
└─────────┘             └──────────────┘             └──────────┘             └───────────┘
     │                        │                              │                          │
     │                        │                              │                          │
     └────────────────────────┴──────────────────────────────┴──────────────────────────┘
                                          │
                                          ▼
                                    ┌──────────┐
                                    │ Archived │
                                    └──────────┘
```

### Workflow Roles

**Content Creator** (User/Sales):
- Creates programs in "Draft" status
- Fills in program information
- Submits for review
- Cannot approve or publish

**Manager**:
- Reviews submitted programs
- Approves programs
- Can publish programs
- Can archive programs

**Administrator**:
- All manager permissions
- Can delete programs
- Full system access

### Workflow Best Practices

1. **Complete Information First**
   - Fill all required fields before submitting
   - Add descriptions, pricing, delivery options

2. **Review Before Submission**
   - Check spelling and grammar
   - Verify pricing accuracy
   - Confirm dates and schedules

3. **Use Comments**
   - Add notes in chatter for reviewers
   - Explain any special requirements
   - Document changes

4. **Monitor Status**
   - Track program through workflow
   - Respond to review comments
   - Update as needed

---

## Integration with Other Modules

### Student Enrollment Portal Integration

If **student_enrollment_portal** module is installed:

**Automatic Integration**:
- "Register Now" button appears on program detail pages
- Links to registration form with program pre-selected
- Program information included in registration

**How It Works**:
1. User clicks "Register Now" on program page
2. Redirects to `/student/register?program_id=X`
3. Registration form shows selected program
4. Program info stored in registration notes

### CRM Integration

**Lead Capture**:
- Programs can generate CRM leads
- Lead information includes program details
- Automatic lead assignment

**Lead Conversion**:
- Track leads from programs
- Measure conversion rates
- Optimize marketing campaigns

### Website Integration

**Automatic Publishing**:
- Published programs appear on website
- SEO metadata included
- Responsive design

**Customization**:
- Customize templates
- Add custom fields
- Modify layouts

---

## Best Practices

### Program Creation

✅ **Do**:
- Use clear, descriptive program names
- Include both English and Arabic names
- Use consistent program codes
- Fill in all required fields
- Add detailed descriptions
- Include pricing information
- Set realistic delivery schedules

❌ **Don't**:
- Use vague program names
- Skip required fields
- Use duplicate program codes
- Publish incomplete programs
- Set unrealistic prices
- Overpromise delivery dates

### Pricing Management

✅ **Do**:
- Create multiple pricing plans
- Set clear validity periods
- Use descriptive plan names
- Keep prices competitive
- Offer installment options
- Update prices regularly

❌ **Don't**:
- Use confusing pricing names
- Set prices without research
- Forget to set validity dates
- Create too many similar plans
- Ignore market trends

### Website Publishing

✅ **Do**:
- Complete all information before publishing
- Use SEO best practices
- Add high-quality descriptions
- Include images (if available)
- Test website display
- Monitor website performance

❌ **Don't**:
- Publish incomplete programs
- Ignore SEO optimization
- Use poor quality content
- Skip testing
- Forget to update published programs

### Workflow Management

✅ **Do**:
- Follow the approval workflow
- Add comments for reviewers
- Respond to review feedback
- Keep programs updated
- Archive old programs

❌ **Don't**:
- Skip workflow steps
- Publish without approval
- Ignore review comments
- Leave programs in draft forever
- Delete instead of archiving

---

## Troubleshooting

### Common Issues and Solutions

#### Issue: Module Won't Install

**Symptoms**:
- Installation fails
- Error messages appear
- Module doesn't appear in Apps

**Solutions**:
1. **Check Dependencies**
   - Ensure all required modules are installed
   - Install: `base`, `website`, `crm`, `sale`, `website_sale`

2. **Check Odoo Version**
   - Verify Odoo 19.0 is installed
   - Check compatibility

3. **Check Server Logs**
   - Review Odoo server logs
   - Look for error messages
   - Contact system administrator

4. **Update Apps List**
   - Go to Apps → Update Apps List
   - Try installing again

#### Issue: Access Denied Errors

**Symptoms**:
- "Access Denied" messages
- Cannot view programs
- Cannot create programs

**Solutions**:
1. **Check User Groups**
   - Go to Settings → Users
   - Verify user has appropriate Motakamel group
   - Assign correct group

2. **Check Record Rules**
   - Verify record rules are loaded
   - Check security files are installed

3. **Check Program Status**
   - Ensure program status allows access
   - Check visibility scope

#### Issue: Programs Not Showing on Website

**Symptoms**:
- Program not visible on `/programs`
- 404 error on program page
- Empty catalog page

**Solutions**:
1. **Check Program Status**
   - Status must be "Published"
   - Verify in program form

2. **Check Visibility Scope**
   - Must be "Public" for public access
   - Or "Registered" for logged-in users

3. **Check Active Status**
   - Program must be active
   - Uncheck "Archive" if archived

4. **Clear Browser Cache**
   - Hard refresh: `Ctrl + Shift + R`
   - Clear browser cache
   - Try incognito mode

5. **Check Website Configuration**
   - Verify website module is installed
   - Check website is active
   - Verify routes are working

#### Issue: "Register Now" Button Not Showing

**Symptoms**:
- Shows "Contact Us" instead
- No registration button

**Solutions**:
1. **Check Enrollment Module**
   - Verify `student_enrollment_portal` is installed
   - Go to Apps and check installation status

2. **Clear Cache**
   - Restart Odoo server
   - Clear browser cache
   - Hard refresh page

3. **Check Module Detection**
   - System automatically detects module
   - If not working, contact administrator

#### Issue: Arabic Text Not Displaying Correctly

**Symptoms**:
- Arabic text appears incorrectly
- RTL not working
- Text alignment issues

**Solutions**:
1. **Check Language Installation**
   - Go to Settings → Translations → Languages
   - Ensure Arabic is installed
   - Load Arabic translation

2. **Check User Language**
   - Go to Settings → Users
   - Set user language to Arabic
   - Save and refresh

3. **Clear Cache**
   - Clear browser cache
   - Restart Odoo
   - Hard refresh

#### Issue: Pricing Calculations Wrong

**Symptoms**:
- Final price incorrect
- Installment amounts wrong
- Discounts not applying

**Solutions**:
1. **Check Pricing Fields**
   - Verify list price is set
   - Check discount percentage/amount
   - Ensure currency is correct

2. **Recalculate**
   - System auto-calculates
   - Save program to recalculate
   - Check final price field

3. **Check Tax Settings**
   - Verify tax configuration
   - Check if tax included in price

---

## FAQ

### General Questions

**Q: What is the difference between a Program and a Course?**
A: In Motakamel, a "Program" is the main entity that represents a complete training program or certification. It can have multiple delivery options, pricing plans, and accreditations. Think of it as a container for all related information.

**Q: Can I have multiple programs with the same name?**
A: No, program codes must be unique. However, program names can be similar as long as codes differ.

**Q: How do I delete a program?**
A: Only Administrators can delete programs. Regular users should use "Archive" instead, which removes it from active listings without deleting the record.

**Q: Can I import programs from Excel?**
A: Currently, programs must be created manually. Bulk import functionality may be available in future versions.

### Pricing Questions

**Q: Can I have different prices for the same program?**
A: Yes! Create multiple pricing plans in the Pricing tab. Each plan can have different prices, discounts, and validity periods.

**Q: How do installments work?**
A: Set "Allows Installments" to True, specify the number of installments, and the system calculates the installment amount automatically.

**Q: Can I set prices in different currencies?**
A: Yes, each pricing plan can have its own currency. The default is your company currency.

### Website Questions

**Q: How long does it take for a program to appear on the website?**
A: Immediately after clicking "Publish". The program appears on `/programs` right away.

**Q: Can I customize how programs appear on the website?**
A: Yes, you can customize templates. Contact your developer for template modifications.

**Q: Do I need to manually update the website when I change a program?**
A: No, changes are reflected immediately on the website when you save the program (if it's published).

### Workflow Questions

**Q: Who can approve programs?**
A: Only users with "Motakamel / Manager" or "Motakamel / Administrator" roles can approve programs.

**Q: Can I skip the approval process?**
A: No, the workflow is designed to ensure quality. However, Managers can approve their own programs if needed.

**Q: What happens if I reject a program?**
A: Currently, there's no explicit "reject" action. You can add comments in the chatter explaining what needs to be fixed, and the creator can resubmit.

### Integration Questions

**Q: Do I need the student_enrollment_portal module?**
A: No, it's optional. Without it, the "Contact Us" button appears instead of "Register Now". The module provides enhanced registration functionality.

**Q: Can I integrate with other LMS systems?**
A: The module is designed to work with Odoo's ecosystem. Integration with external LMS systems would require custom development.

**Q: Does it work with Odoo eLearning?**
A: The module is compatible with Odoo's website and can be extended to work with eLearning modules through custom development.

---

## Additional Resources

### Getting Help

- **Documentation**: Check this manual first
- **Code Comments**: Review code for technical details
- **Odoo Community**: Visit Odoo Community Forum
- **Support**: Contact your Odoo partner or system administrator

### Module Information

- **Version**: 19.0.1.0.0
- **Author**: Your Company
- **License**: LGPL-3
- **Category**: Education
- **Website**: https://www.yourcompany.com

### Updates and Maintenance

- **Regular Updates**: Keep module updated
- **Backup Data**: Regular backups recommended
- **Test Changes**: Test in staging before production
- **Monitor Performance**: Track website and system performance

---

## Appendix

### A. Field Reference

#### Program Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Program ID | Char | Yes | Auto-generated unique identifier |
| Program Name (English) | Char | Yes | English program name |
| Program Name (Arabic) | Char | Yes | Arabic program name |
| Program Code | Char | Yes | Short unique code |
| Program Category | Selection | Yes | Category classification |
| Program Level | Selection | Yes | Difficulty level |
| Provider Name | Char | Yes | Training provider |
| Provider Type | Selection | Yes | Type of provider |
| Description (English) | Html | No | Detailed English description |
| Description (Arabic) | Html | No | Detailed Arabic description |
| Program Objectives | Text | No | Learning objectives |
| Career Outcomes | Text | No | Career benefits |
| Status | Selection | Yes | Workflow status |
| Visibility Scope | Selection | Yes | Who can see program |
| Display Order | Integer | No | Sorting order |
| Active | Boolean | Yes | Active status |

### B. Status Values

- **Draft**: Initial creation, not submitted
- **Under Review**: Submitted, awaiting approval
- **Approved**: Approved, ready to publish
- **Published**: Live on website
- **Archived**: Removed from active listings

### C. Category Values

- Professional Certification
- Technical Training
- Management & Leadership
- Information Technology
- Finance & Accounting
- Human Resources
- Marketing & Sales
- Healthcare
- Engineering
- Legal & Compliance
- Other

### D. Keyboard Shortcuts

- **Ctrl+S**: Save current record
- **Ctrl+Enter**: Save and create new
- **Ctrl+Shift+N**: Create new record
- **Ctrl+F**: Search
- **Esc**: Cancel/Discard changes

---

**End of User Manual**

For the latest version and updates, please visit: https://www.yourcompany.com

**Motakamel** - متكامل - Complete Training & Certification Solution

---

*This manual was generated for Motakamel version 19.0.1.0.0. For questions or support, please contact your system administrator.*

