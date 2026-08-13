from database import driver

with driver.session() as session:
    result = session.run(
        """
        MATCH (developer:Developer)-[:HAS_SKILL]->(skill:Skill)
        WHERE developer.id = $developer_id
        RETURN skill.id AS id, skill.name AS name
        ORDER BY skill.name
        """,
        developer_id="dev_001"
    )

    for record in result:
        print(dict(record))

driver.close()