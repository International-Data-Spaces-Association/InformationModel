import subprocess
import requests
import sys
import os
import shutil
import re
import zipfile
import io
from distutils.dir_util import copy_tree

root = '../../../InformationModel'
copies = f'{root}/copies'
version_folder = copies + '/{ontology_version}/InformationModel-{ontology_version}'


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


# Get files from the repository by release tag (the last release) and build directories
def get_files_from_repository():
    url_api = 'https://api.github.com/repos/International-Data-Spaces-Association/InformationModel/releases'

    response = requests.get(url_api)

    releases = [release['name'] for release in response.json() if release['name'][0] == 'v']
    release_dates = {release['name'][1:]: release['published_at'][:10] for release in response.json() if release['name'][0] == 'v'}
    n_releases = len(releases)

    ontology_latest_version = releases[0][1:]

    for i, version in enumerate(releases[:1]):

        if i == n_releases - 1:
            break

        ontology_version = version[1:]
        ontology_previous_version = releases[i + 1][1:]

        url_get_file = f'https://github.com/International-Data-Spaces-Association/InformationModel/archive/refs/tags/v{ontology_version}.zip'

        response_current_version = requests.get(url_get_file)
        archive = zipfile.ZipFile(io.BytesIO(response_current_version.content))

        archive.extractall(copies + f'/{ontology_version}')

        # Use files we got from the repository and generate documentation, update the corresponding files based on the ontology version
        generate_documentation(ontology_version,ontology_previous_version, ontology_latest_version, release_dates)
        # Update the link to the previous version ontology to point correctly to the documentation
        update_previous_version_information_link(ontology_version, ontology_previous_version)
        # Copy docs to main docs folder
        copy_docs(ontology_version)

    # Keep documentation of the latest version of the ontology at /docs level
    keep_latest_version(ontology_latest_version)


# Run widoco and generate documentation for the last three versions of the ontology
def generate_documentation(ontology_version, ontology_previous_version, ontology_latest_version, release_dates):
    update_config_information(ontology_version, ontology_latest_version, ontology_previous_version, release_dates)

    # Widoco documentation tool execution
    run_widoco(widoco_path, ontology_version)

    # Modify and update generated files
    edit_readme(ontology_version)
    move_ontology_files(ontology_version)
    replace_ontology_download_link(ontology_version)
    #currently getting 401 error while trying to retrieve docs. To investigate with IDSA people
    #insert_jive_information(jive_credentials, ontology_version)
    insert_references(ontology_version)

    # Correction of unwanted behavior from widoco.jar
    adjust_namespaces(ontology_version)
    clean_up_ontology_serialization_owl_imports(ontology_version)
    clean_up_webvowl_json(ontology_version)
    rename_index_file(ontology_version)
    remove_ids_trailingslash('crossref-en.html', ontology_version)
    remove_ids_trailingslash('overview-en.html', ontology_version)
    change_download_file_extension(ontology_version)
    rename_OOPSeval_file(ontology_version)


def clean_up_webvowl_json(ontology_version):
    vf = version_folder.format(ontology_version=ontology_version)
    with open(f'{vf}/docs/webvowl/data/ontology.json', 'r+') as fp:
        content = fp.read()
        new_content = re.sub(r'https://w3id.org/idsa/core-.*/model/security/Token\.ttl',
                             'https://w3id.org/idsa/core',
                             content)
        fp.seek(0)
        fp.write(new_content)
        fp.truncate()


def copy_docs(ontology_version):
    vf = version_folder.format(ontology_version=ontology_version)
    # Path to version of documentation
    source = f'{vf}/docs'
    copy_tree(source, f'../{ontology_version}')


# Copy latest version of documentation to documentation root level
def keep_latest_version(ontology_latest_version):
    vf = version_folder.format(ontology_version=ontology_latest_version)
    # Path to latest version of documentation
    source = f'{vf}/docs'

    # Copy everything from latest version docs to /docs except, however from config only properties
    for file in set(os.listdir(f'{vf}/docs/config')).difference({'config.properties'}):
        os.remove(f'{vf}/docs/config/{file}')
    copy_tree(source, f'..')

    # Update images path for latest version
    update_image_path()


