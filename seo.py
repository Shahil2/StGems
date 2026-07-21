import glob
import os

meta_tags = """    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="St Gregorios English Medium School, Nellipathy, Attappady. Providing quality CBSE education with a focus on holistic development and academic excellence.">
    <meta name="keywords" content="St Gregorios English Medium School, CBSE school Attappady, best school Palakkad, English medium education Kerala">
    <meta property="og:title" content="St Gregorios English Medium School">
    <meta property="og:description" content="Empowering minds and shaping futures at St Gregorios English Medium School, Nellipathy.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://www.stgems.org/">"""

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<meta name="description"' not in content:
        content = content.replace(
            '    <meta name="viewport" content="width=device-width, initial-scale=1.0">',
            meta_tags
        )
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Injected SEO tags into {file}')
    else:
        print(f'SEO tags already present in {file}')
