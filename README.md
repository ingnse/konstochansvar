# Konst och Ansvar - Static Website

A static website for Konst och Ansvar, built with Jekyll and ready for deployment on GitHub Pages.

## Project Overview

This is a static website that replicates the layout and content from [konstochansvar.se](https://konstochansvar.se). The site is built using Jekyll, a static site generator that works seamlessly with GitHub Pages.

## Features

- ✅ **Content Separation**: All text content is stored in Markdown files for easy updates
- ✅ **Easy Page Management**: Add new pages by creating a single Markdown file
- ✅ **Image Management**: Organized image structure in `assets/images/`
- ✅ **Responsive Design**: Mobile-first, fully responsive layout
- ✅ **SEO Optimized**: Meta tags, Open Graph, and structured data
- ✅ **Accessibility**: WCAG 2.1 AA compliant structure

## Technology Stack

- **Static Site Generator**: Jekyll 4.3
- **Template Engine**: Liquid
- **Content Format**: Markdown with YAML front matter
- **Styling**: Custom CSS
- **JavaScript**: Vanilla JS
- **Deployment**: GitHub Pages

## Directory Structure

```
.
├── _config.yml          # Jekyll configuration
├── _data/               # Data files (navigation, site settings)
├── _includes/           # Reusable components
├── _layouts/            # Page templates
├── assets/
│   ├── css/            # Stylesheets
│   ├── js/             # JavaScript files
│   └── images/         # Image assets
├── pages/               # Content pages (Markdown)
├── index.md            # Homepage
└── README.md           # This file
```

## Getting Started

### Prerequisites

- Ruby (version 2.7 or higher)
- Bundler gem

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/konstochansvar_hemsida.git
cd konstochansvar_hemsida
```

2. Install dependencies:
```bash
bundle install
```

3. Run the local development server:
```bash
bundle exec jekyll serve
```

4. Open your browser and navigate to `http://localhost:4000`

## Content Management

### Adding a New Page

1. Create a new `.md` file in the `pages/` directory
2. Add YAML front matter:
```markdown
---
title: "Page Title"
description: "Page description for SEO"
layout: "page"
permalink: "/page-url/"
---
```

3. Write your content in Markdown below the front matter
4. Optionally add the page to `_data/navigation.yml`

### Updating Text Content

Simply edit the Markdown files in the `pages/` directory. No code knowledge required!

### Adding Images

1. Place images in the appropriate `assets/images/` subdirectory:
   - `hero/` - Hero/banner images
   - `content/` - Inline content images
   - `gallery/` - Gallery/portfolio images
   - `icons/` - Icons and logos

2. Reference in Markdown:
```markdown
![Alt text](/assets/images/content/image-name.jpg)
```

3. Or use the image include for advanced features:
```markdown
{% include image.html 
   src="/assets/images/content/image.jpg" 
   alt="Description" 
   caption="Optional caption" %}
```

## Configuration

### Site Settings

Edit `_config.yml` to update:
- Site title and description
- URL and baseurl
- Build settings
- Default values

### Navigation

Edit `_data/navigation.yml` to update the main navigation menu.

### Site Information

Edit `_data/site.yml` to update:
- Company name and tagline
- Contact information
- Social media links

## Deployment to GitHub Pages

### Automatic Deployment (Recommended)

1. Push your code to a GitHub repository
2. Go to repository Settings → Pages
3. Select the source branch (usually `main`)
4. GitHub will automatically build and deploy your site

### Manual Deployment

1. Build the site:
```bash
bundle exec jekyll build
```

2. The `_site` directory contains the static files
3. Deploy the contents of `_site` to your web server

## Development Workflow

1. Make changes to content files or templates
2. Preview locally with `bundle exec jekyll serve`
3. Test your changes
4. Commit and push to GitHub
5. GitHub Pages will automatically rebuild and deploy

## Customization

### Styling

Edit `assets/css/main.css` to customize the appearance. The CSS uses CSS variables for easy theming.

### Layouts

Modify files in `_layouts/` to change page structure:
- `default.html` - Base layout
- `page.html` - Standard page layout
- `home.html` - Homepage layout

### Components

Edit files in `_includes/` to modify reusable components:
- `header.html` - Site header
- `navigation.html` - Navigation menu
- `footer.html` - Site footer
- `image.html` - Image component

## Browser Support

- Chrome (last 2 versions)
- Firefox (last 2 versions)
- Safari (last 2 versions)
- Edge (last 2 versions)

## License

[Add your license here]

## Contact

For questions or support, please contact [your contact information].

---

**Note**: This website structure follows the requirements specified in `SPEC.md`. For detailed specifications, please refer to that document.

