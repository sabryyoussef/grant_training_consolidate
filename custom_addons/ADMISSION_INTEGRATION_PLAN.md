# Admission Integration Plan
## Unified Admission System - Collecting from Multiple Sources

---

## 📋 Executive Summary

This plan outlines the integration of all student registration sources into the OpenEduCat Admission system (`op.admission`). The goal is to create a unified admission tree view (`openeducat_admission.view_op_admission_tree`) that collects eligible students from:

1. **Student Registration Portal** (`student.registration`)
2. **Batch Intake** (`batch.intake`)
3. **Contact Pool Manager** (`contact.pool`)

All eligible students from these sources will appear in the single admission list view for centralized management.

---

## 🎯 Objectives

1. **Unified View**: All student applications appear in `op.admission` tree view
2. **Source Tracking**: Track which module/source each admission came from
3. **Data Synchronization**: Auto-sync or manual sync from source modules
4. **Eligibility Criteria**: Apply eligibility rules before creating admission records
5. **Bidirectional Linking**: Link admission records back to source records
6. **Workflow Integration**: Use existing OpenEduCat admission workflow
7. **No Data Duplication**: Prevent duplicate admissions from same source

---

## 📦 Current State Analysis

### 1. OpenEduCat Admission (`op.admission`)

**Model:** `op.admission`
**Key Fields:**
- `application_number` (sequence)
- `name`, `first_name`, `middle_name`, `last_name`
- `email`, `phone`, `mobile`
- `birth_date`, `gender`
- `course_id`, `batch_id`
- `register_id` (required - links to `op.admission.register`)
- `state`: draft → submit → confirm → admission → done
- `student_id` (Many2one to `op.student`)

**Workflow:**
- Draft → Submit → Confirm → Admission Confirm → Enroll → Done
- Can be Rejected, Cancelled, or set to Pending

**View:** `view_op_admission_tree` (list view)

---

### 2. Student Registration Portal (`student.registration`)

**Model:** `student.registration`
**Key Fields:**
- `name` (Registration Number - sequence)
- `student_name_english`, `student_name_arabic`
- `email`, `phone`
- `birth_date`, `gender` (male/female)
- `nationality`
- `english_level`
- `state`: draft → submitted → eligibility_review → document_review → approved → enrolled

**Eligibility Criteria:**
- Must be in `approved` or `enrolled` state
- Has all required information

**Link to Admission:**
- Need to create `op.admission` when state becomes `approved`

---

### 3. Batch Intake (`batch.intake`)

**Model:** `batch.intake`
**Key Fields:**
- `name`, `code`
- `course_id`, `batch_id` (OpenEduCat)
- `state`: draft → uploaded → validated → processed → open → closed
- `openeducat_student_ids` (One2many to `op.student`)

**Eligibility Criteria:**
- Must be in `processed` state
- Has `openeducat_student_ids` (students created)
- Students should be eligible for admission

**Link to Admission:**
- Need to create `op.admission` for each student in `openeducat_student_ids`
- Link to `batch.intake` record

---

### 4. Contact Pool Manager (`contact.pool`)

**Model:** `contact.pool`
**Key Fields:**
- `name` (Pool Name)
- `contact_ids` (One2many to `res.partner`)
- `sales_person_id`

**Eligibility Criteria:**
- Contacts in pool (`res.partner` records)
- Contacts marked as eligible (may need new field)
- Contacts not already students

**Link to Admission:**
- Need to create `op.admission` for eligible contacts
- Link to `contact.pool` record

---

## 🔄 Integration Architecture

### Approach 1: Extend `op.admission` Model (Recommended)

**Advantages:**
- Uses existing OpenEduCat workflow
- No duplicate data
- Centralized management
- Maintains OpenEduCat standards

**Implementation:**
1. Add source tracking fields to `op.admission`
2. Create sync methods in each source module
3. Auto-create `op.admission` when eligibility criteria met
4. Link admission back to source record

---

## 📝 Implementation Plan

### Phase 1: Extend `op.admission` Model

