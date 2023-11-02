// Import D3 (assuming you're using ES6 modules)
import * as d3 from 'd3';

// Function to create nodes
function createNodes(svg, data) {
    return svg.append("g")
        .selectAll("circle")
        .data(data.nodes)
        .enter().append("circle")
        .attr("r", 5) // Radius of the circle
        .attr("fill", d => d.group); // Fill color based on the group
}

// Function to create links
function createLinks(svg, data) {
    return svg.append("g")
        .selectAll("line")
        .data(data.links)
        .enter().append("line")
        .attr("stroke", "#999") // Color of the link
        .attr("stroke-opacity", 0.6); // Opacity of the link
}

// Export the functions so they can be used in the main visualization script
export { createNodes, createLinks };
