import re

with open('cbse-disclosure.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_content = """    <!-- Page Content -->
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

          <div class="space-y-3">
            <a href="#" class="block p-4 border border-gray-100 rounded-lg hover:border-royal-blue hover:shadow-md transition-all group flex justify-between items-center">
              <span class="font-medium text-gray-700 group-hover:text-royal-blue">Mandatory Disclosure Details</span>
              <span class="text-royal-blue text-sm font-semibold">Click Here</span>
            </a>
            <a href="#" class="block p-4 border border-gray-100 rounded-lg hover:border-royal-blue hover:shadow-md transition-all group flex justify-between items-center">
              <span class="font-medium text-gray-700 group-hover:text-royal-blue">NOC</span>
              <span class="text-royal-blue text-sm font-semibold">Click Here</span>
            </a>
            <a href="#" class="block p-4 border border-gray-100 rounded-lg hover:border-royal-blue hover:shadow-md transition-all group flex justify-between items-center">
              <span class="font-medium text-gray-700 group-hover:text-royal-blue">Society Registration Certificate.</span>
              <span class="text-royal-blue text-sm font-semibold">Click Here</span>
            </a>
            <a href="#" class="block p-4 border border-gray-100 rounded-lg hover:border-royal-blue hover:shadow-md transition-all group flex justify-between items-center">
              <span class="font-medium text-gray-700 group-hover:text-royal-blue">Building Fitness</span>
              <span class="text-royal-blue text-sm font-semibold">Click Here</span>
            </a>
            <a href="#" class="block p-4 border border-gray-100 rounded-lg hover:border-royal-blue hover:shadow-md transition-all group flex justify-between items-center">
              <span class="font-medium text-gray-700 group-hover:text-royal-blue">Affiliation Grant Letter</span>
              <span class="text-royal-blue text-sm font-semibold">Click Here</span>
            </a>
            <a href="#" class="block p-4 border border-gray-100 rounded-lg hover:border-royal-blue hover:shadow-md transition-all group flex justify-between items-center">
              <span class="font-medium text-gray-700 group-hover:text-royal-blue">Affidavit by School Manager regarding Non Proprietary Character of Society</span>
              <span class="text-royal-blue text-sm font-semibold">Click Here</span>
            </a>
            <a href="#" class="block p-4 border border-gray-100 rounded-lg hover:border-royal-blue hover:shadow-md transition-all group flex justify-between items-center">
              <span class="font-medium text-gray-700 group-hover:text-royal-blue">Fire & Safety Certificate</span>
              <span class="text-royal-blue text-sm font-semibold">Click Here</span>
            </a>
            <a href="#" class="block p-4 border border-gray-100 rounded-lg hover:border-royal-blue hover:shadow-md transition-all group flex justify-between items-center">
              <span class="font-medium text-gray-700 group-hover:text-royal-blue">LAND LEASE DEED( for 30 years)</span>
              <span class="text-royal-blue text-sm font-semibold">Click Here</span>
            </a>
            <a href="#" class="block p-4 border border-gray-100 rounded-lg hover:border-royal-blue hover:shadow-md transition-all group flex justify-between items-center">
              <span class="font-medium text-gray-700 group-hover:text-royal-blue">Water and Sanitary Certificate</span>
              <span class="text-royal-blue text-sm font-semibold">Click Here</span>
            </a>
            <a href="#" class="block p-4 border border-gray-100 rounded-lg hover:border-royal-blue hover:shadow-md transition-all group flex justify-between items-center">
              <span class="font-medium text-gray-700 group-hover:text-royal-blue">Hygiene and Sanitary Certificate from Panchayat</span>
              <span class="text-royal-blue text-sm font-semibold">Click Here</span>
            </a>
            <a href="#" class="block p-4 border border-gray-100 rounded-lg hover:border-royal-blue hover:shadow-md transition-all group flex justify-between items-center">
              <span class="font-medium text-gray-700 group-hover:text-royal-blue">School Management Committee</span>
              <span class="text-royal-blue text-sm font-semibold">Click Here</span>
            </a>
            <a href="#" class="block p-4 border border-gray-100 rounded-lg hover:border-royal-blue hover:shadow-md transition-all group flex justify-between items-center">
              <span class="font-medium text-gray-700 group-hover:text-royal-blue">PTA executive members</span>
              <span class="text-royal-blue text-sm font-semibold">Click Here</span>
            </a>
            <a href="#" class="block p-4 border border-gray-100 rounded-lg hover:border-royal-blue hover:shadow-md transition-all group flex justify-between items-center">
              <span class="font-medium text-gray-700 group-hover:text-royal-blue">Fee structure</span>
              <span class="text-royal-blue text-sm font-semibold">Click Here</span>
            </a>
            <a href="#" class="block p-4 border border-gray-100 rounded-lg hover:border-royal-blue hover:shadow-md transition-all group flex justify-between items-center">
              <span class="font-medium text-gray-700 group-hover:text-royal-blue">Staff details</span>
              <span class="text-royal-blue text-sm font-semibold">Click Here</span>
            </a>
            <a href="#" class="block p-4 border border-gray-100 rounded-lg hover:border-royal-blue hover:shadow-md transition-all group flex justify-between items-center">
              <span class="font-medium text-gray-700 group-hover:text-royal-blue">Last 3 years board exam results</span>
              <span class="text-royal-blue text-sm font-semibold">Click Here</span>
            </a>
            <a href="#" class="block p-4 border border-gray-100 rounded-lg hover:border-royal-blue hover:shadow-md transition-all group flex justify-between items-center">
              <span class="font-medium text-gray-700 group-hover:text-royal-blue">School Calendar 2024-2025</span>
              <span class="text-royal-blue text-sm font-semibold">Click Here</span>
            </a>
            <a href="#" class="block p-4 border border-gray-100 rounded-lg hover:border-royal-blue hover:shadow-md transition-all group flex justify-between items-center">
              <span class="font-medium text-gray-700 group-hover:text-royal-blue">Water Test Report</span>
              <span class="text-royal-blue text-sm font-semibold">Click Here</span>
            </a>
            <a href="#" class="block p-4 border border-gray-100 rounded-lg hover:border-royal-blue hover:shadow-md transition-all group flex justify-between items-center">
              <span class="font-medium text-gray-700 group-hover:text-royal-blue">Self Certification Proforma</span>
              <span class="text-royal-blue text-sm font-semibold">Click Here</span>
            </a>
            <a href="#" class="block p-4 border border-gray-100 rounded-lg hover:border-royal-blue hover:shadow-md transition-all group flex justify-between items-center">
              <span class="font-medium text-gray-700 group-hover:text-royal-blue">Land Certicare</span>
              <span class="text-royal-blue text-sm font-semibold">Click Here</span>
            </a>
          </div>

        </div>
      </div>
    </section>"""

replaced = re.sub(r'<!-- Page Content -->.*?</section>', new_content, html, flags=re.DOTALL)

with open('cbse-disclosure.html', 'w', encoding='utf-8') as f:
    f.write(replaced)