# Update images path for latest version
def update_image_path():
    # Read in the file introduction-en.html
    with open('../sections/introduction-en.html', 'r') as file:
        new_path_introfile = file.read()

    # Replace the target string
    new_path_introfile = new_path_introfile.replace('../../images', '../images')

    # Write the file out again
    with open('../sections/introduction-en.html', 'w') as file:
        file.write(new_path_introfile)

    # Read in the file description-en.html
    with open('../sections/description-en.html', 'r') as fp:
        new_path_descriptionfile = fp.read()

    # Replace the target string
    new_path_descriptionfile = new_path_descriptionfile.replace('../../images', '../images')

    # Write the file out again
    with open('../sections/description-en.html', 'w') as fp:
        fp.write(new_path_descriptionfile)


# Update config.properties file first to generate proper versioning documentation
def update_config_information(ontology_version, ontology_latest_version, ontology_previous_version, release_dates):
    vf = version_folder.format(ontology_version=ontology_version)
    new_config = ''
    with open(f'{vf}/docs/config/config.properties', 'r+') as fp:
        for line in fp:
            if line.startswith('dateOfRelease'):
                line = 'dateOfRelease=' + release_dates[ontology_version] + '\n'
            elif line.startswith('thisVersionURI'):
                line = 'thisVersionURI=' + f'https://w3id.org/idsa/core-{ontology_version.replace(".", "")}' + '\n'
            elif line.startswith('latestVersionURI'):
                line = 'latestVersionURI=' + f'https://w3id.org/idsa/core' + '\n'
            elif line.startswith('previousVersionURI'):
                line = 'previousVersionURI=' + f'https://w3id.org/idsa/core-{ontology_previous_version.replace(".", "")}' + '\n'
            elif line.startswith('ontologyRevisionNumber'):
                line = 'ontologyRevisionNumber=' + ontology_version + '\n'

            new_config += line

        fp.seek(0)
        fp.write(new_config)
        fp.truncate()


# Update previous version of the URI in config file
def update_previous_version_information_link(ontology_version, ontology_previous_version):
    vf = version_folder.format(ontology_version=ontology_version)
    previous_version_config = ''
    onto_previous_version = ontology_previous_version.replace('.', '')
    with open(f'{vf}/docs/index.html', 'r') as fp:
        for line in fp:
            if line.startswith(
                    '<dd><a href="https://international-data-spaces-association.github.io/InformationModel/docs'):
                previous_version_config += '<dd><a href="https://w3id.org/idsa/core-' + onto_previous_version + '">https://w3id.org/idsa/core-' + onto_previous_version + '</a></dd>' + '\n'
                continue

            previous_version_config += line

    with open(f'{vf}/docs/index.html', 'w') as fp:
        fp.write(previous_version_config)
        fp.truncate()
    return


# Execute the widoco documentation process.
def run_widoco(widoco_path, ontology_version):
    vf = version_folder.format(ontology_version=ontology_version)
    ontoFile = f'{vf}/Ontology.ttl'
    outFolder = f'{vf}/docs'
    subprocess.run(['java', '-jar', widoco_path,
                    '-ontFile', ontoFile,
                    '-outFolder', outFolder,
                    '-confFile', f'{vf}/docs/config/config.properties',
                    '-webVowl',
                    '-oops',
                    '-rewriteAll',
                    '-ignoreIndividuals'])
    return


# Replace placeholder information in the auto-generated html files with
# a given text or html string.
def replace_widoco_html_output(filename, text, ontology_version):
    vf = version_folder.format(ontology_version=ontology_version)
    newHtml = ''
    skipLines = False
    inserted = False
    with open(f'{vf}/docs/sections/' + filename, 'r') as fp:
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

    with open(f'{vf}/docs/sections/' + filename, 'w') as fp:
        fp.write(newHtml)
        fp.close()
    return


# Remove trailing slahes from html <href> and "id" values.
# Slashes are inserted because ids namespace contains them.
# They break local referencing inside html file.
# workaround until it's otherweise fixed.

