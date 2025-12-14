#!/usr/bin/env python3
"""
Update course names to match program names for proper enrollment linking
"""

print("="*80)
print("UPDATING COURSE NAMES TO MATCH PROGRAMS")
print("="*80 + "\n")

OpCourse = env['op.course']
Program = env['motakamel.program']

try:
    # Get programs
    cbplc_prog = Program.search([('program_code', '=', 'CBPLC')], limit=1)
    phri_prog = Program.search([('program_code', '=', 'PHRI')], limit=1)
    pmp_prog = Program.search([('program_code', '=', 'PMP')], limit=1)
    
    # Get courses
    cbplc_course = OpCourse.search([('code', '=', 'CBPLC-2026')], limit=1)
    phri_course = OpCourse.search([('code', '=', 'PHRI-2026')], limit=1)
    pmp_course = OpCourse.search([('code', '=', 'PMP-2026')], limit=1)
    
    updated = 0
    
    if cbplc_course and cbplc_prog:
        print(f"Updating CBPLC course...")
        print(f"  From: {cbplc_course.name}")
        print(f"  To: {cbplc_prog.program_name}")
        cbplc_course.write({'name': cbplc_prog.program_name})
        updated += 1
    
    if phri_course and phri_prog:
        print(f"\nUpdating PHRI course...")
        print(f"  From: {phri_course.name}")
        print(f"  To: {phri_prog.program_name}")
        phri_course.write({'name': phri_prog.program_name})
        updated += 1
    
    if pmp_course and pmp_prog:
        print(f"\nUpdating PMP course...")
        print(f"  From: {pmp_course.name}")
        print(f"  To: {pmp_prog.program_name}")
        pmp_course.write({'name': pmp_prog.program_name})
        updated += 1
    
    # Commit
    env.cr.commit()
    
    print("\n" + "="*80)
    print(f"✓ SUCCESS! Updated {updated} course names")
    print("="*80 + "\n")
    
except Exception as e:
    print(f"\n✗ ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
    env.cr.rollback()
