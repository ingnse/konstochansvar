# Page Creation Guide

Step-by-step guide for creating new pages on the Konst och Ansvar website.

## Step 1: Create the Markdown File

Create a new file in the `pages/` directory with a descriptive name using kebab-case (lowercase with hyphens).

**Example**: `pages/ny-tjanst.md`

## Step 2: Add Front Matter

Every page needs YAML front matter at the top (between the `---` lines):

```markdown
---
title: "Page Title"
description: "Meta description for SEO"
layout: "page"
permalink: "/custom-url/"
image: "/assets/images/hero/page-hero.jpg" (optional)
---
```

### Front Matter Fields

- **title** (required): The page title shown in the browser tab and on the page
- **description** (required): Short description for SEO and social sharing
- **layout** (required): Usually `"page"` for regular pages, `"home"` for homepage
- **permalink** (optional): Custom URL. If omitted, URL is based on filename
- **image** (optional): Hero image for the page

## Step 3: Write Content

Write your content in Markdown below the front matter:

```markdown
---
title: "Ny Tjänst"
description: "Beskrivning av vår nya tjänst"
layout: "page"
permalink: "/ny-tjanst/"
---

# Ny Tjänst

Detta är vår nya tjänst...

## Funktioner

- Funktion 1
- Funktion 2
- Funktion 3

## Kontakta oss

[Kontakta oss](/kontakt/) för mer information.
```

## Step 4: Add to Navigation (Optional)

If you want the page in the main navigation, edit `_data/navigation.yml`:

```yaml
main:
  - title: "Ny Tjänst"
    url: "/ny-tjanst/"
```

## Step 5: Test Locally

1. Run `bundle exec jekyll serve`
2. Navigate to `http://localhost:4000/ny-tjanst/`
3. Verify the page looks correct

## Complete Example

**File**: `pages/om-foretaget.md`

```markdown
---
title: "Om Företaget"
description: "Lär dig mer om vårt företag och vår historia"
layout: "page"
permalink: "/om-foretaget/"
image: "/assets/images/hero/about-hero.jpg"
---

# Om Företaget

Välkommen till vårt företag!

## Vår historia

Vi grundades 2020 med visionen att...

## Vårt team

Vårt team består av...

## Kontakta oss

Vill du veta mer? [Kontakta oss](/kontakt/).
```

## Tips

- Use descriptive filenames that reflect the page content
- Keep permalinks short and meaningful
- Always include a description for SEO
- Use headings to structure your content
- Add images to make pages more engaging

## Common Layouts

- **page**: Standard page layout (most common)
- **home**: Homepage layout with hero section
- **default**: Base layout (usually not used directly)

## Need Help?

- See `CONTENT_GUIDE.md` for content editing basics
- See `IMAGE_GUIDE.md` for adding images
- See `SPEC.md` for full specifications