#### Step 1.1: Add Source Tracking Fields

**File:** Create new module or extend `openeducat_admission/models/admission.py`

**Fields to Add:**
```python
# Source Tracking
source_type = fields.Selection([
    ('manual', 'Manual Entry'),
    ('student_registration', 'Student Registration Portal'),
    ('batch_intake', 'Batch Intake'),
    ('contact_pool', 'Contact Pool Manager'),
], string='Source Type', default='manual', tracking=True)

source_registration_id = fields.Many2one(
    'student.registration',
    string='Source Registration',
    readonly=True,
    tracking=True,
    help='Student registration record this admission came from'
)

source_batch_intake_id = fields.Many2one(
    'batch.intake',
    string='Source Batch Intake',
    readonly=True,
    tracking=True,
    help='Batch intake record this admission came from'
)

source_contact_pool_id = fields.Many2one(
    'contact.pool',
    string='Source Contact Pool',
    readonly=True,
    tracking=True,
    help='Contact pool this admission came from'
)

source_contact_id = fields.Many2one(
    'res.partner',
    string='Source Contact',
    readonly=True,
    tracking=True,
    help='Contact/Partner record this admission came from'
)

is_imported = fields.Boolean(
    string='Imported from External Source',
    default=False,
    tracking=True,
    help='Indicates if this admission was imported from another module'
)
```

---

### Phase 2: Create Sync Methods

#### Step 2.1: Sync from Student Registration Portal

**File:** `student_enrollment_portal/models/student_registration.py`

**Method to Add:**
```python
def action_create_admission(self):
    """Create op.admission record from approved registration"""
    self.ensure_one()
    
    if self.state != 'approved':
        raise UserError(_('Only approved registrations can create admission records.'))
    
    # Check if admission already exists
    existing_admission = self.env['op.admission'].search([
        ('source_registration_id', '=', self.id)
    ], limit=1)
    
    if existing_admission:
        raise UserError(_('Admission record already exists for this registration.'))
    
    # Get default admission register (or create one)
    admission_register = self._get_default_admission_register()
    
    # Split name into first/last
    name_parts = self.student_name_english.strip().split(' ', 1)
    first_name = name_parts[0] if name_parts else self.student_name_english
    last_name = name_parts[1] if len(name_parts) > 1 else ''
    
    # Map gender
    gender_map = {'male': 'm', 'female': 'f'}
    gender = gender_map.get(self.gender, 'm')
    
    # Create admission record
    admission_vals = {
        'name': self.student_name_english,
        'first_name': first_name,
        'last_name': last_name,
        'email': self.email,
        'phone': self.phone,
        'birth_date': self.birth_date,
        'gender': gender,
        'register_id': admission_register.id,
        'source_type': 'student_registration',
        'source_registration_id': self.id,
        'is_imported': True,
        'state': 'submit',  # Start at submitted state
        'application_date': fields.Datetime.now(),
    }
    
    admission = self.env['op.admission'].create(admission_vals)
    
    self.message_post(
        body=_('Admission record created: %s') % admission.application_number
    )
    
    return admission
```

**Auto-Trigger:**
- Override `action_final_approve()` to auto-create admission
- Or create scheduled action to sync approved registrations

---

#### Step 2.2: Sync from Batch Intake

**File:** `batch_intake/models/batch_intake.py`

