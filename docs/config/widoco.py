import subprocess
import requests
import sys
import os
import shutil
import re
from datetime import datetime


# Get path to widoco executable jar file and jive credentials from
# command line or bamboo variabes.
def parse_arguments():
    if len(sys.argv) == 4:
        # Use command line arguments
        widoco_path = sys.argv[1]
        jive_un = sys.argv[2]
        jive_pw = sys.argv[3]
    elif len(sys.argv) == 2:
        # Use bamboo variables
        widoco_path = sys.argv[1]
        jive_un = os.environ['bamboo_jive_username']
        jive_pw = os.environ['bamboo_jive_password']
    else:
        # Not enough information provided. Exit.
        print('Usage: widoco.py <widoco_path> <jiveon_username> <jiveon_password>')
        exit(0)

    return widoco_path, (jive_un, jive_pw)


# Update date of release parameter in config file.
def update_config_information():
    new_config = ''
    today = datetime.today().strftime('%Y-%m-%d')
    with open('./config.properties', 'r') as fp:
        for line in fp:
            if line.startswith('dateOfRelease'):
                new_config += 'dateOfRelease=' + today + '\n'
                continue

            new_config += line

    with open('./config.properties', 'w') as fp:
        fp.write(new_config)

    return


# Execute the widoco documentation process.
def run_widoco(widoco_path):
    subprocess.run(['java', '-jar', widoco_path,
                    '-ontFile', '../../Ontology.ttl',
                    '-outFolder', '../../docs',
                    '-confFile', './config.properties',
                    '-webVowl',
                    '-oops',
                    '-rewriteAll',
                    '-ignoreIndividuals'])
    return


# Replace placeholder information in the auto-generated html files with
# a given text or html string.
def replace_widoco_html_output(filename, text):
    newHtml = ''
    skipLines = False
    inserted = False
    with open('../sections/' + filename) as fp:
        for line in fp:
            if line.startswith('<span class="markdown">'):
                skipLines = True
            if line.strip().endswith('/span>'):
                skipLines = False
                continue

            if skipLines and not inserted:
                newHtml += text
                inserted = True
            else:
                newHtml += line.strip()

    with open('../sections/' + filename, 'w') as fp:
        fp.write(newHtml)
        fp.close()
    return


# Download information from jive and insert into the widoco output.
def insert_jive_information(jive_credentials):
    intro, description = get_jive_information(jive_credentials)

    download_images(intro, jive_credentials)
    intro = replace_image_paths(intro)
    replace_widoco_html_output('introduction-en.html', intro)

    download_images(description, jive_credentials)
    description = replace_image_paths(description)
    replace_widoco_html_output('description-en.html', description)

    return


# Downloads a given set of documents to describe the InfoModel.
def get_jive_information(jive_credentials):
    # https://industrialdataspace.jiveon.com/docs/DOC-1952 -> current abstract
    # https://industrialdataspace.jiveon.com/docs/DOC-1953 -> current introduction
    # https://industrialdataspace.jiveon.com/docs/DOC-1954 |
    # https://industrialdataspace.jiveon.com/docs/DOC-1971 |
    # https://industrialdataspace.jiveon.com/docs/DOC-1972 |
    # https://industrialdataspace.jiveon.com/docs/DOC-1973 | -> current description
    # suche <div class="jive-rendered-content>"

    intorduction_text = ''
    description_text = ''
    subsection_id = 1

    for doc_id in ['1953', '1954', '1971', '1972', '1973']:
        resp = requests.get('https://industrialdataspace.jiveon.com/docs/DOC-' + doc_id, data={},
                            auth=(jive_credentials[0], jive_credentials[1]))

        html = resp.text
        useful_text = html.split('<div class="jive-rendered-content">')[1].split('<!-- [DocumentBodyEnd:')[0]

        if doc_id == '1953':
            useful_text = re.sub(r'3\.\d\.\d', '', useful_text)
            intorduction_text = useful_text
        else:
            useful_text = re.sub(r'3\.\d\.\d', '3.%d.' % subsection_id, useful_text)
            subsection_id += 1
            description_text += useful_text

    return intorduction_text, description_text


# Downloads the referenced images in the given text from jive.
def download_images(text, jive_credentials):
    images = re.findall('src="(.*?).png"', text)
    for image in images:
        image_name = image[image.rfind('/') + 1:]
        resp = requests.get(image, data={}, auth=(jive_credentials[0], jive_credentials[1]))
        with open('../img/' + image_name + '.png', 'wb') as f:
            f.write(resp.content)
    return


# Replaces the links to the images in the text to the new locations.
def replace_image_paths(text):
    text = re.sub('https://industrialdataspace.jiveon.com/servlet/JiveServlet/(.*?)Image/(.*?)/',
                  'img/', text)
    return text


# Replace the placeholder for additional references.
def insert_references():
    with open('../static_info/references.html', 'r') as fp:
        ref_text = fp.read()

    replace_widoco_html_output('references-en.html', ref_text)


# Add a description how to use this script to the widoco readme.
def edit_readme():
    with open('../static_info/readme_addition.md', 'r') as fp:
        additional_text = fp.read()

    with open('../readme.md', 'r') as fp:
        text = fp.read()

    with open('../readme.md', 'w') as fp:
        fp.write(additional_text)
        fp.write(text)


# Move the generated ontology files into the serialization folder.
def move_ontology_files():
    for data_format in ['.nt', '.ttl', '.xml', '.json']:
        if os.path.exists('../ontology' + data_format):
            shutil.move('../ontology' + data_format, '../serializations/ontology' + data_format)


# Change the download links for the ontologies to the serialization folder.
def replace_ontology_download_link():
    with open('../index-en.html') as fp:
        text = fp.read()

    for data_format in ['.nt', '.ttl', '.xml', '.json']:
        text = text.replace('ontology' + data_format, 'serializations/' + 'ontology' + data_format)

    with open('../index-en.html', 'w') as fp:
        fp.write(text)
        fp.close()


# Preparation
widoco_path, jive_credentials = parse_arguments()
update_config_information()

# Widoco documentation tool execution
run_widoco(widoco_path)

# Modify and update generated files
edit_readme()
move_ontology_files()
replace_ontology_download_link()
insert_jive_information(jive_credentials)
insert_references()
