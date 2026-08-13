import os
from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()

URI = os.getenv("COGNODB_URI")
USERNAME = os.getenv("COGNODB_USERNAME")
PASSWORD = os.getenv("COGNODB_PASSWORD")

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

try:
    driver.verify_connectivity()
    print("✅ Connected to CognoDB")

    with driver.session() as session:

        # Create a test node
        session.run(
            """
            CREATE (n:TestNode {message: $message})
            """,
            message="Hello from WEXA Assignment"
        )

        print("✅ Test node created")

        # Read the test node
        result = session.run(
            """
            MATCH (n:TestNode)
            RETURN n.message AS message
            """
        )

        for record in result:
            print("📌 Database says:", record["message"])

        # Delete the test node
        session.run(
            """
            MATCH (n:TestNode)
            DELETE n
            """
        )

        print("✅ Test node deleted")

finally:
    driver.close()