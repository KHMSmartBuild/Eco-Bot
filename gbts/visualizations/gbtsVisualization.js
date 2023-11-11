// Description: This file contains the main visualization script.
/**
 * This file contains the main visualization script.
 * It is responsible for rendering the GBTS visualization on the webpage.
 * 
 * Author: [Kyle Morgan]
 * Version: 1.0
 * Date: [11/11/2023]
 */
// gbtsVisualization.js

import * as d3 from "../node_modules/d3";
import { createNodes, createLinks } from './nodesAndLinks.js';
import { addDrag, addToolTips, handleMouseOver, handleMouseOut, handleClick, showGBTS } from './interactivity.js';
import seedData from './seedData.js';

// Function to initialize the force-directed graph
function initializeForceGraph() {
    const data = seedData;
    const width = 800;
    const height = 600;

    // Append the SVG object to the body of the page
    const svgContainer = d3.select("#visualization")
        .append("svg")
        .attr("width", width)
        .attr("height", height);

    // Initialize the force simulation
    const simulation = d3.forceSimulation(data.nodes)
        .force("link", d3.forceLink(data.links).id(d => d.id))
        .force("charge", d3.forceManyBody())
        .force("center", d3.forceCenter(width / 2, height / 2));

    // Create the links and nodes using the provided functions
    const links = createLinks(svgContainer, data.links);
    const nodes = createNodes(svgContainer, data.nodes);

    // Add drag behavior to nodes
    nodes.call(addDrag(simulation));

    // Add tooltips to nodes
    addToolTips(nodes);

    // Add mouse event handlers
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

export { initializeForceGraph };
