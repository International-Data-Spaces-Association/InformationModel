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

    image_names = download_images(intro, jive_credentials)
    intro = replace_image_names(intro, image_names)
    replace_widoco_html_output('introduction-en.html', intro)

    image_names = download_images(description, jive_credentials)
    description = replace_image_names(description, image_names)
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
    # search <div class="jive-rendered-content"> for the relevant info

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
            intorduction_text = '<div class="jive-rendered-content">' + useful_text
        else:
            useful_text = re.sub(r'3\.\d\.\d', '3.%d.' % subsection_id, useful_text)
            subsection_id += 1
            description_text += '<div class="jive-rendered-content">' + useful_text

    return intorduction_text, description_text


# Downloads the referenced images in the given text from jive.
def download_images(text, jive_credentials):
    session = requests.Session()
    session.auth = (jive_credentials[0], jive_credentials[1])
    auth = session.post('https://industrialdataspace.jiveon.com')

    images = re.findall('src="(.*?).png"', text)
    image_names = {}

    for image in images:
        image_name = image[image.rfind('/') + 1:] + '.png'
        res = re.search(r'(\d{3}-\d{4}-\d-\d{4})', image)
        image_id = res.group(1)

        if image_name in image_names:
            new_image_name = image_name[:-4] + '_2.png'
        else:
            new_image_name = image_name

        image_names[new_image_name] = (image_name, image_id)

        resp = session.get(image)
        with open('../img/' + new_image_name, 'wb') as f:
            f.write(resp.content)

    session.close()

    return image_names


# Replaces the links to the images in the text to the new locations.
def replace_image_names(text, image_names):
    for image_name in image_names:
        image_id = image_names[image_name][1]
        image_old_name = image_names[image_name][0]
        regex = r'https:\/\/industrialdataspace\.jiveon\.com\/servlet\/JiveServlet\/(\w*)Image\/' + image_id + \
                r'\/(([0-9-]*)\/)?'
        text = re.sub(regex + image_old_name, 'img/' + image_name, text)
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


# Delete the local references from "ontology.json".
def clean_up_json_ontology_owl_imports():
    json_regex = r'"http:\/\/www\.w3\.org\/2002\/07\/owl#imports" : \[ (\{\s*"@id" : "file:.*\s*\},?\s)*\],'
    with open('../serializations/ontology.json', 'r') as fp:
        new_content = fp.read()
        new_content = re.sub(json_regex, '', new_content)

    with open('../serializations/ontology.json', 'w') as fp:
        fp.write(new_content)
        fp.close()


# Delete the local references from "ontology.nt".
def clean_up_nt_ontology_owl_imports():
    nt_regex = r'<https:\/\/w3id\.org\/idsa\/core\/this> <http:\/\/www\.w3\.org\/2002\/07\/owl#imports>'
    new_content = ''
    with open('../serializations/ontology.nt', 'r') as fp:
        for line in fp.readlines():
            res = re.search(nt_regex, line)
            if res:
                continue
            new_content += line

    with open('../serializations/ontology.nt', 'w') as fp:
        fp.write(new_content)
        fp.close()


# Delete the local references from "ontology.ttl".
def clean_up_ttl_ontology_owl_imports():
    ttl_regex = r'owl\:imports\s(<file:.*\.ttl>\s[,;]\n\s*)*'
    with open('../serializations/ontology.ttl', 'r') as fp:
        new_content = fp.read()
        new_content = re.sub(ttl_regex, '', new_content)

    with open('../serializations/ontology.ttl', 'w') as fp:
        fp.write(new_content)
        fp.close()


# Delete the local references from "ontology.xml".
def clean_up_xml_ontology_owl_imports():
    xml_regex = r'<owl\:imports\srdf\:resource="file\:.*\.ttl"\/>'
    new_content = ''
    with open('../serializations/ontology.xml', 'r') as fp:
        for line in fp.readlines():
            res = re.search(xml_regex, line)
            if res:
                continue
            new_content += line

    with open('../serializations/ontology.xml', 'w') as fp:
        fp.write(new_content)
        fp.close()


# Some local references are included to the generated serializations.
# This starts the clean up for all formats.
def clean_up_ontology_serialization_owl_imports():
    clean_up_json_ontology_owl_imports()
    clean_up_nt_ontology_owl_imports()
    clean_up_ttl_ontology_owl_imports()
    clean_up_xml_ontology_owl_imports()


