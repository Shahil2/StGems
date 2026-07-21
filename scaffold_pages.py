import re
import os

files_to_create = [
    ("about.html", "History & Legacy", "About St Gregorios English Medium School"),
    ("vision-mission.html", "Vision & Mission", "Our Vision & Mission"),
    ("management.html", "Management", "School Management"),
    ("principal-message.html", "Principal's Message", "Message from the Principal"),
    ("academics.html", "Academics", "Our Academic Programs"),
    ("admissions.html", "Admissions", "Admissions Information"),
    ("campus.html", "Campus & Facilities", "Explore Our Campus"),
    ("gallery.html", "Gallery", "Photo Gallery"),
    ("achievements.html", "Achievements", "School Achievements"),
    ("faculty.html", "Faculty", "Our Faculty"),
    ("news.html", "News & Events", "Latest News and Events"),
    ("downloads.html", "Downloads", "Downloads and Resources"),
    ("contact.html", "Contact Us", "Get in Touch"),
    ("cbse-disclosure.html", "CBSE Mandatory Disclosure", "CBSE Mandatory Public Disclosure"),
    ("privacy-policy.html", "Privacy Policy", "Privacy Policy"),
    ("terms.html", "Terms and Conditions", "Terms and Conditions")
]

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Extract header (everything before <main id="main-content">)
header_match = re.search(r'(.*?<main id="main-content">)', html, re.DOTALL)
header = header_match.group(1)

# Ensure the header's canonical URL and title are somewhat generic or parameterized later
header = re.sub(r'<title>.*?</title>', '<title>{page_title} | St Gregorios English Medium School</title>', header)
header = re.sub(r'<link rel="canonical" href="https://www.stgems.org/">', '<link rel="canonical" href="https://www.stgems.org/{filename}">', header)
header = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="{page_title} | St Gregorios English Medium School">', header)
header = re.sub(r'<meta property="og:url" content="https://www.stgems.org/">', '<meta property="og:url" content="https://www.stgems.org/{filename}">', header)

# Make sure navbar active states are generic for now, removing active class from Home
header = header.replace('class="nav-link-item text-white px-3 py-2 text-sm active"', 'class="nav-link-item text-white px-3 py-2 text-sm"')

# Extract footer (everything after </main>)
footer_match = re.search(r'(</main>.*)', html, re.DOTALL)
footer = footer_match.group(1)

for filename, title, heading in files_to_create:
    page_header = header.replace("{page_title}", title).replace("{filename}", filename)
    
    # Active class logic (simple hack for now: if title matches partially)
    if title == "About St Gregorios English Medium School":
        # we skip complex active states in static generation, but could add it
        pass

    # Simple page header banner + content container
    content = f"""
    <!-- Page Header -->
    <section class="bg-navy py-16 px-4 relative">
      <div class="max-w-7xl mx-auto relative z-10 text-center">
        <h1 class="font-heading text-3xl md:text-5xl font-bold text-white mb-4">{heading}</h1>
        <div class="text-gold font-semibold text-sm uppercase tracking-wider">
          <a href="index.html" class="hover:text-white transition-colors">Home</a> / {title}
        </div>
      </div>
    </section>

    <!-- Page Content -->
    <section class="py-20 px-4 bg-white min-h-[50vh]">
      <div class="max-w-4xl mx-auto">
        <!-- Content will be injected here by Antigravity later -->
        <h2 class="text-2xl font-heading text-navy font-semibold mb-6">Coming Soon</h2>
        <p class="text-gray-600">The content for {title} is currently being updated.</p>
      </div>
    </section>
"""
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(page_header + content + footer)
        
print("Successfully generated all scaffold pages.")
