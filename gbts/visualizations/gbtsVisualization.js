/**
 * This file contains the main visualization script for rendering the GBTS visualization on the webpage.
 * It utilizes a modular approach, separating the concerns such as data handling, interactivity, and rendering.
 * 
 * Author: [Kyle Morgan]
 * Version: 1.1
 * Date: [2023-11-11]
 * Enhancements: Added comments, responsive SVG, error handling, and accessibility improvements.
 */

// gbtsVisualization.js

// Import D3 modules
import * as d3 from '../../node_modules/d3/dist/d3.js';
// Import necessary modules
import { createNodes, createLinks } from './nodesAndLinks.js';

// Function to initialize the force-directed graph
function initializeForceGraph() {
    const data = seedData; // Assuming seedData is defined elsewhere
    // Making the SVG responsive to window size
    const width = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
    const height = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;

    // Error handling for data loading
    if (!data || !Array.isArray(data.nodes) || !Array.isArray(data.links) || data.nodes.length === 0 || data.links.length === 0) {
        throw new Error('GBTS Visualization: Invalid or missing data'); // Throw an error if data is not correct
    }

    // Append the SVG object to the body of the page
    const svgContainer = d3.select("#visualization");
    if (svgContainer.empty()) {
        throw new Error('GBTS Visualization: Element with id "visualization" not found'); // Throw an error if element is not found
    }

    svgContainer.append("svg")
        // Add viewBox and preserveAspectRatio for responsiveness
        .attr("viewBox", `0 0 ${width} ${height}`)
        .attr("preserveAspectRatio", "xMidYMid meet")
        // Add ARIA role for accessibility
        .attr("role", "img")
        .attr("aria-label", "GBTS Conversation Visualization");

    // Initialize the force simulation
    const simulation = d3.forceSimulation(data.nodes)
        .force("link", d3.forceLink(data.links).id(d => d.id))
        .force("charge", d3.forceManyBody())
        .force("center", d3.forceCenter(width / 2, height / 2));

    // Create the links and nodes using the provided functions
    const links = createLinks(svgContainer, data.links);
    const nodes = createNodes(svgContainer, data.nodes);

    // Add drag behavior to nodes
    nodes.call(d3.drag().on("drag", drag));

    // Add tooltips to nodes
    nodes.on('mouseover', handleMouseOver)
        .on('mouseout', handleMouseOut)
        .on('click', handleClick);

    // Update the positions of the nodes and links on each simulation 'tick'
    simulation.on("tick", () => {
        links.attr("x1", d => d.source.x)
            .attr("y1", d => d.source.y)
            .attr("x2", d => d.target.x)
            .attr("y2", d => d.target.y);

        nodes.attr("cx", d => d.x)
            .attr("cy", d => d.y);
    });
}

// Add an event listener for the 'Show GBTS' button
d3.select('#show-gbts').on('click', showGBTS);

// Call the function to initialize the graph
initializeForceGraph();
