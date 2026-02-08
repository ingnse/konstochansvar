# Image Management Guide

Complete guide for adding and managing images on the Konst och Ansvar website.

## Image Directory Structure

Images are organized in `assets/images/` with the following structure:

```
assets/images/
├── hero/          # Hero/banner images for pages
├── content/       # Inline content images
├── gallery/       # Gallery/portfolio images
│   ├── projekt-1/
│   └── projekt-2/
├── team/          # Team member photos
└── icons/         # Icons, logos, favicon
```

## Adding Images

### Step 1: Place Image in Correct Directory

1. Choose the appropriate subdirectory based on image type
2. Use descriptive, kebab-case filenames (e.g., `service-consultation-hero.jpg`)
3. Place the image file in that directory

### Step 2: Reference in Content

#### Basic Markdown Syntax

```markdown
![Alt text description](/assets/images/content/image-name.jpg)
```

#### With Image Include (Advanced)

For images with captions or special features:

```markdown
{% include image.html 
   src="/assets/images/content/image.jpg" 
   alt="Description of image" 
   caption="Optional caption text" %}
```

## Image Best Practices

### Naming Convention

- Use kebab-case: `service-consultation-hero.jpg`
- Be descriptive: `team-member-john-doe.jpg` not `img1.jpg`
- Include context: `portfolio-project-2024.jpg`

### File Formats

- **Photos**: Use JPG or WebP (WebP preferred for smaller file sizes)
- **Icons/Logos**: Use SVG when possible
- **Graphics**: PNG for images with transparency

### Optimization

Before uploading:
- Compress images to reduce file size
- Use appropriate dimensions (don't upload 4000px images if you only need 800px)
- Consider using WebP format for better compression

### Alt Text

Always include descriptive alt text for accessibility:

```markdown
![A person working on a design project](/assets/images/content/design-work.jpg)
```

Bad example:
```markdown
![image](/assets/images/content/img1.jpg)
```

## Image Types and Usage

### Hero Images

Hero images are large banner images at the top of pages.

**Location**: `assets/images/hero/`

**Usage in front matter**:
```markdown
---
image: "/assets/images/hero/about-hero.jpg"
---
```

**Recommended size**: 1920x1080px or similar wide format

### Content Images

Images used within page content.

**Location**: `assets/images/content/`

**Usage**:
```markdown
![Description](/assets/images/content/example-image.jpg)
```

**Recommended size**: 800-1200px wide

### Gallery Images

Portfolio or project gallery images.

**Location**: `assets/images/gallery/[project-name]/`

**Usage**:
```markdown
![Project image 1](/assets/images/gallery/projekt-1/image-1.jpg)
![Project image 2](/assets/images/gallery/projekt-1/image-2.jpg)
```

### Team Photos

Team member profile photos.

**Location**: `assets/images/team/`

**Usage**:
```markdown
![Team member name](/assets/images/team/member-name.jpg)
```

**Recommended size**: 400x400px (square format)

### Icons and Logos

**Location**: `assets/images/icons/`

**Usage**: Usually referenced in templates, not content

## Responsive Images

Images automatically scale to fit their container. For best results:

- Use appropriate image sizes
- Let the browser handle scaling
- Consider using the image include for lazy loading

## Lazy Loading

Images are automatically lazy-loaded for better performance. The `loading="lazy"` attribute is added automatically by the image include.

## Troubleshooting

### Image Not Showing

1. Check the file path is correct (case-sensitive on some systems)
2. Verify the image file exists in the directory
3. Check the path starts with `/assets/images/`
4. Ensure the file extension matches (.jpg vs .jpeg)

### Image Too Large/Small

- Resize images before uploading
- Use CSS to control display size if needed
- Consider using different image sizes for different screen sizes

## Need Help?

- See `CONTENT_GUIDE.md` for general content editing
- See `PAGE_CREATION.md` for creating pages with images
- See `SPEC.md` for full specifications

