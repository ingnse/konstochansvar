# Static Website Requirement Specification

## 1. Project Overview

### 1.1 Purpose
Create a static website that replicates the layout and content from https://konstochansvar.se, designed for deployment on GitHub Pages. The website must prioritize content management simplicity, maintainability, and ease of extension.

### 1.2 Core Objectives
- **Static Site Generation**: Generate a fully static website deployable on GitHub Pages
- **Content Separation**: All text content must be stored separately from code/templates for easy updates
- **Extensibility**: Simple process for adding new sub-pages
- **Media Management**: Straightforward system for adding and managing images
- **LLM-Friendly**: Architecture and documentation must enable LLM-assisted development and maintenance

## 2. Technology Stack

### 2.1 Recommended Stack
- **Static Site Generator**: Jekyll (native GitHub Pages support) or 11ty/Eleventy (modern, flexible)
- **Template Engine**: Liquid (Jekyll) or Nunjucks (11ty)
- **Content Format**: Markdown (.md) with YAML front matter
- **Styling**: CSS (with optional framework: Tailwind CSS or custom CSS)
- **JavaScript**: Vanilla JS or minimal framework (if needed)
- **Version Control**: Git
- **Deployment**: GitHub Pages

### 2.2 Rationale
- **Jekyll**: Zero-configuration GitHub Pages integration, extensive documentation
- **11ty**: Modern alternative with more flexibility, requires GitHub Actions for deployment
- **Markdown**: Human-readable, easy to edit, LLM-friendly
- **YAML Front Matter**: Structured metadata without complexity

## 3. Content Management Architecture

### 3.1 Text Content Separation

#### 3.1.1 Content Storage Structure
```
content/
├── pages/
│   ├── index.md (homepage)
│   ├── about.md
│   ├── services/
│   │   ├── service-1.md
│   │   └── service-2.md
│   └── contact.md
├── data/
│   ├── navigation.yml (menu structure)
│   ├── site.yml (site-wide settings)
│   ├── footer.yml (footer content)
│   └── metadata.yml (SEO, social media)
└── snippets/
    ├── hero-section.md
    ├── testimonials.md
    └── features.md
```

#### 3.1.2 Content File Format
Each content file must follow this structure:

```markdown
---
title: "Page Title"
description: "Meta description for SEO"
layout: "default" | "page" | "post"
permalink: "/custom-url/" (optional)
date: "2024-01-01" (optional)
image: "/assets/images/page-hero.jpg" (optional)
---

# Page Heading

Main content in Markdown format...

## Section Heading

More content...
```

#### 3.1.3 Data Files Format
**Example: `_data/navigation.yml`**
```yaml
main:
  - title: "Hem"
    url: "/"
  - title: "Om oss"
    url: "/om-oss/"
  - title: "Tjänster"
    url: "/tjanster/"
    children:
      - title: "Tjänst 1"
        url: "/tjanster/tjanst-1/"
      - title: "Tjänst 2"
        url: "/tjanster/tjanst-2/"
  - title: "Kontakt"
    url: "/kontakt/"
```

**Example: `_data/site.yml`**
```yaml
name: "Konst och Ansvar"
tagline: "Your tagline here"
author: "Site Author"
email: "contact@example.com"
phone: "+46 XX XXX XX XX"
address: "Street Address, City"
social:
  facebook: "https://facebook.com/..."
  instagram: "https://instagram.com/..."
  linkedin: "https://linkedin.com/..."
```

### 3.2 Content Update Workflow
1. Edit Markdown files in `content/pages/` or `content/snippets/`
2. Update data files in `content/data/` for structured content
3. Changes automatically reflected after site rebuild
4. No code knowledge required for content updates

## 4. Page and Sub-Page Architecture

### 4.1 Page Organization

#### 4.1.1 Directory Structure
```
pages/
├── index.md (homepage)
├── om-oss.md
├── tjanster/
│   ├── index.md (services listing page)
│   ├── tjanst-1.md
│   ├── tjanst-2.md
│   └── tjanst-3.md
├── portfolio/
│   ├── index.md
│   ├── projekt-1.md
│   └── projekt-2.md
└── kontakt.md
```

