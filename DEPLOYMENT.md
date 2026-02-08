# Deployment Guide

Guide for deploying the Konst och Ansvar website to GitHub Pages.

## Prerequisites

- GitHub account
- Git installed on your computer
- Repository created on GitHub

## Method 1: Automatic Deployment (Recommended)

GitHub Pages can automatically build and deploy Jekyll sites.

### Step 1: Push to GitHub

1. Initialize git (if not already done):
```bash
git init
git add .
git commit -m "Initial commit"
```

2. Add your GitHub repository as remote:
```bash
git remote add origin https://github.com/yourusername/konstochansvar_hemsida.git
```

3. Push to GitHub:
```bash
git branch -M main
git push -u origin main
```

### Step 2: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings**
3. Scroll to **Pages** section
4. Under **Source**, select:
   - Branch: `main`
   - Folder: `/ (root)`
5. Click **Save**

### Step 3: Wait for Build

- GitHub will automatically build your site
- This usually takes 1-2 minutes
- Your site will be available at: `https://yourusername.github.io/konstochansvar_hemsida/`

### Step 4: Custom Domain (Optional)

1. In the Pages settings, enter your custom domain
2. Add a `CNAME` file to your repository root with your domain name
3. Update DNS records as instructed by GitHub

## Method 2: Manual Deployment

If you prefer to build locally and deploy only the static files:

### Step 1: Build the Site

```bash
bundle exec jekyll build
```

This creates a `_site` directory with all static files.

### Step 2: Deploy _site Contents

You can use the `gh-pages` branch method or deploy `_site` to your web server.

## Updating the Site

After making changes:

1. Commit your changes:
```bash
git add .
git commit -m "Description of changes"
```

2. Push to GitHub:
```bash
git push origin main
```

3. GitHub Pages will automatically rebuild and deploy (usually within 1-2 minutes)

## Troubleshooting

### Build Errors

If GitHub Pages build fails:

1. Check the **Actions** tab in your repository for error messages
2. Test locally first: `bundle exec jekyll build`
3. Ensure `_config.yml` is valid YAML
4. Check that all required files are present

### Site Not Updating

- Wait a few minutes (builds can take time)
- Check the **Actions** tab to see if build is in progress
- Clear your browser cache
- Check the repository settings → Pages for any errors

### Plugin Issues

GitHub Pages supports a limited set of Jekyll plugins. If you need additional plugins:

1. Use GitHub Actions to build with custom plugins
2. Or build locally and deploy only `_site` directory

## GitHub Actions (Advanced)

For more control over the build process, you can use GitHub Actions:

1. Create `.github/workflows/jekyll.yml`
2. Configure the workflow to build and deploy
3. This allows custom plugins and build steps

## Local Testing Before Deployment

Always test locally before pushing:

```bash
bundle exec jekyll serve
```

Visit `http://localhost:4000` to preview your site.

## Need Help?

- GitHub Pages Documentation: https://docs.github.com/pages
- Jekyll Documentation: https://jekyllrb.com/docs/
- See `SPEC.md` for full specifications

