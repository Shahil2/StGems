import re

documents = [
    ("Mandatory Disclosure Details", "Mandatory Disclosure Details.pdf"),
    ("NOC", "NOC.pdf"),
    ("Society Registration Certificate.", "Society Registration Certificate.pdf"),
    ("Building Fitness", "Building Fitness.pdf"),
    ("Affiliation Grant Letter", "Affiliation Grant Letter.pdf"),
    ("Affidavit by School Manager regarding Non Proprietary Character of Society", "Affidavit by School Manager regarding Non Proprietary Character of Society.pdf"),
    ("Fire & Safety Certificate", "Fire & Safety Certificate.pdf"),
    ("LAND LEASE DEED( for 30 years)", "LAND LEASE DEED( for 30 years).pdf"),
    ("Water and Sanitary Certificate", "Water and Sanitary Certificate.pdf"),
    ("Hygiene and Sanitary Certificate from Panchayat", "Hygiene and Sanitary Certificate from Panchayat.pdf"),
    ("School Management Committee", "School Management Committee.pdf"),
    ("PTA executive members", "PTA executive members.pdf"),
    ("Fee structure", "Fee structure.pdf"),
    ("Staff details", "Staff details.pdf"),
    ("Last 3 years board exam results", "Last 3 years board exam results.pdf"),
    ("School Calendar 2024-2025", "School Calendar 2024-2025.pdf"),
    ("Water Test Report", "Water Test Report.pdf"),
    ("Self Certification Proforma", "Self Certification Proforma.pdf"),
    ("Land Certicare", "Land Certicare.pdf")
]

links_html = ""
for title, filename in documents:
    # URL encode filename
    import urllib.parse
    url = f"docs/disclosure/{urllib.parse.quote(filename)}"
    
    links_html += f"""
            <a href="{url}" target="_blank" class="block p-4 border border-gray-100 rounded-lg hover:border-royal-blue hover:shadow-md transition-all group flex justify-between items-center">
              <span class="font-medium text-gray-700 group-hover:text-royal-blue">{title}</span>
              <span class="text-royal-blue text-sm font-semibold">Click Here</span>
            </a>"""

new_content = f"""    <!-- Page Content -->
    <section class="py-20 px-4 bg-white min-h-[50vh]">
      <div class="max-w-4xl mx-auto">
        <div class="bg-white border border-gray-200 rounded-xl overflow-hidden shadow-sm p-6">
          
          <div class="mb-8 border-b border-gray-100 pb-4">
            <h2 class="text-2xl font-heading font-bold text-navy mb-4">Mandatory Public Disclosure</h2>
            <div class="flex items-center gap-6 text-sm text-gray-500">
              <span class="inline-flex items-center gap-2"><svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg> Published on : 24/03/2025</span>
              <span class="inline-flex items-center gap-2"><svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z"></path></svg> Category : Content</span>
            </div>
          </div>

          <div class="space-y-3">{links_html}
          </div>

        </div>
      </div>
    </section>"""

with open('cbse-disclosure.html', 'r', encoding='utf-8') as f:
    html = f.read()

replaced = re.sub(r'<!-- Page Content -->.*?</section>', new_content, html, flags=re.DOTALL)

with open('cbse-disclosure.html', 'w', encoding='utf-8') as f:
    f.write(replaced)
