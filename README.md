CareerGraph

Graph-Powered Career Analysis Application

CareerGraph is a graph-powered career analysis application developed for
the Wexa AI CognoDB Take-Home Assignment.

It helps a developer understand how their current skills align with a
target career role, identify skill gaps, discover recommended
technologies, and explore the connected career data through an
interactive graph.

🚀 Live Demo

Frontend:
https://careergraph-cognodb.vercel.app/

Backend API:
https://careergraph-cognodb-jtn4.onrender.com/

API Developers:
https://careergraph-cognodb-jtn4.onrender.com/api/developers

API Roles:
https://careergraph-cognodb-jtn4.onrender.com/api/roles

Database Health:
https://careergraph-cognodb-jtn4.onrender.com/health/db

📌 Project Overview

CareerGraph combines a graph database, REST API, and interactive
frontend to represent relationships between:

Developers

Projects

Technologies

Skills

Roles

Companies

The application follows a simple workflow:

Developer + Target Role → Career Fit → Matched Skills + Skill Gaps →
Recommended Technologies → CareerGraph

The graph structure makes relationship-driven career analysis natural to
query and visualize.

✨ Key Features

1. Career Fit Analysis

A user selects:

Current developer profile

Target career role

The application analyzes the relationship between the developer's
existing skills and the skills required by the selected role.

2. Matched Skills

Skills already possessed by the selected developer and required by the
target role are identified as matching skills.

3. Skill Gap Detection

The application identifies role-required skills that are not currently
associated with the selected developer.

These gaps provide the basis for the recommended learning path.

4. Recommended Technologies

For identified skill gaps, CareerGraph follows technology-to-skill
relationships to recommend relevant technologies.

Examples represented in the project include:

Data Analysis → Python / PostgreSQL

Data Structures & Algorithms → Python / JavaScript

Machine Learning → Python

Frontend Development → React

REST API Development → FastAPI

5. Interactive CareerGraph

The graph visualization connects:

Developer → Project → Technology → Skill → Role → Company

The graph interface supports:

Zoom

Pan

Fit-to-view

Node dragging

Relationship labels

Automatic graph layout

Responsive graph rendering

6. Error and Loading States

The application handles:

API loading

API connection failures

Empty graph responses

Missing skill information

Invalid or incomplete selections

🧠 Why a Graph Database?

CareerGraph is primarily a relationship-driven problem.

The important information is not only the individual entities but also
how those entities are connected.

For example:

Developer ──HAS_SKILL──> Skill
Developer ──BUILT──────> Project ──USES──> Technology
Technology ──RELATED_TO─> Skill
Skill ──REQUIRED_FOR───> Role
Role ──OFFERED_BY──────> Company

These relationships can require multiple traversals to answer questions
such as:

Which skills does this developer already have for the selected role,
which skills are missing, and which technologies could help close
those gaps?

A graph database represents these relationships directly as graph edges,
making traversal-based queries natural and extensible.

🗃️ Graph Data Model

Node Types

Node         Purpose

Developer    Represents a developer profile
Project      Represents a project built by a developer
Technology   Represents a programming technology or tool
Skill        Represents a career skill
Role         Represents a target career role
Company      Represents a company offering a role

Relationships

Relationship     Meaning

HAS_SKILL      Developer possesses a skill
BUILT          Developer built a project
USES           Project uses a technology
RELATED_TO     Technology is related to a skill
REQUIRED_FOR   Skill is required for a role
OFFERED_BY     Role is offered by a company

Graph Model

                         ┌──────────────┐
                         │   Company    │
                         └──────▲───────┘
                                │ OFFERED_BY
                         ┌──────┴───────┐
                         │     Role     │
                         └──────┬───────┘
                                │ REQUIRED_FOR
                                ▼
                         ┌──────────────┐
                         │    Skill     │
                         └──────▲───────┘
                                │ RELATED_TO
                                │
                         ┌──────┴───────┐
                         │ Technology   │
                         └──────▲───────┘
                                │ USES
                         ┌──────┴───────┐
                         │   Project    │
                         └──────▲───────┘
                                │ BUILT
                         ┌──────┴───────┐
                         │  Developer   │
                         └──────────────┘

The actual application renders this connected model as an interactive
CareerGraph.

🏗️ Architecture

┌─────────────────────────────────────────────┐
│                  React UI                   │
│                                             │
│ Developer / Role Selection                  │
│ Career Fit • Skill Gaps • Learning Path     │
│ Interactive CareerGraph                     │
└──────────────────────┬──────────────────────┘
                       │ HTTP / JSON
                       ▼
┌─────────────────────────────────────────────┐
│                 FastAPI                     │
│                                             │
│ API Routes                                  │
│ Career Queries                              │
│ Graph Transformation                        │
│ Error Handling                              │
└──────────────────────┬──────────────────────┘
                       │ Bolt / Cypher
                       ▼
┌─────────────────────────────────────────────┐
│                  CognoDB                    │
│                                             │
│ Developer • Project • Technology            │
│ Skill • Role • Company                      │
└─────────────────────────────────────────────┘

🛠️ Technology Stack

Layer                   Technology / Library    Purpose

Frontend                React                   User interface and
application flow

Frontend                Vite                    Development and
production build
tooling

Frontend                JavaScript              Application logic and
UI interactions

Frontend                React Flow              Interactive graph
(@xyflow/react)       visualization