**Method to Add:**
```python
def action_create_admissions_from_students(self):
    """Create op.admission records for all students in this batch intake"""
    self.ensure_one()
    
    if self.state != 'processed':
        raise UserError(_('Batch intake must be processed before creating admissions.'))
    
    if not self.openeducat_student_ids:
        raise UserError(_('No students found in this batch intake.'))
    
    # Get default admission register
    admission_register = self._get_default_admission_register()
    
    created_admissions = self.env['op.admission']
    
    for student in self.openeducat_student_ids:
        # Check if admission already exists
        existing_admission = self.env['op.admission'].search([
            ('source_batch_intake_id', '=', self.id),
            ('email', '=', student.email)
        ], limit=1)
        
        if existing_admission:
            _logger.warning(f'Admission already exists for student {student.name}')
            continue
        
        # Create admission record
        admission_vals = {
            'name': student.name,
            'first_name': student.first_name,
            'last_name': student.last_name,
            'email': student.email,
            'phone': student.phone or student.mobile,
            'birth_date': student.birth_date,
            'gender': student.gender,
            'course_id': self.course_id.id if self.course_id else False,
            'batch_id': self.batch_id.id if self.batch_id else False,
            'register_id': admission_register.id,
            'source_type': 'batch_intake',
            'source_batch_intake_id': self.id,
            'is_imported': True,
            'state': 'submit',
            'application_date': fields.Datetime.now(),
        }
        
        admission = self.env['op.admission'].create(admission_vals)
        created_admissions += admission
    
    self.message_post(
        body=_('Created %d admission record(s) from batch intake students.') % len(created_admissions)
    )
    
    return created_admissions
```

**Button in View:**
- Add "Create Admissions" button in batch intake form
- Visible when state is `processed` and has students

---

#### Step 2.3: Sync from Contact Pool

**File:** `contact_pool_manager/models/contact_pool.py`

**Method to Add:**
```python
def action_create_admissions_from_contacts(self):
    """Create op.admission records for eligible contacts in pool"""
    self.ensure_one()
    
    if not self.contact_ids:
        raise UserError(_('No contacts in this pool.'))
    
    # Get default admission register
    admission_register = self._get_default_admission_register()
    
    # Filter eligible contacts (not companies, not already students)
    eligible_contacts = self.contact_ids.filtered(
        lambda c: not c.is_company and not c.is_student
    )
    
    if not eligible_contacts:
        raise UserError(_('No eligible contacts found in this pool.'))
    
    created_admissions = self.env['op.admission']
    
    for contact in eligible_contacts:
        # Check if admission already exists
        existing_admission = self.env['op.admission'].search([
            ('source_contact_pool_id', '=', self.id),
            ('source_contact_id', '=', contact.id)
        ], limit=1)
        
        if existing_admission:
            _logger.warning(f'Admission already exists for contact {contact.name}')
            continue
        
        # Split name
        name_parts = contact.name.strip().split(' ', 1)
        first_name = name_parts[0] if name_parts else contact.name
        last_name = name_parts[1] if len(name_parts) > 1 else ''
        
        # Create admission record
        admission_vals = {
            'name': contact.name,
            'first_name': first_name,
            'last_name': last_name,
            'email': contact.email or '',
            'phone': contact.phone or contact.mobile,
            'birth_date': False,  # May not be available
            'gender': 'm',  # Default, can be updated
            'register_id': admission_register.id,
            'source_type': 'contact_pool',
            'source_contact_pool_id': self.id,
            'source_contact_id': contact.id,
            'is_imported': True,
            'state': 'draft',  # Start at draft for manual review
            'application_date': fields.Datetime.now(),
        }
        
        admission = self.env['op.admission'].create(admission_vals)
        created_admissions += admission
    
    self.message_post(
        body=_('Created %d admission record(s) from pool contacts.') % len(created_admissions)
    )
    
    return created_admissions
```

**Button in View:**
- Add "Create Admissions" button in contact pool form
- Visible when pool has contacts

---

### Phase 3: Helper Methods

#### Step 3.1: Default Admission Register

**Add to each source module:**

```python
def _get_default_admission_register(self):
    """Get or create default admission register"""
    # Try to find active admission register
    register = self.env['op.admission.register'].search([
        ('active', '=', True),
        ('start_date', '<=', fields.Date.today()),
        ('end_date', '>=', fields.Date.today())
    ], limit=1, order='start_date desc')
    
    if not register:
        # Create default register if none exists
        register = self.env['op.admission.register'].create({
            'name': 'Default Admission Register %s' % fields.Date.today().year,
            'start_date': fields.Date.today(),
            'end_date': fields.Date.today() + relativedelta(years=1),
            'active': True,
        })
    
    return register
```

