# -*- coding: utf-8 -*-
"""
Demo Data Loader for Motakamel Module
Automatically loads demo data when module is installed/updated
"""

import logging
import os

_logger = logging.getLogger(__name__)

def load_demo_data(env):
    """
    Load all demo data scripts in the correct order
    This function is called by the post_init_hook
    """
    _logger.info("=" * 80)
    _logger.info("LOADING MOTAKAMEL DEMO DATA")
    _logger.info("=" * 80)
    
    # Get the directory containing this file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    scripts_dir = os.path.join(current_dir, 'demo_data_scripts')
    
    # Define scripts in execution order
    scripts = [
        'insert_demo_programs.py',
        'insert_demo_accreditations.py',
        'insert_demo_audiences.py',
        'insert_demo_pricing.py',
        'insert_demo_credentials.py',
        'insert_demo_marketing.py',
        'insert_demo_courses.py',
        'insert_demo_students_batches.py',
        'update_course_names.py',
        'create_deliveries.py',
        'recompute_enrollments.py',
    ]
    
    success_count = 0
    failed_scripts = []
    
    for script_name in scripts:
        script_path = os.path.join(scripts_dir, script_name)
        
        if not os.path.exists(script_path):
            _logger.warning(f"Script not found: {script_name}")
            continue
        
        try:
            _logger.info(f"Executing: {script_name}")
            
            # Read and execute the script
            with open(script_path, 'r', encoding='utf-8') as f:
                script_content = f.read()
            
            # Execute in the environment context
            exec(script_content, {'env': env})
            
            success_count += 1
            _logger.info(f"✓ Successfully executed: {script_name}")
            
        except Exception as e:
            _logger.error(f"✗ Error executing {script_name}: {str(e)}")
            failed_scripts.append(script_name)
            # Continue with next script instead of stopping
            continue
    
    _logger.info("=" * 80)
    _logger.info(f"DEMO DATA LOADING COMPLETE")
    _logger.info(f"Successful: {success_count}/{len(scripts)}")
    if failed_scripts:
        _logger.warning(f"Failed scripts: {', '.join(failed_scripts)}")
    _logger.info("=" * 80)
    
    return True
