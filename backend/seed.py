from database import driver


def seed_database():
    with driver.session() as session:

        # --------------------------------------------------
        # 1. DEVELOPERS
        # --------------------------------------------------

        developers = [
            {
                "id": "dev_001",
                "name": "Aarav Sharma",
                "experience_years": 2
            },
            {
                "id": "dev_002",
                "name": "Priya Verma",
                "experience_years": 1
            },
            {
                "id": "dev_003",
                "name": "Rohan Singh",
                "experience_years": 3
            },
            {
                "id": "dev_004",
                "name": "Ananya Gupta",
                "experience_years": 2
            },
            {
                "id": "dev_005",
                "name": "Kabir Mehta",
                "experience_years": 4
            }
        ]

        for developer in developers:
            session.run(
                """
                MERGE (d:Developer {id: $id})
                SET d.name = $name,
                    d.experience_years = $experience_years
                """,
                **developer
            )

        # --------------------------------------------------
        # 2. SKILLS
        # --------------------------------------------------

        skills = [
            {
                "id": "skill_001",
                "name": "Frontend Development",
                "category": "Software Development"
            },
            {
                "id": "skill_002",
                "name": "Backend Development",
                "category": "Software Development"
            },
            {
                "id": "skill_003",
                "name": "Database Design",
                "category": "Software Development"
            },
            {
                "id": "skill_004",
                "name": "REST API Development",
                "category": "Software Development"
            },
            {
                "id": "skill_005",
                "name": "Data Analysis",
                "category": "Data"
            },
            {
                "id": "skill_006",
                "name": "Machine Learning",
                "category": "Data"
            },
            {
                "id": "skill_007",
                "name": "System Design",
                "category": "Architecture"
            },
            {
                "id": "skill_008",
                "name": "Cloud Computing",
                "category": "Infrastructure"
            },
            {
                "id": "skill_009",
                "name": "DevOps",
                "category": "Infrastructure"
            },
            {
                "id": "skill_010",
                "name": "Data Structures & Algorithms",
                "category": "Computer Science"
            }
        ]

        for skill in skills:
            session.run(
                """
                MERGE (s:Skill {id: $id})
                SET s.name = $name,
                    s.category = $category
                """,
                **skill
            )

        # --------------------------------------------------
        # 3. TECHNOLOGIES
        # --------------------------------------------------

        technologies = [
            {
                "id": "tech_001",
                "name": "Python",
                "category": "Programming Language"
            },
            {
                "id": "tech_002",
                "name": "JavaScript",
                "category": "Programming Language"
            },
            {
                "id": "tech_003",
                "name": "React",
                "category": "Frontend"
            },
            {
                "id": "tech_004",
                "name": "FastAPI",
                "category": "Backend"
            },
            {
                "id": "tech_005",
                "name": "Node.js",
                "category": "Backend"
            },
            {
                "id": "tech_006",
                "name": "PostgreSQL",
                "category": "Database"
            },
            {
                "id": "tech_007",
                "name": "MongoDB",
                "category": "Database"
            },
            {
                "id": "tech_008",
                "name": "Docker",
                "category": "DevOps"
            },
            {
                "id": "tech_009",
                "name": "AWS",
                "category": "Cloud"
            },
            {
                "id": "tech_010",
                "name": "Git",
                "category": "Developer Tools"
            }
        ]

        for technology in technologies:
            session.run(
                """
                MERGE (t:Technology {id: $id})
                SET t.name = $name,
                    t.category = $category
                """,
                **technology
            )

        # --------------------------------------------------
        # 4. ROLES
        # --------------------------------------------------

        roles = [
            {
                "id": "role_001",
                "name": "Frontend Developer",
                "level": "Entry"
            },
            {
                "id": "role_002",
                "name": "Backend Developer",
                "level": "Entry"
            },
            {
                "id": "role_003",
                "name": "Full Stack Developer",
                "level": "Mid"
            },
            {
                "id": "role_004",
                "name": "Data Analyst",
                "level": "Entry"
            },
            {
                "id": "role_005",
                "name": "Machine Learning Engineer",
                "level": "Mid"
            },
            {
                "id": "role_006",
                "name": "DevOps Engineer",
                "level": "Mid"
            },
            {
                "id": "role_007",
                "name": "Software Engineer",
                "level": "Entry"
            }
        ]

        for role in roles:
            session.run(
                """
                MERGE (r:Role {id: $id})
                SET r.name = $name,
                    r.level = $level
                """,
                **role
            )

        # --------------------------------------------------
        # 5. PROJECTS
        # --------------------------------------------------

        projects = [
            {
                "id": "project_001",
                "name": "E-Commerce Platform",
                "description": "Full-stack online shopping platform"
            },
            {
                "id": "project_002",
                "name": "Career Analytics Dashboard",
                "description": "Dashboard for analyzing career and job data"
            },
            {
                "id": "project_003",
                "name": "Food Delivery API",
                "description": "REST API for a food delivery platform"
            },
            {
                "id": "project_004",
                "name": "Student Performance Predictor",
                "description": "Machine learning application for student outcomes"
            },
            {
                "id": "project_005",
                "name": "Cloud Deployment Pipeline",
                "description": "Automated application deployment pipeline"
            },
            {
                "id": "project_006",
                "name": "Portfolio Website",
                "description": "Responsive personal developer portfolio"
            }
        ]

        for project in projects:
            session.run(
                """
                MERGE (p:Project {id: $id})
                SET p.name = $name,
                    p.description = $description
                """,
                **project
            )

        # --------------------------------------------------
        # 6. COMPANIES
        # --------------------------------------------------

        companies = [
            {
                "id": "company_001",
                "name": "NovaTech",
                "industry": "Technology"
            },
            {
                "id": "company_002",
                "name": "CloudBridge",
                "industry": "Cloud & Software"
            },
            {
                "id": "company_003",
                "name": "DataSphere",
                "industry": "Data & Analytics"
            },
            {
                "id": "company_004",
                "name": "FinEdge",
                "industry": "FinTech"
            },
            {
                "id": "company_005",
                "name": "CodeCraft",
                "industry": "Software Services"
            }
        ]

        for company in companies:
            session.run(
                """
                MERGE (c:Company {id: $id})
                SET c.name = $name,
                    c.industry = $industry
                """,
                **company
            )

        # --------------------------------------------------
        # 7. DEVELOPER → SKILL
        # --------------------------------------------------

        developer_skills = [
            ("dev_001", "skill_001", "Advanced", 2),
            ("dev_001", "skill_010", "Intermediate", 2),
            ("dev_001", "skill_004", "Beginner", 1),

            ("dev_002", "skill_001", "Intermediate", 1),
            ("dev_002", "skill_002", "Beginner", 1),
            ("dev_002", "skill_010", "Intermediate", 1),

            ("dev_003", "skill_002", "Advanced", 3),
            ("dev_003", "skill_003", "Advanced", 3),
            ("dev_003", "skill_004", "Advanced", 3),
            ("dev_003", "skill_007", "Intermediate", 2),

            ("dev_004", "skill_005", "Advanced", 2),
            ("dev_004", "skill_006", "Intermediate", 1),
            ("dev_004", "skill_010", "Intermediate", 2),

            ("dev_005", "skill_002", "Advanced", 4),
            ("dev_005", "skill_003", "Advanced", 3),
            ("dev_005", "skill_007", "Advanced", 3),
            ("dev_005", "skill_008", "Intermediate", 2),
            ("dev_005", "skill_009", "Intermediate", 2)
        ]

        for developer_id, skill_id, proficiency, years in developer_skills:
            session.run(
                """
                MATCH (d:Developer {id: $developer_id})
                MATCH (s:Skill {id: $skill_id})
                MERGE (d)-[r:HAS_SKILL]->(s)
                SET r.proficiency = $proficiency,
                    r.years = $years
                """,
                developer_id=developer_id,
                skill_id=skill_id,
                proficiency=proficiency,
                years=years
            )

        # --------------------------------------------------
        # 8. PROJECT → TECHNOLOGY
        # --------------------------------------------------

        project_technologies = [
            ("project_001", "tech_002"),
            ("project_001", "tech_003"),
            ("project_001", "tech_005"),
            ("project_001", "tech_007"),

            ("project_002", "tech_003"),
            ("project_002", "tech_001"),
            ("project_002", "tech_006"),

            ("project_003", "tech_001"),
            ("project_003", "tech_004"),
            ("project_003", "tech_006"),

            ("project_004", "tech_001"),
            ("project_004", "tech_006"),

            ("project_005", "tech_008"),
            ("project_005", "tech_009"),
            ("project_005", "tech_010"),

            ("project_006", "tech_002"),
            ("project_006", "tech_003")
        ]

        for project_id, technology_id in project_technologies:
            session.run(
                """
                MATCH (p:Project {id: $project_id})
                MATCH (t:Technology {id: $technology_id})
                MERGE (p)-[:USES]->(t)
                """,
                project_id=project_id,
                technology_id=technology_id
            )

        # --------------------------------------------------
        # 9. TECHNOLOGY → SKILL
        # --------------------------------------------------

        technology_skills = [
            # Existing mappings
            ("tech_001", "skill_002", 0.95),  # Python → Backend Development
            ("tech_001", "skill_006", 0.90),  # Python → Machine Learning

            ("tech_002", "skill_001", 0.95),  # JavaScript → Frontend Development

            ("tech_003", "skill_001", 0.98),  # React → Frontend Development

            ("tech_004", "skill_004", 0.95),  # FastAPI → REST API Development

            ("tech_005", "skill_002", 0.95),  # Node.js → Backend Development

            ("tech_006", "skill_003", 0.95),  # PostgreSQL → Database Design

            ("tech_007", "skill_003", 0.90),  # MongoDB → Database Design

            ("tech_008", "skill_009", 0.95),  # Docker → DevOps

            ("tech_009", "skill_008", 0.98),  # AWS → Cloud Computing

            ("tech_010", "skill_009", 0.70),  # Git → DevOps

            # New mappings
            ("tech_001", "skill_005", 0.90),  # Python → Data Analysis
            ("tech_006", "skill_005", 0.80),  # PostgreSQL → Data Analysis

            ("tech_001", "skill_010", 0.90),  # Python → DSA
            ("tech_002", "skill_010", 0.70),  # JavaScript → DSA

            ("tech_005", "skill_007", 0.75),  # Node.js → System Design
            ("tech_004", "skill_007", 0.70),  # FastAPI → System Design
            ("tech_009", "skill_007", 0.80),  # AWS → System Design
        ]

        for technology_id, skill_id, relevance in technology_skills:
            session.run(
                """
                MATCH (t:Technology {id: $technology_id})
                MATCH (s:Skill {id: $skill_id})
                MERGE (t)-[r:RELATED_TO]->(s)
                SET r.relevance = $relevance
                """,
                technology_id=technology_id,
                skill_id=skill_id,
                relevance=relevance
            )
        # --------------------------------------------------
        # 10. SKILL → ROLE
        # --------------------------------------------------

        role_requirements = [
            ("skill_001", "role_001", "High"),
            ("skill_010", "role_001", "Medium"),

            ("skill_002", "role_002", "High"),
            ("skill_003", "role_002", "High"),
            ("skill_004", "role_002", "High"),
            ("skill_007", "role_002", "Medium"),

            ("skill_001", "role_003", "High"),
            ("skill_002", "role_003", "High"),
            ("skill_003", "role_003", "Medium"),
            ("skill_004", "role_003", "High"),
            ("skill_007", "role_003", "Medium"),

            ("skill_005", "role_004", "High"),
            ("skill_010", "role_004", "Medium"),

            ("skill_005", "role_005", "High"),
            ("skill_006", "role_005", "High"),
            ("skill_010", "role_005", "Medium"),

            ("skill_008", "role_006", "High"),
            ("skill_009", "role_006", "High"),
            ("skill_007", "role_006", "Medium"),

            ("skill_010", "role_007", "High"),
            ("skill_002", "role_007", "Medium"),
            ("skill_003", "role_007", "Medium")
        ]

        for skill_id, role_id, importance in role_requirements:
            session.run(
                """
                MATCH (s:Skill {id: $skill_id})
                MATCH (r:Role {id: $role_id})
                MERGE (s)-[rel:REQUIRED_FOR]->(r)
                SET rel.importance = $importance
                """,
                skill_id=skill_id,
                role_id=role_id,
                importance=importance
            )

        # --------------------------------------------------
        # 11. ROLE → COMPANY
        # --------------------------------------------------

        role_companies = [
            ("role_001", "company_001"),
            ("role_001", "company_005"),

            ("role_002", "company_001"),
            ("role_002", "company_002"),
            ("role_002", "company_004"),

            ("role_003", "company_001"),
            ("role_003", "company_002"),

            ("role_004", "company_003"),
            ("role_004", "company_004"),

            ("role_005", "company_003"),

            ("role_006", "company_002"),

            ("role_007", "company_001"),
            ("role_007", "company_005")
        ]

        for role_id, company_id in role_companies:
            session.run(
                """
                MATCH (r:Role {id: $role_id})
                MATCH (c:Company {id: $company_id})
                MERGE (r)-[:OFFERED_BY]->(c)
                """,
                role_id=role_id,
                company_id=company_id
            )

        # --------------------------------------------------
        # 12. DEVELOPER → PROJECT
        # --------------------------------------------------

        developer_projects = [
            ("dev_001", "project_006", "Frontend Developer"),
            ("dev_001", "project_002", "Frontend Developer"),

            ("dev_002", "project_006", "Frontend Developer"),
            ("dev_002", "project_001", "Full Stack Developer"),

            ("dev_003", "project_003", "Backend Developer"),
            ("dev_003", "project_001", "Backend Developer"),

            ("dev_004", "project_004", "ML Developer"),
            ("dev_004", "project_002", "Data Analyst"),

            ("dev_005", "project_003", "Backend Developer"),
            ("dev_005", "project_005", "DevOps Engineer")
        ]

        for developer_id, project_id, role in developer_projects:
            session.run(
                """
                MATCH (d:Developer {id: $developer_id})
                MATCH (p:Project {id: $project_id})
                MERGE (d)-[r:BUILT]->(p)
                SET r.role = $role
                """,
                developer_id=developer_id,
                project_id=project_id,
                role=role
            )

        # --------------------------------------------------
        # 13. DEVELOPER → TARGET ROLE
        # --------------------------------------------------

        developer_targets = [
            ("dev_001", "role_003"),
            ("dev_002", "role_003"),
            ("dev_003", "role_003"),
            ("dev_004", "role_005"),
            ("dev_005", "role_006")
        ]

        for developer_id, role_id in developer_targets:
            session.run(
                """
                MATCH (d:Developer {id: $developer_id})
                MATCH (r:Role {id: $role_id})
                MERGE (d)-[:TARGETS]->(r)
                """,
                developer_id=developer_id,
                role_id=role_id
            )

    print("✅ CareerGraph seed data loaded successfully")


if __name__ == "__main__":
    try:
        seed_database()
    finally:
        driver.close()