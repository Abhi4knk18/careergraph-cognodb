CareerGraph

CareerGraph is a graph-powered career analysis application built for the Wexa AI CognoDB take-home assignment.

It helps a developer compare their current skills with the skills required for a target role, identify skill gaps, discover recommended technologies for those gaps, and visually explore relationships between developers, projects, technologies, skills, roles, and companies.

1. Overview

CareerGraph combines:

CognoDB for connected graph data

FastAPI for the backend API

React for the frontend

React Flow for interactive graph visualization

Dagre for automatic graph layout

A user selects a developer and a target role. The application then provides:

Career-fit analysis

Matching and missing skills

Recommended technologies for missing skills

An interactive CareerGraph showing connected entities

A learning path based on the identified skill gaps

2. Why a Graph Database?

CareerGraph is fundamentally a relationship-driven problem.

The important information is not only the individual entities, but how they are connected:

Developer
   │
   ├── HAS_SKILL ───────────────> Skill
   │
   └── BUILT ──> Project
                  │
                  └── USES ──> Technology
                                  │
                                  └── RELATED_TO ──> Skill

Role ── REQUIRED_FOR ──> Skill
Role ── OFFERED_BY ──> Company

For example, to understand a developer's suitability for a role, the application needs to traverse:

Developer → HAS_SKILL → Skill
                         ↑
                         │ REQUIRED_FOR
                         │
                        Role

The application also follows:

Developer → BUILT → Project → USES → Technology
                                      │
                                      └── RELATED_TO → Skill

These multi-hop relationships are naturally represented and queried in a graph database.

A relational approach would require multiple tables and join operations to reconstruct the same connected paths. In CareerGraph, the relationships are first-class graph edges, making traversal-based queries natural and easy to extend.

3. Features

Career Fit Analysis

Select a developer and target role to identify:

Skills already possessed by the developer

Skills required by the target role

Missing skills

Career-fit score

Skill Gap Detection

Missing skills are returned by the backend and highlighted separately in the CareerGraph.

Recommended Learning Path

For each missing skill, the application retrieves related technologies.

For example:

Data Analysis
├── Python
└── PostgreSQL

Data Structures & Algorithms
├── Python
└── JavaScript

Interactive CareerGraph

The graph connects:

Developers

Projects

Technologies

Skills

Roles

Companies

The graph supports:

Zoom

Pan

Fit-to-view

Node dragging

Relationship labels

Graph controls

Responsive graph sizing

Dagre is used to automatically calculate a readable top-to-bottom graph layout before the data is rendered with React Flow.

Loading and Error States

The frontend provides dedicated states for:

Graph loading

Graph API failure

Career analysis errors

Missing/invalid selections

4. Technology Stack

Frontend

React

Vite

JavaScript

React Flow (@xyflow/react)

Dagre (@dagrejs/dagre)

CSS

Backend

Python

FastAPI

Uvicorn

python-dotenv

Official Neo4j Python driver

Database

CognoDB

Cypher / openCypher

Bolt connection

5. Architecture

┌─────────────────────────────────────────┐
│              React Frontend             │
│                                         │
│  Developer / Role Selection             │
│  Career Fit                             │
│  Skill Gaps                             │
│  Learning Path                          │
│  Interactive CareerGraph                │
└───────────────────┬─────────────────────┘
                    │ HTTP / JSON
                    ▼
┌─────────────────────────────────────────┐
│             FastAPI Backend             │
│                                         │
│  API Routes                             │
│  Career Queries                         │
│  Graph Transformation                   │
│  Error Handling                         │
└───────────────────┬─────────────────────┘
                    │ Neo4j Python Driver
                    │ Bolt
                    ▼
┌─────────────────────────────────────────┐
│                CognoDB                  │
│                                         │
│ Developer   Project   Technology        │
│ Skill       Role      Company           │
└─────────────────────────────────────────┘

6. Data Model

Node Types

