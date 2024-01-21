const seedData = {
    nodes: [
        { id: "Seed of Inquiry", group: 1 },
        { id: "Root 1", group: 2 },
        { id: "Root 2", group: 2 },
        { id: "Branch 1", group: 3 },
        { id: "Branch 2", group: 3 },
        { id: "Leaf 1", group: 4 },
        { id: "Leaf 2", group: 4 },
        { id: "Canopy 1", group: 5 },
        { id: "Canopy 2", group: 5 },
        { id: "Wisdom 1", group: 6 },
        { id: "Wisdom 2", group: 6 }
    ],
    links: [
        { source: "Seed of Inquiry", target: "Root 1" },
        { source: "Seed of Inquiry", target: "Root 2" },
        { source: "Seed of Inquiry", target: "Branch 1" },
        { source: "Seed of Inquiry", target: "Branch 2" },
        { source: "Branch 1", target: "Leaf 1" },
        { source: "Branch 2", target: "Leaf 2" },
        { source: "Leaf 1", target: "Canopy 1" },
        { source: "Leaf 2", target: "Canopy 2" },
        { source: "Canopy 1", target: "Wisdom 1" },
        { source: "Canopy 2", target: "Wisdom 2" }
    ]
};
export default seedData;

export {seedData}

