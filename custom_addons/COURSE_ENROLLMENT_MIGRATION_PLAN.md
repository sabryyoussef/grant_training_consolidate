# Course Enrollment Request Migration Plan
## Transfer from `grants_training_suite_v2` to `student_enrollment_portal`

---

## 📋 Executive Summary

This plan outlines the migration of the **Course Enrollment Request** system from `grants_training_suite_v2` to `student_enrollment_portal` module. This consolidation will:
- Group all student enrollment functionality in one module
- Improve module organization and maintainability
- Reduce dependencies between modules
- Create a cohesive student portal experience
- Integrate with OpenEduCat Core instead of grants_training_suite_v2

---

## 🎯 Migration Objectives

1. **Create** `course.enrollment.request` model in `student_enrollment_portal` (new model, not existing in v2)
2. **Adapt** enrollment wizard concepts from `gr.enrollment.wizard` for portal use
3. **Create** portal routes for course enrollment requests
4. **Create** portal templates for enrollment request submission
5. **Update** security rules and access rights
6. **Create** email templates and sequences
7. **Integrate** with OpenEduCat models (`op.student`, `op.course`, `op.batch`)
8. **Test** all functionality after migration

---

## 📦 Components to Migrate/Create

### 1. Model Files

#### Source Reference: `grants_training_suite_v2/models/enrollment_wizard.py`
- **Model:** `gr.enrollment.wizard` (transient wizard - backend only)
- **Purpose:** Backend enrollment wizard for admins
- **Note:** This is a wizard, not a persistent model. We need to CREATE a new `course.enrollment.request` model.

#### New Model: `student_enrollment_portal/models/course_enrollment_request.py`
- **Model Name:** `course.enrollment.request`
- **Type:** Persistent model (not transient)
- **Purpose:** Portal-based enrollment requests from students
- **Dependencies:** 
  - `op.student` (from openeducat_core)
  - `op.course` (from openeducat_core)
  - `op.batch` (from openeducat_core)
  - `mail.thread`, `mail.activity.mixin` (Odoo core)

**Key Fields:**
- `name` - Request number (sequence)
- `student_id` - Many2one to `op.student`
- `course_id` - Many2one to `op.course`
- `batch_id` - Many2one to `op.batch` (optional)
- `state` - Selection: draft, submitted, pending, approved, rejected
- `request_date` - Datetime
- `approval_date` - Datetime
- `rejection_reason` - Text
- `approved_by` - Many2one to `res.users`

**Key Methods:**
- `_compute_name()` - Auto-generate request numbers
- `action_submit()` - Submit request to pending
- `action_approve()` - Approve and create `op.student.course` enrollment
- `action_reject()` - Reject with reason
- `_create_student_course()` - Auto-create enrollment on approval

---

### 2. View Files

#### New File: `student_enrollment_portal/views/course_enrollment_request_views.xml`
- **Contains:**
  - List view (with status colors)
  - Form view (with workflow buttons)
  - Kanban view (grouped by status)
  - Search view (filters and group by)
  - Action windows
  - Menu items

**Menu Structure:**
```
Student Enrollment Portal
└── Enrollment Requests
    ├── All Requests
    ├── Pending Requests
    └── Approved Requests
```

---

### 3. Controller Routes

#### New Routes in: `student_enrollment_portal/controllers/portal.py`

**Routes to Create:**
1. `/my/available-courses` - Browse available courses (OpenEduCat courses)
2. `/my/courses/request/<course_id>` - Enrollment request form
3. `/my/courses/request/submit` - Submit enrollment request (POST)
4. `/my/enrollment-requests` - List student's enrollment requests

**Methods to Add:**
- `portal_available_courses()` - Show available `op.course` records
- `portal_enrollment_request_form()` - Display request form
- `portal_enrollment_request_submit()` - Handle form submission
- `portal_my_enrollment_requests()` - List student's requests

