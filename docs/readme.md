Widoco installation and usage
===================
To use the Widoco documentation tool, please follow this steps:
* You need to download a JAR executable file. Check the latest release for more 
details: (https://github.com/dgarijo/WIDOCO/releases/latest). Alternatively you can clone the repository
(`git clone https://github.com/dgarijo/Widoco`), extract it and run `mvn clean package` to build the jar file.
* Put the resulting jar file into Infomodel\docs\config.
* Run `pip install -r requirements.txt` to make sure, the `request` package is installed.
* Run the `widoco.py` script with `python widoco.py <widoco-filename> <username> <password>` providing your username and
password for the IndustrialDataSpace Jiveon (https://industrialdataspace.jiveon.com/) and the name of the widoco executable (e.g.
`widoco-1.4.11-jar-with-dependencies.jar`).

About Widoco output
===================
The purpose of Widoco is to reuse and integrate existing tools for documentation, plus the set of features listed below:
* Separation of the sections of your html page, so you can write them independently and replace only those needed.
* Automatic annotation in RDF-a of the html produced.
* Association of a provenance page which includes the history of your vocabulary (W3C PROV-O compliant).
* Metadata extraction from the ontology plus the means to complete it on the fly when generating your ontology.
* Guidelines on the main sections that your document should have and how to complete them.

Widoco will create 3 different folders:
|
|-provenance (a folder including a html and RDF serialization of how the documentation page was created)
|-resources (folder with the different resources)
|-sections (folder with the different sections of the documentation, separated for easy editing. Just edit one and the main page will be updated)

Completing ontology metadata.
===================
Widoco uses the ontology metadata to update a configuration file. If you complete that configuration file (ended up widoco.conf), the tool will enhance your html with additional details, such as how to cite the document, previous revisions, icons with the licence, etc.

Browser issues
==========
The result of executing Widoco is a html file. We have tested it in Mozilla, IE and Chrome, and when the page is stored in a server all the browsers work correctly. If you view the file locally, we recommend you to use Mozilla Firefox (or Internet Explorer, if you must). Google Chrome will not show the contents correctly, as it doesn't allow  XMLHttpRequest without HTTP. If you want to view the page locally with Google Chrome you have two possibilities:

a) Place the file in a server and access it via its URL (for example, put it in dropbox and access through its public url).

b) Execute Chrome with the following commands :

(WIN) chrome.exe --allow-file-access-from-files,

(OSX) open /Applications/Google\ Chrome.app/ --args --allow-file-access-from-files

(UNX) /usr/bin/google-chrome --allow-file-access-from-files

Do you have a problem? open an issue at https://github.com/dgarijo/Widoco