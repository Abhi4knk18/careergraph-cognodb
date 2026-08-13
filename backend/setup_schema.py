from database import driver


SCHEMA_QUERIES = [
    """
    CREATE CONSTRAINT developer_id_unique IF NOT EXISTS
    FOR (d:Developer)
    REQUIRE d.id IS UNIQUE
    """,
    """
    CREATE CONSTRAINT skill_id_unique IF NOT EXISTS
    FOR (s:Skill)
    REQUIRE s.id IS UNIQUE
    """,
    """
    CREATE CONSTRAINT role_id_unique IF NOT EXISTS
    FOR (r:Role)
    REQUIRE r.id IS UNIQUE
    """,
    """
    CREATE CONSTRAINT technology_id_unique IF NOT EXISTS
    FOR (t:Technology)
    REQUIRE t.id IS UNIQUE
    """,
    """
    CREATE CONSTRAINT project_id_unique IF NOT EXISTS
    FOR (p:Project)
    REQUIRE p.id IS UNIQUE
    """,
    """
    CREATE CONSTRAINT company_id_unique IF NOT EXISTS
    FOR (c:Company)
    REQUIRE c.id IS UNIQUE
    """
]


def setup_schema():
    with driver.session() as session:
        for query in SCHEMA_QUERIES:
            session.run(query)

    print("✅ CareerGraph schema created successfully")


if __name__ == "__main__":
    try:
        setup_schema()
    finally:
        driver.close()