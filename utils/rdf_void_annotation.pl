#!usr/bin/perl

# Perl script to annotate a RDF/TTL dataset using the VoID vocabulary.
# Requires following libraries:
#       RDF::Generator::Void    https://metacpan.org/pod/RDF::Generator::Void
#       RDF::Trine              https://metacpan.org/pod/RDF::Trine

# Run script in shell / command line as follows:
# perl rdf_void_annotation.pl <input file> <output file>   
# where 
#       <input file> = the RDF / TTL file which should be annotated using VoID
#       <output file> = file where the RDF VoID dataset should be saved. Script output is in RDF/TTL syntax.
# e.g.
# perl rdf_void_annotation.pl data.ttl data_void.ttl


# imports
use RDF::Generator::Void;
use RDF::Trine;
use FileHandle;

# variables
my ($filename, $void_filename) = @ARGV;                 
my $base_uri = "https://w3id.org/idsa/core/";                               # Prefix of IDS Information Model.


# read rdf data
my $model = RDF::Trine::Model->new();                                       # Generate empty RDF::Trine "model" object. 
RDF::Trine::Parser->parse_file_into_model($base_uri, $filename, $model );   # Instantiate parser and parse InfoModel from file (auto-detects serialization).
print $model->size . " RDF statements parsed\n";                            # Count and print parsed RDF statements.

# transform 
my $generator = RDF::Generator::Void->new(inmodel => $model);               # Instantiate VoID Generator and read Information Model.
$generator->urispace($base_uri);                                            # Set URI Space.
my $voidmodel = $generator->generate;                                       # Generate VoID model.
print $voidmodel->size . " RDF statements parsed\n";                        # Count VoID statements.

# save
my $serializer = RDF::Trine::Serializer::Turtle->new();                     # Instantiate Turtle Serializer.
open($fh, '>', $void_filename) or die $!;                                   # Open filename to save results.
$serializer->serialize_model_to_file($fh, $voidmodel);                      # Write VoID results to file.
close($fh);                                                                 # Close file.
