# Quick Start Guide

Get your Konst och Ansvar website up and running quickly!

## Prerequisites

- Ruby 2.7+ installed
- Bundler gem installed (`gem install bundler`)

## Setup (5 minutes)

1. **Install dependencies:**
   ```bash
   bundle install
   ```

2. **Run local server:**
   ```bash
   bundle exec jekyll serve
   ```

3. **View your site:**
   Open http://localhost:4000 in your browser

## Next Steps

### 1. Extract Content from konstochansvar.se

The website structure is ready, but you need to populate it with actual content:

1. Visit https://konstochansvar.se
2. Copy text content to the corresponding Markdown files:
   - Homepage → `index.md`
   - About → `pages/om-oss.md`
   - Services → `pages/tjanster.md`
   - Portfolio → `pages/portfolio.md`
   - Contact → `pages/kontakt.md`
3. Download images and place in `assets/images/` subdirectories
4. Update `_data/site.yml` with actual contact information
5. Update `_data/navigation.yml` if navigation differs

See `extract_website_content.md` for detailed extraction guide.

### 2. Customize Styling

Update colors and fonts in `assets/css/main.css`:

```css
:root {
  --primary-color: #your-color;
  --secondary-color: #your-color;
  /* ... */
}
```

### 3. Add Your Logo

Place your logo in `assets/images/icons/logo.svg` (or `.png`)

### 4. Deploy to GitHub Pages

1. Create a GitHub repository
2. Push your code:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/repo.git
   git push -u origin main
   ```
3. Enable GitHub Pages in repository Settings → Pages
4. Select `main` branch as source

Your site will be live at: `https://yourusername.github.io/repository-name/`

## File Structure Overview

```
.
├── _config.yml          # Site configuration
├── _data/               # Site data (navigation, settings)
├── _includes/           # Reusable components
├── _layouts/            # Page templates
├── assets/              # CSS, JS, images
├── pages/               # Content pages (Markdown)
├── index.md            # Homepage
└── README.md           # Full documentation
```

## Common Tasks

### Update Text Content
Edit the `.md` files in `pages/` directory

### Add a New Page
1. Create `pages/new-page.md`
2. Add front matter (see `PAGE_CREATION.md`)
3. Write content in Markdown
4. Optionally add to navigation in `_data/navigation.yml`

### Add Images
1. Place in `assets/images/[subdirectory]/`
2. Reference: `![alt](/assets/images/content/image.jpg)`

## Need Help?

- **Content updates**: See `CONTENT_GUIDE.md`
- **Creating pages**: See `PAGE_CREATION.md`
- **Managing images**: See `IMAGE_GUIDE.md`
- **Deployment**: See `DEPLOYMENT.md`
- **Full specs**: See `SPEC.md`

## Troubleshooting

**Build errors?**
- Run `bundle exec jekyll build` to see errors
- Check `_config.yml` syntax
- Ensure all required files exist

**Images not showing?**
- Check file paths (case-sensitive)
- Verify images are in correct directories
- Ensure paths start with `/assets/images/`

**Site not updating?**
- Clear browser cache
- Restart Jekyll server
- Check for build errors

---

**Ready to go!** Start by extracting content from konstochansvar.se and customizing the site to match.

