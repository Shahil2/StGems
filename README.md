# St Gregorios English Medium School

This is the official website codebase for **St Gregorios English Medium School**, located in Nellipathy, Attappady. 

## Overview
The website is a fully responsive, static site built using modern web development practices to provide a premium, accessible, and fast experience for parents, students, and staff.

### Tech Stack
- **HTML5**: Semantic and accessible markup.
- **CSS3 / Tailwind CSS**: Utility-first CSS framework (via CDN) for rapid, responsive UI development.
- **JavaScript**: Vanilla JS for interactive elements (mobile menu, scroll animations, lightboxes, and carousels).
- **Formspree**: Handles the "Contact Us" form submissions without needing a backend.

## Features
- **Responsive Design**: Optimized for mobile, tablet, and desktop viewing.
- **Dynamic Interactions**: Scroll reveal animations and sticky navigation.
- **SEO Ready**: Configured with meta descriptions, Open Graph tags, robots.txt, and sitemap.xml.
- **Accessible**: Built with ARIA labels to support screen readers.
- **Component Based**: Standardized layouts for all inner pages (About, Academics, Admissions, etc.).

## Development & Usage

Since this is a static website, you do not need a build process or a backend server to run it.

### Running Locally
To view the website on your local machine, simply open `index.html` in any web browser, or use a local development server for a better experience:

```bash
# Using Python
python -m http.server 5500

# Using Node.js (http-server)
npx http-server -p 5500
```
Then navigate to `http://localhost:5500`.

### Directory Structure
```
/
??? css/
?   ??? style.css         # Custom styles and overrides
??? js/
?   ??? main.js           # Interactive scripts
??? images/             # Image assets (hero, gallery, campus, etc.)
??? *.html              # All static pages (index, about, contact, etc.)
??? scaffold_pages.py   # Python script used to scaffold the inner pages
??? seo.py              # Script to inject SEO tags across all HTML files
??? sitemap.xml         # XML Sitemap
??? robots.txt          # Crawler instructions
```

## Maintenance & Updates
- **Replacing Images**: To update placeholders, drop high-resolution images into the `images/` folder maintaining the same filenames, or update the `src` attribute within the HTML.
- **Contact Form**: The contact form is linked to Formspree (`https://formspree.io/f/xbjnrvnq`). Ensure the associated email address is configured to receive these notifications.

---
*Built with care for St Gregorios English Medium School.*
