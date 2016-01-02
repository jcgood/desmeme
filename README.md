desmeme
=======

This repository contains data and tools for exploring the linguistic typology of templatic constructions described in the form of graphs representing attribute-value matrices. It is associated with a forthcoming book to be published by Cambridge University Press entitled *The linguistic typology of templates* (http://www.cambridge.org/us/academic/subjects/languages-linguistics/grammar-and-syntax/linguistic-typology-templates) authored by Jeff Good, who can be contacted for further information at jcgood@buffalo.edu.

The book contains detailed discussion of the theoretical motivations informing the construction of the database and scripts in this repository. Here, the scripts and data used in the study are briefly described and made available for those wishing to verify the results described in the book or wishing to adapt the methods or data used in the book for their own purposes. The materials here were not formally reviewed as part of the publication process for the book, and they are not intended to be straightforwardly deployed for new projects. The author would be happy to consider working with anyone seeking to use them for testing purposes or who would like to engage in a more formal collaboration.

Please note that the software and associated materials here have been released into the public domain to the extent that this legally allowed. If, for some reason, you believe that any material here has been released erroneously, please contact the author. The release of these materials into the public domain is not meant to relieve any user of the responsibility for adhering to accepted scholarly norms of citation.

Descriptions of each file/folder are as follows, divided across categories of primary resources and secondary resources. The latter class of resources are either generated from the primary resources automatically or quasi-automatically by copying and pasting from automatically generated files.

Primary resources
-----------------

- **GraphJG**: Folder for a Perl module implementing the Similarity Flooding algorithm in Perl (see http://ilpubs.stanford.edu:8090/730/). The module is adapted from the Graph::Similarity module posted to CPAN by Shohei Kameda.
My understanding of the license suggests I can distribute modifications as
long as they are freely available.  I've added "JG" to the name of the module
(and associated files) to make it clear that this is the edited version.

  - **SimilarityJG.pm**: The file that defines the module.

  - **SimilarityJG**: Subfolder for module containing files with implementing the
  algorithm.

    - **MethodJG.pm**: Helper methods for accessing results of Similarity Flooding calculations.
    
    - **SimilarityFloodingJG.pm**: Implementation of Similarity Flooding for the
    database and parameters described in the book.

- **InternalMaterials**: This directory contains various resources used in the creation of the book mentioned above, and included in the repository to assist my own project management, but which are only indirectly connected to the research questions that most of the materials in this repository are intended to explore. Because of this, I do not describe the individual files in this directory here.

- **tdag**: Folder for a Python package which provides functionality for processing the templatic constructions found in the database. The name
stands for "template directed acyclic graph" since it is designed to work with
acyclic directed graphs describing templatic constructions. The package requires
python-graph (https://github.com/pmatiello/python-graph) and rdflib (https://github.com/RDFLib).

  - **\_\_init\_\_.py**: Initialization file for package.
  
  - **avm.py**: Classes and functions for expressing the graphs in the database
  as attribute value matrices for purposes of presentation.
  
  - **comparison.py**: Functions implementing simUI graph similarity method (see http://www.bioconductor.org/packages/release/bioc/vignettes/GOstats/inst/doc/GOvis.pdf) with associated output functions, e.g., for use in SplitsTree4
(http://www.splitstree.org) as well as functions certain kinds of graph visualization.
  
  - **despecification.py**: Functions for processing the templatic descriptions which remove information from them that is not relevant to templatic comparison, such as bibliographic information, labels, and intermediate nodes specifying instances of objects when types are being compared. These functions include some which keep most information associated with templatic components and some which ignore that information.
  
  - **tdag.py**: Defines a class, and associated functions, that build on the graphs constructible using python-graph (https://github.com/pmatiello/python-graph) to allow for proper rendering of graphs that make use of re-entrancy where one node points to another node via two distinct labeled arcs and where nodes a specific type can be repeated. It essentially creates a kind of "shell" layer of the python-graph graphs adding just enough extra information for the needs of this project.

- **LICENSE**: The license for these materials. They are placed in the public domain to the extent that this is legally allowable. The author still requests that, anyone making use of the materials here, acknowledge their use, in particular in scholarly works, following usual practice.

- **RDFtoAVM.py**: A script for reading in an RDF file, finding all described templates, and generating their representations as LaTeX-encoded AVMs for purposes of presentation.

- **RDFtoEntropy.py**: A script for reading in an RDF file and generating an R file for calculating entropy relationships among different templatic features. There may very well be a more efficient way to do some of this processing in R, but, since I don't know R very well, it was easier for me to generate a somewhat verbose R file using Python.

- **RDFtoGraphs.py**: A script for reading in an RDF file, finding all described templates, and generating .dot files based on them which can then be turned into PDF (or whatever's needed) to show node/arc kinds of graphs.

- **RDFtoNexus.py**: A script for reading in an RDF file and generating a file listing pairwise distances between templates using implemented algorithms. These are outputted as nexus files readable by SplitsTree4 (http://www.splitstree.org) and also as LaTeX tables for presentation.

- **RDFtoPerlGraphs.py**: A script for reading in an RDF file, finding all described templates, and generating a Perl script for re-encoding the graphs in a form that is readable by the Perl implementation of the Similarity Flooding algorithm used here. It also generates Perl code for actually comparing all those graphs using the Similarity Flooding library. This is a very strangely roundabout way of doing things (generating Perl from Python), but I found this easier than reimplementing Similarity Flooding in Python.

- **ReadableRDFS.py**: A script for transforming the content of the RDFS file describing the ontology into LaTeX to create a human-readable version.

- **README.md**: This file.

- **template.rdf**: The RDF file containing the description of the templates examined in this study.

- **template.rdfs**: An RDF Schema describing the ontology assumed in the descriptions of the templates found in the template.rdf file.

- **updateAll.py**: Simple script to run other scripts whenever updated
aspects of the book based on changes to the database.


Secondary resources
-------------------


- **EntropyCalcs.r**: An R file generated by RDFtoEntropy.py. It contains
commands to read the data in EntropyTables.txt to calculate entropy values
across a range of templatic features.

- **EntropyTables.txt**: A data file that can be imported into R so that
entropy values across a range of templatic features can be calculated.

- **FloodingSimilarities.txt**: A file generated when GraphFlooding.pl is run
which includes the flooding similarity scores across the relevant nodes of two compared templates. The file itself is created by subroutines called by GraphFlooding.pl that are found in the GraphJG module.

- **GraphFlooding.pl**: A file generated by RDFtoPerlGraphs.py so that the
templates graphs used in this study could be inputted to the Similarity Flooding algorithms implemented in Perl.

- **GraphFloodingAghemMande.pl**: A file made by taking material from GraphFlooding.pl to show just the results for the Aghem and Mande template pairing (for purposes of presentation in the book).

- **GraphFloodingChechenMande.pl**: A file made by taking material from GraphFlooding.pl to show just the results for the Chechen and Mande template pairing (for purposes of presentation in the book).


- **PCGtoDOT-AghemMande.py**: A file automatically generated by PCGtoPython-AghemMande.pl to allow for a pairwise connectivity graph created in Perl to be transformed to a .dot file via a Python library.

- **PCGtoDOT-ChechenMande.py**: A file automatically generated by PCGtoPython-ChechenMande.pl to allow for a pairwise connectivity graph created in Perl to be transformed to a .dot file via a Python library.

- **PCGtoDOT-Example.py**: A file automatically generated by PCGtoPython-Example.pl to allow for a pairwise connectivity graph created in Perl to be transformed to a .dot file via a Python library.

- **PCGtoPython-AghemMande.pl**: A file made by taking material from GraphFlooding.pl to get pairwise connectivity graphs for the Aghem and Mande template pairing (for purposes of presentation in the book).  To limit the amount of new libraries that I had to learn, this file generates a Python script which creates a .dot file for the graph.

- **PCGtoPython-ChechenMande.pl**: A file made by taking material from GraphFlooding.pl to get pairwise connectivity graphs for the Chechen and Mande template pairing (for purposes of presentation in the book). To limit the amount of new libraries that I had to learn, this file generates a Python script which creates a .dot file for the graph.

- **PCGtoPython-Example.pl**: A file made by constructing to small sample graphs to get pairwise connectivity graphs (for purposes of presentation in the book).  To limit the amount of new libraries that I had to learn, this file generates a Python script which creates a .dot file for the graph.

- **template.pprj**: A file generated by Protege (http://protege.stanford.edu) which was used to created the RDF and RDFS files. It is a kind of settings file for the editor.
