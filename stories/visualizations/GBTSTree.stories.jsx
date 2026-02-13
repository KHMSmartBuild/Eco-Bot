import GBTSTree from './GBTSTree';
import { gbtsVisualizationData } from '../data/storyData';

/**
 * GBTSTree component visualizes the Gaia-Bohm Thought Style conversation structure.
 * It renders an interactive tree diagram showing the flow of conversation through
 * different GBTS stages.
 */
export default {
  title: 'Visualizations/GBTSTree',
  component: GBTSTree,
  parameters: {
    layout: 'centered',
    docs: {
      description: {
        component: `
# GBTS Tree Visualization

The GBTSTree component renders an interactive visualization of the Gaia-Bohm Thought Style (GBTS) conversation structure.

## About GBTS

The Gaia-Bohm Thought Style is a unique approach to conversations that follows a tree-like structure:

1. **Seed of Inquiry** 🌱 - The initial question or topic that starts the exploration
2. **Branches of Understanding** 🌿 - Related sub-topics that emerge from the seed
3. **Leaves of Application** 🍃 - Practical applications of the knowledge
4. **Roots of Connection (Infranodes)** 🌳 - Deep underlying connections to other subjects
5. **Forest of Exploration** 🌲 - Broader topics that intertwine with the primary topic
6. **Canopy of Synthesis** 🌴 - Integration of insights into cohesive understanding
7. **Harvest of Wisdom** 🌾 - Key insights gathered from the exploration

## Data Structure

The component accepts data in the following format:

\`\`\`json
{
  "nodes": [
    { "id": "Seed of Inquiry", "group": 1 },
    { "id": "Branch 1", "group": 3 }
  ],
  "links": [
    { "source": "Seed of Inquiry", "target": "Branch 1" }
  ]
}
\`\`\`

## JSON Data Management

Data for this visualization is managed through the \`stories/data/storyData.js\` module which provides:
- Pre-defined GBTS prompt structures
- Sample visualization data
- Data validation utilities
- Transformation functions

\`\`\`javascript
import { gbtsVisualizationData, validateGBTSData } from './storyData';

// Validate data before use
const result = validateGBTSData(myData);
if (result.valid) {
  // Use the data
}
\`\`\`
        `,
      },
    },
  },
  tags: ['autodocs'],
  argTypes: {
    data: {
      control: 'object',
      description: 'Data object with nodes and links arrays',
    },
    width: {
      control: { type: 'range', min: 400, max: 1200, step: 50 },
      description: 'Width of the visualization',
    },
    height: {
      control: { type: 'range', min: 300, max: 800, step: 50 },
      description: 'Height of the visualization',
    },
    onNodeClick: {
      action: 'nodeClicked',
      description: 'Callback when a node is clicked',
    },
  },
};

// Default GBTS Tree with standard data
export const Default = {
  args: {
    data: gbtsVisualizationData,
    width: 600,
    height: 400,
  },
};

// Large visualization
export const LargeVisualization = {
  args: {
    data: gbtsVisualizationData,
    width: 800,
    height: 600,
  },
};

// Compact visualization
export const CompactVisualization = {
  args: {
    data: gbtsVisualizationData,
    width: 400,
    height: 300,
  },
};

// Simple tree with minimal nodes
export const SimpleTree = {
  args: {
    data: {
      nodes: [
        { id: "Seed", group: 1 },
        { id: "Branch A", group: 3 },
        { id: "Branch B", group: 3 },
        { id: "Wisdom", group: 6 },
      ],
      links: [
        { source: "Seed", target: "Branch A" },
        { source: "Seed", target: "Branch B" },
        { source: "Branch A", target: "Wisdom" },
        { source: "Branch B", target: "Wisdom" },
      ],
    },
    width: 500,
    height: 350,
  },
  parameters: {
    docs: {
      description: {
        story: 'A simplified tree structure showing the basic flow from seed to wisdom.',
      },
    },
  },
};

// Complex tree with many nodes
export const ComplexTree = {
  args: {
    data: {
      nodes: [
        { id: "Seed of Inquiry", group: 1 },
        { id: "Root 1", group: 2 },
        { id: "Root 2", group: 2 },
        { id: "Root 3", group: 2 },
        { id: "Branch 1", group: 3 },
        { id: "Branch 2", group: 3 },
        { id: "Branch 3", group: 3 },
        { id: "Leaf 1", group: 4 },
        { id: "Leaf 2", group: 4 },
        { id: "Leaf 3", group: 4 },
        { id: "Leaf 4", group: 4 },
        { id: "Canopy 1", group: 5 },
        { id: "Canopy 2", group: 5 },
        { id: "Wisdom 1", group: 6 },
        { id: "Wisdom 2", group: 6 },
        { id: "Wisdom 3", group: 6 },
      ],
      links: [
        { source: "Seed of Inquiry", target: "Root 1" },
        { source: "Seed of Inquiry", target: "Root 2" },
        { source: "Seed of Inquiry", target: "Root 3" },
        { source: "Root 1", target: "Branch 1" },
        { source: "Root 2", target: "Branch 2" },
        { source: "Root 3", target: "Branch 3" },
        { source: "Branch 1", target: "Leaf 1" },
        { source: "Branch 1", target: "Leaf 2" },
        { source: "Branch 2", target: "Leaf 3" },
        { source: "Branch 3", target: "Leaf 4" },
        { source: "Leaf 1", target: "Canopy 1" },
        { source: "Leaf 3", target: "Canopy 2" },
        { source: "Canopy 1", target: "Wisdom 1" },
        { source: "Canopy 1", target: "Wisdom 2" },
        { source: "Canopy 2", target: "Wisdom 3" },
      ],
    },
    width: 700,
    height: 500,
  },
  parameters: {
    docs: {
      description: {
        story: 'A complex tree with multiple branches and paths showing rich conversation exploration.',
      },
    },
  },
};

// Empty state
export const EmptyState = {
  args: {
    data: null,
    width: 500,
    height: 350,
  },
  parameters: {
    docs: {
      description: {
        story: 'Shows the empty state when no data is provided.',
      },
    },
  },
};
