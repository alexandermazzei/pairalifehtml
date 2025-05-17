#!/usr/bin/env python3
import os
import re
from pathlib import Path

def update_logo_reference(file_path, is_subdirectory=False):
    """Update logo references in HTML file."""
    prefix = "../" if is_subdirectory else "./"
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Update logo reference in the navbar
    content = re.sub(r'<img src="[^"]*" alt="PairaLife Logo"', 
                    f'<img src="{prefix}assets/images/logo.svg" alt="PairaLife Logo"', 
                    content)
    
    # Write the updated content back
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
        
    print(f"Updated logo reference in {file_path}")

def main():
    # Process root directory files
    for file_path in Path('.').glob('*.html'):
        update_logo_reference(file_path)
    
    # Process about directory
    about_dir = Path('./about')
    if about_dir.exists():
        for file_path in about_dir.glob('*.html'):
            update_logo_reference(file_path, is_subdirectory=True)
    
    # Process how-it-works directory
    how_dir = Path('./how-it-works')
    if how_dir.exists():
        for file_path in how_dir.glob('*.html'):
            update_logo_reference(file_path, is_subdirectory=True)
    
    print("Logo reference update completed")

if __name__ == "__main__":
    main() 