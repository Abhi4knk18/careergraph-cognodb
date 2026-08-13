from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from neo4j.exceptions import Neo4jError, ServiceUnavailable

from backend.database import (
    driver,
    verify_database_connection,
    close_database_connection
)

from backend.queries.career_queries import (
    GET_DEVELOPERS,
    GET_ROLES,
    GET_DEVELOPER_SKILLS,
    GET_CAREER_FIT,
    GET_CAREER_GRAPH,
    GET_LEARNING_PATH
)


app = FastAPI(
    title="CareerGraph API",
    description="Graph-based career exploration API powered by CognoDB",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "CareerGraph API is running",
        "status": "ok"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/health/db")
def database_health():
    try:
        verify_database_connection()

        return {
            "status": "healthy",
            "database": "CognoDB",
            "connection": "successful"
        }

    except Exception:
        raise HTTPException(
            status_code=503,
            detail={
                "status": "unhealthy",
                "database": "CognoDB",
                "error": "Database connection unavailable"
            }
        )


@app.get("/api/developers")
def get_developers():
    try:
        with driver.session() as session:
            result = session.run(GET_DEVELOPERS)

            return [
                record.data()
                for record in result
            ]

    except (ServiceUnavailable, Neo4jError):
        raise HTTPException(
            status_code=503,
            detail="CognoDB is temporarily unavailable. Please try again."
        )


@app.get("/api/roles")
def get_roles():
    try:
        with driver.session() as session:
            result = session.run(GET_ROLES)

            return [
                record.data()
                for record in result
            ]

    except (ServiceUnavailable, Neo4jError):
        raise HTTPException(
            status_code=503,
            detail="CognoDB is temporarily unavailable. Please try again."
        )


@app.get("/api/developers/{developer_id}/skills")
def get_developer_skills(developer_id: str):
    try:
        with driver.session() as session:
            result = session.run(
                GET_DEVELOPER_SKILLS,
                developer_id=developer_id
            )

            return [
                record.data()
                for record in result
            ]

    except (ServiceUnavailable, Neo4jError):
        raise HTTPException(
            status_code=503,
            detail="CognoDB is temporarily unavailable. Please try again."
        )


@app.get("/api/career-fit/{developer_id}/{role_id}")
def get_career_fit(developer_id: str, role_id: str):
    try:
        with driver.session() as session:
            result = session.run(
                GET_CAREER_FIT,
                developer_id=developer_id,
                role_id=role_id
            )

            record = result.single()

            if not record:
                raise HTTPException(
                    status_code=404,
                    detail="Developer or role not found"
                )

            return record.data()

    except HTTPException:
        raise

    except (ServiceUnavailable, Neo4jError):
        raise HTTPException(
            status_code=503,
            detail="CognoDB is temporarily unavailable. Please try again."
        )


@app.get("/api/career-graph/{developer_id}/{role_id}")
def get_career_graph(developer_id: str, role_id: str):
    try:
        with driver.session() as session:
            result = session.run(
                GET_CAREER_GRAPH,
                developer_id=developer_id,
                role_id=role_id
            )

            record = result.single()

            if not record:
                return {
                    "nodes": [],
                    "relationships": []
                }

            return record.data()

    except (ServiceUnavailable, Neo4jError):
        raise HTTPException(
            status_code=503,
            detail="CognoDB is temporarily unavailable. Please try again."
        )


@app.get("/api/learning-path/{developer_id}/{role_id}")
def get_learning_path(developer_id: str, role_id: str):
    try:
        with driver.session() as session:
            result = session.run(
                GET_LEARNING_PATH,
                developer_id=developer_id,
                role_id=role_id
            )

            return [
                record.data()
                for record in result
            ]

    except (ServiceUnavailable, Neo4jError):
        raise HTTPException(
            status_code=503,
            detail="CognoDB is temporarily unavailable. Please try again."
        )