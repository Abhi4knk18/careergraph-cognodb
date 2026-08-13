import { useEffect, useMemo, useState } from "react";
import {
  ReactFlow,
  Background,
  Controls,
  MiniMap,
  Position,
} from "@xyflow/react";
import dagre from "@dagrejs/dagre";
import "@xyflow/react/dist/style.css";
const API_BASE_URL =
  import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";
const NODE_WIDTH = 190;
const NODE_HEIGHT = 80;

function getNodeStyle(type, isMissingSkill) {
  if (isMissingSkill) {
    return {
      border: "2px solid #ef4444",
      background: "#fff1f2",
      color: "#dc2626",
    };
  }

  switch (type) {
    case "Developer":
      return {
        border: "2px solid #7c3aed",
        background: "#ffffff",
        color: "#111827",
      };

    case "Role":
      return {
        border: "2px solid #2563eb",
        background: "#ffffff",
        color: "#111827",
      };

    case "Skill":
      return {
        border: "2px solid #16a34a",
        background: "#ffffff",
        color: "#111827",
      };

    case "Technology":
      return {
        border: "2px solid #f97316",
        background: "#ffffff",
        color: "#111827",
      };

    case "Project":
      return {
        border: "2px solid #ec4899",
        background: "#ffffff",
        color: "#111827",
      };

    case "Company":
      return {
        border: "2px solid #0891b2",
        background: "#ffffff",
        color: "#111827",
      };

    default:
      return {
        border: "1px solid #cbd5e1",
        background: "#ffffff",
        color: "#111827",
      };
  }
}

