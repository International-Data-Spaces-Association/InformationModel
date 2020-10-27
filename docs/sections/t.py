import re

def remove_ids_trailingslash(filename):
    newHtml = ''
    with open(filename, encoding="utf-8") as fp:
        for line in fp:
            if '<div class="entity" id="/' in line:
                newHtml+=line.replace('<div class="entity" id="/','<div class="entity" id="')
            elif '<a href="#/' in line:
                newHtml+=line.replace('<a href="#/','<a href="#')
            else:
                newHtml+=line
                
    with open(filename, 'w', encoding="utf-8") as fp:
        fp.write(newHtml)
        fp.close()
    return