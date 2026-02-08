# Content Update Guide

This guide explains how to update content on the Konst och Ansvar website.

## Quick Start

All text content is stored in Markdown (`.md`) files. You don't need to know code to update content - just edit the text in these files!

## Finding Content Files

- **Homepage**: `index.md`
- **Other pages**: `pages/[page-name].md`
- **Navigation menu**: `_data/navigation.yml`
- **Site information**: `_data/site.yml`

## Updating Page Content

1. Open the Markdown file for the page you want to edit
2. The content starts after the `---` section at the top
3. Edit the text as needed
4. Save the file
5. The changes will appear after the site rebuilds

### Example: Updating the About Page

1. Open `pages/om-oss.md`
2. Find the text you want to change
3. Edit it
4. Save

## Adding New Pages

1. Create a new file in the `pages/` directory (e.g., `pages/ny-sida.md`)
2. Add this structure at the top:

```markdown
---
title: "Page Title"
description: "Page description"
layout: "page"
permalink: "/page-url/"
---
```

3. Write your content below in Markdown
4. Optionally add it to the navigation in `_data/navigation.yml`

## Markdown Basics

- **Headings**: Use `#` for main heading, `##` for subheading, etc.
- **Bold**: `**text**` becomes **text**
- **Italic**: `*text*` becomes *text*
- **Links**: `[link text](url)` creates a link
- **Images**: `![alt text](image-url)` inserts an image
- **Lists**: Use `-` for bullet points

## Updating Navigation

Edit `_data/navigation.yml`:

```yaml
main:
  - title: "Page Name"
    url: "/page-url/"
```

## Updating Contact Information

Edit `_data/site.yml` to update:
- Email address
- Phone number
- Address
- Social media links

## Adding Images

See `IMAGE_GUIDE.md` for detailed instructions on adding and managing images.

## Need Help?

Refer to:
- `PAGE_CREATION.md` - Detailed page creation guide
- `IMAGE_GUIDE.md` - Image management guide
- `SPEC.md` - Full specification document

