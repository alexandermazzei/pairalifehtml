#!/bin/bash

# Check if login link was updated in the main index
grep -n "login.html" index.html

# Check if links were updated in about directory
grep -n "../login.html" about/about-us.html

# Check if links were updated in how-it-works directory
grep -n "../login.html" how-it-works/index.html

echo "Link check completed." 