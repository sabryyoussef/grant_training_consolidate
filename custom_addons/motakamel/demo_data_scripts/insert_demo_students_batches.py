#!/usr/bin/env python3
"""
Insert demo students and batch intakes for motakamel module
"""

print("="*80)
print("INSERTING DEMO STUDENTS & BATCH INTAKES")
print("="*80 + "\n")

Student = env['op.student']
BatchIntake = env['batch.intake']
OpCourse = env['op.course']

created_students = 0
created_batches = 0

try:
    # Create 10 demo students
    print("Creating demo students...")
    students = []
    student_data_list = [
        {'name': 'Ahmed Mohamed Ali', 'email': 'ahmed.ali@example.com', 'phone': '+20 100 123 4567'},
        {'name': 'Fatima Hassan Ibrahim', 'email': 'fatima.hassan@example.com', 'phone': '+20 101 234 5678'},
        {'name': 'Mohamed Mahmoud Saeed', 'email': 'mohamed.saeed@example.com', 'phone': '+20 102 345 6789'},
        {'name': 'Sara Ahmed Khalil', 'email': 'sara.khalil@example.com', 'phone': '+20 110 456 7890'},
        {'name': 'Omar Youssef Nabil', 'email': 'omar.nabil@example.com', 'phone': '+20 111 567 8901'},
        {'name': 'Nour Adel Farouk', 'email': 'nour.farouk@example.com', 'phone': '+20 112 678 9012'},
        {'name': 'Youssef Ibrahim Tarek', 'email': 'youssef.tarek@example.com', 'phone': '+20 120 789 0123'},
        {'name': 'Layla Khaled Mostafa', 'email': 'layla.mostafa@example.com', 'phone': '+20 121 890 1234'},
        {'name': 'Hassan Ali Mohamed', 'email': 'hassan.mohamed@example.com', 'phone': '+20 122 901 2345'},
        {'name': 'Amira Samir Galal', 'email': 'amira.galal@example.com', 'phone': '+20 150 012 3456'},
    ]
    
    for student_data in student_data_list:
        # Check if student already exists
        existing = Student.search([('email', '=', student_data['email'])], limit=1)
        if existing:
            students.append(existing)
            continue
            
        student = Student.create({
            'name': student_data['name'],
            'email': student_data['email'],
            'phone': student_data['phone'],
        })
        students.append(student)
        created_students += 1
        
    print(f"  ✓ Created {created_students} new demo students (total available: {len(students)})")
    
    # Get existing courses from OpenEduCat
    print("\nFinding courses...")
    courses = OpCourse.search([], limit=3)
    
    if not courses:
        print("  ⚠ WARNING: No courses found! Batch intakes need courses to function.")
        print("  Please create courses in OpenEduCat first, then run this script again.")
        env.cr.commit()
        exit(0)
    
    print(f"  ✓ Found {len(courses)} courses")
    for course in courses:
        print(f"    - {course.name}")
    
    # Create batch intakes with student enrollments
    print("\nCreating batch intakes with student enrollments...")
    
    # Batch 1 with 4 students
    print(f"\nCreating batch intake for '{courses[0].name}'...")
    batch1_students = students[0:4]
    batch1 = BatchIntake.create({
        'name': f'{courses[0].name} - Jan 2026 Cohort',
        'start_date': '2026-01-05',
        'end_date': '2026-01-09',
        'max_capacity': 25,
        'state': 'open',
        'course_id': courses[0].id,
        'openeducat_student_ids': [(6, 0, [s.id for s in batch1_students])],
    })
    created_batches += 1
    print(f"  ✓ Created batch with {len(batch1_students)} enrolled students:")
    for student in batch1_students:
        print(f"    - {student.name}")
    
    # Batch 2 with 3 students (if enough courses)
    if len(courses) > 1:
        print(f"\nCreating batch intake for '{courses[1].name}'...")
        batch2_students = students[4:7]
        batch2 = BatchIntake.create({
            'name': f'{courses[1].name} - Jan 2026 Cohort',
            'start_date': '2026-01-20',
            'end_date': '2026-01-24',
            'max_capacity': 20,
            'state': 'open',
            'course_id': courses[1].id,
            'openeducat_student_ids': [(6, 0, [s.id for s in batch2_students])],
        })
        created_batches += 1
        print(f"  ✓ Created batch with {len(batch2_students)} enrolled students:")
        for student in batch2_students:
            print(f"    - {student.name}")
    
    # Batch 3 with 3 students (if enough courses)
    if len(courses) > 2:
        print(f"\nCreating batch intake for '{courses[2].name}'...")
        batch3_students = students[7:10]
        batch3 = BatchIntake.create({
            'name': f'{courses[2].name} - Feb 2026 Cohort',
            'start_date': '2026-02-04',
            'end_date': '2026-02-08',
            'max_capacity': 30,
            'state': 'open',
            'course_id': courses[2].id,
            'openeducat_student_ids': [(6, 0, [s.id for s in batch3_students])],
        })
        created_batches += 1
        print(f"  ✓ Created batch with {len(batch3_students)} enrolled students:")
        for student in batch3_students:
            print(f"    - {student.name}")
    
    # Commit the transaction
    env.cr.commit()
    
    print("\n" + "="*80)
    print(f"✓ SUCCESS! Created:")
    print(f"  - {created_students} new students (total {len(students)} available)")
    print(f"  - {created_batches} batch intakes")
    print(f"\nEnrollment Summary:")
    total_enrolled = min(10, len(students))
    print(f"  - Total students enrolled across batches: {total_enrolled}")
    print("="*80 + "\n")
    
except Exception as e:
    print(f"\n✗ ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
    env.cr.rollback()
