#!/usr/bin/env python3
"""
Setup script for Resume Evaluator
"""
import subprocess
import sys
import os

def install_requirements():
    """Install Python requirements"""
    try:
        print("Installing Python requirements...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✓ Python requirements installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to install Python requirements")
        return False
    return True

def download_spacy_model():
    """Download spaCy English model"""
    try:
        print("Downloading spaCy English model...")
        subprocess.check_call([sys.executable, '-m', 'spacy', 'download', 'en_core_web_sm'])
        print("✓ spaCy model downloaded successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to download spaCy model")
        return False
    return True

def main():
    """Main setup function"""
    print("🚀 Setting up Resume Evaluator...")
    
    # Check if requirements.txt exists
    if not os.path.exists('requirements.txt'):
        print("❌ requirements.txt not found")
        return
    
    # Install requirements
    if not install_requirements():
        return
    
    # Download spaCy model
    if not download_spacy_model():
        return
    
    print("\n✅ Setup complete! You can now run the application with:")
    print("   python app.py")
    print("\nThen open your browser and go to: http://localhost:5000")

if __name__ == "__main__":
    main() 