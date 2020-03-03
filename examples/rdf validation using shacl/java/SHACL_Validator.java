import org.apache.jena.graph.Graph;
import org.apache.jena.graph.compose.Union;
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

public class SHACL_Validator {

    final Logger logger = LoggerFactory.getLogger(SHACL_Validator.class);
    private Path ont_path;
    private Path shacl_path;
    private Path instance_path;

    /**
     * main method
     * @throws NullPointerException
     **/
    public static void main(String[] args) {
        try {
             SHACL_Validator validator = new SHACL_Validator(args[0], args[1], args[2]);
            validator.validateRDF();
        } catch (IOException | NullPointerException e) {
            e.printStackTrace();
        }
    }

    /**
     *
     * @param ont_path Path to the IDS Information Model
     * @param shacl_path path to the SHACL shapes. Basically the same as the /testing/ directory of the IDS Information Model repository
     * @param instance_path path to the RDF instance (in JSON-LD) which ha to be validated against SHACL
     * @throws MalformedURLException
     */
    public SHACL_Validator(String ont_path, String shacl_path, String instance_path) throws MalformedURLException {
        this.ont_path = format_rdf_path(ont_path);
        this.shacl_path = format_rdf_path(shacl_path);
        this.instance_path = format_rdf_path(instance_path) ;
    }

    /**
     * Reads SHACL graphes, ontology and RDF instance and runs validation
     * @throws IOException
     */
    void validateRDF() throws IOException {
        Graph data_graph = readModelAndInstance();          // Read ontology and
        Shapes shapes_graph = readSHACL();

        System.out.println("Total RDF triples \t" + data_graph.size());
        System.out.println("Total SHACL shapes \t" + shapes_graph.numShapes());

        ValidationReport report = ShaclValidator.get().validate(shapes_graph, data_graph);
        if (!report.conforms()) {
            logger.error("failed");
            logger.error(String.valueOf(report.getEntries()));
        }
        else {
            System.out.println("Validation successful");
        }

    }

    /**
     * Converts a path provided as string to a Path object
     * @param string_path path to the file / directory
     * @return Representation of the file / directory path as a Path object
     * @throws MalformedURLException
     */
    private Path format_rdf_path(String string_path) throws MalformedURLException {
        URL path_as_url = Paths.get(string_path).toUri().toURL();

        if (path_as_url.getPath().substring(0, 4).contains(":")) {
            return Paths.get(path_as_url.getPath().substring(1));
        }
        else {
            return Paths.get(path_as_url.getPath());
        }
    }

    /**
     * Reads IDS ontology (RDF/Turtle) and the RDF instance (JSON-LD) and builds a union of both.
     * @return Jena Graph object which is the union of the rdf instance and ontology.
     * @throws IOException
     */
    public Graph readModelAndInstance() throws IOException {
        Model ontologyModel = JenaUtil.createMemoryModel();
        ontologyModel.read(Files.newInputStream(this.ont_path)
                , null, "TTL");
        Graph rdfInstanceModel = JenaUtil.createMemoryModel().getGraph();
        byte[] json_ld_arr = Files.readAllBytes(this.instance_path);

        RDFParser parser = RDFParser.create()
                .source(new ByteArrayInputStream(json_ld_arr))
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
        shapes = Shapes.parse(shapesModel);

        return shapes;
    }
}
