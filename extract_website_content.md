# Website Content Extraction Guide

This guide helps you extract the actual content from konstochansvar.se to populate the static website.

## Manual Extraction Steps

### 1. Visit the Website

Go to https://konstochansvar.se and navigate through all pages.

### 2. Extract Text Content

For each page:
1. Copy the main heading
2. Copy all paragraph text
3. Note the page structure (sections, subsections)
4. Save to the corresponding Markdown file in `pages/`

### 3. Extract Images

1. Right-click on images and "Save image as..."
2. Save to the appropriate `assets/images/` subdirectory:
   - Hero images → `assets/images/hero/`
   - Content images → `assets/images/content/`
   - Gallery images → `assets/images/gallery/[project-name]/`
3. Use descriptive filenames matching the content
4. Update image references in Markdown files

### 4. Update Navigation

Check the website's navigation menu and update `_data/navigation.yml` to match.

### 5. Update Site Information

Extract and update in `_data/site.yml`:
- Company name
- Contact email
- Phone number
- Address
- Social media links

### 6. Update Colors and Styling

1. Note the color scheme from the original site
2. Update CSS variables in `assets/css/main.css`:
   ```css
   :root {
     --primary-color: #your-color;
     --secondary-color: #your-color;
     --accent-color: #your-color;
   }
   ```

### 7. Update Typography

Note the fonts used and update in `assets/css/main.css`:
```css
--font-primary: "Font Name", fallback;
--font-heading: "Font Name", fallback;
```

## Automated Extraction (Optional)

You can use browser extensions or tools like:
- **SingleFile** browser extension to save complete pages
- **Web Scraper** browser extension
- **wget** or **curl** commands
- Browser Developer Tools to inspect and copy content

## Content Checklist

- [ ] Homepage content (`index.md`)
- [ ] About page (`pages/om-oss.md`)
- [ ] Services page (`pages/tjanster.md`)
- [ ] Portfolio page (`pages/portfolio.md`)
- [ ] Contact page (`pages/kontakt.md`)
- [ ] All hero images
- [ ] All content images
- [ ] Gallery/portfolio images
- [ ] Logo and favicon
- [ ] Navigation structure
- [ ] Contact information
- [ ] Social media links
- [ ] Color scheme
- [ ] Typography

## After Extraction

1. Test locally: `bundle exec jekyll serve`
2. Verify all pages render correctly
3. Check all images load
4. Test responsive design
5. Verify navigation works
6. Deploy to GitHub Pages

## Need Help?

- See `CONTENT_GUIDE.md` for content editing
- See `PAGE_CREATION.md` for page structure
- See `IMAGE_GUIDE.md` for image management