**Dashboard Integration:**
- Update portal home to include enrollment request counts

---

### 4. Portal Templates

#### Update: `student_enrollment_portal/views/portal_templates.xml`

**Templates to Add:**
1. `portal_available_courses` - Course catalog for authenticated users
2. `portal_enrollment_request_form` - Request submission form
3. `portal_enrollment_request_success` - Success confirmation page
4. `portal_enrollment_request_error` - Error page
5. `portal_my_enrollment_requests` - Student's request list

**Dashboard Updates:**
- Update portal dashboard to show pending enrollment requests
- Add enrollment request badge/count

---

### 5. Security Files

#### Update: `student_enrollment_portal/security/ir.model.access.csv`

**Access Rules to Add:**
```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_course_enrollment_request_public,course.enrollment.request.public,model_course_enrollment_request,base.group_public,1,0,0,0
access_course_enrollment_request_portal,course.enrollment.request.portal,model_course_enrollment_request,base.group_portal,1,1,1,0
access_course_enrollment_request_user,course.enrollment.request.user,model_course_enrollment_request,base.group_user,1,0,0,0
access_course_enrollment_request_faculty,course.enrollment.request.faculty,model_course_enrollment_request,openeducat_core.group_op_faculty,1,1,1,1
access_course_enrollment_request_manager,course.enrollment.request.manager,model_course_enrollment_request,openeducat_core.group_op_back_office_admin,1,1,1,1
```

#### Update: `student_enrollment_portal/security/security_rules.xml`

**Record Rules to Add:**
- Portal users can only see their own enrollment requests
- Managers and Faculty can see all requests

---

### 6. Data Files

#### Sequences
**Update:** `student_enrollment_portal/data/sequences.xml`

**Sequence Definition:**
```xml
<record id="sequence_course_enrollment_request" model="ir.sequence">
    <field name="name">Course Enrollment Request Sequence</field>
    <field name="code">course.enrollment.request</field>
    <field name="prefix">ENR</field>
    <field name="padding">5</field>
    <field name="number_increment">1</field>
    <field name="number_next">1</field>
</record>
```

#### Email Templates
**Update:** `student_enrollment_portal/data/email_templates.xml`

**Templates to Add:**
1. `email_template_enrollment_request_submitted` - Admin notification
2. `email_template_enrollment_request_approved` - Student approval notification
3. `email_template_enrollment_request_rejected` - Student rejection notification

---

### 7. Model Initialization

#### Update: `student_enrollment_portal/models/__init__.py`
```python
from . import student_registration
from . import course_enrollment_request  # NEW
```

---

## 🔄 Migration Steps

### Phase 1: Preparation (Before Migration)

1. **Backup Database**
   ```bash
   # Create full database backup
   pg_dump -U odoo <database_name> > backup_before_migration.sql
   ```

2. **Document Current State**
   - Note any existing enrollment workflows
   - Document OpenEduCat course structure
   - Document any customizations

3. **Create Migration Branch**
   ```bash
   git checkout -b feature/migrate-enrollment-requests
   ```

---

### Phase 2: Create New Model in Target Module (student_enrollment_portal)

#### Step 1: Create Model File
**File:** `student_enrollment_portal/models/course_enrollment_request.py`

**Key Points:**
- Model name: `course.enrollment.request`
- Inherit: `['mail.thread', 'mail.activity.mixin']`
- Use `op.student` instead of `gr.student`
- Use `op.course` instead of `gr.course.integration`
- Use `op.batch` instead of `gr.course.session`
- Create `op.student.course` on approval (OpenEduCat enrollment)

