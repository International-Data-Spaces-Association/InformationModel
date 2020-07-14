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
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.topbraid.jenax.util.JenaUtil;

import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.Stream;


/**
 * @author Haydar Akyürek, Johannes Lipp
 * A Java application to demonstrate the usage of the Jena framework for SHACL validation.
 * Supports both single and multiple instances during validation. Prints the validation results.
 */
public class SHACL_Validator {

    private static final Logger logger = LogManager.getLogger(SHACL_Validator.class);

    /**
     * Reads three locations from varargs, namely base model, shapes, and instance(s).
     * Validates these iteratively and prints the results.
     *
     * @param args the command line args base model, shapes, and instance(s).
     * @throws IOException on I/O error on any given path
     */
    public static void main(String[] args) throws IOException {
        if (args.length != 3) {
            logger.error("usage: SHACL_Validator.java <base model> <shapes dir> <instance file / instances dir>");
            logger.info("exit");
            return;
        }

        logger.info("Loading base model");
        Graph model = readBaseModel(formatRdfPath(args[0]));
        logger.info("The base model contains {} triples", model.size());

        logger.info("Loading SHACL shapes");
        Shapes shapes = readSHACL(formatRdfPath(args[1]));
        logger.info("{} SHACL shapes in total", shapes.numShapes());

        File instances = new File(args[2]);
        if (instances.isDirectory()) {
            logger.info("Verifying all *.ttl files in directory {}", instances.getPath());
            File[] foundFiles = instances.listFiles((file, s) -> s.endsWith(".ttl"));
            List<File> files = ((foundFiles == null)) ? new ArrayList<>() : List.of(foundFiles);
            logger.info("Found {} files for validation: {}", files.size(), files);

            for (File file : files) {
                validate(model, file, shapes, true);
            }
        } else {
            validate(model, instances, shapes, false);
        }
    }

    /**
     * Validates an instance against a set of shapes, with knowledge from a given ontology
     *
     * @param model        the base model to use for ontology knowledge, e.g. for subClassOf
     * @param instanceFile the instance to validate
     * @param shapes       a number of shapes to use for validation
     * @param waitForUser  whether to ask the user to manually trigger each validation
     * @throws IOException on I/O exception on the given instance file
     */
    public static void validate(Graph model, File instanceFile, Shapes shapes, boolean waitForUser) throws IOException {
        logger.info("Loading instance {}", instanceFile.getName());
        Graph instance = readInstance(formatRdfPath(instanceFile.getPath()));
        logger.info("The instance contains {} RDF triples", instance.size());

        logger.info("Joining base model with instance");
        Graph joinedGraph = new Union(model, instance);
        logger.info("Total RDF triples: {} (roughly {}+{})", joinedGraph.size(), model.size(), instance.size());

        ValidationReport report = ShaclValidator.get().validate(shapes, joinedGraph);
        if (!report.conforms()) {
            logger.error("Validation failed");
            logger.error(String.valueOf(report.getEntries()));
        } else {
            logger.info("Validation successful");
        }

        if (waitForUser) {
            logger.info("Press ENTER to continue, or type \"q\" to quit");
            String input = new Scanner(System.in).nextLine();
            if ("q".equals(input)) {
                logger.info("Quit");
                System.exit(0);
            }
        }
    }

    /**
     * Converts a path provided as string to a Path object
     *
     * @param path path to the file / directory
     * @return a representation of the file / directory path as a Path object
     * @throws MalformedURLException if the given path cannot be converted into a URL
     */
    private static Path formatRdfPath(String path) throws MalformedURLException {
        URL path_as_url = Paths.get(path).toUri().toURL();

        if (path_as_url.getPath().substring(0, 4).contains(":")) {
            return Paths.get(path_as_url.getPath().substring(1));
        } else {
            return Paths.get(path_as_url.getPath());
        }
    }

    /**
     * Reads a base graph model into memory.
     *
     * @param path the path to load the model from
     * @return the loaded graph model
     * @throws IOException on I/O error on the given path
     */
    public static Graph readBaseModel(Path path) throws IOException {
        return JenaUtil.createMemoryModel().read(Files.newInputStream(path), null, "TTL").getGraph();
    }

    /**
     * Reads an instance graph model into memory.
     *
     * @param path the path to load the model from
     * @return the loaded graph model
     * @throws IOException on I/O error on the given path
     */
    public static Graph readInstance(Path path) throws IOException {
        Graph rdfInstanceModel = JenaUtil.createMemoryModel().getGraph();
        byte[] json_ld_arr = Files.readAllBytes(path);

        RDFParser parser = RDFParser.create()
                .source(new ByteArrayInputStream(json_ld_arr))
                .lang(RDFLanguages.TURTLE)
                .errorHandler(ErrorHandlerFactory.errorHandlerWarn).build();
        parser.parse(rdfInstanceModel);

        return rdfInstanceModel;
    }

    /**
     * Reads all SHACL shapes files from the given path, and merges these
     *
     * @param path the path to load the shapes from
     * @return all loaded shapes merged together
     * @throws IOException on I/O error on the given path
     */
    private static Shapes readSHACL(Path path) throws IOException {
        Shapes shapes ;
        Model shapesModel = JenaUtil.createMemoryModel();

        //Get all regular SHACL files
        Stream<Path> paths = Files.walk(path)
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
