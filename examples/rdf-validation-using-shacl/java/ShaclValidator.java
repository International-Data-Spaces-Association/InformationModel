import org.apache.jena.graph.Graph;
import org.apache.jena.graph.compose.Union;
import org.apache.jena.ontology.OntModel;
import org.apache.jena.ontology.OntModelSpec;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.riot.RDFLanguages;
import org.apache.jena.riot.RDFParser;
import org.apache.jena.riot.system.ErrorHandlerFactory;
import org.apache.jena.shacl.ShaclValidator;
import org.apache.jena.shacl.Shapes;
import org.apache.jena.shacl.ValidationReport;
import org.apache.jena.util.FileUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.topbraid.jenax.util.JenaUtil;

import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/** Represents an employee.
 * @author Haydar Akyürek
 * A simple Java application to demonstrate the usage of the Jena framework for SHACL validation.
 */

public class ShaclValidator {

    final Logger logger = LoggerFactory.getLogger(SHACL_Validator.class);
    private Path ont_path;
    private Path shacl_path;
    private File instance_file;

    /**
     * main method
     * @throws NullPointerException
     **/
    public static void main(String[] args) throws IOException {
        File[] instances = new File(args[2]).listFiles((dir, name) -> name.toLowerCase().endsWith(".jsonld"));
        for (File p : instances){
            SHACL_Validator validator = new ShaclValidator(args[0], args[1], p);
            validator.validateRDF();
        }
    }

    /**
     *
     * @param ontPath Path to the IDS Information Model
     * @param shaclPath path to the SHACL shapes. Basically the same as the /testing/ directory of the IDS Information Model repository
     * @param instanceFile File of the RDF instance (in JSON-LD) which ha to be validated against SHACL
     * @throws MalformedURLException
     */
    public ShaclValidator(String ontPath, String shaclPath, File instanceFile) throws MalformedURLException {
        this.ont_path = formatRdfPath(ontPath);
        this.shacl_path = formatRdfPath(shaclPath);
        //this.instance_path = formatRdfPath(instance_path) ;
        this.instance_file = instanceFile;
    }

    /**
     * Reads SHACL graphes, ontology and RDF instance and runs validation
     * @throws IOException
     */
    void validateRDF() throws IOException {
        Graph dataGraph = readModelAndInstance();          // Read ontology and
        Shapes shapesGraph = readSHACL();

        System.out.println("Total RDF triples \t" + dataGraph.size());
        System.out.println("Total SHACL shapes \t" + shapesGraph.numShapes());

        ValidationReport report = ShaclValidator.get().validate(shapesGraph, dataGraph);
        if (!report.conforms()) {
            System.out.println(instance_file.toString() + " failed");
            System.out.println(String.valueOf(report.getEntries()));
        }
        else {
            System.out.println("Validation successful");
        }

    }

    /**
     * Converts a path provided as string to a Path object
     * @param stringPath path to the file / directory
     * @return Representation of the file / directory path as a Path object
     * @throws MalformedURLException
     */
    private Path formatRdfPath(String stringPath) throws MalformedURLException {
        URL pathAsUrl = Paths.get(stringPath).toUri().toURL();

        if (pathAsUrl.getPath().substring(0, 4).contains(":")) {
            return Paths.get(pathAsUrl.getPath().substring(1));
        }
        else {
            return Paths.get(pathAsUrl.getPath());
        }
    }

    /**
     * Reads IDS ontology (RDF/Turtle) and the RDF instance (JSON-LD) and builds a union of both.
     * @return Jena Graph object which is the union of the rdf instance and ontology.
     * @throws IOException
     */
    public Graph readModelAndInstance() throws IOException {
        Model model = JenaUtil.createMemoryModel();
        OntModel ontologyModel = JenaUtil.createOntologyModel(OntModelSpec.OWL_DL_MEM, model);
        ontologyModel.read(Files.newInputStream(this.ont_path)
                , null, "TTL");
        Graph rdfInstanceModel = JenaUtil.createMemoryModel().getGraph();
        byte[] jsonLdArr = Files.readAllBytes(this.instance_file.toPath());

        RDFParser parser = RDFParser.create()
                .source(new ByteArrayInputStream(jsonLdArr))
                .lang(RDFLanguages.JSONLD)
                .errorHandler(ErrorHandlerFactory.errorHandlerWarn).build();
        parser.parse(rdfInstanceModel);

        return new Union(rdfInstanceModel, ontologyModel.getGraph());
    }

    /**
     * Read all SHACL shapes files from the path provided
     * @return Shapes object with all graphs parsed
     * @throws IOException
     */
    private Shapes readSHACL() throws IOException {
        Shapes shapes ;
        Model shapesModel = JenaUtil.createMemoryModel();

        //Get all regular SHACL files
        System.out.println(this.shacl_path);
        Stream<Path> paths = Files.walk(this.shacl_path)
                            .filter(p -> p.toString().endsWith(".ttl"));

        List<String> result = paths.filter(Files::isRegularFile)
                                    .map(Path::toString)
                                    .collect(Collectors.toList());

        // generate SHACL shapes graph
        result.forEach(file -> shapesModel.read(file, FileUtils.langTurtle));

        //System.out.println(shapesModel.toString());

        shapes = Shapes.parse(shapesModel);

        return shapes;
    }
}