#### 4.1.2 Adding New Pages
**Process for adding a new page:**
1. Create a new `.md` file in the appropriate directory
2. Add YAML front matter with required metadata
3. Write content in Markdown
4. Optionally add to navigation in `_data/navigation.yml`
5. Page automatically appears in site structure

**Process for adding a new sub-section:**
1. Create a new directory (e.g., `pages/ny-sektion/`)
2. Add `index.md` for the section landing page
3. Add individual pages as `.md` files in the directory
4. Update navigation.yml to include the new section

#### 4.1.3 URL Structure
- Pages follow directory structure: `/pages/about.md` → `/about/`
- Custom URLs via `permalink` in front matter
- Clean URLs (no `.html` extension)
- Automatic sitemap generation

### 4.2 Layout System

#### 4.2.1 Layout Hierarchy
```
_layouts/
├── default.html (base layout)
├── page.html (standard page layout)
├── home.html (homepage layout)
└── post.html (blog/article layout, if needed)
```

#### 4.2.2 Layout Components
```
_includes/
├── header.html
├── navigation.html
├── footer.html
├── hero.html
├── section.html
└── image-gallery.html
```

## 5. Image Management

### 5.1 Image Storage Structure
```
assets/
└── images/
    ├── hero/ (hero/banner images)
    │   ├── home-hero.jpg
    │   └── about-hero.jpg
    ├── content/ (inline content images)
    │   ├── service-1-image.jpg
    │   └── service-2-image.jpg
    ├── gallery/ (gallery/portfolio images)
    │   ├── project-1/
    │   │   ├── image-1.jpg
    │   │   └── image-2.jpg
    │   └── project-2/
    ├── team/ (team member photos)
    └── icons/ (icons, logos)
        ├── logo.svg
        └── favicon.ico
```

### 5.2 Image Usage in Content

#### 5.2.1 Markdown Image Syntax
```markdown
![Alt text description](/assets/images/content/image-name.jpg)
```

#### 5.2.2 Image with Caption (via include)
```markdown
{% include image.html 
   src="/assets/images/content/image.jpg" 
   alt="Description" 
   caption="Optional caption text" %}
```

#### 5.2.3 Responsive Images
```markdown
{% include responsive-image.html 
   src="/assets/images/content/image.jpg" 
   alt="Description" 
   sizes="(max-width: 768px) 100vw, 50vw" %}
```

### 5.3 Image Best Practices
- **Naming Convention**: Use kebab-case, descriptive names (e.g., `service-consultation-hero.jpg`)
- **Optimization**: Images should be optimized before upload (compressed, appropriate format)
- **Formats**: Use WebP for photos, SVG for icons/logos, JPG for photos if WebP not available
- **Alt Text**: Always include descriptive alt text for accessibility
- **Sizing**: Store original high-res versions; use responsive image techniques for display

### 5.4 Adding New Images
1. Place image file in appropriate `assets/images/` subdirectory
2. Reference in Markdown using relative path: `/assets/images/[subdir]/filename.ext`
3. Include alt text for accessibility
4. Optionally use image includes for advanced features (captions, lazy loading)

## 6. File Structure

### 6.1 Complete Directory Structure
```
.
├── _config.yml (site configuration)
├── _data/ (data files)
│   ├── navigation.yml
│   ├── site.yml
│   └── metadata.yml
├── _includes/ (reusable components)
│   ├── header.html
│   ├── navigation.html
│   ├── footer.html
│   └── image.html
├── _layouts/ (page templates)
│   ├── default.html
│   ├── page.html
│   └── home.html
├── _sass/ (Sass partials, if using Sass)
│   └── main.scss
├── assets/
│   ├── css/
│   │   └── main.css
│   ├── js/
│   │   └── main.js
│   └── images/
│       ├── hero/
│       ├── content/
│       ├── gallery/
│       └── icons/
├── pages/ (content pages)
│   ├── index.md
│   ├── om-oss.md
│   ├── tjanster/
│   └── kontakt.md
├── .gitignore
├── README.md
├── LICENSE (optional)
└── package.json (if using build tools)
```