def remove_ids_trailingslash(filename, ontology_version):
    vf = version_folder.format(ontology_version=ontology_version)
    newHtml = ''
    with open(f'{vf}/docs/sections/' + filename, encoding="utf-8") as fp:
        for line in fp:
            if '<div class="entity" id="/' in line:
                newHtml += line.replace('<div class="entity" id="/', '<div class="entity" id="')
            elif '<a href="#/' in line:
                newHtml += line.replace('<a href="#/', '<a href="#')
            else:
                newHtml += line

    with open(f'{vf}/docs/sections/' + filename, 'w', encoding="utf-8") as fp:
        fp.write(newHtml)
        fp.close()
    return


# Download information from jive and insert into the widoco output.
def insert_jive_information(jive_credentials, ontology_version):
    intro, description = get_jive_information(jive_credentials)
    image_names = get_image_names()

    intro = replace_image_names(intro, image_names)
    replace_widoco_html_output('introduction-en.html', intro, ontology_version)

    description = replace_image_names(description, image_names)
    replace_widoco_html_output('description-en.html', description, ontology_version)

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

    # Fix a enumeration mistake in the current version of the jive documents (last checked: 08/19)
    description_text = re.sub(r'Figure\s3\s20:', 'Figure 3.24:', description_text)
    description_text = re.sub(r'Figure\s3\s21:', 'Figure 3.25:', description_text)

    return intorduction_text, description_text


# Not used right now because the current version in jive does not have
# pictures with a high resolution.
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


# Define a translation from the jive image-names to the ones with better resolution.
def get_image_names():
    return {'pastedImage_1.png': 'Figure_3_13_Representations_of_the_Information_Model.png',
            'pastedImage_9.png': 'Table_2_01_Class_diagram.png',
            'pastedImage_10.png': 'Table_2_02_Association.png',
            'pastedImage_15.png': 'Table_2_03_Association_Class.png',
            'pastedImage_16.png': 'Table_2_04_1_Aggregation_and_Composition.png',
            'pastedImage_16_2.png': 'Figure_3_14_Facets_of_the_Information_Model.png',
            'pastedImage_17.png': 'Table_2_04_2_Aggregation_and_Composition.png',
            'pastedImage_20.png': 'Figure_3_15_Taxonomy_of_the_resource_concept.png',
            'pastedImage_23.png': 'Figure_3_16_Views_of_the_resource_(3C_principle).png',
            'pastedImage_25.png': 'Table_2_05_Generalization.png',
            'pastedImage_27.png': 'Figure_3_17_Relation_of_Views_and_Layers.png',
            'pastedImage_32.png': 'Figure_3_18_Layers_of_the_Content_view.png',
            'pastedImage_37.png': 'Figure_3_19_Partial_taxonomy_of_content_kinds.png',
            'pastedImage_46.png': 'Figure_3_20_Outline_of_the_Representation_concept.png',
            'pastedImage_52.png': 'Figure_3_21_Outline_of_the_Provenance_concept.png',
            'pastedImage_57.png': 'Figure_3_22_Layers_of_the_Communication_view.png',
            'pastedImage_67.png': 'Figure_3_23_Outline_of_the_Interface_concept.png',
            'pastedImage_71.png': 'Figure_3_24_Outline_of_the_Operation_concept.png',
            'pastedImage_79.png': 'Figure_3_25_Outline_of_the_Parameter_concept.png',
            'pastedImage_88.png': 'Figure_3_26_Outline_of_the_resource_endpoint_concept.png',
            'pastedImage_91.png': 'Figure_3_27_Outline_of_the_Product_concept.png',
            'pastedImage_102.png': 'Figure_3_28_Taxonomy_of_Product_Pricing_concepts.png',
            'pastedImage_109.png': 'Figure_3_29.png',
            'pastedImage_120.png': 'Figure_3_30_Taxonomy_of_the_Data_Asset_Context.png',
            'pastedImage_131.png': 'Figure_3_31_Dimensions_of_Data_Apps.png',
            'pastedImage_140.png': 'Figure_3_32_Content_view_of_the_Data_App_resource.png',
            'pastedImage_157.png': 'Figure_3_33_Description_matrix_of_the_Data_App_Functionality_dimension.png',
            'pastedImage_163.png': 'Figure_3_34_Data_App_taxonomy.png',
            'pastedImage_170.png': 'Figure_3_35_Outline_of_the_Data_Providing_App_concept.png',
            'pastedImage_185.png': 'Figure_3_36_Taxonomy_of_infrastructure_components.png',
            'pastedImage_196.png': 'Figure_3_37_Outline_of_the_Connector_concept.png',
            'pastedImage_204.png': 'Figure_3_38_Outline_of_the_Security_Profile_concept.png',
            'pastedImage_212.png': 'Figure_3_39_Outline_of_the_Participant_concept.png',
            'pastedImage_227.png': 'Figure_3_40_Outline_of_the_Usage_Contract_concept.png',
            'pastedImage_233.png': 'Figure_3_41_Outline_of_the_Rule_concept.png',
            'pastedImage_241.png': 'Figure_3_42_Outline_of_the_Subscription_concept.png',
            'pastedImage_253.png': 'Figure_3_43_Outline_of_the_Data_Transfer_concept.png',
            'pastedImage_262.png': 'Figure_3_44_Outline_of_the_Entity_with_Lifecycle.png'}


