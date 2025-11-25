# Student Lifecycle Dashboard

## Overview

The Student Lifecycle Dashboard provides a comprehensive workflow management system for tracking students from initial registration through to completion. It integrates all registration sources and provides managers with a unified view of the student journey.

## Features

### 📊 Visual Workflow Management
- **Kanban View**: Overview of all workflows with real-time statistics
- **Stage-based Navigation**: Easy access to each stage of the student lifecycle
- **Visual Workflow Diagram**: Graphical representation of the complete student journey

### 📈 Real-time Statistics
- Total registrations from all sources
- Admission counts
- Enrollment statistics
- Student population tracking
- Source breakdown (Portal, Batch, Contact Pool)

### 🔄 Complete Lifecycle Stages

1. **Registration Sources**
   - Portal Registration (student_enrollment_portal)
   - Batch Intake (batch_intake)
   - Contact Pool (contact_pool_manager)

2. **Admission Process**
   - Admission Processing (openeducat_admission)
   - Application Review

3. **Enrollment**
   - Student Enrollment (op.student.course)
   - Student Management (op.student)

4. **Academic Progress**
   - Attendance Tracking (openeducat_attendance)
   - Assignments (openeducat_assignment)
   - Examinations (openeducat_exam)

5. **Completion**
   - Graduation tracking
   - Performance analytics

## Installation

1. Ensure all dependencies are installed:
   - `openeducat_core`
   - `openeducat_admission`
   - `student_enrollment_portal`
   - `batch_intake`
   - `contact_pool_manager`
   - `admission_integration`

2. Install the module through Odoo Apps

3. Access the dashboard via: **Student Lifecycle > Dashboard**

## Usage

### For Managers

1. **View Dashboard**: Navigate to Student Lifecycle > Dashboard
2. **Select Workflow**: Click on the Student Lifecycle card
3. **Navigate Stages**: Use the stage cards to access different modules
4. **Monitor Statistics**: View real-time statistics on the dashboard
5. **Track Progress**: Follow students through each stage of the lifecycle

### Stage Actions

Each stage provides quick access to related modules:
- Click the action button on any stage card
- Direct navigation to relevant records
- Filtered views based on stage context

## Module Structure

```
student_lifecycle_dashboard/
├── models/
│   ├── student_lifecycle_dashboard.py  # Main dashboard model
│   └── student_lifecycle_stage.py      # Stage model
├── views/
│   ├── student_lifecycle_dashboard_views.xml  # Kanban and form views
│   └── student_lifecycle_menu.xml             # Menu definitions
├── data/
│   └── student_lifecycle_data.xml      # Workflow and stage data
├── security/
│   └── ir.model.access.csv              # Access rights
└── static/
    └── src/css/
        └── dashboard.css                # Custom styling
```

## Integration Points

### Registration Sources
- **Portal**: `student.registration` model
- **Batch Intake**: `batch.intake` model
- **Contact Pool**: `contact.pool` model

### Admission
- **Admissions**: `op.admission` model (via admission_integration)

### Enrollment
- **Students**: `op.student` model
- **Enrollments**: `op.student.course` model

### Academic
- **Attendance**: `op.attendance.sheet` model
- **Assignments**: `op.assignment` model
- **Exams**: `op.exam` model

## Customization

### Adding New Stages

1. Create a new stage record in `data/student_lifecycle_data.xml`
2. Define the action method in `models/student_lifecycle_stage.py`
3. Add the action mapping to `action_execute_stage` method

### Modifying Statistics

Edit the `_compute_statistics` method in `student_lifecycle_dashboard.py` to add or modify statistics calculations.

## Technical Details

- **Odoo Version**: 19.0
- **License**: LGPL-3
- **Author**: Edafa

## Support

For issues or questions, contact the development team.