# Renames widoco output file "index-en.html" to "index.html".
# Only "index.html" gets displayed correctly with github pages.
def rename_index_file():
    # Replace reference in index-en.html itself
    with open('../index-en.html') as fp:
        text = fp.read()

    text = re.sub('index-en.html', 'index.html', text)

    with open('../index-en.html', 'w') as fp:
        fp.write(text)
        fp.close()

    # Replace reference in provenance-en.html
    with open('../provenance/provenance-en.html') as fp:
        text = fp.read()

    text = re.sub('index-en.html', 'index.html', text)

    with open('../provenance/provenance-en.html', 'w') as fp:
        fp.write(text)
        fp.close()

    # Finally rename the index-en.html file
    if os.path.exists('../index.html'):
        os.remove('../index.html')
    os.rename('../index-en.html', '../index.html')


# Executes the renaming or deletion of incorrect namespaces.
def rename_namespace(old_ns, uri, new_ns):
    with open('../sections/introduction-en.html') as fp:
        text = fp.read()

    regex = r'<tr><td><b>%s</b></td><td>&lt;%s&gt;</td></tr>' % (old_ns, uri)
    if new_ns == '-delete':
        new_line = ''
    else:
        new_line = '<tr><td><b>%s</b></td><td>&lt;%s&gt;</td></tr>' % (new_ns, uri)

    text = re.sub(regex, new_line, text)

    with open('../sections/introduction-en.html', 'w') as fp:
        fp.write(text)
        fp.close()


# Define all namespaces which are not wanted to be added to the namespaces.
# Most of them come from "rdfs:seeAlso"-links or the additional references.
# Additionally defines some incorrectly named namespaces and starts the
# substitution process.
def adjust_namespaces():
    # Entry format for the list:
    # ('<old_namespace>', '<namespace_uri>', '<new_namespace>|-delete')
    namespaces_to_adjust = [
        ('auth', 'https://w3id.org/idsa/code/auth', 'ids-auth'),
        ('ns1', 'http://creativecommons.org/ns', 'cc'),
        ('metamodel', 'https://w3id.org/idsa/metamodel', 'idsm'),
        ('terms', 'http://purl.org/dc/terms', 'dcterms'),
        ('dc', 'http://purl.org/dc/elements/1.1', 'dcelem'),
        ('wgs84_pos', 'http://www.w3.org/2003/01/geo/wgs84_pos', 'wgs84'),
        ('ontology', 'http://www.geonames.org/ontology', 'geonames'),
        ('duv', 'http://www.w3.org/ns/duv', '-delete'),
        ('lcco', 'http://lcweb.loc.gov/catdir/cpso/lcco', '-delete'),
        ('ontology101-noy-mcguinness-html',
         'https://protege.stanford.edu/publications/ontology_development/ontology101-noy-mcguinness.html', '-delete'),
        ('collections', 'https://docs.oracle.com/javase/8/docs/technotes/guides/collections', '-delete'),
        ('html', 'https://tools.ietf.org/html', '-delete'),
        ('iso639-2', 'http://lcweb.loc.gov/standards/iso639-2', '-delete'),
        ('wot', 'http://xmlns.com/wot/0.1', '-delete'),
        ('10-6084', 'http://dx.doi.org/10.6084', '-delete'),
        ('util', 'https://docs.oracle.com/javase/8/docs/api/java/util', '-delete'),
        ('ns', 'http://www.w3.org/2003/06/sw-vocab-status/ns', '-delete'),
        ('github-com', 'https://github.com', '-delete'),
        ('powder-s', 'http://www.w3.org/2007/05/powder-s', '-delete'),
        ('error', 'http://org.semanticweb.owlapi/error', '-delete'),
        ('www-ontodm-com', 'http://www.ontodm.com', '-delete'),
        ('tgn', 'http://www.getty.edu/research/tools/vocabulary/tgn', '-delete'),
        ('assettype', 'http://purl.org/adms/assettype', '-delete'),
        ('rdfg-1', 'http://www.w3.org/2004/03/trix/rdfg-1', '-delete'),
        ('rfc2046', 'https://tools.ietf.org/html/rfc2046', '-delete'),
        ('licenses', 'http://www.apache.org/licenses', '-delete'),
        ('02iso-3166-code-lists', 'http://www.iso.org/iso/en/prods-services/iso3166ma/02iso-3166-code-lists',
         '-delete'),
        ('tr', 'http://www.w3.org/TR', '-delete'),
        ('default namespace', 'https://w3id.org/idsa/core/this', '-delete'),
        ('wiki', 'https://en.wikipedia.org/wiki', '-delete'),
        ('ddi-cv', 'http://www.ddialliance.org/Specification/DDI-CV', '-delete'),
        ('wiki', 'https://github.com/mqtt/mqtt.github.io/wiki', '-delete')
    ]

    for ns in namespaces_to_adjust:
        rename_namespace(ns[0], ns[1], ns[2])


if __name__ == '__main__':
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

    # Correction of unwanted behavior from widoco.jar
    adjust_namespaces()
    clean_up_ontology_serialization_owl_imports()
    rename_index_file()
