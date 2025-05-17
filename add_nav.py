#!/usr/bin/env python3
import os
import re
from pathlib import Path

def create_nav_html(is_subdirectory=False):
    """Create the navigation HTML with proper paths."""
    prefix = "../" if is_subdirectory else "./"
    
    nav_html = f'''
    <nav class="navbar">
        <div class="navbar-container">
            <a href="{prefix}index.html" class="logo">
                <img src="{prefix}assets/images/logo.png" alt="PairaLife Logo" />
                <span>PairaLife</span>
            </a>
            <div class="nav-links">
                <a href="{prefix}how-it-works/index.html" class="nav-link">How It Works</a>
                <a href="{prefix}browse-listings.html" class="nav-link">Browse Listings</a>
                <a href="{prefix}about/about-us.html" class="nav-link">About</a>
                <a href="{prefix}safety-center.html" class="nav-link">Safety</a>
                <a href="{prefix}faq.html" class="nav-link">FAQ</a>
                <a href="{prefix}contact-support.html" class="nav-link">Contact</a>
            </div>
            <div class="auth-buttons">
                <a href="{prefix}login.html" class="btn btn-secondary">Log In</a>
                <a href="{prefix}signup.html" class="btn">Sign Up</a>
            </div>
        </div>
    </nav>
    '''
    return nav_html

def create_footer_html(is_subdirectory=False):
    """Create the footer HTML with proper paths."""
    prefix = "../" if is_subdirectory else "./"
    
    footer_html = f'''
    <footer class="site-footer">
        <div class="footer-container">
            <div class="footer-section">
                <h3>PairaLife</h3>
                <ul class="footer-links">
                    <li class="footer-link"><a href="{prefix}browse-listings.html">Find a Home</a></li>
                    <li class="footer-link"><a href="{prefix}create-listing.html">List Your Space</a></li>
                    <li class="footer-link"><a href="{prefix}how-it-works/index.html">How It Works</a></li>
                    <li class="footer-link"><a href="{prefix}dashboard.html">Community</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h3>Company</h3>
                <ul class="footer-links">
                    <li class="footer-link"><a href="{prefix}about/about-us.html">About Us</a></li>
                    <li class="footer-link"><a href="{prefix}about/team.html#careers">Careers</a></li>
                    <li class="footer-link"><a href="{prefix}about/press.html">Press</a></li>
                    <li class="footer-link"><a href="{prefix}contact-support.html">Contact</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h3>Support</h3>
                <ul class="footer-links">
                    <li class="footer-link"><a href="{prefix}help-center.html">Help Center</a></li>
                    <li class="footer-link"><a href="{prefix}safety-center.html">Safety Center</a></li>
                    <li class="footer-link"><a href="{prefix}help-center.html#resources">Resources</a></li>
                    <li class="footer-link"><a href="{prefix}faq.html">FAQ</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h3>Legal</h3>
                <ul class="footer-links">
                    <li class="footer-link"><a href="{prefix}privacy-policy.html">Privacy Policy</a></li>
                    <li class="footer-link"><a href="{prefix}terms-of-service.html">Terms of Service</a></li>
                    <li class="footer-link"><a href="{prefix}cookie-policy.html">Cookie Policy</a></li>
                    <li class="footer-link"><a href="{prefix}sitemap.html">Sitemap</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2023 PairaLife. All rights reserved.</p>
            <div class="social-icons">
                <a href="#" class="social-icon"><i class="fab fa-facebook-f"></i></a>
                <a href="#" class="social-icon"><i class="fab fa-twitter"></i></a>
                <a href="#" class="social-icon"><i class="fab fa-instagram"></i></a>
                <a href="#" class="social-icon"><i class="fab fa-linkedin-in"></i></a>
            </div>
        </div>
    </footer>
    '''
    return footer_html

def add_navigation(file_path, is_subdirectory=False):
    """Add navigation to HTML file if it doesn't already have it."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check if there's already a navbar
    if '<nav class="navbar">' in content:
        print(f"Navigation already exists in {file_path}")
        return
    
    # Find the body tag
    body_match = re.search(r'<body[^>]*>', content)
    if body_match:
        # Get the navigation HTML
        nav_html = create_nav_html(is_subdirectory)
        
        # Insert after the body tag
        insertion_point = body_match.end()
        content = content[:insertion_point] + nav_html + content[insertion_point:]
        
        # Now check for a footer and add if missing
        if '<footer' not in content:
            # Find closing body tag
            body_close_match = re.search(r'</body>', content)
            if body_close_match:
                # Get the footer HTML
                footer_html = create_footer_html(is_subdirectory)
                
                # Insert before the closing body tag
                insertion_point = body_close_match.start()
                content = content[:insertion_point] + footer_html + content[insertion_point:]
        
        # Write the updated content back
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
            
        print(f"Added navigation to {file_path}")
    else:
        print(f"No body tag found in {file_path}")

def main():
    # Process root directory files
    for file_path in Path('.').glob('*.html'):
        add_navigation(file_path)
    
    # Process about directory
    about_dir = Path('./about')
    if about_dir.exists():
        for file_path in about_dir.glob('*.html'):
            add_navigation(file_path, is_subdirectory=True)
    
    # Process how-it-works directory
    how_dir = Path('./how-it-works')
    if how_dir.exists():
        for file_path in how_dir.glob('*.html'):
            add_navigation(file_path, is_subdirectory=True)
    
    print("Navigation update completed")

if __name__ == "__main__":
    main() 