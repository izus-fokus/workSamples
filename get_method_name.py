from rdflib import Graph
g = Graph()
g.parse("data.jsonld")
method_query = """
PREFIX m4i: <http://w3id.org/nfdi4ing/metadata4ing#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?methodname 
WHERE {
  ?step m4i:realizesMethod ?method .
  ?method rdfs:label ?methodname .
}"""

result = g.query(method_query)

for row in result:
    print(f"Methodname: {row.methodname}")