# Static Assets - Course Certification Extension

## 📁 Folder Structure

```
static/
├── description/
│   └── index.html              # Module description page
└── src/
    ├── css/
    │   └── course_certification.css    # Main stylesheet
    └── js/
        └── (future JavaScript files)
```

## 🎨 CSS File

### **Location:**
`static/src/css/course_certification.css`

### **Purpose:**
Contains all styling for the course certification form view, matching the design from `course_1.html`.

### **CSS Classes:**

#### **Badges:**
- `.certification_badge` - Base badge style
- `.certification_badge.international` - Green international certification badge
- `.certification_badge.local` - Blue local accreditation badge

#### **Target Sectors:**
- `.target_sector` - Base sector box style
- `.target_public` - Orange public sector box
- `.target_private` - Red private sector box
- `.target_individuals` - Blue individuals box
- `.target_nonprofit` - Green non-profit box

#### **Certification Body:**
- `.certification_body_badge` - Purple gradient IBTA badge

#### **Course Titles:**
- `.course_title_ar` - Arabic title styling (20px, bold, RTL)
- `.course_title_en` - English subtitle styling (16px, gray)

#### **Section Headers:**
- `.section_header` - Blue header bars with white text

#### **Layout:**
- `.certification_section` - Section container with margins
- `.target_beneficiaries_grid` - 2-column grid for target sectors
- `.badge_container` - Container for certification badges
- `.course_title_container` - Container for course titles

#### **Other:**
- `.accreditation_tags` - Styling for accreditation body tags
- `.certificate_image_preview` - Certificate image preview styling

## 🔧 How It's Loaded

The CSS file is loaded through the module manifest (`__manifest__.py`):

```python
'assets': {
    'web.assets_backend': [
        'course_certification_extension/static/src/css/course_certification.css',
    ],
},
```

This ensures the CSS is loaded in the Odoo backend for all users.

## 📝 View Integration

The XML view (`views/slide_channel_views.xml`) uses these CSS classes instead of inline styles:

```xml
<!-- Example: Certification Badge -->
<span class="certification_badge international">
    ✅ معتمدة دوليًا
</span>

<!-- Example: Target Sector -->
<span class="target_sector target_public">
    القطاع العام (Public Sector)
</span>

<!-- Example: Section Header -->
<div class="section_header">
    الجهات المستفيدة (Target Beneficiaries)
</div>
```

## 🎨 Color Scheme

| Element | Color | Hex Code |
|---------|-------|----------|
| International Badge | Light Green | #d1fae5 (bg), #065f46 (text) |
| Local Badge | Light Blue | #dbeafe (bg), #1e40af (text) |
| Public Sector | Orange | #f59e0b |
| Private Sector | Red | #ef4444 |
| Individuals | Blue | #3b82f6 |
| Non-Profit | Green | #22c55e |
| Section Headers | Blue | #2b4eff |
| IBTA Badge | Purple Gradient | #667eea → #764ba2 |

## 📱 Responsive Design

The CSS includes media queries for mobile devices:

```css
@media (max-width: 768px) {
    .target_beneficiaries_grid {
        grid-template-columns: 1fr;  /* Single column on mobile */
    }
    /* Smaller font sizes for titles */
}
```

## 🔄 Updating Styles

To modify the design:

1. **Edit the CSS file:**
   ```bash
   nano static/src/css/course_certification.css
   ```

2. **Update the module:**
   ```bash
   docker exec odoo19_grant_edit odoo -d courses --stop-after-init -u course_certification_extension
   ```

3. **Reload Odoo:**
   ```bash
   docker exec odoo19_grant_edit pkill -HUP -f "odoo"
   ```

4. **Hard refresh browser:**
   - Press `Ctrl+Shift+R` (Linux/Windows)
   - Press `Cmd+Shift+R` (Mac)

## 📚 Best Practices

1. **Use CSS classes** instead of inline styles
2. **Follow Odoo naming conventions** (lowercase with underscores)
3. **Keep specificity low** for easier overrides
4. **Use semantic class names** that describe purpose, not appearance
5. **Include responsive breakpoints** for mobile support
6. **Document color schemes** for consistency

## 🎯 Benefits of Separation

- ✅ **Maintainability**: Easier to update styles
- ✅ **Reusability**: Classes can be reused across views
- ✅ **Performance**: CSS is cached by browser
- ✅ **Organization**: Clear separation of concerns
- ✅ **Standards**: Follows Odoo best practices
- ✅ **Collaboration**: Easier for teams to work on

## 🔍 Debugging

If styles don't appear:

1. **Check browser console** for CSS loading errors
2. **Verify file path** in manifest matches actual location
3. **Clear browser cache** (Ctrl+Shift+Delete)
4. **Check Odoo logs** for asset compilation errors
5. **Inspect element** to see if classes are applied

## 📖 Related Files

- **Manifest**: `__manifest__.py` (defines assets)
- **View XML**: `views/slide_channel_views.xml` (uses CSS classes)
- **Model**: `models/slide_channel.py` (defines fields)

---

**Last Updated**: 2025-12-06
**Version**: 19.0.1.0.0

