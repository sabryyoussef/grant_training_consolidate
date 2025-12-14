#!/usr/bin/env python3
"""
Check and debug enrollment data visibility
"""

print("="*80)
print("CHECKING ENROLLMENT DATA")
print("="*80 + "\n")

Marketing = env['motakamel.marketing']
Program = env['motakamel.program']
BatchIntake = env['batch.intake']
OpCourse = env['op.course']

# Get the PHRI marketing campaign
phri_marketing = Marketing.search([('campaign_name', 'ilike', 'PHRI')], limit=1)

if phri_marketing:
    print(f"Found Marketing Campaign: {phri_marketing.campaign_name}")
    print(f"  Program: {phri_marketing.program_id.program_name if phri_marketing.program_id else 'None'}")
    print(f"  Enrolled Count: {phri_marketing.enrolled_count}")
    print()
    
    if phri_marketing.program_id:
        program_name = phri_marketing.program_id.program_name
        print(f"Searching for batch intakes matching: '{program_name}'")
        
        # Search like the compute method does
        batches = BatchIntake.search([
            '|',
            ('course_id.name', 'ilike', program_name),
            ('name', 'ilike', program_name)
        ])
        
        print(f"  Found {len(batches)} batch intakes:")
        for batch in batches:
            print(f"    - {batch.name}")
            print(f"      Course: {batch.course_id.name if batch.course_id else 'None'}")
            print(f"      Students: {len(batch.openeducat_student_ids)}")
        print()
        
        # Force recompute
        print("Forcing recomputation of enrolled students...")
        phri_marketing._compute_students_and_leads()
        
        print(f"After recompute - Enrolled Count: {phri_marketing.enrolled_count}")
        if phri_marketing.enrolled_student_ids:
            print("  Enrolled Students:")
            for student in phri_marketing.enrolled_student_ids:
                print(f"    - {student.name}")
else:
    print("PHRI Marketing campaign not found!")
    print("\nAll marketing campaigns:")
    all_marketing = Marketing.search([])
    for m in all_marketing:
        print(f"  - {m.campaign_name} (Program: {m.program_id.program_name if m.program_id else 'None'})")

print("\n" + "="*80)
print("All Batch Intakes:")
all_batches = BatchIntake.search([])
for batch in all_batches:
    print(f"  - {batch.name}")
    print(f"    Course: {batch.course_id.name if batch.course_id else 'None'}")
    print(f"    Students: {len(batch.openeducat_student_ids)}")
    if batch.openeducat_student_ids:
        for student in batch.openeducat_student_ids[:3]:  # First 3
            print(f"      * {student.name}")

print("\n" + "="*80)
print("All Programs:")
all_programs = Program.search([])
for prog in all_programs:
    print(f"  - {prog.program_name} ({prog.program_code})")

print("="*80 + "\n")
