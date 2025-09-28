#!/usr/bin/env python3
"""
Grants Training Suite - Checkpoint Testing Script
================================================

This script automates the testing process for each phase checkpoint.
Run this script after completing each phase to verify functionality.

Usage:
    python3 checkpoint_testing_script.py --phase 1
    python3 checkpoint_testing_script.py --phase 2 --verbose
    python3 checkpoint_testing_script.py --all-phases
"""

import argparse
import sys
import os
import subprocess
import json
import time
from datetime import datetime
from pathlib import Path

class CheckpointTester:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.results = {}
        self.error_logs = []
        self.project_root = Path(__file__).parent.parent
        self.log_dir = self.project_root / "logs"
        self.error_tracking_dir = self.log_dir / "error_tracking"
        
    def log(self, message, level="INFO"):
        """Log message with timestamp."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {level}: {message}")
        
    def run_command(self, command, description=""):
        """Run a command and return result."""
        if self.verbose:
            self.log(f"Running: {command}")
            
        try:
            result = subprocess.run(
                command, 
                shell=True, 
                capture_output=True, 
                text=True, 
                timeout=300
            )
            
            if result.returncode == 0:
                self.log(f"✅ {description} - SUCCESS")
                return True, result.stdout
            else:
                self.log(f"❌ {description} - FAILED: {result.stderr}")
                return False, result.stderr
                
        except subprocess.TimeoutExpired:
            self.log(f"⏰ {description} - TIMEOUT")
            return False, "Command timed out"
        except Exception as e:
            self.log(f"💥 {description} - ERROR: {str(e)}")
            return False, str(e)
    
    def check_file_exists(self, file_path, description=""):
        """Check if file exists."""
        if os.path.exists(file_path):
            self.log(f"✅ {description} - File exists: {file_path}")
            return True
        else:
            self.log(f"❌ {description} - File missing: {file_path}")
            return False
    
    def check_directory_exists(self, dir_path, description=""):
        """Check if directory exists."""
        if os.path.isdir(dir_path):
            self.log(f"✅ {description} - Directory exists: {dir_path}")
            return True
        else:
            self.log(f"❌ {description} - Directory missing: {dir_path}")
            return False
    
    def test_phase_1_foundation(self):
        """Test Phase 1: Foundation & Core Models."""
        self.log("🧪 Testing Phase 1: Foundation & Core Models")
        phase_results = {"passed": 0, "failed": 0, "tests": []}
        
        # Test 1.1: Module Structure
        self.log("📁 Testing module structure...")
        required_files = [
            "grants_training_suite/__init__.py",
            "grants_training_suite/__manifest__.py",
            "grants_training_suite/models/__init__.py",
            "grants_training_suite/models/intake_batch.py",
            "grants_training_suite/models/student.py",
            "grants_training_suite/models/assignment.py",
            "grants_training_suite/security/ir.model.access.csv",
            "grants_training_suite/views/menu.xml"
        ]
        
        for file_path in required_files:
            full_path = self.project_root / file_path
            if self.check_file_exists(full_path, f"Module file: {file_path}"):
                phase_results["passed"] += 1
            else:
                phase_results["failed"] += 1
            phase_results["tests"].append(f"File exists: {file_path}")
        
        # Test 1.2: Error Tracking System
        self.log("🔍 Testing error tracking system...")
        error_files = [
            "logs/error_tracking/README.md",
            "logs/error_tracking/sample_errors.log"
        ]
        
        for file_path in error_files:
            full_path = self.project_root / file_path
            if self.check_file_exists(full_path, f"Error tracking: {file_path}"):
                phase_results["passed"] += 1
            else:
                phase_results["failed"] += 1
            phase_results["tests"].append(f"Error tracking: {file_path}")
        
        # Test 1.3: Configuration Files
        self.log("⚙️ Testing configuration files...")
        config_files = [
            "odoo_conf/odoo.conf",
            "DEVELOPMENT_RULES.md",
            "GRANTS_TRAINING_PROJECT_PLAN.md"
        ]
        
        for file_path in config_files:
            full_path = self.project_root / file_path
            if self.check_file_exists(full_path, f"Config file: {file_path}"):
                phase_results["passed"] += 1
            else:
                phase_results["failed"] += 1
            phase_results["tests"].append(f"Config file: {file_path}")
        
        # Test 1.4: Odoo Configuration
        self.log("🔧 Testing Odoo configuration...")
        odoo_conf_path = self.project_root / "odoo_conf/odoo.conf"
        if odoo_conf_path.exists():
            with open(odoo_conf_path, 'r') as f:
                content = f.read()
                if "grants_training_suite:DEBUG" in content:
                    self.log("✅ Odoo configuration - Module logging configured")
                    phase_results["passed"] += 1
                else:
                    self.log("❌ Odoo configuration - Module logging not configured")
                    phase_results["failed"] += 1
                phase_results["tests"].append("Odoo logging configuration")
        
        self.results["phase_1"] = phase_results
        return phase_results["failed"] == 0
    
    def test_phase_2_intake_processing(self):
        """Test Phase 2: Intake Processing & Validation."""
        self.log("🧪 Testing Phase 2: Intake Processing & Validation")
        phase_results = {"passed": 0, "failed": 0, "tests": []}
        
        # Test 2.1: Intake Models
        self.log("📊 Testing intake models...")
        intake_files = [
            "grants_training_suite/models/intake_batch.py",
            "grants_training_suite/wizard/intake_validate_wizard.py",
            "grants_training_suite/wizard/intake_validate_wizard_views.xml"
        ]
        
        for file_path in intake_files:
            full_path = self.project_root / file_path
            if self.check_file_exists(full_path, f"Intake file: {file_path}"):
                phase_results["passed"] += 1
            else:
                phase_results["failed"] += 1
            phase_results["tests"].append(f"Intake file: {file_path}")
        
        # Test 2.2: File Processing Logic
        self.log("📁 Testing file processing logic...")
        intake_batch_file = self.project_root / "grants_training_suite/models/intake_batch.py"
        if intake_batch_file.exists():
            with open(intake_batch_file, 'r') as f:
                content = f.read()
                required_methods = [
                    "_parse_csv",
                    "_parse_excel", 
                    "_create_students",
                    "_assess_eligibility"
                ]
                
                for method in required_methods:
                    if method in content:
                        self.log(f"✅ Method exists: {method}")
                        phase_results["passed"] += 1
                    else:
                        self.log(f"❌ Method missing: {method}")
                        phase_results["failed"] += 1
                    phase_results["tests"].append(f"Method: {method}")
        
        # Test 2.3: Error Handling
        self.log("🚨 Testing error handling...")
        if "error_tracker" in content:
            self.log("✅ Error tracking integrated")
            phase_results["passed"] += 1
        else:
            self.log("❌ Error tracking not integrated")
            phase_results["failed"] += 1
        phase_results["tests"].append("Error tracking integration")
        
        self.results["phase_2"] = phase_results
        return phase_results["failed"] == 0
    
    def test_phase_3_agent_assignment(self):
        """Test Phase 3: Agent Assignment & Workflow."""
        self.log("🧪 Testing Phase 3: Agent Assignment & Workflow")
        phase_results = {"passed": 0, "failed": 0, "tests": []}
        
        # Test 3.1: Assignment Models
        self.log("👥 Testing assignment models...")
        assignment_files = [
            "grants_training_suite/models/assignment.py",
            "grants_training_suite/views/assignment_views.xml"
        ]
        
        for file_path in assignment_files:
            full_path = self.project_root / file_path
            if self.check_file_exists(full_path, f"Assignment file: {file_path}"):
                phase_results["passed"] += 1
            else:
                phase_results["failed"] += 1
            phase_results["tests"].append(f"Assignment file: {file_path}")
        
        # Test 3.2: Assignment Logic
        self.log("🔄 Testing assignment logic...")
        assignment_file = self.project_root / "grants_training_suite/models/assignment.py"
        if assignment_file.exists():
            with open(assignment_file, 'r') as f:
                content = f.read()
                required_methods = [
                    "auto_assign_students",
                    "_get_next_agent",
                    "action_mark_contacted",
                    "action_mark_done"
                ]
                
                for method in required_methods:
                    if method in content:
                        self.log(f"✅ Method exists: {method}")
                        phase_results["passed"] += 1
                    else:
                        self.log(f"❌ Method missing: {method}")
                        phase_results["failed"] += 1
                    phase_results["tests"].append(f"Method: {method}")
        
        # Test 3.3: Cron Jobs
        self.log("⏰ Testing cron jobs...")
        cron_file = self.project_root / "grants_training_suite/data/cron.xml"
        if cron_file.exists():
            with open(cron_file, 'r') as f:
                content = f.read()
                if "auto_assign_students" in content:
                    self.log("✅ Auto-assignment cron configured")
                    phase_results["passed"] += 1
                else:
                    self.log("❌ Auto-assignment cron not configured")
                    phase_results["failed"] += 1
                phase_results["tests"].append("Auto-assignment cron")
        
        self.results["phase_3"] = phase_results
        return phase_results["failed"] == 0
    
    def test_error_tracking_system(self):
        """Test the error tracking system."""
        self.log("🔍 Testing error tracking system...")
        error_results = {"passed": 0, "failed": 0, "tests": []}
        
        # Test error tracking directory
        if self.check_directory_exists(self.error_tracking_dir, "Error tracking directory"):
            error_results["passed"] += 1
        else:
            error_results["failed"] += 1
        error_results["tests"].append("Error tracking directory")
        
        # Test error tracking utility
        error_tracker_file = self.project_root / "grants_training_suite/utils/error_tracker.py"
        if self.check_file_exists(error_tracker_file, "Error tracker utility"):
            error_results["passed"] += 1
        else:
            error_results["failed"] += 1
        error_results["tests"].append("Error tracker utility")
        
        # Test error integration
        if error_tracker_file.exists():
            with open(error_tracker_file, 'r') as f:
                content = f.read()
                required_methods = [
                    "log_error",
                    "log_intake_error",
                    "log_assignment_error",
                    "get_error_summary"
                ]
                
                for method in required_methods:
                    if method in content:
                        self.log(f"✅ Error method exists: {method}")
                        error_results["passed"] += 1
                    else:
                        self.log(f"❌ Error method missing: {method}")
                        error_results["failed"] += 1
                    error_results["tests"].append(f"Error method: {method}")
        
        self.results["error_tracking"] = error_results
        return error_results["failed"] == 0
    
    def generate_report(self):
        """Generate test report."""
        self.log("📊 Generating test report...")
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "total_phases": len(self.results),
            "phases": self.results,
            "summary": {
                "total_tests": 0,
                "total_passed": 0,
                "total_failed": 0
            }
        }
        
        for phase, results in self.results.items():
            report["summary"]["total_tests"] += len(results["tests"])
            report["summary"]["total_passed"] += results["passed"]
            report["summary"]["total_failed"] += results["failed"]
        
        # Save report
        report_file = self.project_root / "logs" / f"checkpoint_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        self.log(f"📄 Report saved: {report_file}")
        
        # Print summary
        self.log("=" * 50)
        self.log("📊 CHECKPOINT TEST SUMMARY")
        self.log("=" * 50)
        self.log(f"Total Tests: {report['summary']['total_tests']}")
        self.log(f"Passed: {report['summary']['total_passed']}")
        self.log(f"Failed: {report['summary']['total_failed']}")
        self.log(f"Success Rate: {(report['summary']['total_passed'] / report['summary']['total_tests'] * 100):.1f}%")
        
        for phase, results in self.results.items():
            self.log(f"\n{phase.upper()}:")
            self.log(f"  Passed: {results['passed']}")
            self.log(f"  Failed: {results['failed']}")
            if results['failed'] > 0:
                self.log(f"  ❌ PHASE FAILED")
            else:
                self.log(f"  ✅ PHASE PASSED")
        
        return report["summary"]["total_failed"] == 0
    
    def run_phase_tests(self, phase):
        """Run tests for specific phase."""
        if phase == 1:
            return self.test_phase_1_foundation()
        elif phase == 2:
            return self.test_phase_2_intake_processing()
        elif phase == 3:
            return self.test_phase_3_agent_assignment()
        else:
            self.log(f"❌ Phase {phase} not implemented yet")
            return False
    
    def run_all_tests(self):
        """Run all available tests."""
        self.log("🚀 Running all checkpoint tests...")
        
        # Test error tracking system
        self.test_error_tracking_system()
        
        # Test available phases
        for phase in [1, 2, 3]:
            self.run_phase_tests(phase)
        
        # Generate report
        return self.generate_report()

def main():
    parser = argparse.ArgumentParser(description="Grants Training Suite Checkpoint Tester")
    parser.add_argument("--phase", type=int, help="Test specific phase (1-9)")
    parser.add_argument("--all-phases", action="store_true", help="Test all available phases")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")
    
    args = parser.parse_args()
    
    tester = CheckpointTester(verbose=args.verbose)
    
    if args.phase:
        success = tester.run_phase_tests(args.phase)
        tester.generate_report()
        sys.exit(0 if success else 1)
    elif args.all_phases:
        success = tester.run_all_tests()
        sys.exit(0 if success else 1)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
