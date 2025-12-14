#!/usr/bin/env python3
"""
Insert Motakamel Demo Credentials
"""

# Run in odoo shell: echo "exec(open('insert_demo_credentials.py').read())" | odoo-bin shell ...

try:
    print("\n" + "="*80)
    print("INSERTING MOTAKAMEL DEMO CREDENTIALS")
    print("="*80 + "\n")
    
    Program = env['motakamel.program']
    Credential = env['motakamel.credential']
    
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
    
    # CBPLC Credential
    print(f"\nCreating credential for {cbplc.program_code}...")
    Credential.create({
        'program_id': cbplc.id,
        'credential_name': 'Certified Business Professional in Leading Through Change',
        'certificate_issued': True,
        'certificate_type': 'professional',
        'certificate_serial_format': 'IBTA-CBPLC-{YEAR}-{NUMBER:05d}',
        'issuing_authority': 'IBTA',
        'certificate_delivery_days': 10,
        'delivery_method': 'both',
        'renewal_required': False,
        'verification_available': True,
        'verification_url': 'https://www.ibta.org/verify/CBPLC',
        'verification_method': 'serial_number',
        'digital_badge_available': True,
        'badge_platform': 'open_badges',
        'linkedin_integration': True,
        'transcript_available': True,
        'active': True,
    })
    created_count += 1
    print(f"  ✓ Created credential for {cbplc.program_code}")
    
    # PHRI Credential
    print(f"\nCreating credential for {phri.program_code}...")
    Credential.create({
        'program_id': phri.id,
        'credential_name': 'Professional in Human Resources – International (PHRI)',
        'certificate_issued': True,
        'certificate_type': 'professional',
        'certificate_serial_format': 'HRCI-PHRI-{YEAR}-{NUMBER:06d}',
        'issuing_authority': 'HRCI',
        'certificate_delivery_days': 14,
        'delivery_method': 'both',
        'renewal_required': True,
        'renewal_cycle_years': 3,
        'continuing_education_required': True,
        'ce_hours_required': 60.0,
        'verification_available': True,
        'verification_url': 'https://www.hrci.org/certification/verify/phri',
        'verification_method': 'serial_number',
        'digital_badge_available': True,
        'badge_platform': 'credly',
        'linkedin_integration': True,
        'transcript_available': True,
        'wallet_card_available': True,
        'active': True,
    })
    created_count += 1
    print(f"  ✓ Created credential for {phri.program_code}")
    
    # PMP Credential
    print(f"\nCreating credential for {pmp.program_code}...")
    Credential.create({
        'program_id': pmp.id,
        'credential_name': 'Project Management Professional (PMP)',
        'certificate_issued': True,
        'certificate_type': 'professional',
        'certificate_serial_format': 'PMI-PMP-{YEAR}-{NUMBER:07d}',
        'issuing_authority': 'PMI',
        'certificate_delivery_days': 21,
        'delivery_method': 'both',
        'renewal_required': True,
        'renewal_cycle_years': 3,
        'continuing_education_required': True,
        'ce_hours_required': 35.0,
        'verification_available': True,
        'verification_url': 'https://www.pmi.org/certifications/certified-project-managers/pmp/verify',
        'verification_method': 'serial_number',
        'digital_badge_available': True,
        'badge_platform': 'credly',
        'linkedin_integration': True,
        'transcript_available': True,
        'wallet_card_available': True,
        'certificate_features': 'Embossed PMI seal, holographic security features, premium paper quality',
        'active': True,
    })
    created_count += 1
    print(f"  ✓ Created credential for {pmp.program_code}")
    
    # CBPCS Credential
    print(f"\nCreating credential for {cbpcs.program_code}...")
    Credential.create({
        'program_id': cbpcs.id,
        'credential_name': 'Certified Business Professional in Customer Services',
        'certificate_issued': True,
        'certificate_type': 'professional',
        'certificate_serial_format': 'IBTA-CBPCS-{YEAR}-{NUMBER:05d}',
        'issuing_authority': 'IBTA',
        'certificate_delivery_days': 10,
        'delivery_method': 'both',
        'renewal_required': False,
        'verification_available': True,
        'verification_url': 'https://www.ibta.org/verify/CBPCS',
        'verification_method': 'serial_number',
        'digital_badge_available': True,
        'badge_platform': 'open_badges',
        'linkedin_integration': True,
        'transcript_available': True,
        'active': True,
    })
    created_count += 1
    print(f"  ✓ Created credential for {cbpcs.program_code}")
    
    # CAFM Credential
    print(f"\nCreating credential for {cafm.program_code}...")
    Credential.create({
        'program_id': cafm.id,
        'credential_name': 'Certified Associate in Facilities Management (CAFM)',
        'certificate_issued': True,
        'certificate_type': 'professional',
        'certificate_serial_format': 'IFMA-CAFM-{YEAR}-{NUMBER:06d}',
        'issuing_authority': 'IFMA',
        'certificate_delivery_days': 14,
        'delivery_method': 'both',
        'renewal_required': True,
        'renewal_cycle_years': 3,
        'continuing_education_required': True,
        'ce_hours_required': 30.0,
        'verification_available': True,
        'verification_url': 'https://www.ifma.org/credentials/cafm/verify',
        'verification_method': 'serial_number',
        'digital_badge_available': True,
        'badge_platform': 'credly',
        'linkedin_integration': True,
        'transcript_available': True,
        'wallet_card_available': True,
        'certificate_features': 'IFMA official seal, digital QR code verification, professional certificate frame included',
        'active': True,
    })
    created_count += 1
    print(f"  ✓ Created credential for {cafm.program_code}")
    
    env.cr.commit()
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    
    # Count credentials per program
    for prog in [cbplc, phri, pmp, cbpcs, cafm]:
        if prog:
            cred_count = Credential.search_count([('program_id', '=', prog.id)])
            creds = Credential.search([('program_id', '=', prog.id)])
            print(f"\n[{prog.program_code}] {prog.program_name}:")
            for cred in creds:
                renewal_info = f" (Renewal every {int(cred.renewal_cycle_years)} years)" if cred.renewal_required else " (No renewal required)"
                print(f"  - {cred.credential_name}")
                print(f"    Issuing Authority: {cred.issuing_authority}")
                print(f"    Delivery: {cred.certificate_delivery_days} days via {cred.delivery_method}")
                print(f"    Digital Badge: {cred.badge_platform if cred.digital_badge_available else 'Not available'}")
                print(f"    Renewal: {renewal_info}")
    
    total_credentials = Credential.search_count([])
    print(f"\n{'='*80}")
    print(f"Total credentials in database: {total_credentials}")
    print(f"Created in this session: {created_count}")
    
    print("\n" + "="*80)
    print("DEMO CREDENTIALS CREATED SUCCESSFULLY")
    print("="*80 + "\n")
    
except Exception as e:
    print(f"\n✗ ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
    env.cr.rollback()