**Model Structure:**
```python
class CourseEnrollmentRequest(models.Model):
    _name = 'course.enrollment.request'
    _description = 'Course Enrollment Request'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc'
    
    name = fields.Char(string='Request Number', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    student_id = fields.Many2one('op.student', string='Student', required=True, tracking=True)
    course_id = fields.Many2one('op.course', string='Course', required=True, tracking=True)
    batch_id = fields.Many2one('op.batch', string='Batch', domain="[('course_id', '=', course_id)]", tracking=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('pending', 'Pending Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Status', default='draft', required=True, tracking=True)
    request_date = fields.Datetime(string='Request Date', default=fields.Datetime.now, tracking=True)
    approval_date = fields.Datetime(string='Approval Date', tracking=True)
    rejection_reason = fields.Text(string='Rejection Reason', tracking=True)
    approved_by = fields.Many2one('res.users', string='Approved By', tracking=True)
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('course.enrollment.request') or _('New')
        return super(CourseEnrollmentRequest, self).create(vals_list)
    
    def action_submit(self):
        """Submit request for review"""
        self.write({'state': 'submitted'})
        # Send notification to admins
    
    def action_approve(self):
        """Approve request and create enrollment"""
        self.ensure_one()
        # Create op.student.course record
        self._create_student_course()
        self.write({
            'state': 'approved',
            'approval_date': fields.Datetime.now(),
            'approved_by': self.env.user.id
        })
        # Send approval email
    
    def action_reject(self):
        """Reject request with reason"""
        self.ensure_one()
        if not self.rejection_reason:
            raise UserError(_('Please provide a rejection reason.'))
        self.write({'state': 'rejected'})
        # Send rejection email
    
    def _create_student_course(self):
        """Create op.student.course enrollment record"""
        self.ensure_one()
        # Check if already enrolled
        existing = self.env['op.student.course'].search([
            ('student_id', '=', self.student_id.id),
            ('course_id', '=', self.course_id.id),
            ('batch_id', '=', self.batch_id.id) if self.batch_id else [('batch_id', '=', False)]
        ])
        if existing:
            raise UserError(_('Student is already enrolled in this course/batch.'))
        
        # Create enrollment
        self.env['op.student.course'].create({
            'student_id': self.student_id.id,
            'course_id': self.course_id.id,
            'batch_id': self.batch_id.id if self.batch_id else False,
            'state': 'running',
        })
```

#### Step 2: Update models/__init__.py
```python
from . import student_registration
from . import course_enrollment_request
```

#### Step 3: Create View File
**File:** `student_enrollment_portal/views/course_enrollment_request_views.xml`

- List view with status colors
- Form view with workflow buttons
- Kanban view grouped by status
- Search view with filters
- Action windows
- Menu items

#### Step 4: Add Controller Routes
**File:** `student_enrollment_portal/controllers/portal.py`

Add methods:
- `portal_available_courses()` - List available `op.course` records
- `portal_enrollment_request_form()` - Show request form
- `portal_enrollment_request_submit()` - Handle POST submission
- `portal_my_enrollment_requests()` - List student's requests

#### Step 5: Add Portal Templates
**File:** `student_enrollment_portal/views/portal_templates.xml`

Add templates for:
- Course catalog
- Request form
- Success page
- Error page
- Request list

#### Step 6: Update Security Files
- Add access rules to `ir.model.access.csv`
- Add record rules to `security_rules.xml`
- Use `openeducat_core` groups instead of `grants_training_suite_v19` groups

#### Step 7: Update Data Files
- Add sequence to `sequences.xml`
- Add email templates to `email_templates.xml`

#### Step 8: Update Manifest
```python
'data': [
    # ... existing files ...
    'views/course_enrollment_request_views.xml',  # NEW
],
```

---

### Phase 3: Testing

#### Backend Testing
- [ ] Install/upgrade `student_enrollment_portal` module
- [ ] Verify model `course.enrollment.request` exists
- [ ] Check menu "Enrollment Requests" appears
- [ ] Create manual enrollment request
- [ ] Test workflow: Draft → Submitted → Pending → Approved
- [ ] Test workflow: Draft → Submitted → Pending → Rejected
- [ ] Verify `op.student.course` creation on approval
- [ ] Check email templates render correctly
- [ ] Verify security rules (portal users see only their requests)
- [ ] Test search and filters
- [ ] Test kanban view

