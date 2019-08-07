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