# Replaces the links to the images in the text to the new locations.
def replace_image_names(text, image_names):
    images_in_text = re.findall('src="(.*?).png"', text)

    # Replace links from pastedImage_XXX.png to new paths.
    for text_name in images_in_text:
        old_name = text_name[text_name.rfind('/') + 1:] + '.png'
        res = re.search(r'(\d{3}-\d{4}-\d-\d{4})', text_name)
        image_id = res.group(1)
        regex = r'https:\/\/industrialdataspace\.jiveon\.com\/servlet\/JiveServlet\/(\w*)Image\/' + image_id + \
                r'\/(([0-9-]*)\/)?' + old_name
        text = re.sub(regex, '../../images/' + image_names[old_name], text)

        if old_name == 'pastedImage_16.png':
            image_names[old_name] = image_names['pastedImage_16_2.png']

    # Remove fixed width/height tags, to get better sized images.
    regex = r'(<img\sclass="jive-image\simage-\d+\s(?:[\w-]*\s?)*"\sheight="([\d]*)"\ssrc="\.\.\/images\/' \
            r'(?:Figure|Table)[_\d]*[\w_]*\.png"\s(?:style="(?:\s?[\w-]*\:\s[\w-]*;)*"\s)width="([\d]*)"\/>)'

    results = re.findall(regex, text)
    for res in results:
        new_text = res[0].replace('height="%d"' % int(res[1]), '')
        new_text = new_text.replace('width="%d"' % int(res[2]), '')
        text = text.replace(res[0], new_text)

    return text


# Replace the placeholder for additional references.
def insert_references(ontology_version):
    vf = version_folder.format(ontology_version=ontology_version)
    with open(f'{vf}/docs/static_info/references.html', 'r') as fp:
        ref_text = fp.read()

    replace_widoco_html_output('references-en.html', ref_text, ontology_version)


# Add a description how to use this script to the widoco readme.
def edit_readme(ontology_version):
    vf = version_folder.format(ontology_version=ontology_version)
    with open(f'{vf}/docs/static_info/readme_addition.md', 'r') as fp:
        additional_text = fp.read()

    with open(f'{vf}/docs/readme.md', 'r') as fp:
        text = fp.read()

    with open(f'{vf}/docs/readme.md', 'w') as fp:
        fp.write(additional_text)
        fp.write(text)


# Move the generated ontology files into the serialization folder.
def move_ontology_files(ontology_version):
    vf = version_folder.format(ontology_version=ontology_version)
    for data_format in ['.nt', '.ttl', '.xml', '.json', '.rdf', '.n3', '.jsonld']:
        if os.path.exists(f'{vf}/docs/ontology' + data_format):
            shutil.move(f'{vf}/docs/ontology' + data_format, f'{vf}/docs/serializations/ontology' + data_format)