Node

Purpose

Developer

Represents a developer profile

Project

Represents a project built by a developer

Technology

Represents a programming technology/tool

Skill

Represents a career skill

Role

Represents a target career role

Company

Represents a company offering a role

Relationships

Relationship

Meaning

HAS_SKILL

Developer possesses a skill

BUILT

Developer built a project

USES

Project uses a technology

RELATED_TO

Technology is related to a skill

REQUIRED_FOR

Skill is required for a role

OFFERED_BY

Role is offered by a company

Graph Structure

graph TD
    D[Developer] -->|HAS_SKILL| S[Skill]
    D -->|BUILT| P[Project]
    P -->|USES| T[Technology]
    T -->|RELATED_TO| S
    R[Role] -->|REQUIRED_FOR| S
    R -->|OFFERED_BY| C[Company]

7. Important Cypher Queries

7.1 Career Graph Query

The CareerGraph query combines three graph paths.

Developer → Skill → Role

Developer
   │
   └── HAS_SKILL → Skill ── REQUIRED_FOR → Role

This exposes the relationship between the developer's current skills and the selected role.

Developer → Project → Technology → Skill

Developer
   │
   └── BUILT → Project
                │
                └── USES → Technology
                              │
                              └── RELATED_TO → Skill

This connects the developer's practical project experience to related skills.

Role → Company

Role ── OFFERED_BY → Company

This connects the target role to companies offering that role.

The backend collects these paths and converts the resulting Neo4j nodes and relationships into the JSON structure consumed by React Flow.

7.2 Learning Path Query

The learning-path query identifies skills required for the selected role that are not already covered by the developer.

It then follows technology-to-skill relationships to recommend technologies for those gaps:

Role
 │
 └── REQUIRED_FOR → Missing Skill
                       ▲
                       │ RELATED_TO
                       │
                  Technology

The API returns:

skill_id
skill_name
category
recommended_technologies

This allows the frontend to display each missing skill together with its recommended technologies.

7.3 Technology → Skill Mapping

Technology relationships are stored with a relevance value.

Example:

Python ── RELATED_TO ──> Machine Learning
Python ── RELATED_TO ──> Data Analysis
React ── RELATED_TO ──> Frontend Development
FastAPI ── RELATED_TO ──> REST API Development

The relevance value allows the graph data to retain how strongly a technology relates to a skill.

8. API Endpoints

The frontend communicates with the FastAPI backend through JSON APIs.

Developers

GET /api/developers

Returns available developer profiles.

Roles

GET /api/roles

Returns available target roles.

Career Fit

GET /api/career-fit/{developer_id}/{role_id}

Calculates the selected developer's fit for the selected role.

Learning Path

GET /api/learning-path/{developer_id}/{role_id}

Returns missing skills and recommended technologies.

Career Graph

GET /api/career-graph/{developer_id}/{role_id}

Returns graph nodes and relationships used by the React Flow visualization.

9. Project Structure

WEXA_COGNODB_ASSIGNMENT/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── seed.py
│   ├── test_role_relationships.py
│   └── queries/
│       └── career_queries.py
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── GraphView.jsx
│   ├── package.json
│   └── ...
│
├── .env
├── .gitignore
├── README.md
└── ...

Update this tree if additional files are added before the final repository push.

10. Prerequisites

Before running the project, install:

Python 3.12+

Node.js and npm

A CognoDB instance

Git

11. Backend Setup

Create a virtual environment

From the project root:

python -m venv venv

Activate it on Windows PowerShell:

.\venv\Scripts\Activate.ps1

Install dependencies

pip install -r backend\requirements.txt

12. CognoDB Configuration

The backend reads database credentials from environment variables using python-dotenv.

Create a .env file in the project root:

COGNODB_URI=<your-cognodb-bolt-uri>
COGNODB_USERNAME=<your-cognodb-username>
COGNODB_PASSWORD=<your-cognodb-password>

