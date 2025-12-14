#!/usr/bin/env python3
"""
Check OpenEduCat module installation and op.student model availability
"""

print("="*80)
print("CHECKING OPENEDUCAT INSTALLATION")
print("="*80 + "\n")

try:
    # Check if op.student model exists
    try:
        Student = env['op.student']
        print("✓ op.student model is available")
        
        # Check for views
        View = env['ir.ui.view']
        student_views = View.search([
            ('model', '=', 'op.student'),
            ('type', '=', 'tree')
        ])
        
        print(f"  Found {len(student_views)} tree views for op.student:")
        for view in student_views:
            print(f"    - {view.name} (ID: {view.id})")
        
        if not student_views:
            print("  ⚠ WARNING: No tree view found for op.student!")
            
        # Check for actions
        Action = env['ir.actions.act_window']
        student_actions = Action.search([('res_model', '=', 'op.student')])
        print(f"\n  Found {len(student_actions)} actions for op.student:")
        for action in student_actions[:5]:
            print(f"    - {action.name} (view_mode: {action.view_mode})")
            
    except KeyError:
        print("✗ op.student model NOT FOUND")
        print("  OpenEduCat core module may not be installed")
    
    # Check installed modules
    print("\n" + "="*80)
    print("Checking installed modules related to OpenEduCat:")
    Module = env['ir.module.module']
    
    openeducat_modules = Module.search([
        ('name', 'ilike', 'openeducat'),
        ('state', '=', 'installed')
    ])
    
    if openeducat_modules:
        print(f"✓ Found {len(openeducat_modules)} installed OpenEduCat modules:")
        for mod in openeducat_modules:
            print(f"  - {mod.name} ({mod.shortdesc})")
    else:
        print("✗ No OpenEduCat modules installed!")
    
    # Check batch_intake module
    batch_module = Module.search([('name', '=', 'batch_intake')], limit=1)
    if batch_module:
        print(f"\n✓ batch_intake module: {batch_module.state}")
    
    print("="*80 + "\n")
    
except Exception as e:
    print(f"\n✗ ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
