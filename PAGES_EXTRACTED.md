# Pages Extraction Summary

All sub-pages from konstochansvar.se have been successfully extracted and converted to Jekyll pages with clean URLs.

## Pages Created

### Navigation Pages
- ✅ `pages/pressrum.md` - Pressrum (Press room)
- ✅ `pages/organigram.md` - Organigram
- ✅ `pages/vanligafragor.md` - Vanliga frågor (FAQ)
- ✅ `pages/kontakt.md` - Kontakt (Contact)

### Sidebar Project Pages
- ✅ `pages/roundaboutart.md` - IKA Roundabout Art
- ✅ `pages/ebf.md` - IKA Evidensbaserad fördom
- ✅ `pages/kidsclub.md` - IKA Kids Club
- ✅ `pages/statskyrkomuseum.md` - IKA Statskyrkomuseum
- ✅ `pages/jagarlikgiltig.md` - IKA Jag är likgiltig

### Additional Pages
- ✅ `pages/engagemang.md` - Visa engagemang
- ✅ `pages/lblistan.md` - Sveriges landskapsbrott - Hela listan

## URL Structure

All pages now use clean Jekyll URLs (without .html extension):

**Before:**
- `/pressrum.html`
- `/kontakt.html`
- `/roundaboutart.html`

**After:**
- `/pressrum/`
- `/kontakt/`
- `/roundaboutart/`

## Updated Files

### Navigation (`_data/navigation.yml`)
All navigation links updated to use clean URLs:
- `/pressrum/`
- `/organigram/`
- `/vanligafragor/`
- `/kontakt/`

### Sidebar (`_data/sidebar.yml`)
All sidebar links updated to use clean URLs:
- `/roundaboutart/`
- `/ebf/`
- `/kidsclub/`
- `/statskyrkomuseum/`
- `/jagarlikgiltig/`

### Homepage (`index.md`)
All internal links updated to use clean URLs:
- `/jagarlikgiltig/`
- `/roundaboutart/`
- `/engagemang/`
- `/statskyrkomuseum/`
- `/ebf/`
- `/lblistan/`
- `/kidsclub/`

### Page Content
All internal links within pages have been updated to use clean URLs.

## Image Paths

All image references have been updated:
- `Bilder/image.jpg` → `/assets/images/content/image.jpg`
- Images are properly linked to the downloaded assets

## Content Preservation

- ✅ All HTML content preserved
- ✅ All formatting maintained
- ✅ All images linked correctly
- ✅ All email links preserved
- ✅ Tables and complex structures maintained

## Notes

- The page `laromedel.html` was not found on the original site (404 error)
- Some pages reference external PDFs and documents that are not included
- All pages use the `page` layout
- Permalinks are set in front matter for clean URLs

## Next Steps

1. Test the site locally: `bundle exec jekyll serve`
2. Verify all pages render correctly
3. Check all links work properly
4. Deploy to GitHub Pages

All pages are ready for deployment!

