#!/usr/bin/env python3
"""
Setup script for Grants Training Suite Odoo Addons
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(command, description=""):
    """Run a command and handle errors."""
    print(f"Running: {description or command}")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ Success: {description or command}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {description or command}")
        print(f"Error output: {e.stderr}")
        return None

def check_odoo_installation():
    """Check if Odoo is installed."""
    print("🔍 Checking Odoo installation...")
    result = run_command("odoo --version", "Check Odoo version")
    if result:
        print(f"Odoo version: {result.strip()}")
        return True
    else:
        print("❌ Odoo not found. Please install Odoo first.")
        return False

def install_requirements():
    """Install Python requirements."""
    print("📦 Installing Python requirements...")
    requirements_file = Path(__file__).parent / "requirements.txt"
    if requirements_file.exists():
        run_command(f"pip install -r {requirements_file}", "Install requirements")
    else:
        print("⚠️  requirements.txt not found")

def setup_addons_path():
    """Setup addons path in Odoo configuration."""
    print("⚙️  Setting up addons path...")
    addons_path = Path(__file__).parent.absolute()
    print(f"Addons path: {addons_path}")
    print(f"Add this path to your Odoo configuration file:")
    print(f"addons_path = {addons_path}")

def main():
    """Main setup function."""
    print("🚀 Grants Training Suite Setup")
    print("=" * 40)
    
    # Check Odoo installation
    if not check_odoo_installation():
        sys.exit(1)
    
    # Install requirements
    install_requirements()
    
    # Setup addons path
    setup_addons_path()
    
    print("\n✅ Setup completed!")
    print("\nNext steps:")
    print("1. Add the addons path to your Odoo configuration")
    print("2. Restart your Odoo server")
    print("3. Update the module list in Odoo")
    print("4. Install the desired module (v1 or v2)")

if __name__ == "__main__":
    main()
