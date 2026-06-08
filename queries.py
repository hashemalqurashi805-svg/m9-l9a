"""Three SPARQL queries against the recipes ontology.

Each function returns a SPARQL query string. The autograder parses your TTL
file with rdflib and runs each query both in-memory and against the live
Fuseki endpoint at http://localhost:3030/recipes/sparql.
"""

def q1():
    """Q1 — List all recipes and their names."""
    return """
    PREFIX : <http://aispire.example.org/recipes/>
    SELECT ?recipe ?name WHERE {
        ?recipe a :Recipe ; 
                :name ?name .
    }
    """

def q2():
    """Q2 — List all Italian recipes matching either skos:prefLabel "Italian"
    OR skos:altLabel "italiano".
    """
    return """
    PREFIX : <http://aispire.example.org/recipes/>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    SELECT ?recipe ?name WHERE {
        ?recipe a :Recipe ; 
                :name ?name ; 
                :cuisine ?cuisine .
        ?cuisine skos:prefLabel|skos:altLabel ?label .
        FILTER (?label = "Italian" || ?label = "italiano")
    }
    """

def q3():
    """Q3 — List recipes published after 2020 with their primary ingredient."""
    return """
    PREFIX : <http://aispire.example.org/recipes/>
    SELECT ?recipe ?ingredient WHERE {
        ?recipe :year ?year ; 
                :primaryIngredient ?ingredient .
        FILTER (?year > 2020)
    }
    """
def q4():
    return """
    PREFIX : <http://aispire.example.org/recipes/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?recipe WHERE {
        ?recipe :cuisine ?c .
        ?c rdfs:subClassOf* :European .
    }
    """
