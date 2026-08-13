"""
CareerGraph Cypher queries.

All queries in this module use parameters for user-provided values.
"""


GET_DEVELOPERS = """
MATCH (d:Developer)
RETURN
    d.id AS id,
    d.name AS name,
    d.experience_years AS experience_years
ORDER BY d.name
"""


GET_ROLES = """
MATCH (r:Role)
RETURN
    r.id AS id,
    r.name AS name,
    r.level AS level
ORDER BY r.name
"""


GET_DEVELOPER_SKILLS = """
MATCH (d:Developer {id: $developer_id})
      -[hs:HAS_SKILL]->(s:Skill)
RETURN
    s.id AS id,
    s.name AS name,
    s.category AS category,
    hs.proficiency AS proficiency,
    hs.years AS years
ORDER BY s.name
"""

GET_CAREER_FIT = """
MATCH (d:Developer {id: $developer_id})
MATCH (r:Role {id: $role_id})

OPTIONAL MATCH (d)-[:HAS_SKILL]->(current_skill:Skill)

OPTIONAL MATCH (required_skill:Skill)-[:REQUIRED_FOR]->(r)

WITH
    d,
    r,
    collect(DISTINCT current_skill) AS current_skills,
    collect(DISTINCT required_skill) AS required_skills

WITH
    d,
    r,
    current_skills,
    required_skills,
    [skill IN required_skills
        WHERE any(current IN current_skills
            WHERE current.id = skill.id)
    ] AS matched_skills

WITH
    d,
    r,
    current_skills,
    required_skills,
    matched_skills,
    [skill IN required_skills
        WHERE NOT any(current IN current_skills
            WHERE current.id = skill.id)
    ] AS missing_skills

RETURN
    d.id AS developer_id,
    d.name AS developer_name,
    r.id AS role_id,
    r.name AS role_name,
    r.level AS role_level,

    [skill IN current_skills |
        {
            id: skill.id,
            name: skill.name,
            category: skill.category
        }
    ] AS current_skills,

    [skill IN required_skills |
        {
            id: skill.id,
            name: skill.name,
            category: skill.category
        }
    ] AS required_skills,

    [skill IN matched_skills |
        {
            id: skill.id,
            name: skill.name,
            category: skill.category
        }
    ] AS matched_skills,

    [skill IN missing_skills |
        {
            id: skill.id,
            name: skill.name,
            category: skill.category
        }
    ] AS missing_skills,

    CASE
    WHEN size(required_skills) = 0 THEN 0
    ELSE round(
        100.0 * size(matched_skills) / size(required_skills)
    )
END AS match_percentage
"""
GET_CAREER_GRAPH = """
MATCH (d:Developer {id: $developer_id})
MATCH (r:Role {id: $role_id})

OPTIONAL MATCH p1 =
    (d)-[:HAS_SKILL]->(skill:Skill)-[:REQUIRED_FOR]->(r)

OPTIONAL MATCH p2 =
    (d)-[:BUILT]->(project:Project)-[:USES]->(technology:Technology)
        -[:RELATED_TO]->(project_skill:Skill)

OPTIONAL MATCH p3 =
    (r)-[:OFFERED_BY]->(company:Company)

OPTIONAL MATCH p4 =
    (required_skill:Skill)-[:REQUIRED_FOR]->(r)

WITH
    collect(DISTINCT p1) +
    collect(DISTINCT p2) +
    collect(DISTINCT p3) +
    collect(DISTINCT p4) AS paths

UNWIND paths AS path

WITH
    nodes(path) AS path_nodes,
    relationships(path) AS path_relationships

UNWIND path_nodes AS node

WITH
    collect(DISTINCT {
        id: node.id,
        label: coalesce(node.name, node.id),
        type: labels(node)[0]
    }) AS nodes,
    collect(DISTINCT path_relationships) AS relationship_lists

UNWIND relationship_lists AS rel_list
UNWIND rel_list AS rel

RETURN
    nodes,
    collect(DISTINCT {
        id: elementId(rel),
        source: startNode(rel).id,
        target: endNode(rel).id,
        type: type(rel)
    }) AS relationships
"""
GET_LEARNING_PATH = """
MATCH (d:Developer {id: $developer_id})
MATCH (r:Role {id: $role_id})

OPTIONAL MATCH (d)-[:HAS_SKILL]->(current_skill:Skill)
OPTIONAL MATCH (required_skill:Skill)-[:REQUIRED_FOR]->(r)

WITH
    d,
    collect(DISTINCT current_skill) AS current_skills,
    collect(DISTINCT required_skill) AS required_skills

WITH
    current_skills,
    [skill IN required_skills
        WHERE NOT any(current IN current_skills
            WHERE current.id = skill.id)
    ] AS missing_skills

UNWIND missing_skills AS missing

OPTIONAL MATCH (technology:Technology)-[:RELATED_TO]->(missing)

WITH
    missing,
    collect(DISTINCT {
        id: technology.id,
        name: technology.name
    }) AS technologies

WITH
    missing,
    [tech IN technologies
        WHERE tech.id IS NOT NULL
    ] AS recommended_technologies

RETURN
    missing.id AS skill_id,
    missing.name AS skill_name,
    missing.category AS category,
    recommended_technologies

ORDER BY skill_name
"""