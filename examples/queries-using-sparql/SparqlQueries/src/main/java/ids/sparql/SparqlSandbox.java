package ids.sparql;

import org.apache.jena.query.*;
import org.apache.jena.rdf.model.*;
import org.apache.jena.util.FileManager;

import java.io.IOException;
import java.net.URISyntaxException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * A minimal class that executes SPARQL queries on an input, and prints their results.
 * Simply run the main method for a pre-defined example. We use the Apache Jena RDF modules.
 *
 * We currently do not support command line arguments. Instead, please update the fields INPUT and QUERY_LOCATIONS,
 * respectively to your use-case.
 */
public class SparqlSandbox {

    // Input 1/2: An RDF/TTl serialization of an ids:Resource
    private static final String INPUT = "1_LIFE_EXPECTANCY_RESOURCE.ttl";

    // Input 2/2: A list of SPARQL query files to be fired against the input file above
    private static final String[] QUERY_LOCATIONS = new String[]{
            "2_DataCube_hasDimensionCount.sparql",
            "3_DataCube_usesDimension.sparql",
            "4_VoID_usesNamespace.sparql",
            "5_VoID_usesClass.sparql",
            "6_VoID_usesProperty.sparql",
            "7_SHACL_hasDatatype.sparql",
            "8_SHACL_isInRange.sparql",
            "9a_SHACL_hasCardinality1-1.sparql",
            "9b_SHACL_hasCardinality1-n.sparql"
    };

    public static void main(String[] args) throws IOException, URISyntaxException {
        // Load the input file
        FileManager.get().addLocatorClassLoader(SparqlSandbox.class.getClassLoader());
        Model model = FileManager.get().loadModel(INPUT, null, "TURTLE");

        // Iterate over all query files: Load query, execute it, and print results
        for (String queryLocation : QUERY_LOCATIONS) {
            System.out.println("Executing " + queryLocation);
            Path path = Paths.get(ClassLoader.getSystemResource(queryLocation).toURI());
            executeQueryAndPrintResults(path, model);
        }
    }

    /**
     * Reads a SPARQL query from file, executes it against the preloaded target, and prints the results to console.
     * @param queryPath the file path to load the SPARQL query from
     * @param model the preloaded RDF model of the input/target
     * @throws IOException on I/O error while reading the query from the given file path
     */
    private static void executeQueryAndPrintResults(Path queryPath, Model model) throws IOException {
        Query query = QueryFactory.create(Files.readString(queryPath));
        try (QueryExecution queryExecution = QueryExecutionFactory.create(query, model)) {
            ResultSet results = queryExecution.execSelect();
            System.out.println("Query results:");
            while (results.hasNext()) {
                QuerySolution solution = results.nextSolution();
                System.out.println("" + solution);
            }
            System.out.println();
        }
    }
}
