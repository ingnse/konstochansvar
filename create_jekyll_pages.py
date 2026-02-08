#!/usr/bin/env python3
"""
Script to convert extracted HTML pages to Jekyll Markdown pages
"""

import re
import os
from pathlib import Path

# Page titles mapping
PAGE_TITLES = {
    "pressrum": "Pressrum",
    "organigram": "Organigram",
    "vanligafragor": "Vanliga frågor",
    "kontakt": "Kontakt",
    "roundaboutart": "IKA Roundabout Art",
    "ebf": "IKA Evidensbaserad fördom",
    "kidsclub": "IKA Kids Club",
    "statskyrkomuseum": "IKA Statskyrkomuseum",
    "jagarlikgiltig": "IKA Jag är likgiltig",
    "engagemang": "Visa engagemang",
    "lblistan": "Sveriges landskapsbrott - Hela listan"
}

def extract_main_content(html_content):
    """Extract content from #mainContent div"""
    # Find the mainContent div - handle different closing patterns
    patterns = [
        r'<div id="mainContent">(.*?)<!-- end #mainContent --></div>',
        r'<div id="mainContent">(.*?)<!-- This clearing element',
        r'<div id="mainContent">(.*?)<br class="clearfloat"',
    ]
    
    content = None
    for pattern in patterns:
        match = re.search(pattern, html_content, re.DOTALL)
        if match:
            content = match.group(1)
            break
    
    if not content:
        return None
    
    # Remove empty h3 tags and excessive whitespace
    content = re.sub(r'<h3>&nbsp;</h3>', '', content)
    content = re.sub(r'<p>&nbsp;</p>', '', content)
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    
    # Update image paths
    content = re.sub(r'src="Bilder/([^"]+)"', r'src="/assets/images/content/\1"', content)
    content = re.sub(r'src="Bilder/([^"]+)"', r'src="/assets/images/content/\1"', content)
    
    # Update links - remove .html extension and update paths
    # Fix internal page links
    internal_pages = ['pressrum', 'organigram', 'vanligafragor', 'kontakt', 'roundaboutart', 
                     'ebf', 'kidsclub', 'laromedel', 'statskyrkomuseum', 'jagarlikgiltig', 
                     'engagemang', 'lblistan']
    
    for page in internal_pages:
        # Match href="page.html" or href="page.html#anchor"
        content = re.sub(rf'href="{re.escape(page)}\.html(#[^"]*)?"', rf'href="/{page}/\1"', content)
        content = re.sub(rf'href="{re.escape(page)}\.html"', rf'href="/{page}/"', content)
    
    # Fix index/home links
    content = re.sub(r'href="index\.html"', 'href="/"', content)
    content = re.sub(r'href="http://www\.konstochansvar\.se"', 'href="/"', content)
    content = re.sub(r'href="http://www\.konstochansvar\.se/"', 'href="/"', content)
    
    # Fix email links
    content = re.sub(r'href="mailto:([^"]+)"', r'href="mailto:\1"', content)
    
    return content.strip()

def create_jekyll_page(page_name, content):
    """Create Jekyll Markdown page"""
    title = PAGE_TITLES.get(page_name, page_name.capitalize())
    permalink = f"/{page_name}/"
    
    front_matter = f"""---
title: "{title}"
description: "{title}"
layout: "page"
permalink: "{permalink}"
---

"""
    
    return front_matter + content

def process_page(page_file):
    """Process a single HTML page file"""
    page_name = Path(page_file).stem
    
    with open(page_file, 'r', encoding='utf-8', errors='ignore') as f:
        html_content = f.read()
    
    content = extract_main_content(html_content)
    if not content:
        print(f"Warning: Could not extract content from {page_file}")
        return None
    
    jekyll_content = create_jekyll_page(page_name, content)
    
    output_file = f"pages/{page_name}.md"
    os.makedirs("pages", exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(jekyll_content)
    
    print(f"Created: {output_file}")
    return output_file

def main():
    """Process all extracted pages"""
    extracted_dir = Path("extracted_pages")
    
    if not extracted_dir.exists():
        print("Error: extracted_pages directory not found")
        return
    
    pages = list(extracted_dir.glob("*.html"))
    
    if not pages:
        print("No HTML files found in extracted_pages")
        return
    
    print(f"Processing {len(pages)} pages...\n")
    
    for page_file in sorted(pages):
        try:
            process_page(page_file)
        except Exception as e:
            print(f"Error processing {page_file}: {e}")
    
    print(f"\nDone! Created {len(pages)} Jekyll pages in pages/ directory")

if __name__ == "__main__":
    main()