def replace_ontology_download_link(ontology_version):
    vp = version_folder.format(ontology_version=ontology_version)
    with open(f'{vp}/docs/index-en.html', 'r+') as fp:
        text = fp.read()

        for data_format in ['.nt', '.ttl', '.xml', '.json', '.rdf', '.n3', '.jsonld']:
            text = text.replace('ontology' + data_format, 'serializations/' + 'ontology' + data_format)

        fp.seek(0)
        fp.write(text)
        fp.truncate()


# Delete the local references from "ontology.json".
def clean_up_json_ontology_owl_imports(ontology_version):
    vf = version_folder.format(ontology_version=ontology_version)
    regex_owl_import = r'"http:\/\/www\.w3\.org\/2002\/07\/owl#imports" : \[ (\{\s*"@id" : "file:.*\s*\},?\s)*\],'
    regex_ontology_refs = r'file\:[\w\/\.\:]*'
    new_ref = 'https://w3id.org/idsa/core'

    with open(f'{vf}/docs/serializations/ontology.json', 'r', encoding="latin-1") as fp:
        new_content = fp.read()

    new_content = re.sub(regex_owl_import, '', new_content)
    new_content = re.sub(regex_ontology_refs, new_ref, new_content)

    with open(f'{vf}/docs/serializations/ontology.json', 'w', encoding="latin-1") as fp:
        fp.write(new_content)


# Delete the local references from "ontology.nt".
def clean_up_nt_ontology_owl_imports(ontology_version):
    vf = version_folder.format(ontology_version=ontology_version)
    new_ref = 'https://w3id.org/idsa/core'

    with open(f'{vf}/docs/serializations/ontology.nt', 'r+', encoding="latin-1") as fp:
        content = fp.read()
        new_content = re.sub(r'<file.*Token\.ttl', '<' + new_ref, content)
        fp.seek(0)
        fp.write(new_content)
        fp.truncate()


# Delete the local references from "ontology.ttl".
def clean_up_ttl_ontology_owl_imports(ontology_version):
    vf = version_folder.format(ontology_version=ontology_version)
    new_ref = 'https://w3id.org/idsa/core'

    # <https://w3id.org/idsa/core> rdf:type owl:Ontology ;
    with open(f'{vf}/docs/serializations/ontology.ttl', 'r+', encoding="latin-1") as fp:
        content = fp.read()
        new_content = re.sub(r'<file:/.*#>', '<' + new_ref + '>', content)
        new_content = re.sub(r'<file:/.*Token\.ttl>', '<' + new_ref + '>', new_content)
        fp.seek(0)
        fp.write(new_content)
        fp.truncate()


# Delete the local references from "ontology.xml".
def clean_up_xml_ontology_owl_imports(ontology_version):
    vf = version_folder.format(ontology_version=ontology_version)
    regex_owl_imports = r'<owl\:imports\srdf\:resource="file\:.*\.ttl"\/>'
    regex_ontology_refs = r'file\:[\w\/\.\:#]*'
    new_ref = 'https://w3id.org/idsa/core'

    new_content = ''
    with open(f'{vf}/docs/serializations/ontology.xml', 'r', encoding="latin-1") as fp:
        for line in fp.readlines():
            res = re.search(regex_owl_imports, line)
            if res:
                continue
            new_content += line

    new_content = re.sub(regex_ontology_refs, new_ref, new_content)

    with open(f'{vf}/docs/serializations/ontology.xml', 'w', encoding="latin-1") as fp:
        fp.write(new_content)


def clean_up_webvowl_ontology(ontology_version):
    vf = version_folder.format(ontology_version=ontology_version)
    regex_ontology_ref = r'file\:[\w\/\.\:#]*'
    new_ref = 'https://w3id.org/idsa/core'

    with open(f'{vf}/docs/webvowl/data/ontology.json', 'r') as fp:
        new_content = fp.read()

    new_content = re.sub(regex_ontology_ref, new_ref, new_content)

    with open(f'{vf}/docs/webvowl/data/ontology.json', 'w') as fp:
        fp.write(new_content)


# Some local references are included to the generated serializations.
# This starts the clean up for all formats.
def clean_up_ontology_serialization_owl_imports(ontology_version):
    clean_up_json_ontology_owl_imports(ontology_version)
    clean_up_nt_ontology_owl_imports(ontology_version)
    clean_up_ttl_ontology_owl_imports(ontology_version)
    clean_up_xml_ontology_owl_imports(ontology_version)
    clean_up_webvowl_ontology(ontology_version)

