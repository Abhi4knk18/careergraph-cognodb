import { useEffect, useState } from "react";
import "./App.css";
import GraphView from "./GraphView";
const API_BASE_URL =
  import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";
function App() {
  const [developers, setDevelopers] = useState([]);
  const [roles, setRoles] = useState([]);

  const [selectedDeveloper, setSelectedDeveloper] = useState("");
  const [selectedRole, setSelectedRole] = useState("");

  const [careerFit, setCareerFit] = useState(null);
  const [learningPath, setLearningPath] = useState([]);

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // ----------------------------------------
  // Load developers and roles
  // ----------------------------------------
  useEffect(() => {
    loadInitialData();
  }, []);

  async function loadInitialData() {
    try {
      const [developersResponse, rolesResponse] = await Promise.all([
        fetch(`${API_BASE_URL}/api/developers`),
        fetch(`${API_BASE_URL}/api/roles`),
      ]);

      if (!developersResponse.ok || !rolesResponse.ok) {
        throw new Error("Failed to load CareerGraph data");
      }

      const developersData = await developersResponse.json();
      const rolesData = await rolesResponse.json();

      setDevelopers(developersData);
      setRoles(rolesData);
    } catch (err) {
      console.error("Initial data error:", err);
      setError("Unable to connect to the CareerGraph API.");
    }
  }

  // ----------------------------------------
  // Analyze Career Fit + Learning Path
  // ----------------------------------------
  async function analyzeCareerFit() {
    if (!selectedDeveloper || !selectedRole) {
      setError("Please select a developer and a target role.");
      return;
    }

    setLoading(true);
    setError("");
    setCareerFit(null);
    setLearningPath([]);

    try {
      const [careerFitResponse, learningPathResponse] =
        await Promise.all([
          fetch(
            `${API_BASE_URL}/api/career-fit/${selectedDeveloper}/${selectedRole}`
          ),
          fetch(
            `${API_BASE_URL}/api/learning-path/${selectedDeveloper}/${selectedRole}`
          ),
        ]);

      if (!careerFitResponse.ok) {
        throw new Error("Career fit request failed");
      }

      if (!learningPathResponse.ok) {
        throw new Error("Learning path request failed");
      }

      const careerFitData = await careerFitResponse.json();
      const learningPathData = await learningPathResponse.json();

      setCareerFit(careerFitData);
      setLearningPath(learningPathData);
    } catch (err) {
      console.error("Career analysis error:", err);
      setError("Unable to analyze career fit.");
    } finally {
      setLoading(false);
    }
  }

  // ----------------------------------------
  // Reset results when developer changes
  // ----------------------------------------
  function handleDeveloperChange(event) {
    setSelectedDeveloper(event.target.value);
    setCareerFit(null);
    setLearningPath([]);
    setError("");
  }

  // ----------------------------------------
  // Reset results when role changes
  // ----------------------------------------
  function handleRoleChange(event) {
    setSelectedRole(event.target.value);
    setCareerFit(null);
    setLearningPath([]);
    setError("");
  }

  return (
    <div className="app">

      {/* ======================================
          HERO
      ====================================== */}
      <header className="hero">
  <div className="hero-content">

    <div className="hero-image">
      <img
        src="https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=1200&q=85"
        alt="Developer working with code"
      />
    </div>

    <div className="hero-copy">
      <div className="brand">CareerGraph</div>

      <h1>
        Explore your career path.
        <br />
        <span>Close your skill gaps.</span>
      </h1>

      <p>
        Discover how your current skills align with your target career role.
      </p>
    </div>

  </div>
</header>

      <main className="container">

        {/* ======================================
            CAREER ANALYSIS
        ====================================== */}
        <section className="analysis-card">

          <div className="section-heading">
            <span className="eyebrow">CAREER ANALYSIS</span>

            <h2>Find your career fit</h2>

            <p>
              Select your current profile and the role you're aiming for.
            </p>
          </div>

          <div className="selection-grid">

            {/* Developer */}
            <div className="field">
              <label htmlFor="developer">
                Your Profile
              </label>

              <select
                id="developer"
                value={selectedDeveloper}
                onChange={handleDeveloperChange}
              >
                <option value="">
                  Select a developer
                </option>

                {developers.map((developer) => (
                  <option
                    key={developer.id}
                    value={developer.id}
                  >
                    {developer.name}
                  </option>
                ))}
              </select>
            </div>

            {/* Target Role */}
            <div className="field">
              <label htmlFor="role">
                Target Role
              </label>

              <select
                id="role"
                value={selectedRole}
                onChange={handleRoleChange}
              >
                <option value="">
                  Select a target role
                </option>

                {roles.map((role) => (
                  <option
                    key={role.id}
                    value={role.id}
                  >
                    {role.name}
                  </option>
                ))}
              </select>
            </div>

          </div>

          <button
            className="analyze-button"
            onClick={analyzeCareerFit}
            disabled={loading}
          >
            {loading
              ? "Analyzing..."
              : "Analyze Career Fit"}
          </button>

          {error && (
            <div className="error-message">
              {error}
            </div>
          )}

        </section>

        {/* ======================================
            RESULTS
        ====================================== */}
        {careerFit && (
          <>
            {/* ==================================
                CAREER FIT RESULT
            ================================== */}
            <section className="results">

              <div className="results-header">

                <div>
                  <span className="eyebrow">
                    YOUR RESULT
                  </span>

                  <h2>
                    {careerFit.developer_name}
                    {" → "}
                    {careerFit.role_name}
                  </h2>

                  <p>
                    Here's how your current skill profile
                    compares with the requirements for this role.
                  </p>
                </div>

                <div className="score">
                  <strong>
                    {careerFit.match_percentage}%
                  </strong>

                  <span>
                    Match
                  </span>
                </div>

              </div>

              {/* Skill columns */}
              <div className="skill-columns">

                {/* Matched */}
                <div className="skill-card matched">

                  <h3>
                    ✓ Matched Skills
                  </h3>

                  {careerFit.matched_skills.length > 0 ? (
                    careerFit.matched_skills.map((skill) => (
                      <div
                        className="skill-item"
                        key={skill.id}
                      >
                        <span>
                          {skill.name}
                        </span>
                      </div>
                    ))
                  ) : (
                    <p>
                      No matched skills yet.
                    </p>
                  )}

                </div>

                {/* Missing */}
                <div className="skill-card missing">

                  <h3>
                    ○ Skills to Develop
                  </h3>

                  {careerFit.missing_skills.length > 0 ? (
                    careerFit.missing_skills.map((skill) => (
                      <div
                        className="skill-item"
                        key={skill.id}
                      >
                        <span>
                          {skill.name}
                        </span>
                      </div>
                    ))
                  ) : (
                    <p>
                      You have all the required skills.
                    </p>
                  )}

                </div>

              </div>

            </section>

            {/* ==================================
                LEARNING PATH
            ================================== */}
            {learningPath.length > 0 && (
              <section className="learning-section">

                <div className="section-heading">

                  <span className="eyebrow">
                    RECOMMENDED LEARNING PATH
                  </span>

                  <h2>
                    Close your skill gaps
                  </h2>

                  <p>
                    Build the skills required for your target role
                    with technology recommendations from the career graph.
                  </p>

                </div>

                <div className="learning-grid">

                  {learningPath.map((item) => (
                    <div
                      className="learning-card"
                      key={item.skill_id}
                    >

                      <div className="learning-card-header">

                        <div>
                          <h3>
                            {item.skill_name}
                          </h3>

                          <span>
                            {item.category}
                          </span>
                        </div>

                      </div>

                      <div className="technology-list">

                        {item.recommended_technologies &&
                        item.recommended_technologies.length > 0 ? (
                          item.recommended_technologies.map(
                            (technology) => (
                              <span
                                className="technology-pill"
                                key={technology.id}
                              >
                                {technology.name}
                              </span>
                            )
                          )
                        ) : (
                          <p className="no-technology">
                            No direct technology mapped yet.
                          </p>
                        )}

                      </div>

                    </div>
                  ))}

                </div>

              </section>
            )}

            {/* ==================================
                CAREER GRAPH
            ================================== */}
            <section className="graph-section">

              <div className="section-heading">

                <span className="eyebrow">
                  CAREER GRAPH
                </span>

                <h2>
                  Explore your career connections
                </h2>

                <p>
                  Follow the relationships between your profile,
                  projects, technologies, skills, roles, and companies.
                </p>

              </div>

              <GraphView
                developerId={selectedDeveloper}
                roleId={selectedRole}
                missingSkills={careerFit.missing_skills}
              />

            </section>

          </>
        )}

      </main>
    </div>
  );
}

export default App;