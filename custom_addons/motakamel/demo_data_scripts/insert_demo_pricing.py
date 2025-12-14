#!/usr/bin/env python3
"""
Insert Motakamel Demo Pricing Plans
"""

# Run in odoo shell: echo "exec(open('insert_demo_pricing.py').read())" | odoo-bin shell ...

from datetime import datetime, timedelta

try:
    print("\n" + "="*80)
    print("INSERTING MOTAKAMEL DEMO PRICING PLANS")
    print("="*80 + "\n")
    
    Program = env['motakamel.program']
    Pricing = env['motakamel.pricing']
    
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
    
    # CBPLC Pricing (2 plans)
    print(f"\nCreating pricing plans for {cbplc.program_code}...")
    
    Pricing.create({
        'program_id': cbplc.id,
        'pricing_name': 'Standard Plan',
        'pricing_type': 'standard',
        'list_price': 12500.0,
        'discount_price': 11500.0,
        'installments_allowed': True,
        'number_of_installments': 3,
        'installment_terms': 'Three equal installments: 40% upon registration, 30% before program start, 30% before exam date',
        'valid_from': '2025-11-06',
        'valid_to': '2026-06-04',
        'tax_applicable': True,
        'refund_policy': 'conditional',
        'refund_policy_details': 'Full refund if cancellation 14 days before start date. 50% refund if cancellation 7 days before. No refund after program starts.',
        'includes_exam_fee': True,
        'includes_materials': True,
        'includes_certificate': True,
        'is_default': True,
        'active': True,
    })
    created_count += 1
    
    Pricing.create({
        'program_id': cbplc.id,
        'pricing_name': 'Early Bird Discount',
        'pricing_type': 'early_bird',
        'list_price': 12500.0,
        'discount_price': 10500.0,
        'installments_allowed': True,
        'number_of_installments': 2,
        'valid_from': (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d'),
        'valid_to': '2025-12-21',
        'tax_applicable': True,
        'refund_policy': 'conditional',
        'includes_exam_fee': True,
        'includes_materials': True,
        'includes_certificate': True,
        'active': True,
    })
    created_count += 1
    print(f"  ✓ Created 2 pricing plans for {cbplc.program_code}")
    
    # PHRI Pricing (2 plans)
    print(f"\nCreating pricing plans for {phri.program_code}...")
    
    Pricing.create({
        'program_id': phri.id,
        'pricing_name': 'Standard Plan',
        'pricing_type': 'standard',
        'list_price': 18500.0,
        'discount_price': 17500.0,
        'installments_allowed': True,
        'number_of_installments': 4,
        'installment_terms': 'Four equal installments: 30% upon registration, 25% before program start, 25% mid-program, 20% before exam',
        'valid_from': '2025-11-11',
        'valid_to': '2026-06-24',
        'tax_applicable': True,
        'refund_policy': 'conditional',
        'refund_policy_details': 'Full refund if cancellation 21 days before start date. 70% refund if cancellation 14 days before. 50% refund if cancellation 7 days before. No refund after program starts.',
        'includes_exam_fee': True,
        'includes_materials': True,
        'includes_certificate': True,
        'is_default': True,
        'active': True,
    })
    created_count += 1
    
    Pricing.create({
        'program_id': phri.id,
        'pricing_name': 'Corporate Bulk',
        'pricing_type': 'corporate',
        'list_price': 18500.0,
        'discount_price': 16500.0,
        'corporate_bulk_discount': 10.0,
        'min_bulk_quantity': 5,
        'bulk_price': 14850.0,
        'valid_from': (datetime.now() - timedelta(days=25)).strftime('%Y-%m-%d'),
        'tax_applicable': True,
        'includes_exam_fee': True,
        'includes_materials': True,
        'includes_certificate': True,
        'active': True,
    })
    created_count += 1
    print(f"  ✓ Created 2 pricing plans for {phri.program_code}")
    
    # PMP Pricing (2 plans)
    print(f"\nCreating pricing plans for {pmp.program_code}...")
    
    Pricing.create({
        'program_id': pmp.id,
        'pricing_name': 'Standard Plan',
        'pricing_type': 'standard',
        'list_price': 22000.0,
        'discount_price': 21000.0,
        'installments_allowed': True,
        'number_of_installments': 4,
        'installment_terms': 'Four equal installments: 30% upon registration, 25% before program start, 25% mid-program, 20% before exam date',
        'valid_from': '2025-11-16',
        'valid_to': '2026-07-14',
        'tax_applicable': True,
        'refund_policy': 'conditional',
        'refund_policy_details': 'Full refund if cancellation 30 days before start date. 70% refund if cancellation 21 days before. 50% refund if cancellation 14 days before. No refund after program starts.',
        'includes_exam_fee': True,
        'includes_materials': True,
        'includes_certificate': True,
        'additional_inclusions': '35 PDUs certificate, PMI membership application support, 180-day access to exam simulator',
        'is_default': True,
        'active': True,
    })
    created_count += 1
    
    Pricing.create({
        'program_id': pmp.id,
        'pricing_name': 'Early Bird Special',
        'pricing_type': 'early_bird',
        'list_price': 22000.0,
        'discount_price': 19500.0,
        'installments_allowed': True,
        'number_of_installments': 3,
        'valid_from': (datetime.now() - timedelta(days=20)).strftime('%Y-%m-%d'),
        'valid_to': '2025-12-26',
        'tax_applicable': True,
        'refund_policy': 'conditional',
        'includes_exam_fee': True,
        'includes_materials': True,
        'includes_certificate': True,
        'active': True,
    })
    created_count += 1
    print(f"  ✓ Created 2 pricing plans for {pmp.program_code}")
    
    # CBPCS Pricing (1 plan)
    print(f"\nCreating pricing plans for {cbpcs.program_code}...")
    
    Pricing.create({
        'program_id': cbpcs.id,
        'pricing_name': 'Standard Plan',
        'pricing_type': 'standard',
        'list_price': 9500.0,
        'discount_price': 8500.0,
        'installments_allowed': True,
        'number_of_installments': 2,
        'installment_terms': 'Two equal installments: 50% upon registration, 50% before program start',
        'valid_from': '2025-11-21',
        'valid_to': '2026-05-05',
        'tax_applicable': True,
        'refund_policy': 'conditional',
        'refund_policy_details': 'Full refund if cancellation 10 days before start date. 50% refund if cancellation 5 days before. No refund after program starts.',
        'includes_exam_fee': True,
        'includes_materials': True,
        'includes_certificate': True,
        'is_default': True,
        'active': True,
    })
    created_count += 1
    print(f"  ✓ Created 1 pricing plan for {cbpcs.program_code}")
    
    # CAFM Pricing (2 plans)
    print(f"\nCreating pricing plans for {cafm.program_code}...")
    
    Pricing.create({
        'program_id': cafm.id,
        'pricing_name': 'Standard Plan',
        'pricing_type': 'standard',
        'list_price': 15000.0,
        'discount_price': 14000.0,
        'installments_allowed': True,
        'number_of_installments': 3,
        'installment_terms': 'Three equal installments: 40% upon registration, 30% before program start, 30% before exam date',
        'valid_from': '2025-11-26',
        'valid_to': '2026-05-25',
        'tax_applicable': True,
        'refund_policy': 'conditional',
        'refund_policy_details': 'Full refund if cancellation 14 days before start date. 50% refund if cancellation 7 days before. No refund after program starts.',
        'includes_exam_fee': True,
        'includes_materials': True,
        'includes_certificate': True,
        'additional_inclusions': 'IFMA study materials, online practice exams, facilities management toolkit',
        'is_default': True,
        'active': True,
    })
    created_count += 1
    
    Pricing.create({
        'program_id': cafm.id,
        'pricing_name': 'Early Bird Offer',
        'pricing_type': 'early_bird',
        'list_price': 15000.0,
        'discount_price': 12500.0,
        'installments_allowed': True,
        'number_of_installments': 2,
        'valid_from': (datetime.now() - timedelta(days=15)).strftime('%Y-%m-%d'),
        'valid_to': '2025-12-31',
        'tax_applicable': True,
        'refund_policy': 'conditional',
        'includes_exam_fee': True,
        'includes_materials': True,
        'includes_certificate': True,
        'active': True,
    })
    created_count += 1
    print(f"  ✓ Created 2 pricing plans for {cafm.program_code}")
    
    env.cr.commit()
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    
    # Count pricing plans per program
    for prog in [cbplc, phri, pmp, cbpcs, cafm]:
        if prog:
            price_count = Pricing.search_count([('program_id', '=', prog.id)])
            prices = Pricing.search([('program_id', '=', prog.id)])
            print(f"\n[{prog.program_code}] {prog.program_name}: {price_count} pricing plan(s)")
            for price in prices:
                print(f"  - {price.pricing_name}: {price.discount_price} EGP ({price.pricing_type})")
    
    total_pricing = Pricing.search_count([])
    print(f"\nTotal pricing plans in database: {total_pricing}")
    print(f"Created in this session: {created_count}")
    
    print("\n" + "="*80)
    print("DEMO PRICING PLANS CREATED SUCCESSFULLY")
    print("="*80 + "\n")
    
except Exception as e:
    print(f"\n✗ ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
    env.cr.rollback()
