// Assuming D3 is loaded globally from the CDN in your HTML

// Importing other modules
import { createNodes, createLinks } from './nodesAndLinks.js';
import { addDrag, addToolTips } from './interactivity.js';
import seedData from './seedData.js';

const data = seedData;
console.log("Script is running");
// Create SVG container
const svg = d3.select("body").append("svg")
    .attr("width", 800)
    .attr("height", 600);

// Initialize force simulation
const simulation = d3.forceSimulation(data.nodes)
    .force("link", d3.forceLink(data.links).id(d => d.id))
    .force("charge", d3.forceManyBody())
    .force("center", d3.forceCenter(400, 300));

// Create nodes and links using the modular functions
const nodes = createNodes(svg, data);
const links = createLinks(svg, data);

// Add drag behavior to nodes
nodes.call(addDrag(simulation));

// Add tooltips to nodes
addToolTips(nodes);

// Update positions on tick
simulation.on("tick", () => {
    links.attr("x1", d => d.source.x)
        .attr("y1", d => d.source.y)
        .attr("x2", d => d.target.x)
        .attr("y2", d => d.target.y);

    nodes.attr("cx", d => d.x)
        .attr("cy", d => d.y);
});

// Drag functions (these can be removed if you're using the addDrag function)
function dragstarted(d) {
    if (!d3.event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
}

function dragged(d) {
    d.fx = d3.event.x;
    d.fy = d3.event.y;
}

function dragended(d) {
    if (!d3.event.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
}
