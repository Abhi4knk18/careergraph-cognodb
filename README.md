# CareerGraph

### Graph-Powered Career Analysis Application

CareerGraph is a graph-based career analysis application developed for the **Wexa AI CognoDB Take-Home Assignment**.

It helps developers analyze their fit for a target role, identify matched skills, detect skill gaps, discover recommended technologies, and explore career relationships through an interactive graph.

---

## 🚀 Live Demo

**Frontend:**  
https://careergraph-cognodb.vercel.app/

**Backend API:**  
https://careergraph-cognodb-jtn4.onrender.com/

---

## ✨ Key Features

- **Career Fit Analysis** — compares a developer's skills with the requirements of a target role.
- **Matched Skills** — identifies skills already possessed by the developer and required by the selected role.
- **Skill Gap Detection** — identifies missing skills required for the target role.
- **Learning Path** — recommends technologies related to missing skills.
- **Interactive CareerGraph** — visualizes relationships between developers, projects, technologies, skills, roles, and companies.
- **Error Handling** — includes loading, API failure, empty-state, and database connection handling.

---

## 🧠 Graph Model

The core graph relationships are:

Developer → HAS_SKILL → Skill  
Skill → REQUIRED_FOR → Role  
Developer → BUILT → Project  
Project → USES → Technology  
Technology → RELATED_TO → Skill  
Role → OFFERED_BY → Company

These relationships power the career-fit analysis, skill-gap detection, learning recommendations, and interactive CareerGraph.

---

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| Frontend | React, Vite, JavaScript, CSS |
| Graph Visualization | React Flow, Dagre |
| Backend | Python, FastAPI, Uvicorn |
| Database | CognoDB |
| Query Language | Cypher / openCypher |
| Deployment | Vercel + Render |

---

## 📄 Project Documentation

📘 [View CareerGraph Project Documentation](https://drive.google.com/file/d/1jsnYuaPt1adBgvlyOWRB-dYAcQBdJqKn/view?usp=drive_link)

---
## 🎥 Demo Video

[Watch the CareerGraph Demo](PASTE_SCREEN_RECORDING_LINK_HERE)

The demonstration covers the hosted application, career-fit analysis, matched skills, skill gaps, learning path, and interactive CareerGraph.

---

## ⚙️ Local Setup

### Backend

Install the backend dependencies:

    pip install -r backend/requirements.txt

Run the backend from the project root:

    uvicorn backend.main:app --reload

### Frontend

Install the frontend dependencies:

    cd frontend
    npm install

Run the frontend:

    npm run dev

Create a `.env` file in the project root with your CognoDB credentials:

    COGNODB_URI=your_cognodb_uri
    COGNODB_USERNAME=your_cognodb_username
    COGNODB_PASSWORD=your_cognodb_password

---

## 🔐 Security

Database credentials are stored using environment variables and are not committed to GitHub.

---

## 👨‍💻 Author

**Abhishant Kumar**

Mail: **veerusonic.com**

GitHub:  
https://github.com/Abhi4knk18

---

### Wexa AI CognoDB Take-Home Assignment
