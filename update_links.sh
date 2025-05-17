#!/bin/bash

# Function to update links in HTML files
update_links() {
  local pattern="$1"
  local replacement="$2"
  find . -name "*.html" -type f -exec sed -i '' "s|$pattern|$replacement|g" {} \;
}

# Update login and signup links
update_links '<a href="#" class="btn btn-secondary">Log In</a>' '<a href="./login.html" class="btn btn-secondary">Log In</a>'
update_links '<a href="#" class="btn">Sign Up</a>' '<a href="./signup.html" class="btn">Sign Up</a>'

# Update main navigation
update_links '<a href="#how-it-works" class="nav-link">How It Works</a>' '<a href="./how-it-works/index.html" class="nav-link">How It Works</a>'
update_links '<a href="#benefits" class="nav-link">Benefits</a>' '<a href="./index.html#benefits" class="nav-link">Benefits</a>'
update_links '<a href="#features" class="nav-link">Features</a>' '<a href="./index.html#features" class="nav-link">Features</a>'
update_links '<a href="#about" class="nav-link">About</a>' '<a href="./about/about-us.html" class="nav-link">About</a>'

# Update footer links
update_links '<li class="footer-link"><a href="#">Find a Home</a></li>' '<li class="footer-link"><a href="./browse-listings.html">Find a Home</a></li>'
update_links '<li class="footer-link"><a href="#">List Your Space</a></li>' '<li class="footer-link"><a href="./create-listing.html">List Your Space</a></li>'
update_links '<li class="footer-link"><a href="#">How It Works</a></li>' '<li class="footer-link"><a href="./how-it-works/index.html">How It Works</a></li>'
update_links '<li class="footer-link"><a href="#">Community</a></li>' '<li class="footer-link"><a href="./dashboard.html">Community</a></li>'

# Update footer company section
update_links '<li class="footer-link"><a href="#">About Us</a></li>' '<li class="footer-link"><a href="./about/about-us.html">About Us</a></li>'
update_links '<li class="footer-link"><a href="#">Careers</a></li>' '<li class="footer-link"><a href="./about/team.html#careers">Careers</a></li>'
update_links '<li class="footer-link"><a href="#">Press</a></li>' '<li class="footer-link"><a href="./about/press.html">Press</a></li>'
update_links '<li class="footer-link"><a href="#">Contact</a></li>' '<li class="footer-link"><a href="./contact-support.html">Contact</a></li>'

# Update footer support section
update_links '<li class="footer-link"><a href="#">Help Center</a></li>' '<li class="footer-link"><a href="./help-center.html">Help Center</a></li>'
update_links '<li class="footer-link"><a href="#">Safety Center</a></li>' '<li class="footer-link"><a href="./safety-center.html">Safety Center</a></li>'
update_links '<li class="footer-link"><a href="#">Resources</a></li>' '<li class="footer-link"><a href="./help-center.html#resources">Resources</a></li>'
update_links '<li class="footer-link"><a href="#">FAQ</a></li>' '<li class="footer-link"><a href="./faq.html">FAQ</a></li>'

# Update CTA buttons
update_links '<a href="#" class="btn btn-large">Find a Home</a>' '<a href="./browse-listings.html" class="btn btn-large">Find a Home</a>'
update_links '<a href="#" class="btn btn-secondary btn-large">List Your Space</a>' '<a href="./create-listing.html" class="btn btn-secondary btn-large">List Your Space</a>'
update_links '<a href="#" class="btn btn-large cta-button">Get Started</a>' '<a href="./signup.html" class="btn btn-large cta-button">Get Started</a>'
update_links '<a href="#" class="btn btn-large cta-button">Get Started Today</a>' '<a href="./signup.html" class="btn btn-large cta-button">Get Started Today</a>'

# Fix paths in about directory
find ./about -name "*.html" -type f -exec sed -i '' 's|href="./login|href="../login|g' {} \;
find ./about -name "*.html" -type f -exec sed -i '' 's|href="./signup|href="../signup|g' {} \;
find ./about -name "*.html" -type f -exec sed -i '' 's|href="./how-it-works|href="../how-it-works|g' {} \;
find ./about -name "*.html" -type f -exec sed -i '' 's|href="./index.html|href="../index.html|g' {} \;
find ./about -name "*.html" -type f -exec sed -i '' 's|href="./browse-listings|href="../browse-listings|g' {} \;
find ./about -name "*.html" -type f -exec sed -i '' 's|href="./create-listing|href="../create-listing|g' {} \;
find ./about -name "*.html" -type f -exec sed -i '' 's|href="./dashboard|href="../dashboard|g' {} \;
find ./about -name "*.html" -type f -exec sed -i '' 's|href="./help-center|href="../help-center|g' {} \;
find ./about -name "*.html" -type f -exec sed -i '' 's|href="./safety-center|href="../safety-center|g' {} \;
find ./about -name "*.html" -type f -exec sed -i '' 's|href="./faq|href="../faq|g' {} \;
find ./about -name "*.html" -type f -exec sed -i '' 's|href="./contact-support|href="../contact-support|g' {} \;

# Fix paths in how-it-works directory
find ./how-it-works -name "*.html" -type f -exec sed -i '' 's|href="./login|href="../login|g' {} \;
find ./how-it-works -name "*.html" -type f -exec sed -i '' 's|href="./signup|href="../signup|g' {} \;
find ./how-it-works -name "*.html" -type f -exec sed -i '' 's|href="./about|href="../about|g' {} \;
find ./how-it-works -name "*.html" -type f -exec sed -i '' 's|href="./index.html|href="../index.html|g' {} \;
find ./how-it-works -name "*.html" -type f -exec sed -i '' 's|href="./browse-listings|href="../browse-listings|g' {} \;
find ./how-it-works -name "*.html" -type f -exec sed -i '' 's|href="./create-listing|href="../create-listing|g' {} \;
find ./how-it-works -name "*.html" -type f -exec sed -i '' 's|href="./dashboard|href="../dashboard|g' {} \;
find ./how-it-works -name "*.html" -type f -exec sed -i '' 's|href="./help-center|href="../help-center|g' {} \;
find ./how-it-works -name "*.html" -type f -exec sed -i '' 's|href="./safety-center|href="../safety-center|g' {} \;
find ./how-it-works -name "*.html" -type f -exec sed -i '' 's|href="./faq|href="../faq|g' {} \;
find ./how-it-works -name "*.html" -type f -exec sed -i '' 's|href="./contact-support|href="../contact-support|g' {} \;

echo "Link updates completed." 