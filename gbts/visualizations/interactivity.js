// Description: This file contains functions for adding interactivity to the visualization.

// Import D3 modules
import * as d3 from 'https://cdn.jsdelivr.net/npm/d3@6/dist/d3.min.js';


// Singleton tooltip
const tooltip = d3.select("body").append("div")
    .attr("class", "tooltip")
    .style("opacity", 0);

function addDrag(simulation) {
    // Updated for D3 v6 event handling
    function dragstarted(event, d) {
        if (!event.active) simulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
    }

    function dragged(event, d) {
        d.fx = event.x;
        d.fy = event.y;
    }

    function dragended(event, d) {
        if (!event.active) simulation.alphaTarget(0);
        d.fx = null;
        d.fy = null;
    }

    return d3.drag()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended);
}

function addToolTips(node) {
    // Reuse the singleton tooltip for all nodes
    node.on("mouseover", (event, d) => {
        tooltip.transition()
            .duration(200)
            .style("opacity", 0.9);
        tooltip.html(d.id)
            .style("left", (event.pageX + 15) + "px")
            .style("top", (event.pageY - 35) + "px");
    })
    .on("mouseout", (event, d) => {
        tooltip.transition()
            .duration(500)
            .style("opacity", 0);
    });
}

function handleMouseOver(event, d) {
    // Add hover styling or logic here
    d3.select(this).classed('node-hover', true);
}

function handleMouseOut(event, d) {
    // Reset hover styling or logic here
    d3.select(this).classed('node-hover', false);
}

function handleClick(event, d) {
    // Implement click behavior, like expanding a node, or showing more information
    // For example, toggle node size on click
    const isLarge = d3.select(this).classed('node-large');
    d3.select(this)
        .classed('node-large', !isLarge)
        .attr('r', !isLarge ? 10 : 5); // Toggle radius size
}

function showGBTS() {
    // Implement logic to highlight GBTS nodes
    d3.selectAll(".node")
        .transition()
        .duration(500)
        .style("fill", d => d.group === 1 ? "red" : "black");
}

// Export the functions
export { addDrag, addToolTips, handleMouseOver, handleMouseOut, handleClick, showGBTS };
