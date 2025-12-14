#!/usr/bin/env python3
"""
Insert Motakamel Demo Target Audiences
"""

# Run in odoo shell: echo "exec(open('insert_demo_audiences.py').read())" | odoo-bin shell ...

try:
    print("\n" + "="*80)
    print("INSERTING MOTAKAMEL DEMO TARGET AUDIENCES")
    print("="*80 + "\n")
    
    Program = env['motakamel.program']
    Audience = env['motakamel.audience']
    
    # Get the programs by code
    cbplc = Program.search([('program_code', '=', 'CBPLC')], limit=1)
    phri = Program.search([('program_code', '=', 'PHRI')], limit=1)
    pmp = Program.search([('program_code', '=', 'PMP')], limit=1)
    cbpcs = Program.search([('program_code', '=', 'CBPCS')], limit=1)
    cafm = Program.search([('program_code', '=', 'CAFM')], limit=1)
    
    if not all([cbplc, phri, pmp, cbpcs, cafm]):
        print("\n✗ Some programs are missing. Please create programs first.")
        exit(1)
    
    created_count = 0
    
    # CBPLC Audiences (3 records)
    print(f"\nCreating audiences for {cbplc.program_code}...")
    
    Audience.create({
        'program_id': cbplc.id,
        'target_sector': 'public',
        'career_level': 'senior',
        'prerequisites_required': True,
        'prerequisites_description': 'Minimum 5 years of management experience. Bachelor\'s degree or equivalent. Experience in leading teams through organizational change.',
        'min_education_level': 'bachelor',
        'min_experience_years': 5,
        'eligible_job_titles': '''Senior Manager
Department Head
Director
Deputy Director
Change Management Officer
Organizational Development Manager''',
        'active': True,
    })
    created_count += 1
    
    Audience.create({
        'program_id': cbplc.id,
        'target_sector': 'private',
        'career_level': 'senior',
        'prerequisites_required': True,
        'prerequisites_description': 'Minimum 5 years of management experience. Bachelor\'s degree or equivalent. Experience in leading teams through organizational change.',
        'min_education_level': 'bachelor',
        'min_experience_years': 5,
        'eligible_job_titles': '''Senior Manager
Business Unit Head
Operations Director
Change Management Consultant
Transformation Manager''',
        'active': True,
    })
    created_count += 1
    
    Audience.create({
        'program_id': cbplc.id,
        'target_sector': 'individual',
        'career_level': 'mid',
        'prerequisites_required': True,
        'prerequisites_description': 'Minimum 3 years of professional experience. Bachelor\'s degree preferred. Aspiring leaders seeking career advancement.',
        'min_education_level': 'diploma',
        'min_experience_years': 3,
        'active': True,
    })
    created_count += 1
    print(f"  ✓ Created 3 audience records for {cbplc.program_code}")
    
    # PHRI Audiences (3 records)
    print(f"\nCreating audiences for {phri.program_code}...")
    
    Audience.create({
        'program_id': phri.id,
        'target_sector': 'public',
        'career_level': 'mid',
        'prerequisites_required': True,
        'prerequisites_description': 'Minimum 2 years of HR experience. Bachelor\'s degree in HR, Business, or related field. Understanding of HR fundamentals.',
        'min_education_level': 'bachelor',
        'min_experience_years': 2,
        'eligible_job_titles': '''HR Specialist
HR Officer
HR Coordinator
Personnel Officer
Recruitment Specialist''',
        'active': True,
    })
    created_count += 1
    
    Audience.create({
        'program_id': phri.id,
        'target_sector': 'private',
        'career_level': 'mid',
        'prerequisites_required': True,
        'prerequisites_description': 'Minimum 2 years of HR experience. Bachelor\'s degree in HR, Business, or related field. Understanding of HR fundamentals.',
        'min_education_level': 'bachelor',
        'min_experience_years': 2,
        'eligible_job_titles': '''HR Business Partner
HR Generalist
Talent Acquisition Specialist
HR Manager
Compensation & Benefits Specialist''',
        'active': True,
    })
    created_count += 1
    
    Audience.create({
        'program_id': phri.id,
        'target_sector': 'individual',
        'career_level': 'entry',
        'prerequisites_required': False,
        'min_education_level': 'bachelor',
        'min_experience_years': 0,
        'active': True,
    })
    created_count += 1
    print(f"  ✓ Created 3 audience records for {phri.program_code}")
    
    # PMP Audiences (3 records)
    print(f"\nCreating audiences for {pmp.program_code}...")
    
    Audience.create({
        'program_id': pmp.id,
        'target_sector': 'public',
        'career_level': 'senior',
        'prerequisites_required': True,
        'prerequisites_description': 'Minimum 3 years of project management experience. 35 hours of project management education. Bachelor\'s degree or equivalent. Experience leading and directing projects.',
        'min_education_level': 'bachelor',
        'min_experience_years': 3,
        'eligible_job_titles': '''Project Manager
Program Manager
Project Coordinator
Project Director
Portfolio Manager''',
        'active': True,
    })
    created_count += 1
    
    Audience.create({
        'program_id': pmp.id,
        'target_sector': 'private',
        'career_level': 'senior',
        'prerequisites_required': True,
        'prerequisites_description': 'Minimum 3 years of project management experience. 35 hours of project management education. Bachelor\'s degree or equivalent. Experience leading and directing projects.',
        'min_education_level': 'bachelor',
        'min_experience_years': 3,
        'eligible_job_titles': '''Project Manager
Senior Project Manager
Program Manager
Project Director
PMO Manager''',
        'active': True,
    })
    created_count += 1
    
    Audience.create({
        'program_id': pmp.id,
        'target_sector': 'individual',
        'career_level': 'mid',
        'prerequisites_required': True,
        'prerequisites_description': 'Minimum 2 years of project management experience. 35 hours of project management education required.',
        'min_education_level': 'bachelor',
        'min_experience_years': 2,
        'active': True,
    })
    created_count += 1
    print(f"  ✓ Created 3 audience records for {pmp.program_code}")
    
    # CBPCS Audiences (3 records)
    print(f"\nCreating audiences for {cbpcs.program_code}...")
    
    Audience.create({
        'program_id': cbpcs.id,
        'target_sector': 'public',
        'career_level': 'mid',
        'prerequisites_required': False,
        'min_education_level': 'diploma',
        'min_experience_years': 1,
        'eligible_job_titles': '''Customer Service Representative
Client Relations Officer
Service Desk Agent
Call Center Supervisor
Customer Support Specialist''',
        'active': True,
    })
    created_count += 1
    
    Audience.create({
        'program_id': cbpcs.id,
        'target_sector': 'private',
        'career_level': 'mid',
        'prerequisites_required': False,
        'min_education_level': 'diploma',
        'min_experience_years': 1,
        'eligible_job_titles': '''Customer Service Manager
Account Manager
Client Success Manager
Customer Experience Specialist
Service Quality Manager''',
        'active': True,
    })
    created_count += 1
    
    Audience.create({
        'program_id': cbpcs.id,
        'target_sector': 'individual',
        'career_level': 'entry',
        'prerequisites_required': False,
        'min_education_level': 'high_school',
        'min_experience_years': 0,
        'active': True,
    })
    created_count += 1
    print(f"  ✓ Created 3 audience records for {cbpcs.program_code}")
    
    # CAFM Audiences (3 records)
    print(f"\nCreating audiences for {cafm.program_code}...")
    
    Audience.create({
        'program_id': cafm.id,
        'target_sector': 'public',
        'career_level': 'mid',
        'prerequisites_required': True,
        'prerequisites_description': 'Minimum 2 years of facilities or building management experience. Understanding of building systems and maintenance operations.',
        'min_education_level': 'diploma',
        'min_experience_years': 2,
        'eligible_job_titles': '''Facilities Coordinator
Building Supervisor
Maintenance Manager
Property Manager
Operations Coordinator''',
        'active': True,
    })
    created_count += 1
    
    Audience.create({
        'program_id': cafm.id,
        'target_sector': 'private',
        'career_level': 'mid',
        'prerequisites_required': True,
        'prerequisites_description': 'Minimum 2 years of facilities or building management experience. Understanding of building systems and maintenance operations.',
        'min_education_level': 'diploma',
        'min_experience_years': 2,
        'eligible_job_titles': '''Facilities Manager
Building Manager
Real Estate Manager
Workplace Services Manager
Asset Manager''',
        'active': True,
    })
    created_count += 1
    
    Audience.create({
        'program_id': cafm.id,
        'target_sector': 'individual',
        'career_level': 'entry',
        'prerequisites_required': False,
        'min_education_level': 'diploma',
        'min_experience_years': 0,
        'active': True,
    })
    created_count += 1
    print(f"  ✓ Created 3 audience records for {cafm.program_code}")
    
    env.cr.commit()
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    
    # Count audiences per program
    for prog in [cbplc, phri, pmp, cbpcs, cafm]:
        if prog:
            aud_count = Audience.search_count([('program_id', '=', prog.id)])
            print(f"[{prog.program_code}] {prog.program_name}: {aud_count} audience(s)")
    
    total_aud = Audience.search_count([])
    print(f"\nTotal target audiences in database: {total_aud}")
    print(f"Created in this session: {created_count}")
    
    print("\n" + "="*80)
    print("DEMO TARGET AUDIENCES CREATED SUCCESSFULLY")
    print("="*80 + "\n")
    
except Exception as e:
    print(f"\n✗ ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
    env.cr.rollback()
