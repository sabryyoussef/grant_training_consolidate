#!/usr/bin/env python3
"""
Force recomputation of enrollment data for all marketing campaigns
"""

print("="*80)
print("RECOMPUTING ENROLLMENT DATA FOR ALL MARKETING CAMPAIGNS")
print("="*80 + "\n")

Marketing = env['motakamel.marketing']

try:
    all_marketing = Marketing.search([])
    print(f"Found {len(all_marketing)} marketing campaigns\n")
    
    for marketing in all_marketing:
        print(f"Processing: {marketing.campaign_name}")
        print(f"  Program: {marketing.program_id.program_name if marketing.program_id else 'None'}")
        
        # Force recompute
        marketing._compute_students_and_leads()
        
        print(f"  ✓ Enrolled Students: {marketing.enrolled_count}")
        if marketing.enrolled_student_ids:
            for student in marketing.enrolled_student_ids[:3]:  # First 3
                print(f"    - {student.name}")
            if len(marketing.enrolled_student_ids) > 3:
                print(f"    ... and {len(marketing.enrolled_student_ids) - 3} more")
        print()
    
    # Commit
    env.cr.commit()
    
    print("="*80)
    print("✓ SUCCESS! All marketing campaigns updated")
    print("="*80 + "\n")
    
except Exception as e:
    print(f"\n✗ ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
    env.cr.rollback()