### 6.2 Configuration File (`_config.yml`)
```yaml
# Site Settings
title: "Konst och Ansvar"
description: "Site description"
url: "https://username.github.io" # or custom domain
baseurl: "/repository-name" # if not root

# Build Settings
markdown: kramdown
highlighter: rouge
plugins:
  - jekyll-feed
  - jekyll-sitemap

# Collections (if needed)
collections:
  services:
    output: true
  portfolio:
    output: true

# Defaults
defaults:
  - scope:
      path: ""
      type: "pages"
    values:
      layout: "page"
      author: "Site Author"
```

## 7. Best Practices Implementation

### 7.1 Code Organization
- **Separation of Concerns**: Content, presentation, and logic clearly separated
- **DRY Principle**: Reusable includes and layouts
- **Modularity**: Components can be modified independently
- **Consistency**: Uniform naming conventions and file structure

### 7.2 Accessibility (WCAG 2.1 AA Compliance)
- Semantic HTML5 elements
- ARIA labels where appropriate
- Keyboard navigation support
- Color contrast ratios meet standards
- Alt text for all images
- Form labels and error messages

### 7.3 SEO Optimization
- Semantic HTML structure
- Meta tags in front matter (title, description, keywords)
- Open Graph tags for social sharing
- Structured data (JSON-LD) where applicable
- Clean URL structure
- XML sitemap generation
- robots.txt configuration

### 7.4 Performance
- Optimized images (compression, appropriate formats)
- Minified CSS and JavaScript
- Lazy loading for images
- Efficient asset loading
- Minimal external dependencies

### 7.5 Responsive Design
- Mobile-first approach
- Flexible grid system
- Responsive images
- Touch-friendly navigation
- Viewport meta tag configuration

### 7.6 Browser Compatibility
- Support for modern browsers (last 2 versions)
- Graceful degradation for older browsers
- Progressive enhancement approach

## 8. Development Workflow

### 8.1 Local Development
1. Install dependencies (Jekyll or 11ty)
2. Run local server: `bundle exec jekyll serve` or `npx @11ty/eleventy --serve`
3. Edit content files or templates
4. Preview changes in browser
5. Commit changes to Git

### 8.2 Content Update Process
1. **Text Updates**: Edit `.md` files in `pages/` directory
2. **Navigation Changes**: Edit `_data/navigation.yml`
3. **Site Settings**: Edit `_data/site.yml` or `_config.yml`
4. **New Pages**: Create new `.md` file with front matter
5. **Images**: Add to `assets/images/` and reference in content

### 8.3 Version Control
- All content files tracked in Git
- Clear commit messages
- Branch strategy (main for production, develop for work-in-progress)
- `.gitignore` excludes build artifacts and OS files

## 9. GitHub Pages Deployment

### 9.1 Repository Setup
- Repository name: `konstochansvar_hemsida` (or desired name)
- Public repository (required for free GitHub Pages)
- Main branch as source branch

### 9.2 Deployment Configuration
- **Jekyll**: Automatic build on push to main branch
- **11ty**: Requires GitHub Actions workflow for build
- Custom domain support (optional)
- HTTPS enabled by default

### 9.3 GitHub Actions Workflow (if using 11ty)
```yaml
name: Build and Deploy
on:
  push:
    branches: [ main ]
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Setup Node
        uses: actions/setup-node@v2
        with:
          node-version: '18'
      - run: npm install
      - run: npm run build
      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./_site
```

## 10. LLM-Friendly Documentation

### 10.1 Code Comments
- Clear comments explaining template logic
- Front matter field documentation
- Include parameter documentation
- Complex logic explanations

### 10.2 README.md Requirements
The README must include:
- Project overview and purpose
- Technology stack
- Installation instructions
- Directory structure explanation
- Content update guide
- Image addition guide
- Page creation guide
- Deployment instructions
- Development workflow

### 10.3 Documentation Files
- `CONTENT_GUIDE.md`: How to update content
- `PAGE_CREATION.md`: Step-by-step page creation
- `IMAGE_GUIDE.md`: Image management procedures
- `DEPLOYMENT.md`: Deployment process

