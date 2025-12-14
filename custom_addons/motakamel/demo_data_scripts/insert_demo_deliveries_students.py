#!/usr/bin/env python3
"""
Insert Demo Batch Intakes and Students for Motakamel Deliveries
"""

# Run in odoo shell: echo "exec(open('insert_demo_deliveries_students.py').read())" | odoo-bin shell ...

try:
    print("\n" + "="*80)
    print("INSERTING MOTAKAMEL DEMO DELIVERIES & STUDENT ENROLLMENTS")
    print("="*80 + "\n")
    
    Program = env['motakamel.program']
    Delivery = env['motakamel.delivery']
    BatchIntake = env['batch.intake']
    Student = env['op.student']
    Partner = env['res.partner']
    Course = env['op.course']
    
    # Get the programs by code
    cbplc = Program.search([('program_code', '=', 'CBPLC')], limit=1)
    phri = Program.search([('program_code', '=', 'PHRI')], limit=1)
    pmp = Program.search([('program_code', '=', 'PMP')], limit=1)
    cbpcs = Program.search([('program_code', '=', 'CBPCS')], limit=1)
    cafm = Program.search([('program_code', '=', 'CAFM')], limit=1)
    
    if not all([cbplc, phri, pmp, cbpcs, cafm]):
        print("\n✗ Some programs are missing. Please create programs first.")
        exit(1)
    
    created_deliveries = 0
    created_students = 0
    created_batches = 0
    
    # First, create some demo students
    print("\nCreating demo students...")
    
    demo_students_data = [
        {'name': 'Ahmed Hassan', 'email': 'ahmed.hassan@example.com', 'phone': '+20 100 123 4567'},
        {'name': 'Fatima Ali', 'email': 'fatima.ali@example.com', 'phone': '+20 100 234 5678'},
        {'name': 'Mohamed Khalil', 'email': 'mohamed.khalil@example.com', 'phone': '+20 100 345 6789'},
        {'name': 'Sara Ibrahim', 'email': 'sara.ibrahim@example.com', 'phone': '+20 100 456 7890'},
        {'name': 'Omar Youssef', 'email': 'omar.youssef@example.com', 'phone': '+20 100 567 8901'},
        {'name': 'Nour Ahmed', 'email': 'nour.ahmed@example.com', 'phone': '+20 100 678 9012'},
        {'name': 'Heba Mahmoud', 'email': 'heba.mahmoud@example.com', 'phone': '+20 100 789 0123'},
        {'name': 'Khaled Salem', 'email': 'khaled.salem@example.com', 'phone': '+20 100 890 1234'},
        {'name': 'Mona Fawzy', 'email': 'mona.fawzy@example.com', 'phone': '+20 100 901 2345'},
        {'name': 'Tarek Nabil', 'email': 'tarek.nabil@example.com', 'phone': '+20 100 012 3456'},
    ]
    
    students = []
    for i, student_data in enumerate(demo_students_data, 1):
        # Create partner first
        partner = Partner.create({
            'name': student_data['name'],
            'email': student_data['email'],
            'phone': student_data['phone'],
            'customer_rank': 1,
        })
        
        # Create student
        student = Student.create({
            'partner_id': partner.id,
            'name': student_data['name'],
            'middle_name': '',
            'last_name': student_data['name'].split()[-1],
            'birth_date': f'199{i % 10}-0{(i % 9) + 1}-15',
            'gender': 'm' if i % 2 == 0 else 'f',
            'email': student_data['email'],
            'phone': student_data['phone'],
        })
        students.append(student)
        created_students += 1
        
    print(f"  ✓ Created {created_students} demo students")
    
    # Create delivery schedules and batch intakes
    print("\nCreating delivery schedules and batch intakes...")
    
    # CBPLC Delivery
    print(f"\nCreating delivery for {cbplc.program_code}...")
    cbplc_delivery = Delivery.create({
        'program_id': cbplc.id,
        'training_mode': 'hybrid',
        'training_language': 'bilingual',
        'total_training_hours': 35.0,
        'daily_training_hours': 7.0,
        'program_duration_days': 5,
        'start_date': '2026-01-05',
        'end_date': '2026-01-09',
        'schedule_details': '''Day 1-2: Online sessions (9:00 AM - 4:00 PM)
Day 3: On-site workshop (9:00 AM - 5:00 PM)
Day 4-5: Online sessions with practical exercises (9:00 AM - 4:00 PM)
All sessions include breaks and interactive activities''',
        'exam_included': True,
        'exam_format': 'online',
        'exam_date': '2026-01-10',
        'study_material_included': True,
        'study_material_details': 'Comprehensive course materials, case studies, templates, and access to online learning platform',
        'mock_exam_included': True,
        'venue_name': 'Cairo Training Center',
        'venue_address': '123 Tahrir Street, Downtown',
        'venue_city': 'Cairo',
        'online_platform': 'Zoom & Microsoft Teams',
        'max_participants': 25,
        'min_participants': 10,
        'current_enrollments': 4,
        'delivery_status': 'open',
        'active': True,
    })
    created_deliveries += 1
    
    # Create batch intake for CBPLC with 4 students
    cbplc_students = students[0:4]
    cbplc_batch = BatchIntake.create({
        'name': f'CBPLC Batch - Jan 2026',
        'start_date': '2026-01-05',
        'end_date': '2026-01-09',
        'max_capacity': 25,
        'state': 'open',
        'motakamel_program_id': cbplc.id,
        'openeducat_student_ids': [(6, 0, [s.id for s in cbplc_students])],
    })
    created_batches += 1
    print(f"  ✓ Created CBPLC delivery with {len(cbplc_students)} enrolled students")
    
    # PHRI Delivery
    print(f"\nCreating delivery for {phri.program_code}...")
    phri_delivery = Delivery.create({
        'program_id': phri.id,
        'training_mode': 'hybrid',
        'training_language': 'bilingual',
        'total_training_hours': 40.0,
        'daily_training_hours': 8.0,
        'program_duration_days': 5,
        'start_date': '2026-01-20',
        'end_date': '2026-01-24',
        'schedule_details': '''Day 1-3: Online intensive sessions (9:00 AM - 5:00 PM)
Day 4: On-site exam preparation workshop (9:00 AM - 5:00 PM)
Day 5: Online review and Q&A session (9:00 AM - 1:00 PM)
Exam scheduled separately after completion''',
        'exam_included': True,
        'exam_format': 'proctored',
        'exam_date': '2026-01-27',
        'study_material_included': True,
        'study_material_details': 'HRCI study guide, practice exams, flashcards, online resources, and exam preparation materials',
        'mock_exam_included': True,
        'venue_name': 'Alexandria Business Center',
        'venue_address': '45 Corniche Road, Sidi Gaber',
        'venue_city': 'Alexandria',
        'online_platform': 'Zoom & HRCI Learning Portal',
        'max_participants': 20,
        'min_participants': 8,
        'current_enrollments': 3,
        'delivery_status': 'open',
        'active': True,
    })
    created_deliveries += 1
    
    # Create batch intake for PHRI with 3 students
    phri_students = students[4:7]
    phri_batch = BatchIntake.create({
        'name': f'PHRI Batch - Jan 2026',
        'start_date': '2026-01-20',
        'end_date': '2026-01-24',
        'max_capacity': 20,
        'state': 'open',
        'motakamel_program_id': phri.id,
        'openeducat_student_ids': [(6, 0, [s.id for s in phri_students])],
    })
    created_batches += 1
    print(f"  ✓ Created PHRI delivery with {len(phri_students)} enrolled students")
    
    # PMP Delivery
    print(f"\nCreating delivery for {pmp.program_code}...")
    pmp_delivery = Delivery.create({
        'program_id': pmp.id,
        'training_mode': 'hybrid',
        'training_language': 'bilingual',
        'total_training_hours': 35.0,
        'daily_training_hours': 7.0,
        'program_duration_days': 5,
        'start_date': '2026-02-04',
        'end_date': '2026-02-08',
        'schedule_details': '''Day 1-2: Online PMBOK Guide sessions (9:00 AM - 4:00 PM)
Day 3: On-site intensive workshop (9:00 AM - 6:00 PM)
Day 4-5: Online exam simulation and review (9:00 AM - 4:00 PM)
180-day access to PMI exam preparation materials''',
        'exam_included': True,
        'exam_format': 'proctored',
        'exam_date': '2026-03-06',
        'study_material_included': True,
        'study_material_details': 'PMBOK Guide 7th Edition, PMI exam simulator, practice questions bank, formula guide, and 35 PDUs certificate',
        'mock_exam_included': True,
        'venue_name': 'Cairo Project Management Institute',
        'venue_address': '789 Nasr City, Fifth District',
        'venue_city': 'Cairo',
        'online_platform': 'Zoom & PMI Learning Platform',
        'max_participants': 30,
        'min_participants': 12,
        'current_enrollments': 3,
        'delivery_status': 'open',
        'active': True,
    })
    created_deliveries += 1
    
    # Create batch intake for PMP with 3 students
    pmp_students = students[7:10]
    pmp_batch = BatchIntake.create({
        'name': f'PMP Batch - Feb 2026',
        'start_date': '2026-02-04',
        'end_date': '2026-02-08',
        'max_capacity': 30,
        'state': 'open',
        'motakamel_program_id': pmp.id,
        'openeducat_student_ids': [(6, 0, [s.id for s in pmp_students])],
    })
    created_batches += 1
    print(f"  ✓ Created PMP delivery with {len(pmp_students)} enrolled students")
    
    env.cr.commit()
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    
    print(f"\nDemo Students Created: {created_students}")
    for i, student in enumerate(students, 1):
        print(f"  {i}. {student.name} ({student.email})")
    
    print(f"\nDelivery Schedules Created: {created_deliveries}")
    print(f"Batch Intakes Created: {created_batches}")
    
    print(f"\nEnrollment Distribution:")
    print(f"  - {cbplc.program_code}: 4 students")
    print(f"  - {phri.program_code}: 3 students")
    print(f"  - {pmp.program_code}: 3 students")
    
    total_deliveries = Delivery.search_count([])
    total_batches = BatchIntake.search_count([])
    total_students = Student.search_count([])
    
    print(f"\nDatabase Totals:")
    print(f"  - Total Deliveries: {total_deliveries}")
    print(f"  - Total Batch Intakes: {total_batches}")
    print(f"  - Total Students: {total_students}")
    
    print("\n" + "="*80)
    print("DEMO DELIVERIES & ENROLLMENTS CREATED SUCCESSFULLY")
    print("="*80 + "\n")
    
except Exception as e:
    print(f"\n✗ ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
    env.cr.rollback()