# Change "Download serialization" file extensions in "index.html" as the generated widoco information is not correct, for example Json-ld label reference to json file
def change_download_file_extension(ontology_version):
    vp = version_folder.format(ontology_version=ontology_version)

    with open(f'{vp}/docs/index.html', 'r+') as fp:
        text = fp.read()
        text = re.sub('serializations/ontology.json', 'serializations/ontology.jsonld', text)
        text = re.sub('serializations/ontology.xml', 'serializations/ontology.rdf', text)
        fp.seek(0)
        fp.write(text)
        fp.truncate()

# Renames widoco output file "oopsEval.html" to "OOPSeval.html".
# Only "index.html" gets displayed correctly with github pages.
def rename_OOPSeval_file(ontology_version):
    vp = version_folder.format(ontology_version=ontology_version)

    # Replace reference in index.html
    with open(f'{vp}/docs/index.html', 'r+') as fp:
        text = fp.read()
        text = re.sub('OOPSEvaluation/oopsEval.html', 'OOPSevaluation/OOPSeval.html', text)
        fp.seek(0)
        fp.write(text)
        fp.truncate()

    # Finally rename the oopsEval.html file
    if os.path.exists(f'{vp}/docs/OOPSevaluation/oopsEval.html'):
        #os.remove(f'{vp}/docs/index.html')
        os.rename(f'{vp}/docs/OOPSevaluation/oopsEval.html', f'{vp}/docs/OOPSevaluation/OOPSeval.html')
    
# Renames widoco output file "index-en.html" to "index.html".
# Only "index.html" gets displayed correctly with github pages.
def rename_index_file(ontology_version):
    vp = version_folder.format(ontology_version=ontology_version)

    # Replace reference in index-en.html itself
    with open(f'{vp}/docs/index-en.html', 'r+') as fp:
        text = fp.read()
        text = re.sub('index-en.html', 'index.html', text)
        fp.seek(0)
        fp.write(text)
        fp.truncate()

    # Replace reference in provenance-en.html
    with open(f'{vp}/docs/provenance/provenance-en.html', 'r+') as fp:
        text = fp.read()
        text = re.sub('index-en.html', 'index.html', text)
        fp.seek(0)
        fp.write(text)
        fp.truncate()

    # Finally rename the index-en.html file
    if os.path.exists(f'{vp}/docs/index.html'):
        os.remove(f'{vp}/docs/index.html')
    os.rename(f'{vp}/docs/index-en.html', f'{vp}/docs/index.html')

# Executes the renaming or deletion of incorrect namespaces.
def rename_namespace(old_ns, uri, new_ns, ontology_version):
    vf = version_folder.format(ontology_version=ontology_version)
    with open(f'{vf}/docs/sections/introduction-en.html') as fp:
        text = fp.read()

    regex = r'<tr><td><b>%s</b></td><td>&lt;%s&gt;</td></tr>' % (old_ns, uri)
    if new_ns == '-delete':
        new_line = ''
    else:
        new_line = '<tr><td><b>%s</b></td><td>&lt;%s&gt;</td></tr>' % (new_ns, uri)

    text = re.sub(regex, new_line, text)

    with open(f'{vf}/docs/sections/introduction-en.html', 'w') as fp:
        fp.write(text)


# Define all namespaces which are not wanted to be added to the namespaces.
# Most of them come from "rdfs:seeAlso"-links or the additional references.
# Additionally defines some incorrectly named namespaces and starts the
# substitution process.
def adjust_namespaces(ontology_version):
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
        ('wiki', 'https://github.com/mqtt/mqtt.github.io/wiki', '-delete'),
        ('default namespace', r'file\:[\w\/\.\:]*', '-delete')
    ]

    for ns in namespaces_to_adjust:
        rename_namespace(ns[0], ns[1], ns[2], ontology_version)


if __name__ == '__main__':
    # Preparation
    widoco_path, jive_credentials = parse_arguments()
    # Get files by tag from repository and then run widoco documentation process
    get_files_from_repository()