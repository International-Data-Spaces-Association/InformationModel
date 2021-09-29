from bs4 import BeautifulSoup as Soup

eval_line = ["""
<dt>Evaluation:</dt><dd><a href="OOPSevaluation/OOPSeval.html#" target="_blank"><img src="https://img.shields.io/badge/Evaluate_with-OOPS! (OntOlogy Pitfall Scanner!)-blue.svg" alt="OOPS Evaluation" /></a></dd>
"""]
html_result_lines = []
with open("index.html") as html_file:
    html_lines = html_file.readlines()
    for index,line in enumerate(html_lines):
        if line.startswith("</dd><dt>Visualization:</dt><dd>"):
            print ("found")
            html_result_lines = html_lines[:index+1]
            html_result_lines += eval_line + html_lines[index+1:]
    with open("ind.html","w") as outfile:
        outfile.write("".join(html_result_lines))