### 10.4 Schema Documentation
- YAML front matter schema for all page types
- Data file structure documentation
- Include parameter specifications
- Layout variable documentation

## 11. Content Migration from konstochansvar.se

### 11.1 Content Extraction
- Extract all text content from existing site
- Identify page structure and hierarchy
- Document navigation structure
- List all images and their usage context

### 11.2 Layout Analysis
- Document color scheme and typography
- Identify layout components (header, footer, sections)
- Note responsive breakpoints
- Document interactive elements

### 11.3 Migration Process
1. Set up new site structure
2. Create base layouts matching original design
3. Migrate content to Markdown files
4. Add images to assets directory
5. Configure navigation and site data
6. Test responsive behavior
7. Deploy to GitHub Pages

## 12. Quality Assurance

### 12.1 Pre-Deployment Checklist
- [ ] All pages render correctly
- [ ] Navigation works on all pages
- [ ] Images load and display properly
- [ ] Responsive design tested on multiple devices
- [ ] Links are valid (internal and external)
- [ ] Forms function correctly (if applicable)
- [ ] SEO meta tags present on all pages
- [ ] Accessibility audit passed
- [ ] Performance metrics acceptable
- [ ] Cross-browser testing completed

### 12.2 Testing Requirements
- Manual testing on desktop and mobile
- Automated link checking
- Accessibility testing (WAVE, axe DevTools)
- Performance testing (Lighthouse)
- SEO validation

## 13. Maintenance and Updates

### 13.1 Regular Maintenance Tasks
- Update dependencies periodically
- Review and optimize images
- Update content as needed
- Monitor site performance
- Review and update SEO

### 13.2 Update Procedures
- Content updates: Edit Markdown files
- Design updates: Modify CSS and layouts
- Feature additions: Extend includes and layouts
- All changes tracked in Git with descriptive commits

## 14. Success Criteria

### 14.1 Functional Requirements
✅ Static website successfully deployed on GitHub Pages  
✅ All content from original site migrated  
✅ Text content easily editable via Markdown files  
✅ New pages can be added by creating a single Markdown file  
✅ Images can be added by placing files in assets directory  
✅ Site maintains original design and layout  

### 14.2 Non-Functional Requirements
✅ Site loads in under 3 seconds  
✅ Mobile-responsive design  
✅ WCAG 2.1 AA accessibility compliance  
✅ SEO optimized  
✅ Cross-browser compatible  
✅ Zero build errors or warnings  

### 14.3 LLM Development Support
✅ Clear file structure enables LLM navigation  
✅ Comprehensive documentation supports LLM understanding  
✅ Consistent patterns enable LLM code generation  
✅ Schema documentation enables LLM content creation  

---

## Appendix A: Example Content Files

### A.1 Homepage Example (`pages/index.md`)
```markdown
---
title: "Välkommen till Konst och Ansvar"
description: "Vi erbjuder konstnärliga lösningar med ansvar"
layout: "home"
image: "/assets/images/hero/home-hero.jpg"
---

# Välkommen

Välkommen till vår hemsida...

## Våra tjänster

Vi erbjuder...
```

### A.2 Service Page Example (`pages/tjanster/tjanst-1.md`)
```markdown
---
title: "Tjänst 1"
description: "Beskrivning av tjänst 1"
layout: "page"
permalink: "/tjanster/tjanst-1/"
image: "/assets/images/content/service-1-hero.jpg"
---

# Tjänst 1

Detaljerad beskrivning av tjänsten...

![Service image](/assets/images/content/service-1-image.jpg)
```

## Appendix B: Technology-Specific Notes

### B.1 Jekyll-Specific
- Uses Liquid templating
- Automatic sitemap and feed generation
- Built-in pagination support
- Plugin ecosystem available

### B.2 11ty-Specific
- Uses Nunjucks templating (more powerful)
- Requires build step (GitHub Actions)
- More flexible data processing
- Better performance

---

**Document Version**: 1.0  
**Last Updated**: 2024  
**Status**: Draft for Review

