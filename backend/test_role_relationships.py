from database import driver

session = driver.session()

query = """
MATCH (r:Role)
WHERE r.id = 'role_002'
MATCH (r)-[rel]-(n)
RETURN
    type(rel) AS relationship,
    labels(n) AS node_labels,
    n.id AS node_id,
    n.name AS node_name
"""

result = session.run(query)

for record in result:
    print(dict(record))

session.close()
driver.close()