The backend validates that all three values are present before creating the database driver.

Never commit the real .env file or database password to GitHub.

A safe .env.example should be committed instead:

COGNODB_URI=
COGNODB_USERNAME=
COGNODB_PASSWORD=

13. Seed the Database

From the project root:

python backend\seed.py

A successful seed prints:

✅ CareerGraph seed data loaded successfully

The seed data contains connected developers, roles, skills, technologies, projects, and companies used to demonstrate the application.

14. Run the Backend

From the project root:

cd backend
uvicorn main:app --reload

The local API will run at:

http://127.0.0.1:8000

Because main.py uses imports beginning with backend..., running Uvicorn from the project root may instead be done as uvicorn backend.main:app --reload. Use the command that matches the final import structure after repository cleanup.

15. Run the Frontend

Open a second terminal:

cd frontend
npm install
npm run dev

Vite will display the local frontend URL in the terminal, normally:

http://localhost:5173

Open that URL in a browser.

16. Error Handling

The application includes explicit loading and error states.

Frontend

The graph component handles:

Loading state while the CareerGraph API request is running

API failure state

Empty graph state

Missing skill information

The main application also prevents analysis when the required developer/role selection is not available.

Backend

The database layer checks for the required CognoDB environment variables before creating the database driver.

If credentials are missing, the application raises:

Missing CognoDB environment variables. Check your .env file.

The database connection can also be verified through the backend connectivity check.

17. UI Flow

Select Developer
       │
       ▼
Select Target Role
       │
       ▼
Career Fit Analysis
       │
       ├───────────────┐
       ▼               ▼
Matching Skills     Missing Skills
                       │
                       ▼
                 Learning Path
                       │
                       ▼
                Recommended
                Technologies
                       │
                       ▼
                Interactive
                CareerGraph

The graph provides a visual explanation of the same connected data used by the analysis.

18. Screenshots

Add final screenshots to the repository before submission.

Recommended structure:

docs/
└── screenshots/
    ├── home.png
    ├── career-fit.png
    ├── learning-path.png
    └── career-graph.png

Recommended screenshots:

Main application / selection screen

Career-fit result with skill gaps

Learning-path recommendations

CareerGraph with highlighted skill gaps

19. Production Deployment

The project is designed to be deployed as separate frontend and backend services.

Before deployment:

Configure production CognoDB credentials through environment variables.

Do not expose database credentials in frontend code.

Build the frontend with:

npm run build

Deploy the generated frontend build to the selected static hosting provider.

Deploy the FastAPI backend to the selected backend hosting provider.

Configure the frontend API base URL for the production backend.

Verify the hosted application against the production CognoDB instance.

The final repository should include the hosted application URL and screen recording link.

20. GitHub Checklist

Before pushing the final repository:

Remove unnecessary files

Remove __pycache__

Remove .pyc files

Remove local virtual environment

Remove build artifacts that should not be committed

Confirm .env is ignored

Add .env.example

Confirm no passwords or secrets are present

Update README

Add screenshots

Add final project structure

Test a clean setup from the README

Push the final repository

21. Assignment Alignment

CareerGraph demonstrates the core requirements of the Wexa AI CognoDB assignment:

Graph-based data model

Connected developer/skill/role/project/technology/company entities

Typed relationships

Realistic seed data

Multi-hop graph traversal

Parameterized Cypher queries

Career-fit analysis

Skill-gap identification

Technology recommendations

Interactive graph visualization

Loading and error states

Environment-based database credentials

Responsive UI

Documented setup and query logic

22. Future Improvements

Possible extensions include:

Skill proficiency levels

Weighted career-fit scoring

Personalized learning resources

Job recommendations

More detailed company-role relationships

User authentication

Persistent developer profiles

Graph filtering and search

Additional career analytics

23. Author

Abhishant Kumar

Computer Science & Engineering

GitHub: Abhi4knk18