Frontend                Dagre                   Automatic graph layout
(@dagrejs/dagre)

Frontend                CSS                     Styling and responsive
presentation

Backend                 Python                  Backend programming
language

Backend                 FastAPI                 REST API framework

Backend                 Uvicorn                 ASGI server

Backend                 python-dotenv           Environment
configuration

Backend                 Neo4j Python Driver     Graph database
connectivity

Database                CognoDB                 Connected graph data
storage

Database                Cypher / openCypher     Graph querying

Database                Bolt                    Database connection
protocol

Hosting                 Vercel                  Frontend deployment

Hosting                 Render                  Backend API deployment

🔌 API Endpoints

Area              Method            Endpoint                                        Description

Developers        GET               /api/developers                               Returns available
developer
profiles

Roles             GET               /api/roles                                    Returns available
target roles

Career Fit        GET               /api/career-fit/{developer_id}/{role_id}      Calculates career
fit

Learning Path     GET               /api/learning-path/{developer_id}/{role_id}   Returns missing
skills and
recommended
technologies

🔍 Important Graph Query Logic

Career Fit

The career-fit analysis compares the developer's existing skills against
the skills required by the selected role.

Conceptually:

Developer ──HAS_SKILL──> Skill <──REQUIRED_FOR── Role

The backend uses this relationship to identify matched and missing
skills.

Learning Path

The learning-path logic follows:

Role ──REQUIRED_FOR──> Missing Skill <──RELATED_TO── Technology

This allows the API to return:

Missing skill

Skill category

Recommended technologies

CareerGraph

The CareerGraph combines multiple connected paths:

Developer → Skill → Role
Developer → Project → Technology → Skill
Role → Company

The backend converts the graph result into nodes and edges consumed by
React Flow.

📁 Project Structure

WEXA_COGNODB_ASSIGNMENT/
│
├── backend/
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   ├── seed.py
│   ├── setup_schema.py
│   ├── test_connection.py
│   ├── test_learning.py
│   ├── test_role_relationships.py
│   ├── requirements.txt
│   ├── cypher/
│   │   └── schema.cypher
│   └── queries/
│       └── career_queries.py
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── GraphView.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── docs/
│   └── CareerGraph_Project_Documentation.pdf
│
├── .env.example
├── .gitignore
├── README.md
└── test_connection.py

⚙️ Local Setup

Prerequisites

Make sure the following are installed:

Python 3.12+

Node.js

npm

Git

CognoDB access

1. Clone the Repository

git clone https://github.com/Abhi4knk18/careergraph-cognodb.git
cd careergraph-cognodb

2. Backend Setup

Create and activate a virtual environment:

Windows

python -m venv venv
.\venv\Scripts\Activate.ps1

Install backend dependencies:

pip install -r backend\requirements.txt

3. Configure CognoDB

Create a .env file in the project root:

COGNODB_URI=your_cognodb_uri
COGNODB_USERNAME=your_cognodb_username
COGNODB_PASSWORD=your_cognodb_password

Never commit the real .env file.

The repository contains .env.example as the safe configuration
template.

4. Seed the Database

python backend\seed.py

The seed data creates the connected career entities used by the
application.

5. Run the Backend

From the project root:

uvicorn backend.main:app --reload

The local API will be available at:

http://127.0.0.1:8000

6. Run the Frontend

Open another terminal:

cd frontend
npm install
npm run dev

Vite will provide the local frontend URL.

🧪 Verification

The backend can be verified using:

GET /health

and:

GET /health/db

A successful database health response confirms that the API is connected
to CognoDB.

Example:

{
  "status": "healthy",
  "database": "CognoDB",
  "connection": "successful"
}

The following APIs can also be checked directly:

/api/developers
/api/roles

🚀 Production Deployment

Backend

The FastAPI backend is deployed on Render.

Production start command:

uvicorn backend.main:app --host 0.0.0.0 --port $PORT

Production API:

https://careergraph-cognodb-jtn4.onrender.com/

Frontend

The React/Vite frontend is deployed on Vercel.

Production API configuration uses:

VITE_API_URL=https://careergraph-cognodb-jtn4.onrender.com

Production frontend:

https://careergraph-cognodb.vercel.app/

 Environment Variables

Backend

COGNODB_URI
COGNODB_USERNAME
COGNODB_PASSWORD

Frontend

VITE_API_URL

Secrets and credentials are intentionally excluded from version control
through .gitignore.

 Error Handling

Frontend

The frontend handles:

API loading

API connection errors

Empty graph results

Missing skill data

Invalid selections

Backend

The backend validates required CognoDB environment variables before
creating the database driver.

This prevents the application from silently starting with an invalid
database configuration.

 CareerGraph Workflow

                Select Developer
                       │
                       ▼
                 Select Role
                       │
                       ▼
               Analyze Career Fit
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
    Matched Skills             Skill Gaps
                                    │
                                    ▼
                         Recommended Technologies
                                    │
                                    ▼
                           Interactive CareerGraph

📄 Detailed Documentation

A complete project documentation PDF is included in the repository:

docs/CareerGraph_Project_Documentation.pdf

It contains detailed information about:

Project overview

Technology stack

Architecture

Graph data model

Node types

Relationships

Important Cypher logic

API endpoints

Setup instructions

Environment configuration

Error handling

Project summary

 Author

Abhishant Kumar

Mail: veerusonic.com

GitHub:
https://github.com/Abhi4knk18