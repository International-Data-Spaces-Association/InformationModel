General Information about the ontology documentation and its structure
===================
The ontology documentation is structured in a way that different versions are contained in different folders inside Infomodel/docs. Each folder is named based on the ontology version. Additionally, a copy of the ontology file is kept at /InformationModel
For example, /InformationModel/docs/4.0.0 contains all the files required to build the documentation of the ontology version "4.0.0". And the corresponding ontology file is "Ontology-4.0.0.ttl" can be found on /InformationModel

Moreover, the latest version of the documentation corresponding to the most recent version of the ontology is kept at `/docs`.

Widoco installation and usage
===================
To use the Widoco documentation tool, please follow this steps:
* You need to download a JAR executable file. Check the latest release for more 
details: (https://github.com/dgarijo/WIDOCO/releases/latest). Alternatively you can clone the repository
(`git clone https://github.com/dgarijo/Widoco`), extract it and run `mvn clean package` to build the jar file.
* Put the resulting jar file into Infomodel\docs\config.
* Run `pip install -r requirements.txt` to make sure, the `request` package is installed.
* Run the `widoco.py` script with `python widoco.py <widoco-filename>` providing the name of the widoco executable (e.g.
`widoco-1.4.17-jar-with-dependencies`).

