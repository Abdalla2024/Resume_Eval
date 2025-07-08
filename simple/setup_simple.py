#!/usr/bin/env python3
"""
Simple setup script for Resume Evaluator (without spaCy)
"""
import subprocess
import sys
import os

def install_requirements():
    """Install Python requirements"""
    try:
        print("🔧 Installing Python requirements...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements_simple.txt'])
        print("✅ Python requirements installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to install Python requirements")
        return False
    return True

def main():
    """Main setup function"""
    print("🚀 Setting up Resume Evaluator (Simple Version)...")
    
    # Check if requirements.txt exists
    if not os.path.exists('requirements_simple.txt'):
        print("❌ requirements_simple.txt not found")
        return
    
    # Install requirements
    if not install_requirements():
        return
    
    print("\n✅ Setup complete! You can now run the application with:")
    print("   python3 app_simple.py")
    print("\nThen open your browser and go to: http://localhost:5001")
    print("\nNote: Using port 5001 because port 5000 is often used by macOS AirPlay")

if __name__ == "__main__":
    main() 