#### Portal Testing
- [ ] Access `/my/available-courses` (authenticated)
- [ ] Browse available courses
- [ ] Click "Request Enrollment" button
- [ ] Fill and submit enrollment request form
- [ ] Verify success message
- [ ] Access `/my/enrollment-requests`
- [ ] View request status
- [ ] Check dashboard shows pending count
- [ ] Test duplicate request prevention
- [ ] Test already-enrolled prevention

#### Email Testing
- [ ] Submit request → verify admin receives email
- [ ] Approve request → verify student receives email
- [ ] Reject request → verify student receives email with reason

#### Integration Testing
- [ ] Approved request creates `op.student.course` record
- [ ] Enrollment linked to student and course correctly
- [ ] Batch assignment works if batch selected
- [ ] Student can see enrollment in OpenEduCat portal

---

## ⚠️ Key Differences from Original Plan

### Model Changes:
- **Source:** `gr.enrollment.wizard` (transient wizard) → **Target:** `course.enrollment.request` (persistent model)
- **Student Model:** `gr.student` → `op.student` (OpenEduCat)
- **Course Model:** `gr.course.integration` → `op.course` (OpenEduCat)
- **Session Model:** `gr.course.session` → `op.batch` (OpenEduCat)
- **Enrollment Model:** Create `op.student.course` instead of session

### Group Changes:
- **Source Groups:** `grants_training_suite_v19.group_manager`, `grants_training_suite_v19.group_agent`
- **Target Groups:** `openeducat_core.group_op_back_office_admin`, `openeducat_core.group_op_faculty`

### Module Dependencies:
- **Source:** `grants_training_suite_v19`
- **Target:** `openeducat_core` (already in dependencies)

---

## 🔙 Rollback Plan

If migration fails:

1. **Restore Database Backup**
   ```bash
   psql -U odoo <database_name> < backup_before_migration.sql
   ```

2. **Revert Code Changes**
   ```bash
   git checkout main
   git branch -D feature/migrate-enrollment-requests
   ```

3. **Reinstall Modules**
   - Upgrade `student_enrollment_portal`
   - Restart Odoo

---

## 📊 Migration Checklist

### Pre-Migration
- [ ] Database backup created
- [ ] Git branch created
- [ ] Current state documented
- [ ] Team notified of migration

### Migration - Create New Model
- [ ] Model file created
- [ ] Model imports updated
- [ ] View file created
- [ ] Controller routes added
- [ ] Portal templates added
- [ ] Security rules added
- [ ] Sequences added
- [ ] Email templates added
- [ ] Manifest updated

### Testing
- [ ] Backend tests passed
- [ ] Portal tests passed
- [ ] Email tests passed
- [ ] Integration tests passed

### Post-Migration
- [ ] Documentation updated
- [ ] Changes committed
- [ ] Team notified of completion

---

## 📝 Notes

- **Estimated Time:** 6-8 hours (creating new model vs migrating existing)
- **Risk Level:** Medium (new model creation)
- **Downtime:** None (new functionality, doesn't affect existing)
- **Testing Required:** Comprehensive (all workflows)

---

## 🎯 Success Criteria

1. ✅ Enrollment request model works in `student_enrollment_portal`
2. ✅ Portal routes work correctly
3. ✅ Students can request enrollment through portal
4. ✅ Admins can approve/reject requests
5. ✅ Approved requests create OpenEduCat enrollments
6. ✅ Email notifications work
7. ✅ Security rules enforced correctly
8. ✅ No errors in logs
9. ✅ All tests pass

---

**Created:** 2025-11-24  
**Last Updated:** 2025-11-24  
**Status:** Ready for Implementation  
**Source Module:** `grants_training_suite_v2`  
**Target Module:** `student_enrollment_portal`  
**Integration:** OpenEduCat Core
