#!/usr/bin/env python3
import os
import re
from pathlib import Path

def update_file_links(file_path, is_subdirectory=False):
    """Update links in an HTML file."""
    prefix = "../" if is_subdirectory else "./"
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Update header links
    content = content.replace('<a href="#" class="btn btn-secondary">Log In</a>', 
                             f'<a href="{prefix}login.html" class="btn btn-secondary">Log In</a>')
    content = content.replace('<a href="#" class="btn">Sign Up</a>', 
                             f'<a href="{prefix}signup.html" class="btn">Sign Up</a>')
    
    # Update main navigation
    content = content.replace('<a href="#how-it-works" class="nav-link">How It Works</a>', 
                             f'<a href="{prefix}how-it-works/index.html" class="nav-link">How It Works</a>')
    content = content.replace('<a href="#benefits" class="nav-link">Benefits</a>', 
                             f'<a href="{prefix}index.html#benefits" class="nav-link">Benefits</a>')
    content = content.replace('<a href="#features" class="nav-link">Features</a>', 
                             f'<a href="{prefix}index.html#features" class="nav-link">Features</a>')
    content = content.replace('<a href="#about" class="nav-link">About</a>', 
                             f'<a href="{prefix}about/about-us.html" class="nav-link">About</a>')
    
    # Update footer links
    content = content.replace('<li class="footer-link"><a href="#">Find a Home</a></li>', 
                             f'<li class="footer-link"><a href="{prefix}browse-listings.html">Find a Home</a></li>')
    content = content.replace('<li class="footer-link"><a href="#">List Your Space</a></li>', 
                             f'<li class="footer-link"><a href="{prefix}create-listing.html">List Your Space</a></li>')
    content = content.replace('<li class="footer-link"><a href="#">How It Works</a></li>', 
                             f'<li class="footer-link"><a href="{prefix}how-it-works/index.html">How It Works</a></li>')
    content = content.replace('<li class="footer-link"><a href="#">Community</a></li>', 
                             f'<li class="footer-link"><a href="{prefix}dashboard.html">Community</a></li>')
    
    # Update company links
    content = content.replace('<li class="footer-link"><a href="#">About Us</a></li>', 
                             f'<li class="footer-link"><a href="{prefix}about/about-us.html">About Us</a></li>')
    content = content.replace('<li class="footer-link"><a href="#">Careers</a></li>', 
                             f'<li class="footer-link"><a href="{prefix}about/team.html#careers">Careers</a></li>')
    content = content.replace('<li class="footer-link"><a href="#">Press</a></li>', 
                             f'<li class="footer-link"><a href="{prefix}about/press.html">Press</a></li>')
    content = content.replace('<li class="footer-link"><a href="#">Contact</a></li>', 
                             f'<li class="footer-link"><a href="{prefix}contact-support.html">Contact</a></li>')
    
    # Update support links
    content = content.replace('<li class="footer-link"><a href="#">Help Center</a></li>', 
                             f'<li class="footer-link"><a href="{prefix}help-center.html">Help Center</a></li>')
    content = content.replace('<li class="footer-link"><a href="#">Safety Center</a></li>', 
                             f'<li class="footer-link"><a href="{prefix}safety-center.html">Safety Center</a></li>')
    content = content.replace('<li class="footer-link"><a href="#">Resources</a></li>', 
                             f'<li class="footer-link"><a href="{prefix}help-center.html#resources">Resources</a></li>')
    content = content.replace('<li class="footer-link"><a href="#">FAQ</a></li>', 
                             f'<li class="footer-link"><a href="{prefix}faq.html">FAQ</a></li>')
    
    # Update CTA buttons
    content = content.replace('<a href="#" class="btn btn-large">Find a Home</a>', 
                             f'<a href="{prefix}browse-listings.html" class="btn btn-large">Find a Home</a>')
    content = content.replace('<a href="#" class="btn btn-secondary btn-large">List Your Space</a>', 
                             f'<a href="{prefix}create-listing.html" class="btn btn-secondary btn-large">List Your Space</a>')
    content = content.replace('<a href="#" class="btn btn-large cta-button">Get Started</a>', 
                             f'<a href="{prefix}signup.html" class="btn btn-large cta-button">Get Started</a>')
    content = content.replace('<a href="#" class="btn btn-large cta-button">Get Started Today</a>', 
                             f'<a href="{prefix}signup.html" class="btn btn-large cta-button">Get Started Today</a>')
    
    # Fix about directory links
    if "about/" in str(file_path):
        # Fix links to other about pages
        content = re.sub(r'href="about/', 'href="', content)
        content = re.sub(r'href="our-story', 'href="our-story', content)
        content = re.sub(r'href="press', 'href="press', content)
        content = re.sub(r'href="team', 'href="team', content)
    
    # Fix how-it-works directory links
    if "how-it-works/" in str(file_path):
        # Fix links to other how-it-works pages
        content = re.sub(r'href="how-it-works/', 'href="', content)
        content = re.sub(r'href="index', 'href="index', content)
        content = re.sub(r'href="for-homeowners', 'href="for-homeowners', content)
        content = re.sub(r'href="for-seniors', 'href="for-seniors', content)
        content = re.sub(r'href="for-young-adults', 'href="for-young-adults', content)
        content = re.sub(r'href="safety-process', 'href="safety-process', content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"Updated links in {file_path}")

def main():
    # Process root directory files
    for file_path in Path('.').glob('*.html'):
        update_file_links(file_path)
    
    # Process about directory
    about_dir = Path('./about')
    if about_dir.exists():
        for file_path in about_dir.glob('*.html'):
            update_file_links(file_path, is_subdirectory=True)
    
    # Process how-it-works directory
    how_dir = Path('./how-it-works')
    if how_dir.exists():
        for file_path in how_dir.glob('*.html'):
            update_file_links(file_path, is_subdirectory=True)
    
    print("Link update completed")

if __name__ == "__main__":
    main() 