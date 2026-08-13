import os

from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()

URI = os.getenv("COGNODB_URI")
USERNAME = os.getenv("COGNODB_USERNAME")
PASSWORD = os.getenv("COGNODB_PASSWORD")


if not all([URI, USERNAME, PASSWORD]):
    raise RuntimeError(
        "Missing CognoDB environment variables. "
        "Check your .env file."
    )


driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)


def verify_database_connection():
    driver.verify_connectivity()
    return True


def close_database_connection():
    driver.close()