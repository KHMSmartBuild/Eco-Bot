// Import D3
import * as d3 from 'd3';

// Define a color scale for node groups
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

    // Append interactive labels to each group
    nodeEnter.append('text')
        .text(d => d.id)
        .attr('x', 12)
        .attr('dy', '.35em')
        .style('display', 'none');

    nodeEnter.on('mouseover', function() {
        d3.select(this).select('text').style('display', null);
    })
    .on('mouseout', function() {
        d3.select(this).select('text').style('display', 'none');
    });

    return nodeEnter;
}

function createLinks(svg, links) {
    // For curved links
    const linkEnter = svg.append("g")
        .attr("class", "links")
        .selectAll("path")
        .data(links)
        .join("path")
        .attr("stroke", "#999")
        .attr("stroke-opacity", 0.6)
        .attr("fill", "none")
        .attr("marker-end", "url(#arrow)"); // Add this line for arrowheads

    // Define the path for each link
    linkEnter.attr('d', d => {
        const dx = d.target.x - d.source.x,
              dy = d.target.y - d.source.y,
              dr = Math.sqrt(dx * dx + dy * dy);
        return `M${d.source.x},${d.source.y}A${dr},${dr} 0 0,1 ${d.target.x},${d.target.y}`;
    });

    return linkEnter;
}

// Export the functions
export { createNodes, createLinks };
