import subprocess
from datetime import datetime


def update_config_information():
    newConfig = ''
    today = datetime.today().strftime('%Y-%m-%d')
    with open('./config/config.properties', 'r') as fp:
        for line in fp:
            if line.startswith('dateOfRelease'):
                newConfig += 'dateOfRelease=' + today + '\n'
                continue

            newConfig += line

    with open('./config/config.properties', 'w') as fp:
        fp.write(newConfig)

    return


def run_widoco():
    subprocess.run(['java', '-jar', 'widoco-1.4.1-jar-with-dependencies.jar',
                    '-ontFile', '../Ontology.ttl',
                    '-outFolder', '../docs',
                    '-confFile', './config/config.properties',
                    '-webVowl',
                    '-oops',
                    '-rewriteAll',
                    '-ignoreIndividuals'])
    return


def replace_widoco_html_output(filename, text):
    newHtml = ''
    skipLines = False
    inserted = False
    with open('../docs/sections/' + filename) as fp:
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

    with open('../docs/sections/' + filename, 'w') as fp:
        fp.write(newHtml)
        fp.close()
    return


def load_new_html_text(filename):
    with open('../docs/jiveinfos/' + filename, 'r') as fp:
        text = fp.read()

    return text


def insert_into_widoco(section):
    text = load_new_html_text(section + '.html')
    replace_widoco_html_output(section + '-en.html', text)
    return


def finish_widoco_html():
    insert_into_widoco('introduction')
    insert_into_widoco('description')
    insert_into_widoco('references')


update_config_information()
run_widoco()
finish_widoco_html()
