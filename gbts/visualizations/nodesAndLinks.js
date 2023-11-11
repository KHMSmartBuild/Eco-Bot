// Import D3
import * as d3 from 'd3';

// Define a color scale for node groups if not yet defined
const colorScale = d3.scaleOrdinal(d3.schemeCategory10);

function createNodes(svg, nodes) {
    // Append groups for nodes
    const nodeEnter = svg.append("g")
        .attr("class", "nodes")
        .selectAll(".node")
        .data(nodes)
        .join('g')
        .attr('class', 'node');

    // Append circles to each group
    nodeEnter.append('circle')
        .attr('r', 5)
        .attr('fill', d => colorScale(d.group));

    // Append labels to each group
    nodeEnter.append('text')
        .text(d => d.id)
        .attr('x', 12)
        .attr('dy', '.35em');

    return nodeEnter;
}

function createLinks(svg, links) {
    // For straight links:
    // const linkEnter = svg.append("g")
    //     .attr("class", "links")
    //     .selectAll("line")
    //     .data(links)
    //     .join("line")
    //     .attr("stroke", "#999")
    //     .attr("stroke-opacity", 0.6);

    // For curved links:
    const linkEnter = svg.append("g")
        .attr("class", "links")
        .selectAll("path")
        .data(links)
        .join("path")
        .attr("stroke", "#999")
        .attr("stroke-opacity", 0.6)
        .attr('d', d => {
            // Placeholder values, you will need to replace these with actual coordinates
            const sourceX = d.source.x;
            const sourceY = d.source.y;
            const targetX = d.target.x;
            const targetY = d.target.y;
            // Define the control point for the curve
            const controlX = (sourceX + targetX) / 2;
            const controlY = (sourceY + targetY) / 2 - 50; // Adjust the -50 to set the height of the curve
            return `M${sourceX},${sourceY} Q${controlX},${controlY} ${targetX},${targetY}`;
        });

    return linkEnter;
}

// Export the functions so they can be used in the main visualization script
export { createNodes, createLinks};
