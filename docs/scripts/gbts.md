# GBTS Module Documentation

## Overview

The GBTS (Gaia-Bohm Thought Style) module implements a sophisticated conversation tree management system that guides agent interactions using a structured thought pattern approach. It combines philosophical principles with practical AI conversation management.

## Module Structure

```
gbts/
├── __init__.py
├── gbts.py                    # Core GBTS implementation
├── gaia_assit.py              # Gaia assistance module
├── eco_bot3D.js               # 3D visualization interface
└── visualizations/            # Visualization components
    ├── conversation_tree.js   # Tree structure visualization
    ├── dataPreparation.js     # Data preprocessing
    ├── gbtsVisualization.js   # Main visualization
    ├── interactivity.js       # User interaction handling
    ├── nodesAndLinks.js       # Node/link rendering
    ├── seedData.js            # Initial data structures
    ├── Frontend/              # Frontend components
    │   ├── __init__.py
    │   ├── dashboardRenderer.js    # Dashboard UI
    │   ├── growVisualization.js    # Growth animations
    │   └── userInterface.js        # UI components
    └── Backend/               # Backend processing
        ├── __init__.py
        ├── dataLayer/         # Data management
        │   ├── blockchainVerifier.js    # Blockchain verification
        │   ├── dataRetriever.js         # Data retrieval
        │   ├── dataVersioning.js        # Version control
        │   └── neuralMemoryGrid.js      # Memory grid
        └── processingLayer/   # Processing logic
            └── responseFormatter.js      # Response formatting
```

## Core Components

### 1. gbts.py

**Purpose:** Core GBTS implementation with conversation tree management.

**Key Classes:**

#### PromptTreeNode
Represents a node in the conversation tree.

```python
class PromptTreeNode:
    def __init__(self, role, message):
        """
        Initialize a prompt tree node.
        
        Args:
            role (str): Role identifier (user/assistant/system)
            message (str): Message content
        """
        self.role = role
        self.message = message
        self.children = []
```

**Methods:**
- `add_child(child_node)` - Add child node to tree
- `traverse(graph, parent_name, node_name)` - Traverse tree structure
- `to_dict()` - Convert to dictionary representation

#### PromptTree
Main tree structure for managing conversation flows.

**Features:**
- Hierarchical conversation management
- Branch creation and traversal
- Path finding through conversation
- Tree visualization preparation

**Usage:**
```python
from gbts.gbts import PromptTree, PromptTreeNode

# Create tree
tree = PromptTree()

# Add nodes
root = PromptTreeNode("system", "Welcome to Eco-Bot")
child = PromptTreeNode("user", "How can I recycle?")
root.add_child(child)
```

**Dependencies:**
- `json` - Data serialization
- `matplotlib` - Visualization
- `networkx` - Graph operations

### 2. gaia_assit.py

**Purpose:** Gaia assistance module providing environmental guidance.

**Key Features:**
- Environmental knowledge integration
- Context-aware assistance
- Integration with GBTS conversation flow

**Integration:**
Works alongside the main GBTS system to provide domain-specific assistance.

### 3. Visualization System

#### Frontend Components

##### dashboardRenderer.js

**Purpose:** Render dashboard interface for GBTS visualization.

**Key Features:**
- Real-time conversation tree display
- Interactive node exploration
- Metrics and statistics display

**Key Functions:**
- `renderDashboard(data)` - Render main dashboard
- `updateMetrics(metrics)` - Update statistics
- `refreshView()` - Refresh dashboard state

##### growVisualization.js

**Purpose:** Animated growth visualization of conversation trees.

**Key Features:**
- Organic growth animations
- Branch expansion effects
- Real-time tree evolution

**Animation Types:**
- Node appearance animations
- Branch growth transitions
- Interactive hover effects

##### userInterface.js

**Purpose:** User interface components and controls.

**Key Components:**
- Navigation controls
- Zoom/pan controls
- Node inspection panels
- Settings interface

#### Backend Components

##### Data Layer

###### blockchainVerifier.js

**Purpose:** Verify data integrity using blockchain principles.

**Key Features:**
- Data immutability verification
- Consensus validation
- Hash chain verification
- Timestamp validation

**Functions:**
```javascript
verifyBlock(block) {
  // Verify block integrity
  // Check hash chain
  // Validate consensus
  return isValid;
}
```

###### dataRetriever.js

**Purpose:** Retrieve data from various storage layers.

**Key Features:**
- Multi-source data retrieval
- Cache management
- Query optimization
- Batch retrieval

**Storage Sources:**
- Blockchain truth datacore
- P2P information nodes
- Neural memory grid
- Local cache

###### dataVersioning.js

**Purpose:** Manage data versions and evolution.

**Key Features:**
- Version tracking
- Historical data access
- Change logging
- Rollback capabilities

**Version Structure:**
```javascript
{
  id: "unique_id",
  version: "1.2.0",
  timestamp: "2023-10-29T12:00:00Z",
  data: {...},
  previousVersion: "1.1.0"
}
```

###### neuralMemoryGrid.js

**Purpose:** Neural network overlay for contextual memory.

**Key Features:**
- Contextual relationship mapping
- Semantic similarity
- Pattern recognition
- Memory consolidation

**Grid Structure:**
- Nodes: Data points
- Edges: Relationships
- Weights: Relevance scores
- Clusters: Topic groups

##### Processing Layer

###### responseFormatter.js

**Purpose:** Format responses for consistent output.

**Key Features:**
- Template-based formatting
- Content sanitization
- Multi-format output (JSON, text, HTML)
- Error message formatting

**Output Formats:**
```javascript
{
  success: true,
  data: {...},
  metadata: {
    timestamp: "...",
    version: "...",
    source: "..."
  }
}
```