function GraphView({
  developerId,
  roleId,
  missingSkills = [],
}) {
  const [graph, setGraph] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  /*
   * ---------------------------------------------------------
   * Load graph from backend
   * ---------------------------------------------------------
   */

  useEffect(() => {
    async function loadGraph() {
      try {
        setLoading(true);
        setError("");

        const response = await fetch(
          `${API_BASE_URL}/api/career-graph/${developerId}/${roleId}`
        );

        if (!response.ok) {
          throw new Error("Failed to load graph");
        }

        const data = await response.json();

        setGraph(data);
      } catch (err) {
        console.error("CareerGraph error:", err);

        setError(
          "Unable to load CareerGraph visualization."
        );
      } finally {
        setLoading(false);
      }
    }

    if (developerId && roleId) {
      loadGraph();
    }
  }, [developerId, roleId]);

  /*
   * ---------------------------------------------------------
   * Build React Flow graph using Dagre
   * ---------------------------------------------------------
   */

  const { nodes, edges } = useMemo(() => {
    if (!graph) {
      return {
        nodes: [],
        edges: [],
      };
    }

    const missingSkillIds = new Set(
      missingSkills.map((skill) => skill.id)
    );

    /*
     * Dagre graph
     */

    const dagreGraph = new dagre.graphlib.Graph();

    dagreGraph.setDefaultEdgeLabel(() => ({}));

    dagreGraph.setGraph({
      rankdir: "TB",
      ranksep: 100,
      nodesep: 80,
      edgesep: 40,
      marginx: 40,
      marginy: 40,
    });

    /*
     * Add nodes
     */

    graph.nodes.forEach((node) => {
      dagreGraph.setNode(node.id, {
        width: NODE_WIDTH,
        height: NODE_HEIGHT,
      });
    });

    /*
     * Add relationships
     */

    graph.relationships.forEach((relationship) => {
      dagreGraph.setEdge(
        relationship.source,
        relationship.target
      );
    });

    /*
     * Calculate layout
     */

    dagre.layout(dagreGraph);

    /*
     * Convert Neo4j nodes into React Flow nodes
     */

    const flowNodes = graph.nodes.map((node) => {
      const position = dagreGraph.node(node.id);

      const isMissingSkill =
        node.type === "Skill" &&
        missingSkillIds.has(node.id);

      const style = getNodeStyle(
        node.type,
        isMissingSkill
      );

      return {
        id: node.id,

        position: {
          x: position.x - NODE_WIDTH / 2,
          y: position.y - NODE_HEIGHT / 2,
        },

        sourcePosition: Position.Bottom,
        targetPosition: Position.Top,

        className: [
          `node-${node.type.toLowerCase()}`,
          isMissingSkill ? "node-skill-gap" : "",
        ]
          .filter(Boolean)
          .join(" "),

        style: {
          width: NODE_WIDTH,
          minHeight: NODE_HEIGHT,
          borderRadius: 12,
          padding: "10px 14px",
          boxSizing: "border-box",
          boxShadow:
            "0 4px 12px rgba(15, 23, 42, 0.08)",
          ...style,
        },

        data: {
          nodeType: node.type,
          isMissingSkill,
          label: (
            <div
              style={{
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                justifyContent: "center",
                height: "100%",
                textAlign: "center",
                gap: "5px",
              }}
            >
              <strong
                style={{
                  fontSize: "14px",
                  lineHeight: "1.2",
                }}
              >
                {node.label}
              </strong>

              <small
                style={{
                  fontSize: "11px",
                  opacity: 0.7,
                }}
              >
                {isMissingSkill
                  ? "Skill Gap"
                  : node.type}
              </small>
            </div>
          ),
        },
      };
    });

    /*
     * Convert Neo4j relationships into React Flow edges
     */

    const flowEdges = graph.relationships.map(
      (relationship) => ({
        id: relationship.id,

        source: relationship.source,

        target: relationship.target,

        label: relationship.type,

        type: "smoothstep",

        animated: false,

        style: {
          stroke: "#94a3b8",
          strokeWidth: 1.5,
        },

        labelStyle: {
          fontSize: 12,
          fontWeight: 700,
          fill: "#475569",
        },

        labelBgStyle: {
          fill: "#ffffff",
          fillOpacity: 0.95,
        },

        labelBgPadding: [5, 3],

        labelBgBorderRadius: 4,
      })
    );

    return {
      nodes: flowNodes,
      edges: flowEdges,
    };
  }, [graph, missingSkills]);

  /*
   * ---------------------------------------------------------
   * Loading
   * ---------------------------------------------------------
   */

  if (loading) {
    return (
      <div className="graph-state">
        Loading CareerGraph...
      </div>
    );
  }

  /*
   * ---------------------------------------------------------
   * Error
   * ---------------------------------------------------------
   */

  if (error) {
    return (
      <div className="graph-state error">
        {error}
      </div>
    );
  }

  /*
   * ---------------------------------------------------------
   * No graph
   * ---------------------------------------------------------
   */

  if (!graph) {
    return null;
  }

  /*
   * ---------------------------------------------------------
   * Render
   * ---------------------------------------------------------
   */

  return (
    <div className="graph-wrapper">

      {/* Legend */}

      <div className="graph-legend">

        <span className="legend-developer">
          Developer
        </span>

        <span className="legend-role">
          Role
        </span>

        <span className="legend-skill">
          Skill
        </span>

        <span className="legend-skill-gap">
          Skill Gap
        </span>

        <span className="legend-technology">
          Technology
        </span>

        <span className="legend-project">
          Project
        </span>

        <span className="legend-company">
          Company
        </span>

      </div>

      {/* Graph */}

      <div
        className="graph-container">
        <ReactFlow
          nodes={nodes}
          edges={edges}
          onNodesChange={() => {}}
          fitView
          fitViewOptions={{
            padding: 0.08,
            minZoom: 0.3,
            maxZoom: 1.2,
          }}
          attributionPosition="bottom-left"
          nodesConnectable={false}
          nodesDraggable={true}
          elementsSelectable={true}
          defaultEdgeOptions={{
            type: "smoothstep",
          }}
        >

          <Background />

          <Controls
  position="bottom-left"
/>


<MiniMap
  position="bottom-right"
  pannable
  zoomable
  nodeColor="#94a3b8"
  nodeStrokeColor="#475569"
  nodeStrokeWidth={2}
/>
        </ReactFlow>
      </div>

    </div>
  );
}

export default GraphView;