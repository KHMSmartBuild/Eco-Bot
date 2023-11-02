const svg = d3.select("#avatar-container");

const avatar = svg.append("g")
    .attr("class", "eco-bot");

const image = avatar.append("image")
    .attr("xlink:href", "streamlit_app/assets/images/Eco_bot-1.png")
    .attr("x", 0)
    .attr("y", 0)
    .attr("width", 100)
    .attr("height", 100);

// Attach nodes to different parts of the image
const arms = avatar.append("g")
    .attr("class", "arms");
// Add arm elements to the "arms" group

const leaves = avatar.append("g")
    .attr("class", "leaves");
// Add leaf elements to the "leaves" group

// Hover effect: Scale the Eco-bot character
avatar.on("mouseover", function(event) {
    d3.select(this).transition()
        .duration(200)
        .attr("transform", "scale(1.2)");
})
.on("mouseout", function(event) {
    d3.select(this).transition()
        .duration(200)
        .attr("transform", "scale(1)");
});

// Click effect: Rotate the Eco-bot character
avatar.on("click", function(event) {
    d3.select(this).transition()
        .duration(500)
        .attr("transform", "rotate(360)");
});

// Reset rotation after animation
avatar.on("end", function(event) {
    d3.select(this).attr("transform", "");
});
