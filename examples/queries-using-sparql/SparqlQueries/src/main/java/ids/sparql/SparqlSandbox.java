package ids.sparql;

import org.apache.jena.query.*;
import org.apache.jena.rdf.model.*;
import org.apache.jena.util.FileManager;

import java.io.IOException;
import java.net.URISyntaxException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class SparqlSandbox {
    private static final String INPUT = "1_LIFE_EXPECTANCY_RESOURCE.ttl";

    private static final String[] QUERY_LOCATIONS = new String[]{
            "2_DataCube_hasDimensionCount.sparql",
            "3_DataCube_usesDimension.sparql",
            "4_VoID_usesNamespace.sparql",
            "5_VoID_usesClass.sparql",
            "6_VoID_usesProperty.sparql"
    };

    public static void main(String[] args) throws IOException, URISyntaxException {
        FileManager.get().addLocatorClassLoader(SparqlSandbox.class.getClassLoader());
        Model model = FileManager.get().loadModel(INPUT, null, "TURTLE");

        for (String queryLocation : QUERY_LOCATIONS) {
            System.out.println("Executing " + queryLocation);
            Path path = Paths.get(ClassLoader.getSystemResource(queryLocation).toURI());
            executeQueryAndPrintResults(path, model);
        }
    }

    private static void executeQueryAndPrintResults(Path path, Model model) throws IOException {
        Query query = QueryFactory.create(Files.readString(path));
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