---

### Phase 4: Update Views

#### Step 4.1: Update Admission Tree View

**File:** `openeducat_admission/views/admission_view.xml`

**Add Fields:**
```xml
<field name="source_type" optional="show"/>
<field name="source_registration_id" optional="hide"/>
<field name="source_batch_intake_id" optional="hide"/>
<field name="source_contact_pool_id" optional="hide"/>
<field name="is_imported" optional="hide"/>
```

**Add Filters:**
```xml
<filter string="From Registration Portal" name="filter_source_registration" 
        domain="[('source_type', '=', 'student_registration')]"/>
<filter string="From Batch Intake" name="filter_source_batch_intake" 
        domain="[('source_type', '=', 'batch_intake')]"/>
<filter string="From Contact Pool" name="filter_source_contact_pool" 
        domain="[('source_type', '=', 'contact_pool')]"/>
<filter string="Imported" name="filter_imported" 
        domain="[('is_imported', '=', True)]"/>
```

---

#### Step 4.2: Update Admission Form View

**Add Source Information Section:**
```xml
<group string="Source Information" invisible="source_type == 'manual'">
    <field name="source_type" readonly="1"/>
    <field name="source_registration_id" readonly="1" 
           invisible="source_type != 'student_registration'"/>
    <field name="source_batch_intake_id" readonly="1" 
           invisible="source_type != 'batch_intake'"/>
    <field name="source_contact_pool_id" readonly="1" 
           invisible="source_type != 'contact_pool'"/>
    <field name="source_contact_id" readonly="1" 
           invisible="source_type != 'contact_pool'"/>
    <field name="is_imported" readonly="1"/>
</group>
```

---

### Phase 5: Add Buttons to Source Modules

#### Step 5.1: Student Registration Portal

**File:** `student_enrollment_portal/views/student_registration_views.xml`

**Add Button:**
```xml
<button name="action_create_admission" string="Create Admission" 
        type="object" class="oe_highlight" 
        invisible="state != 'approved' or source_admission_id"
        groups="openeducat_core.group_op_back_office_admin"/>
```

**Add Field:**
```python
# In student_registration.py
source_admission_id = fields.Many2one(
    'op.admission',
    string='Admission Record',
    readonly=True,
    tracking=True
)
```

---

#### Step 5.2: Batch Intake

**File:** `batch_intake/views/batch_intake_views.xml`

**Add Button:**
```xml
<button name="action_create_admissions_from_students" 
        string="Create Admissions" 
        type="object" class="oe_highlight" 
        invisible="state != 'processed' or not openeducat_student_ids"
        groups="openeducat_core.group_op_back_office_admin"/>
```

---

#### Step 5.3: Contact Pool

**File:** `contact_pool_manager/views/contact_pool_views.xml`

**Add Button:**
```xml
<button name="action_create_admissions_from_contacts" 
        string="Create Admissions from Contacts" 
        type="object" class="oe_highlight" 
        invisible="contact_count == 0"
        groups="sales_team.group_sale_manager"/>
```

---

### Phase 6: Automated Sync (Optional)

#### Step 6.1: Scheduled Actions

**Create scheduled actions to auto-sync:**

1. **Student Registration Auto-Sync:**
   - Run daily
   - Find approved registrations without admission
   - Auto-create admissions

2. **Batch Intake Auto-Sync:**
   - Run after batch processing
   - Auto-create admissions for processed batches

3. **Contact Pool Auto-Sync:**
   - Manual only (recommended)
   - Or scheduled for specific pools

---

## 🔒 Security & Access Rights

### Update Access Rules

**File:** `openeducat_admission/security/ir.model.access.csv`

Ensure all modules have read access to `op.admission`:
- Student Registration Portal: Read/Write
- Batch Intake: Read/Write
- Contact Pool: Read/Write

---

## 📊 Data Flow Diagram

