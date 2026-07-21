import glob
import os

html_files = glob.glob('*.html')

desktop_campus_link = '<a href="campus.html" class="nav-link-item text-white px-3 py-2 text-sm">Campus</a>'
desktop_disclosure_link = '<a href="cbse-disclosure.html" class="nav-link-item text-white px-3 py-2 text-sm">Mandatory Public Disclosure</a>'

mobile_campus_link = '<a href="campus.html" class="block py-3 px-4 rounded-lg text-navy font-medium hover:bg-blue-50 transition-colors">Campus</a>'
mobile_disclosure_link = '<a href="cbse-disclosure.html" class="block py-3 px-4 rounded-lg text-navy font-medium hover:bg-blue-50 transition-colors">Mandatory Public Disclosure</a>'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # 1. Fix bg-transparent to bg-navy
    if '<nav class="navbar-main sticky top-0 bg-transparent' in content:
        content = content.replace(
            '<nav class="navbar-main sticky top-0 bg-transparent',
            '<nav class="navbar-main sticky top-0 bg-navy'
        )
        modified = True

    # 2. Add Mandatory Public Disclosure to desktop nav
    if desktop_campus_link in content and desktop_disclosure_link not in content:
        content = content.replace(
            desktop_campus_link,
            desktop_campus_link + '\n        ' + desktop_disclosure_link
        )
        modified = True

    # 3. Add Mandatory Public Disclosure to mobile nav
    if mobile_campus_link in content and mobile_disclosure_link not in content:
        content = content.replace(
            mobile_campus_link,
            mobile_campus_link + '\n      ' + mobile_disclosure_link
        )
        modified = True

    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
