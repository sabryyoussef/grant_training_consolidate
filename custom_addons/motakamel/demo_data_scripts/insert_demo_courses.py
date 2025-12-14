#!/usr/bin/env python3
"""
Insert demo courses for OpenEduCat
"""

print("="*80)
print("INSERTING DEMO COURSES")
print("="*80 + "\n")

OpCourse = env['op.course']
created_courses = 0

try:
    # Create 3 demo courses matching our motakamel programs
    print("Creating demo courses...")
    
    courses_data = [
        {
            'name': 'Certified Business Professional in Leadership & Coaching (CBPLC)',
            'code': 'CBPLC-2026',
        },
        {
            'name': 'Professional in Human Resources Innovation (PHRI)',
            'code': 'PHRI-2026',
        },
        {
            'name': 'Project Management Professional (PMP)',
            'code': 'PMP-2026',
        },
    ]
    
    for course_data in courses_data:
        # Check if course already exists
        existing = OpCourse.search([('code', '=', course_data['code'])], limit=1)
        if existing:
            print(f"  ⊘ Course {course_data['code']} already exists, skipping...")
            continue
            
        course = OpCourse.create(course_data)
        created_courses += 1
        print(f"  ✓ Created course: {course.name}")
    
    # Commit the transaction
    env.cr.commit()
    
    print("\n" + "="*80)
    print(f"✓ SUCCESS! Created {created_courses} new courses")
    print("="*80 + "\n")
    
except Exception as e:
    print(f"\n✗ ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
    env.cr.rollback()
