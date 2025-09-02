#!/usr/bin/env python3
"""
Installation script for Gear Wear Analysis System
This script checks prerequisites and installs required dependencies
"""

import sys
import subprocess
import os

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def install_package(package):
    """Install a single package using pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        return True
    except subprocess.CalledProcessError:
        return False

def install_requirements():
    """Install packages from requirements.txt"""
    print("📦 Installing dependencies...")
    
    # Core packages (install these first)
    core_packages = [
        "numpy",
        "opencv-python",
        "pandas",
        "matplotlib"
    ]
    
    for package in core_packages:
        print(f"Installing {package}...")
        if install_package(package):
            print(f"✅ {package} installed successfully")
        else:
            print(f"❌ Failed to install {package}")
            return False
    
    # Try to install from requirements.txt
    if os.path.exists("requirements.txt"):
        print("Installing from requirements.txt...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
            print("✅ All requirements installed successfully")
        except subprocess.CalledProcessError:
            print("⚠️ Some packages from requirements.txt failed to install")
            print("Core packages are installed, you can continue")
    
    return True

def create_directories():
    """Create necessary directories if they don't exist"""
    directories = ["database", "results", "logs"]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"📁 Created directory: {directory}")

def main():
    """Main installation function"""
    print("⚙️ Gear Wear Analysis System - Installation")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install dependencies
    if not install_requirements():
        print("❌ Installation failed")
        sys.exit(1)
    
    # Create directories
    create_directories()
    
    print("\n🎉 Installation completed successfully!")
    print("\nNext steps:")
    print("1. Place your gear images in the 'database' folder")
    print("2. Run 'python Main.py' to start the application")
    print("3. Check README.md for detailed usage instructions")

if __name__ == "__main__":
    main()