### 4. Visualization Core

#### conversation_tree.js

**Purpose:** Core conversation tree visualization logic.

**Key Features:**
- D3.js-based tree rendering
- Interactive node manipulation
- Branch highlighting
- Path tracing

**Dependencies:**
- `d3` v7.8.5 - Data visualization
- Custom styling

**Rendering:**
```javascript
renderTree(treeData) {
  // Create SVG canvas
  // Render nodes
  // Draw connections
  // Add interactivity
}
```

#### gbtsVisualization.js

**Purpose:** Main GBTS visualization orchestrator.

**Key Features:**
- Complete visualization coordination
- Multiple view modes
- Export capabilities
- Real-time updates

**View Modes:**
- Tree view
- Graph view
- Timeline view
- 3D view (via eco_bot3D.js)

#### nodesAndLinks.js

**Purpose:** Node and link rendering primitives.

**Key Elements:**
- Node shapes and colors
- Link styles and arrows
- Labels and tooltips
- Selection indicators

**Node Types:**
- User nodes (blue)
- Assistant nodes (green)
- System nodes (orange)
- Tool nodes (purple)

#### dataPreparation.js

**Purpose:** Prepare data for visualization.

**Key Functions:**
- Data transformation
- Hierarchy creation
- Layout calculation
- Coordinate mapping

**Transformations:**
- Flatten nested structures
- Calculate tree layout
- Generate coordinates
- Apply physics simulation

#### interactivity.js

**Purpose:** Handle user interactions with visualizations.

**Interaction Types:**
- Node click/hover
- Zoom and pan
- Branch expansion/collapse
- Context menus

**Event Handlers:**
```javascript
handleNodeClick(node) {
  // Show node details
  // Highlight path
  // Update UI
}

handleZoom(event) {
  // Update zoom level
  // Recalculate visible nodes
  // Update rendering
}
```

#### seedData.js

**Purpose:** Initial data structures and examples.

**Contains:**
- Sample conversation trees
- Template structures
- Default configurations
- Test data

### 5. eco_bot3D.js

**Purpose:** 3D visualization of GBTS structures.

**Key Features:**
- Three.js-based 3D rendering
- Interactive 3D exploration
- Spatial conversation mapping
- VR-ready visualization

**Dependencies:**
- `three` v0.158.0 - 3D rendering

**3D Elements:**
- Nodes as spheres
- Connections as lines/tubes
- Camera controls
- Lighting effects

## Data Flow

### Conversation Creation Flow
1. User input received
2. GBTS creates new node
3. Node added to tree structure
4. Relationships calculated
5. Memory grid updated
6. Visualization refreshed

### Data Retrieval Flow
1. Query initiated
2. dataRetriever checks cache
3. Query blockchain if needed
4. Check P2P nodes
5. Consult neural memory grid
6. Format and return results

### Verification Flow
1. Data submitted
2. blockchainVerifier checks integrity
3. Consensus validation
4. Version tracking updated
5. Neural grid relationships updated
6. Confirmation returned

## Usage Examples

### Creating a Conversation Tree

```python
from gbts.gbts import PromptTree, PromptTreeNode

# Initialize tree
tree = PromptTree()

# Create conversation
system_node = PromptTreeNode("system", "I'm here to help with recycling")
user_node = PromptTreeNode("user", "How do I recycle plastic bottles?")
assistant_node = PromptTreeNode("assistant", "Rinse and place in blue bin")

# Build tree
tree.root = system_node
system_node.add_child(user_node)
user_node.add_child(assistant_node)

# Visualize
tree.visualize()
```

### Using the Visualization

```javascript
// Load visualization
import { renderTree } from './gbts/visualizations/gbtsVisualization.js';

// Prepare data
const treeData = {
  nodes: [...],
  links: [...]
};

// Render
renderTree(treeData, {
  width: 800,
  height: 600,
  interactive: true
});
```

### Blockchain Verification

```javascript
import { verifyBlock } from './gbts/visualizations/Backend/dataLayer/blockchainVerifier.js';

// Verify data
const block = {
  id: "block_123",
  data: {...},
  previousHash: "...",
  hash: "..."
};

const isValid = verifyBlock(block);
```

## Configuration

### Visualization Settings

```javascript
const config = {
  nodeRadius: 10,
  linkDistance: 100,
  colors: {
    user: "#3498db",
    assistant: "#2ecc71",
    system: "#e67e22"
  },
  animation: {
    duration: 500,
    easing: "ease-in-out"
  }
};
```

### Memory Grid Settings

```javascript
const gridConfig = {
  dimensions: 3,
  clusterThreshold: 0.7,
  decayRate: 0.1,
  consolidationInterval: 3600000  // 1 hour
};
```

## Testing

```bash
# Run conversation tree tests
npm test tests/conversation_tree.test.js
```

## Dependencies

```json
{
  "d3": "^7.8.5",
  "three": "^0.158.0",
  "@types/d3": "^7.4.3",
  "@types/three": "^0.159.0"
}
```

## Performance Considerations

1. **Large Trees**: Use virtualization for >1000 nodes
2. **Memory**: Implement cleanup for old nodes
3. **Rendering**: Use canvas for very large trees
4. **3D**: Reduce polygon count for performance

## Future Enhancements

- [ ] VR/AR visualization support
- [ ] Real-time collaborative editing
- [ ] Advanced search and filtering
- [ ] Export to various formats
- [ ] Machine learning integration for pattern detection

## Related Documentation

- [Agents Module](./agents.md)
- [Data Integration](./data-integration.md)
- [Architecture Overview](../ARCHITECTURE.md)
