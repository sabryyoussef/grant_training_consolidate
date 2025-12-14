#!/usr/bin/env python3
"""
Create delivery records for motakamel programs to populate enrollment stats
"""

print("="*80)
print("CREATING DELIVERY RECORDS")
print("="*80 + "\n")

Program = env['motakamel.program']
Delivery = env['motakamel.delivery']
BatchIntake = env['batch.intake']

try:
    # Get programs with batch intakes but no deliveries
    cbplc = Program.search([('program_code', '=', 'CBPLC')], limit=1)
    phri = Program.search([('program_code', '=', 'PHRI')], limit=1)
    pmp = Program.search([('program_code', '=', 'PMP')], limit=1)
    
    created = 0
    
    for program in [cbplc, phri, pmp]:
        if not program:
            continue
            
        # Check if delivery already exists
        existing = Delivery.search([('program_id', '=', program.id)], limit=1)
        if existing:
            print(f"⊘ Delivery for {program.program_code} already exists, skipping...")
            continue
        
        # Find related batch intakes
        batches = BatchIntake.search([
            ('course_id.name', 'ilike', program.program_name),
            ('state', '=', 'open')
        ])
        
        if not batches:
            print(f"⚠ No batch intakes found for {program.program_code}")
            continue
        
        # Get the first batch for dates
        batch = batches[0]
        
        # Calculate duration
        duration_days = (batch.end_date - batch.start_date).days + 1 if batch.end_date and batch.start_date else 5
        
        # Create delivery
        delivery = Delivery.create({
            'program_id': program.id,
            'delivery_name': f'{program.program_name} - 2026 Cohort',
            'start_date': batch.start_date,
            'end_date': batch.end_date,
            'delivery_status': 'open',
            'training_mode': 'hybrid',
            'training_language': 'bilingual',
            'program_duration_days': duration_days,
            'total_training_hours': duration_days * 7.0,
            'daily_training_hours': 7.0,
            'max_participants': batch.max_capacity,
            'current_enrollments': sum(len(b.openeducat_student_ids) for b in batches),
        })
        created += 1
        
        print(f"✓ Created delivery for {program.program_code}")
        print(f"  - Name: {delivery.delivery_name}")
        print(f"  - Capacity: {delivery.max_participants}")
        print(f"  - Related batches: {len(batches)}")
        print(f"  - Enrolled students: {sum(len(b.openeducat_student_ids) for b in batches)}")
        print()
    
    # Commit
    env.cr.commit()
    
    print("="*80)
    print(f"✓ SUCCESS! Created {created} delivery records")
    print("="*80 + "\n")
    
except Exception as e:
    print(f"\n✗ ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
    env.cr.rollback()
