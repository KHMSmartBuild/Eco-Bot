// Description: This file contains functions for adding interactivity to the visualization.

// Import D3 modules
import * as d3 from 'd3';

// Function to add drag behavior to nodes
function addDrag(simulation) {
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

    return d3.drag()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended);
}

// Function to add tooltips to nodes
function addToolTips(node) {
    const tooltip = d3.select("body").append("div")
        .attr("class", "tooltip")
        .style("opacity", 0);

    node.on("mouseover", function(d) {
        tooltip.transition()
            .duration(200)
            .style("opacity", .9);
        tooltip.html(d.id)
            .style("left", (d3.event.pageX + 5) + "px")
            .style("top", (d3.event.pageY - 28) + "px");
    })
    .on("mouseout", function(d) {
        tooltip.transition()
            .duration(500)
            .style("opacity", 0);
    });
}


function handleMouseOver(event, d) {
    // Update for D3 v6 event handling
    tooltip.transition()
        .duration(200)
        .style("opacity", .9);
    tooltip.html(d.id)
        .style("left", (event.pageX + 5) + "px")
        .style("top", (event.pageY - 28) + "px");

    // Change style
    d3.select(this)
        .style("fill", "red");
}


function handleMouseOut(event, d) {
    // Reset any styles set on mouseover
    tooltip.transition()
        .duration(500)
        .style("opacity", 0);
    d3.select(this)
        .style("fill", null);
}


function handleClick(d) {
    // Implement click behavior, like expanding a node, or showing more information
    d3.select(this)
        .transition()
        .duration(500)
        .attr("r", 10); // Increase the radius of the node

    // Example: Show more information in a tooltip
    const tooltip = d3.select("body").append("div")
        .attr("class", "tooltip")
        .style("opacity", 0);

    tooltip.transition()
        .duration(200)
        .style("opacity", .9);
    tooltip.html("Additional information")
        .style("left", (d3.event.pageX + 5) + "px")
        .style("top", (d3.event.pageY - 28) + "px");
    }

    // add functions for main script to use
    // add show gbts function this highlights the nodes from the gbts initialization
function showGBTS() {
    d3.selectAll("circle")
        .style("fill", function(d) {
            if (d.group == 1) {
                return "red";
            } else {
                return "black";
            }
        });
    }


// Export the functions
export { addDrag, addToolTips, handleMouseOver, handleMouseOut, handleClick, showGBTS };
