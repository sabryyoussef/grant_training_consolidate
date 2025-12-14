#!/usr/bin/env python3
"""
Load Motakamel Demo Data
This script loads demo data for the motakamel module by directly calling Odoo's data loading mechanism.
"""

import sys
import os

# This script should be run with odoo-bin shell
# Example: echo "exec(open('load_motakamel_demo.py').read())" | odoo-bin shell -c odoo.conf -d database_name

try:
    # Get the environment from the shell context
    # env should be available when running in odoo shell
    
    print("\n" + "="*80)
    print("LOADING MOTAKAMEL DEMO DATA")
    print("="*80 + "\n")
    
    # Check current state
    Program = env['motakamel.program']
    existing_count = Program.search_count([])
    print(f"Current programs in database: {existing_count}")
    
    # Get module path
    import odoo.modules as addons
    module_path = addons.get_module_path('motakamel')
    print(f"Module path: {module_path}")
    
    # List of demo files to load
    demo_files = [
        'data/motakamel_program_demo.xml',
        'data/motakamel_accreditation_demo.xml',
        'data/motakamel_audience_demo.xml',
        'data/motakamel_delivery_demo.xml',
        'data/motakamel_pricing_demo.xml',
        'data/motakamel_credential_demo.xml',
        'data/motakamel_marketing_demo.xml',
    ]
    
    print(f"\nLoading {len(demo_files)} demo data files...\n")
    
    # Load each demo file
    for demo_file in demo_files:
        full_path = os.path.join(module_path, demo_file)
        if os.path.exists(full_path):
            print(f"Loading: {demo_file}")
            try:
                # Use Odoo's convert_file to load XML data
                from odoo.tools import convert
                with open(full_path, 'rb') as fp:
                    convert.convert_xml_import(env.cr, 'motakamel', fp, idref={}, mode='init', noupdate=False)
                env.cr.commit()
                print(f"  ✓ Successfully loaded {demo_file}")
            except Exception as e:
                print(f"  ✗ Error loading {demo_file}: {str(e)}")
                env.cr.rollback()
        else:
            print(f"  ⚠ File not found: {full_path}")
    
    # Check final state
    final_count = Program.search_count([])
    print(f"\n" + "="*80)
    print(f"SUMMARY")
    print("="*80)
    print(f"Programs before: {existing_count}")
    print(f"Programs after: {final_count}")
    print(f"Programs added: {final_count - existing_count}")
    
    # List all programs
    if final_count > 0:
        print(f"\nAll programs in database:")
        programs = Program.search([])
        for p in programs:
            print(f"  - [{p.program_code}] {p.program_name} (Status: {p.status})")
    
    print("\n" + "="*80)
    print("DEMO DATA LOADING COMPLETE")
    print("="*80 + "\n")
    
except Exception as e:
    print(f"\n✗ ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
