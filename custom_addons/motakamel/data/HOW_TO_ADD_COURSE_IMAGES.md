# How to Add and Change Course Photos

## Overview
Each marketing campaign in Motakamel can have promotional photos that appear on the website, social media, and landing pages.

## Image Fields Available

### 1. **Open Graph Image** (`og_image`)
- **Purpose**: Main image for social media sharing (Facebook, Twitter, LinkedIn)
- **Recommended Size**: 1200x630 pixels
- **Format**: JPG or PNG
- **Use**: When someone shares the course link on social media

### 2. **Promotional Images** (`promo_images`)
- **Purpose**: Gallery of images for course landing pages
- **Recommended Size**: 1920x1080 pixels (or any HD resolution)
- **Format**: JPG or PNG
- **Use**: Course catalog, landing pages, marketing materials

## How to Add/Change Photos

### Method 1: Through Odoo Interface (Easiest)

1. **Login to Odoo** as Administrator
2. **Navigate to**: Motakamel → Marketing → Marketing Campaigns
3. **Select** the course you want to edit (e.g., "PMP Certification Premium Program 2025")
4. **Click Edit**
5. **Upload Image**:
   - For social media image: Click on "Open Graph Image" field → Upload File
   - For promotional gallery: Scroll to "Promotional Images" → Add images
6. **Click Save**

### Method 2: Through Database (Advanced)

If you have direct database access or want to prepare images in bulk:

1. **Prepare your images** with proper naming:
   ```
   pmp_og_image.jpg          (1200x630px)
   pmp_promo_1.jpg           (1920x1080px)
   pmp_promo_2.jpg           (1920x1080px)
   phri_og_image.jpg         (1200x630px)
   cbplc_og_image.jpg        (1200x630px)
   etc.
   ```

2. **Upload to Odoo attachments** folder or use the interface

### Method 3: Update Demo Data (For Development)

Edit the file: `motakamel_marketing_demo.xml`

```xml
<record id="demo_marketing_pmp" model="motakamel.marketing">
    <field name="program_id" ref="demo_program_pmp"/>
    
    <!-- Add image filename (image must exist in Odoo) -->
    <field name="og_image_filename">pmp_og_image.jpg</field>
    
    <!-- Other fields... -->
</record>
```

## Current Course Images Setup

| Course Code | Image Filename | Status |
|-------------|----------------|--------|
| CBPLC | cbplc_og_image.jpg | ✅ Ready to upload |
| PHRI | phri_og_image.jpg | ✅ Ready to upload |
| PMP | pmp_og_image.jpg | ✅ Ready to upload |
| CBPCS | cbpcs_og_image.jpg | ✅ Ready to upload |
| CBPL | cbpl_og_image.jpg | ✅ Ready to upload |

## Image Best Practices

### Social Media Images (OG Image)
- **Size**: 1200x630 pixels (Facebook/LinkedIn standard)
- **Format**: JPG (smaller file size) or PNG (better quality)
- **Content**: 
  - Course logo/badge
  - Course name
  - Key benefit (e.g., "Get Certified in 5 Days")
  - Provider logo (IBTA, PMI, HRCI)
  - Avoid too much text

### Promotional Images
- **Size**: 1920x1080 pixels (Full HD) or 1200x800 pixels
- **Format**: JPG or PNG
- **Content**:
  - Training session photos
  - Certificate images
  - Instructor photos
  - Classroom/venue photos
  - Success stories/testimonials

## Example: Adding Photo to PMP Course

### Step-by-Step:

1. **Prepare the image**:
   - Create or select a professional image
   - Resize to 1200x630 pixels
   - Add PMP logo, text: "PMP Certification - Premium Training"
   - Save as `pmp_og_image.jpg`

2. **Upload to Odoo**:
   - Go to Settings → Technical → Attachments
   - Click "Create"
   - Name: "pmp_og_image.jpg"
   - Upload file
   - Save

3. **Link to Marketing Record**:
   - Go to Motakamel → Marketing → "PMP Certification Premium Program 2025"
   - Click Edit
   - In "Open Graph Image" field, select the uploaded image
   - Save

4. **Verify**:
   - Check the course landing page
   - Share the link on Facebook/LinkedIn to test OG image
   - Image should appear in social preview

## Quick Image Templates

### Recommended Tools:
- **Canva**: Free templates for social media images
- **Adobe Spark**: Quick image creation
- **Photoshop**: Professional editing
- **GIMP**: Free alternative to Photoshop

### Template Ideas:
1. **Professional Certificate Template**
   - Course name at top
   - Large certification logo (PMI, IBTA, HRCI)
   - "Enroll Now" call-to-action
   - Training dates

2. **Success Story Template**
   - Photo of happy graduate
   - Quote: "Best investment in my career"
   - Course badge
   - Rating stars

3. **Urgency Template**
   - "Limited Seats Available"
   - Countdown timer graphic
   - Course details
   - "Register Now" button

## Changing Images Later

To update/change an image:

1. **Through Interface**:
   - Edit the marketing record
   - Remove old image (click X)
   - Upload new image
   - Save

2. **Keep Same Filename**:
   - If you replace the file with the same name in attachments
   - The system will automatically use the new image
   - No code changes needed

## Troubleshooting

### Image Not Showing
- Check file size (max 10MB recommended)
- Verify file format (JPG, PNG supported)
- Clear browser cache
- Check image permissions in Odoo

### Image Quality Poor
- Use higher resolution source
- Avoid over-compression
- Use PNG for graphics with text
- Use JPG for photos

### Social Media Preview Not Working
- Validate OG tags using Facebook Debugger
- Check image dimensions (1200x630)
- Verify canonical_url is correct
- Clear social media cache

## Support

For questions or assistance:
- **Documentation**: See Motakamel module README
- **Technical Support**: Contact system administrator
- **Image Design**: Contact marketing team

---

**Last Updated**: December 2025  
**Module**: Motakamel Marketing  
**Version**: Compatible with Odoo 17.0
