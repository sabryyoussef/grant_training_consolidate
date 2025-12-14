# Motakamel Demo Data Scripts

This directory contains Python scripts for populating demo data in the Motakamel module. These scripts use Odoo's shell interface to insert test data directly into the database.

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Core Demo Data Scripts](#core-demo-data-scripts)
3. [Utility Scripts](#utility-scripts)
4. [Execution Order](#execution-order)
5. [Usage Instructions](#usage-instructions)

---

## Prerequisites

- Odoo 19 server installed and configured
- `test_project_dev` database created
- Virtual environment activated (`venv19`)
- OpenEduCat modules installed
- Batch Intake module installed
- Motakamel module installed

## 🚀 Automatic Demo Data Loading

**NEW**: Demo data now loads automatically when the module is installed or updated!

The module includes a `post_init_hook` that automatically executes all demo data scripts in the correct order. This means:

- ✅ Install/upgrade the module → Demo data loads automatically
- ✅ No manual script execution needed
- ✅ All scripts run in proper sequence
- ✅ Errors are logged but don't stop the process
- ✅ Progress tracked in Odoo logs

To install with auto-loading:
```bash
odoo-bin -c config.conf -d database -i motakamel
```

To upgrade with auto-loading:
```bash
odoo-bin -c config.conf -d database -u motakamel
```

---

## Core Demo Data Scripts

### 1. `insert_demo_programs.py`
**Purpose**: Creates 5 certification programs with complete details

**Creates**:
- CBPLC - Certified Business Professional in Leading Through Change
- PHRI - Professional in Human Resources – International
- PMP - Project Management Professional
- CBPCS - Certified Business Professional in Customer Services
- CAFM - Certified Associate in Facilities Management

**Data includes**: Program names, codes, descriptions (EN/AR), levels, durations, pricing, status

**Usage**:
```bash
cd /home/sabry3/sabry_backup/odoo_base/base_odoo_19
echo "exec(open('projects/test_project/custom_addons/grant_training_consolidate/custom_addons/motakamel/demo_data_scripts/insert_demo_programs.py').read())" | venv19/bin/python odoo19/odoo19/odoo-bin shell -c projects/test_project/config/odoo.conf -d test_project_dev --no-http
```

---

### 2. `insert_demo_accreditations.py`
**Purpose**: Creates accreditation records linking programs to international bodies

**Creates**:
- 5 accreditation records (one per program)
- Links to bodies: IBTA, HRCI, PMI, IBTA, IFMA

**Data includes**: Issuing bodies, accreditation codes, validity dates, verification URLs, renewal requirements

---

### 3. `insert_demo_audiences.py`
**Purpose**: Creates target audience profiles for each program

**Creates**:
- 15 audience records (3 per program)
- Public sector, private sector, and individual audiences

**Data includes**: Sector types, career levels, experience requirements, prerequisites, job titles

---

### 4. `insert_demo_pricing.py`
**Purpose**: Creates pricing plans with payment options

**Creates**:
- 9 pricing plans across programs
- Standard, early bird, and corporate pricing tiers

**Data includes**: Price amounts (EGP), installments, refund policies, payment methods, discounts

---

### 5. `insert_demo_credentials.py`
**Purpose**: Creates digital credential and certificate configurations

**Creates**:
- 5 credential records (one per program)
- Certificate templates and badge configurations

**Data includes**: Serial number formats, template references, digital badge platforms (Credly/Open Badges), renewal cycles

---

### 6. `insert_demo_marketing.py`
**Purpose**: Creates marketing campaigns for each program

**Creates**:
- 5 comprehensive marketing campaigns
- SEO, social media, and analytics configurations

**Data includes**:
- Campaign names, budgets (35K-95K EGP), dates
- Meta titles, descriptions, keywords
- Social media posts (Facebook, LinkedIn, Instagram)
- Analytics IDs (Google Analytics, Facebook Pixel)
- Performance metrics (impressions, clicks, leads, conversions)

---

### 7. `insert_demo_courses.py`
**Purpose**: Creates OpenEduCat courses matching motakamel programs

**Creates**:
- 3 courses: CBPLC, PHRI, PMP
- Course codes for identification

**Note**: Course names must match program names for proper enrollment linking

---

### 8. `insert_demo_students_batches.py`
**Purpose**: Creates demo students and batch intakes with enrollments

**Creates**:
- 10 demo students with Egyptian names
- 3 batch intakes linked to courses
- Student enrollments (4 + 3 + 3 distribution)

**Data includes**: Student names, emails, phones, batch capacities, enrollment dates

---

### 9. `create_deliveries.py`
**Purpose**: Creates delivery schedules to populate enrollment statistics

**Creates**:
- 3 delivery records linked to programs
- Delivery details matching batch intakes

**Data includes**: Delivery names, dates, capacities, training modes, current enrollments

**Note**: Required for enrollment summary statistics to display in marketing campaigns

---

## Utility Scripts

### 10. `update_course_names.py`
**Purpose**: Synchronizes course names with program names for proper enrollment linking

**What it does**: Updates OpenEduCat course names to exactly match motakamel program names, enabling the computed field `_compute_students_and_leads` to find related batch intakes

---

### 11. `recompute_enrollments.py`
**Purpose**: Forces recomputation of enrollment data for all marketing campaigns

**What it does**: Manually triggers `_compute_students_and_leads` to update enrolled student counts and statistics

---

### 12. `debug_enrollment.py`
**Purpose**: Diagnostic tool to check enrollment data connections

**What it shows**:
- Marketing campaign details
- Batch intake relationships
- Enrolled student counts
- Program and course name matching

---

### 13. `check_openeducat.py`
**Purpose**: Verifies OpenEduCat installation and module availability

**What it checks**:
- `op.student` model availability
- View definitions (tree/list views)
- Actions for student records
- Installed OpenEduCat modules
- Batch intake module status

---

### 14. `load_motakamel_demo.py`
**Purpose**: Master script to load all demo data in sequence

**Executes**: All core demo data scripts in the correct order

---

### 15. `insert_demo_deliveries_students.py`
**Purpose**: Earlier version of delivery and student creation (superseded by separate scripts)

**Status**: Legacy - use `insert_demo_students_batches.py` and `create_deliveries.py` instead

---

## Execution Order

For a fresh database, execute scripts in this order:

```bash
# 1. Core Program Data
./insert_demo_programs.py
./insert_demo_accreditations.py
./insert_demo_audiences.py
./insert_demo_pricing.py
./insert_demo_credentials.py
./insert_demo_marketing.py

# 2. OpenEduCat Integration
./insert_demo_courses.py
./insert_demo_students_batches.py

# 3. Synchronization
./update_course_names.py

# 4. Delivery Schedules
./create_deliveries.py

# 5. Refresh Computed Fields
./recompute_enrollments.py

# 6. Verify (optional)
./debug_enrollment.py
./check_openeducat.py
```

---

## Usage Instructions

### Running Individual Scripts

All scripts are designed to be executed via Odoo shell:

```bash
cd /home/sabry3/sabry_backup/odoo_base/base_odoo_19

echo "exec(open('projects/test_project/custom_addons/grant_training_consolidate/custom_addons/motakamel/demo_data_scripts/SCRIPT_NAME.py').read())" | \
venv19/bin/python odoo19/odoo19/odoo-bin shell \
-c projects/test_project/config/odoo.conf \
-d test_project_dev \
--no-http
```

### Running All Scripts (Master Loader)

```bash
cd /home/sabry3/sabry_backup/odoo_base/base_odoo_19

echo "exec(open('projects/test_project/custom_addons/grant_training_consolidate/custom_addons/motakamel/demo_data_scripts/load_motakamel_demo.py').read())" | \
venv19/bin/python odoo19/odoo19/odoo-bin shell \
-c projects/test_project/config/odoo.conf \
-d test_project_dev \
--no-http
```

---

## Data Summary

After running all scripts, the database will contain:

| Entity | Count | Details |
|--------|-------|---------|
| **Programs** | 5 | Complete certification programs |
| **Accreditations** | 5 | International accreditation bodies |
| **Target Audiences** | 15 | 3 per program (public/private/individual) |
| **Pricing Plans** | 9 | Multiple tiers per program |
| **Credentials** | 5 | Certificate and badge configurations |
| **Marketing Campaigns** | 5 | Full campaigns with social media |
| **Courses** | 3 | OpenEduCat courses |
| **Students** | 10 | Demo student records |
| **Batch Intakes** | 3 | Enrollment cohorts |
| **Deliveries** | 3 | Delivery schedules |

**Total Enrolled Students**: 10 (distributed: 4 + 3 + 3)

---

## Notes

- **Database Safety**: All scripts check for existing records before inserting
- **Transactions**: Scripts use `env.cr.commit()` for safe data persistence
- **Error Handling**: Includes try/catch blocks with rollback on failure
- **Idempotent**: Can be run multiple times without creating duplicates
- **Bilingual**: Data includes both English and Arabic content where applicable

---

## Troubleshooting

### Issue: Enrollment data not showing
**Solution**: Run `update_course_names.py` then `recompute_enrollments.py`

### Issue: View type error "tree not found"
**Solution**: Module was updated to use `list` instead of `tree` view mode (already fixed in code)

### Issue: Students created but not appearing in marketing
**Solution**: Run `create_deliveries.py` to create delivery records

### Issue: Want to verify installation
**Solution**: Run `check_openeducat.py` and `debug_enrollment.py`

---

## File Locations

```
motakamel/
├── demo_data_scripts/
│   ├── README.md                           # This file
│   ├── insert_demo_programs.py             # Core program data
│   ├── insert_demo_accreditations.py       # Accreditation records
│   ├── insert_demo_audiences.py            # Target audiences
│   ├── insert_demo_pricing.py              # Pricing plans
│   ├── insert_demo_credentials.py          # Certificates & badges
│   ├── insert_demo_marketing.py            # Marketing campaigns
│   ├── insert_demo_courses.py              # OpenEduCat courses
│   ├── insert_demo_students_batches.py     # Students & batch intakes
│   ├── create_deliveries.py                # Delivery schedules
│   ├── update_course_names.py              # Sync course names
│   ├── recompute_enrollments.py            # Refresh computed fields
│   ├── debug_enrollment.py                 # Diagnostic tool
│   ├── check_openeducat.py                 # Installation checker
│   ├── load_motakamel_demo.py              # Master loader script
│   └── insert_demo_deliveries_students.py  # Legacy combined script
```

---

## Contact & Support

For issues or questions about these scripts, refer to the main Motakamel module documentation or contact the development team.

**Module**: Motakamel Training & Certification Platform  
**Version**: 19.0  
**Last Updated**: December 14, 2025