```
┌─────────────────────────┐
│ Student Registration    │
│ (approved state)        │
└───────────┬─────────────┘
            │
            │ action_create_admission()
            ▼
┌─────────────────────────┐
│   op.admission          │
│   (source_type =        │
│    student_registration)│
└─────────────────────────┘
            ▲
            │
┌───────────┴─────────────┐
│  Batch Intake          │
│  (processed state)     │
└───────────┬─────────────┘
            │
            │ action_create_admissions_from_students()
            ▼
┌─────────────────────────┐
│   op.admission          │
│   (source_type =        │
│    batch_intake)        │
└─────────────────────────┘
            ▲
            │
┌───────────┴─────────────┐
│  Contact Pool           │
│  (eligible contacts)   │
└───────────┬─────────────┘
            │
            │ action_create_admissions_from_contacts()
            ▼
┌─────────────────────────┐
│   op.admission          │
│   (source_type =        │
│    contact_pool)        │
└─────────────────────────┘
```

---

## ✅ Implementation Checklist

### Phase 1: Model Extension
- [ ] Extend `op.admission` model with source tracking fields
- [ ] Add source type selection field
- [ ] Add source reference fields (Many2one)
- [ ] Add `is_imported` boolean field
- [ ] Update model constraints if needed

### Phase 2: Sync Methods
- [ ] Add `action_create_admission()` to `student.registration`
- [ ] Add `action_create_admissions_from_students()` to `batch.intake`
- [ ] Add `action_create_admissions_from_contacts()` to `contact.pool`
- [ ] Add `_get_default_admission_register()` helper method
- [ ] Add duplicate prevention logic

### Phase 3: Views
- [ ] Update admission tree view with source fields
- [ ] Update admission form view with source section
- [ ] Add filters for source types
- [ ] Add buttons to source module views
- [ ] Add source reference fields to source modules

### Phase 4: Testing
- [ ] Test sync from Student Registration
- [ ] Test sync from Batch Intake
- [ ] Test sync from Contact Pool
- [ ] Test duplicate prevention
- [ ] Test admission workflow after sync
- [ ] Test view filters and grouping

### Phase 5: Documentation
- [ ] Document sync process
- [ ] Document eligibility criteria
- [ ] Create user guide
- [ ] Update module descriptions

---

## ⚠️ Important Considerations

1. **Admission Register Requirement:**
   - `op.admission` requires `register_id`
   - Must create default register or select existing one
   - Register must be active and within date range

2. **Data Mapping:**
   - Gender mapping: `male/female` → `m/f`
   - Name splitting: Full name → first_name/last_name
   - Date formats: Ensure compatibility

3. **Eligibility Criteria:**
   - Student Registration: Must be `approved`
   - Batch Intake: Must be `processed` with students
   - Contact Pool: Must be eligible contacts (not companies, not students)

4. **Duplicate Prevention:**
   - Check by email + source
   - Check by source record ID
   - Prevent multiple admissions from same source

5. **State Management:**
   - Student Registration: Start at `submit` state
   - Batch Intake: Start at `submit` state
   - Contact Pool: Start at `draft` state (needs review)

6. **Course/Batch Assignment:**
   - Batch Intake: Has course/batch info
   - Student Registration: May need manual assignment
   - Contact Pool: Needs manual assignment

---

## 🎯 Success Criteria

1. ✅ All eligible students appear in `op.admission` tree view
2. ✅ Source tracking works correctly
3. ✅ No duplicate admissions created
4. ✅ Admission workflow functions normally
5. ✅ Links back to source records work
6. ✅ Filters and views display correctly
7. ✅ Buttons and actions work as expected

---

## 📝 Notes

- **Estimated Time:** 12-16 hours
- **Risk Level:** Medium (extends core OpenEduCat module)
- **Dependencies:** All three source modules must be installed
- **Testing Required:** Comprehensive (all sync paths)

---

**Created:** 2025-11-24  
**Last Updated:** 2025-11-24  
**Status:** Ready for Implementation  
**Target View:** `openeducat_admission.view_op_admission_tree`  
**Source Modules:** `student_enrollment_portal`, `batch_intake`, `contact_pool_manager`

