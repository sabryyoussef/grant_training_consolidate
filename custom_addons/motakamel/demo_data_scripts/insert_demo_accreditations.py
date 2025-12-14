#!/usr/bin/env python3
"""
Insert Motakamel Demo Accreditations
"""

# Run in odoo shell: echo "exec(open('insert_demo_accreditations.py').read())" | odoo-bin shell ...

try:
    print("\n" + "="*80)
    print("INSERTING MOTAKAMEL DEMO ACCREDITATIONS")
    print("="*80 + "\n")
    
    Program = env['motakamel.program']
    Accreditation = env['motakamel.accreditation']
    
    # Get the programs by code
    cbplc = Program.search([('program_code', '=', 'CBPLC')], limit=1)
    phri = Program.search([('program_code', '=', 'PHRI')], limit=1)
    pmp = Program.search([('program_code', '=', 'PMP')], limit=1)
    cbpcs = Program.search([('program_code', '=', 'CBPCS')], limit=1)
    cafm = Program.search([('program_code', '=', 'CAFM')], limit=1)
    
    if not cbplc:
        print("✗ Program CBPLC not found!")
    if not phri:
        print("✗ Program PHRI not found!")
    if not pmp:
        print("✗ Program PMP not found!")
    if not cbpcs:
        print("✗ Program CBPCS not found!")
    if not cafm:
        print("✗ Program CAFM not found!")
    
    if not all([cbplc, phri, pmp, cbpcs, cafm]):
        print("\n✗ Some programs are missing. Please create programs first.")
        exit(1)
    
    # Accreditation 1: CBPLC - IBTA
    if cbplc:
        print(f"Creating accreditation for {cbplc.program_code}...")
        acc1 = Accreditation.create({
            'program_id': cbplc.id,
            'international_accreditation_body': 'IBTA',
            'accreditation_code': 'IBTA-CBPLC-2025',
            'accreditation_valid_from': '2025-11-06',
            'accreditation_valid_to': '2028-12-05',
            'certificate_type': 'professional',
            'accreditation_level': 'international',
            'is_primary': True,
            'verification_url': 'https://www.ibta.org/verify/CBPLC',
            'active': True,
        })
        print(f"  ✓ Created: {acc1.accreditation_code} for {cbplc.program_name}")
    
    # Accreditation 2: PHRI - HRCI
    if phri:
        print(f"Creating accreditation for {phri.program_code}...")
        acc2 = Accreditation.create({
            'program_id': phri.id,
            'international_accreditation_body': 'HRCI',
            'accreditation_code': 'HRCI-PHRI-2025',
            'accreditation_valid_from': '2025-11-11',
            'accreditation_valid_to': '2028-12-05',
            'certificate_type': 'professional',
            'accreditation_level': 'international',
            'is_primary': True,
            'verification_url': 'https://www.hrci.org/certification/verify/phri',
            'active': True,
        })
        print(f"  ✓ Created: {acc2.accreditation_code} for {phri.program_name}")
    
    # Accreditation 3: PMP - PMI
    if pmp:
        print(f"Creating accreditation for {pmp.program_code}...")
        acc3 = Accreditation.create({
            'program_id': pmp.id,
            'international_accreditation_body': 'PMI',
            'accreditation_code': 'PMI-PMP-2025',
            'accreditation_valid_from': '2025-11-16',
            'accreditation_valid_to': '2028-12-05',
            'certificate_type': 'professional',
            'accreditation_level': 'international',
            'is_primary': True,
            'verification_url': 'https://www.pmi.org/certifications/certified-project-managers/pmp/verify',
            'active': True,
        })
        print(f"  ✓ Created: {acc3.accreditation_code} for {pmp.program_name}")
    
    # Accreditation 4: CBPCS - IBTA
    if cbpcs:
        print(f"Creating accreditation for {cbpcs.program_code}...")
        acc4 = Accreditation.create({
            'program_id': cbpcs.id,
            'international_accreditation_body': 'IBTA',
            'accreditation_code': 'IBTA-CBPCS-2025',
            'accreditation_valid_from': '2025-11-21',
            'accreditation_valid_to': '2028-12-05',
            'certificate_type': 'professional',
            'accreditation_level': 'international',
            'is_primary': True,
            'verification_url': 'https://www.ibta.org/verify/CBPCS',
            'active': True,
        })
        print(f"  ✓ Created: {acc4.accreditation_code} for {cbpcs.program_name}")
    
    # Accreditation 5: CAFM - IFMA
    if cafm:
        print(f"Creating accreditation for {cafm.program_code}...")
        acc5 = Accreditation.create({
            'program_id': cafm.id,
            'international_accreditation_body': 'IFMA',
            'accreditation_code': 'IFMA-CAFM-2025',
            'accreditation_valid_from': '2025-11-26',
            'accreditation_valid_to': '2028-12-05',
            'certificate_type': 'professional',
            'accreditation_level': 'international',
            'is_primary': True,
            'verification_url': 'https://www.ifma.org/credentials/cafm/verify',
            'active': True,
        })
        print(f"  ✓ Created: {acc5.accreditation_code} for {cafm.program_name}")
    
    env.cr.commit()
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    
    # Count accreditations per program
    for prog in [cbplc, phri, pmp, cbpcs, cafm]:
        if prog:
            acc_count = Accreditation.search_count([('program_id', '=', prog.id)])
            print(f"[{prog.program_code}] {prog.program_name}: {acc_count} accreditation(s)")
    
    total_acc = Accreditation.search_count([])
    print(f"\nTotal accreditations in database: {total_acc}")
    
    print("\n" + "="*80)
    print("DEMO ACCREDITATIONS CREATED SUCCESSFULLY")
    print("="*80 + "\n")
    
except Exception as e:
    print(f"\n✗ ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
    env.cr.rollback()
