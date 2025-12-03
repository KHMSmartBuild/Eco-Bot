import React, { useRef } from 'react';
import PropTypes from 'prop-types';
import './GBTSTree.css';

/**
 * GBTSTree - Interactive visualization of the Gaia-Bohm Thought Style tree structure
 * Renders nodes and links representing conversation flow through GBTS stages
 */
function GBTSTree({ data, width, height, onNodeClick }) {
  const containerRef = useRef(null);

  const nodeColors = {
    1: '#4CAF50', // Seed - Green
    2: '#8B4513', // Roots - Brown
    3: '#228B22', // Branches - Forest Green
    4: '#90EE90', // Leaves - Light Green
    5: '#006400', // Canopy - Dark Green
    6: '#FFD700', // Wisdom - Gold
  };

  const getNodePosition = (index, total) => {
    const angle = (index / total) * 2 * Math.PI - Math.PI / 2;
    const radius = Math.min(width, height) / 3;
    return {
      x: width / 2 + radius * Math.cos(angle),
      y: height / 2 + radius * Math.sin(angle),
    };
  };

  const handleNodeClick = (node) => {
    if (onNodeClick) {
      onNodeClick(node);
    }
  };

  if (!data || !data.nodes || !data.links) {
    return (
      <div className="gbts-tree-error" style={{ width, height }}>
        <p>No data available for visualization</p>
      </div>
    );
  }

  const nodePositions = {};
  data.nodes.forEach((node, index) => {
    nodePositions[node.id] = getNodePosition(index, data.nodes.length);
  });

  return (
    <div ref={containerRef} className="gbts-tree-container" style={{ width, height }}>
      <svg width={width} height={height} className="gbts-tree-svg">
        {/* Render links */}
        <g className="links">
          {data.links.map((link, index) => {
            const sourcePos = nodePositions[link.source];
            const targetPos = nodePositions[link.target];
            if (!sourcePos || !targetPos) return null;
            
            return (
              <line
                key={`link-${link.source}-${link.target}`}
                x1={sourcePos.x}
                y1={sourcePos.y}
                x2={targetPos.x}
                y2={targetPos.y}
                className="gbts-link"
                stroke="#999"
                strokeWidth="2"
                strokeOpacity="0.6"
              />
            );
          })}
        </g>
        
        {/* Render nodes */}
        <g className="nodes">
          {data.nodes.map((node, index) => {
            const pos = nodePositions[node.id];
            return (
              <g
                key={`node-${index}`}
                className="gbts-node"
                transform={`translate(${pos.x}, ${pos.y})`}
                onClick={() => handleNodeClick(node)}
                style={{ cursor: 'pointer' }}
              >
                <circle
                  r={20}
                  fill={nodeColors[node.group] || '#4CAF50'}
                  stroke="#fff"
                  strokeWidth="2"
                  className="node-circle"
                />
                <text
                  dy=".35em"
                  textAnchor="middle"
                  className="node-label"
                  fill="#fff"
                  fontSize="10"
                >
                  {node.id.length > 10 ? node.id.substring(0, 8) + '...' : node.id}
                </text>
              </g>
            );
          })}
        </g>
      </svg>
      
      {/* Legend */}
      <div className="gbts-legend">
        <h4>GBTS Stages</h4>
        <div className="legend-item">
          <span className="legend-color" style={{ backgroundColor: nodeColors[1] }}></span>
          <span>Seed of Inquiry</span>
        </div>
        <div className="legend-item">
          <span className="legend-color" style={{ backgroundColor: nodeColors[2] }}></span>
          <span>Roots of Connection</span>
        </div>
        <div className="legend-item">
          <span className="legend-color" style={{ backgroundColor: nodeColors[3] }}></span>
          <span>Branches of Understanding</span>
        </div>
        <div className="legend-item">
          <span className="legend-color" style={{ backgroundColor: nodeColors[4] }}></span>
          <span>Leaves of Application</span>
        </div>
        <div className="legend-item">
          <span className="legend-color" style={{ backgroundColor: nodeColors[5] }}></span>
          <span>Canopy of Synthesis</span>
        </div>
        <div className="legend-item">
          <span className="legend-color" style={{ backgroundColor: nodeColors[6] }}></span>
          <span>Harvest of Wisdom</span>
        </div>
      </div>
    </div>
  );
}

GBTSTree.propTypes = {
  /** Data object containing nodes and links arrays */
  data: PropTypes.shape({
    nodes: PropTypes.arrayOf(
      PropTypes.shape({
        id: PropTypes.string.isRequired,
        group: PropTypes.number,
        description: PropTypes.string,
      })
    ).isRequired,
    links: PropTypes.arrayOf(
      PropTypes.shape({
        source: PropTypes.string.isRequired,
        target: PropTypes.string.isRequired,
      })
    ).isRequired,
  }).isRequired,
  /** Width of the visualization in pixels */
  width: PropTypes.number,
  /** Height of the visualization in pixels */
  height: PropTypes.number,
  /** Callback when a node is clicked */
  onNodeClick: PropTypes.func,
};

GBTSTree.defaultProps = {
  width: 600,
  height: 400,
};

export default GBTSTree;
