#!/usr/bin/env python3
import os
import re
from pathlib import Path

def add_css_link(file_path, is_subdirectory=False):
    """Add CSS link to HTML file if it doesn't already have it."""
    prefix = "../" if is_subdirectory else "./"
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check if the file already has the CSS link
    if f'href="{prefix}styles.css"' in content:
        print(f"CSS link already exists in {file_path}")
        return
    
    # Add the Font Awesome link if it doesn't exist
    if 'font-awesome' not in content:
        content = content.replace('</head>', 
                                 f'    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">\n</head>')
    
    # Add the CSS link
    content = content.replace('</head>', 
                             f'    <link rel="stylesheet" href="{prefix}styles.css">\n</head>')
    
    # Write the updated content back
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
        
    print(f"Added CSS link to {file_path}")

def main():
    # Process root directory files
    for file_path in Path('.').glob('*.html'):
        add_css_link(file_path)
    
    # Process about directory
    about_dir = Path('./about')
    if about_dir.exists():
        for file_path in about_dir.glob('*.html'):
            add_css_link(file_path, is_subdirectory=True)
    
    # Process how-it-works directory
    how_dir = Path('./how-it-works')
    if how_dir.exists():
        for file_path in how_dir.glob('*.html'):
            add_css_link(file_path, is_subdirectory=True)
    
    print("CSS link update completed")

if __name__ == "__main__":
    main() 