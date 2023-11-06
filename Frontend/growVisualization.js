// This function simulates an agent adding new nodes and links to the data
function growVisualization(seedData) {
    // Define a new node and link
    const newNode = { id: `Node ${seedData.nodes.length + 1}`, group: 1 };
    const newLink = { source: "Seed of Inquiry", target: newNode.id };

    // Add the new node and link to the seed data
    seedData.nodes.push(newNode);
    seedData.links.push(newLink);

    // Update the visualization with the new data
    updateVisualization(seedData);
}

// This function updates the D3 visualization with new data
function updateVisualization(data) {
    // Assuming you have functions to update nodes and links
    // You would need to implement these to handle entering and exiting elements
    updateNodes(data.nodes);
    updateLinks(data.links);

    // Restart the simulation if necessary
    simulation.nodes(data.nodes);
    simulation.force("link").links(data.links);
    simulation.alpha(0.3).restart();
}

// Call growVisualization periodically to simulate data growth
setInterval(() => {
    growVisualization(seedData);
}, 5000); // Update every 5 seconds
