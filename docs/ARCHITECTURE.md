# Eco-Bot System Architecture

## Overview

Eco-Bot is a multi-agent AI system focused on promoting ecological and environmental awareness. The system uses a Gaia-Bohm Thought Style (GBTS) guided prompt tree approach to facilitate communication between agents and their digital twins.

## System Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Eco-Bot System                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌─────────────────┐  │
│  │  Streamlit   │  │  API Gateway │  │  Security Layer │  │
│  │  Frontend    │◄─┤              │◄─┤                 │  │
│  └──────────────┘  └──────────────┘  └─────────────────┘  │
│         │                  │                                │
│         ▼                  ▼                                │
│  ┌──────────────────────────────────────────────────────┐  │
│  │           Agent Orchestration Layer                  │  │
│  │  ┌────────────┐  ┌────────────┐  ┌──────────────┐  │  │
│  │  │   Agents   │  │ Eco-Buddies│  │ Digital Twins│  │  │
│  │  └────────────┘  └────────────┘  └──────────────┘  │  │
│  └──────────────────────────────────────────────────────┘  │
│         │                  │                  │             │
│         ▼                  ▼                  ▼             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              GBTS (Thought Style Engine)             │  │
│  │  - Conversation Trees                                │  │
│  │  - Prompt Management                                 │  │
│  │  - Visualization Components                          │  │
│  └──────────────────────────────────────────────────────┘  │
│         │                                                   │
│         ▼                                                   │
│  ┌──────────────────────────────────────────────────────┐  │
│  │        Hybrid Decentralized Memory System            │  │
│  │  ┌──────────────┐  ┌──────────────┐  ┌────────────┐ │  │
│  │  │  Blockchain  │  │   P2P Nodes  │  │  Neural    │ │  │
│  │  │  Truth Core  │  │              │  │  Memory    │ │  │
│  │  │              │  │              │  │  Grid      │ │  │
│  │  └──────────────┘  └──────────────┘  └────────────┘ │  │
│  └──────────────────────────────────────────────────────┘  │
│         │                                                   │
│         ▼                                                   │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              Data & Integration Layer                │  │
│  │  - Database Operations                               │  │
│  │  - Notion Integration                                │  │
│  │  - Real-Time Processing                              │  │
│  └──────────────────────────────────────────────────────┘  │
│         │                                                   │
│         ▼                                                   │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                  ML Models Layer                     │  │
│  │  - Vision Model                                      │  │
│  │  - Audio Model                                       │  │
│  │  - GMA (Gaia Mind Architecture)                      │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Core Components

### 1. Agent System (`/agents`)
Multi-agent orchestration system using AutoGen framework.

**Key Files:**
- `agent_classes.py` - Core agent class definitions
- `assistants/` - Specialized assistant agents
- `config/` - LLM configuration and setup
- `tools/` - Agent tools and functions

**Responsibilities:**
- Agent lifecycle management
- Group chat coordination
- Task distribution
- Agent-to-agent communication

### 2. GBTS System (`/gbts`)
Gaia-Bohm Thought Style system for managing conversation trees and prompt flows.

**Key Files:**
- `gbts.py` - Core GBTS implementation
- `gaia_assit.py` - Gaia assistance module
- `visualizations/` - Visualization components
- `eco_bot3D.js` - 3D visualization interface

**Responsibilities:**
- Conversation tree management
- Prompt flow orchestration
- Thought pattern visualization
- Interactive conversation interfaces

### 3. Eco-Buddies (`/eco_buddies`)
User-facing chatbot and interaction layer.

**Key Files:**
- `Eco_Bot.py` - Main Eco-Bot vision implementation
- `Eco_Buddies.py` - Eco-Buddies orchestration
- `eco_chat.py` - Chat interface
- `eco_bot_mvp.js` - JavaScript MVP implementation

**Responsibilities:**
- User interaction handling
- Chat session management
- Vision-based interactions
- Logging and monitoring

### 4. Hybrid Decentralized Memory System

#### Blockchain Truth Datacore
Immutable storage for verified environmental facts and data.

**Location:** `gbts/visualizations/Backend/dataLayer/blockchainVerifier.js`

**Features:**
- Consensus-based verification
- Immutable fact storage
- Categorized retrieval
- Version tracking

#### P2P Information Nodes
Distributed storage for transient and agent-specific data.

**Features:**
- Decentralized data sharing
- Agent-specific storage
- Dynamic data exchange
- Network resilience

#### Neural Memory Grid
Contextual overlay providing relationships between data points.

**Location:** `gbts/visualizations/Backend/dataLayer/neuralMemoryGrid.js`

**Features:**
- Contextual linking
- Pattern recognition
- Semantic relationships
- Enhanced retrieval

### 5. API Gateway (`/APIGateway`)
Central routing and request handling layer.

**Key Files:**
- `gbts_handler.py` - GBTS request handler
- `queryHandler.js` - Query processing

**Responsibilities:**
- Request routing
- Response formatting
- API versioning
- Rate limiting

### 6. Data Layer (`/data`)
Database operations and external integrations.

**Key Components:**
- `database/utils/` - Database operations and connections
- `intergration/` - External service integrations (Notion, etc.)

**Responsibilities:**
- Data persistence
- External API integration
- Async data operations
- Connection pooling

### 7. ML Models (`/models`)
Machine learning model definitions and implementations.

**Key Files:**
- `Eco_Bot_model.py` - Main Eco-Bot model
- `computer_vision_model.py` - Vision capabilities
- `audio_model.py` - Audio processing
- `gma_model.py` - Gaia Mind Architecture model
- `DT_Model.py` - Digital Twin model

### 8. Streamlit Application (`/streamlit_app`)
Web-based user interface for monitoring and interaction.

**Key Components:**
- `eco_bot_main.py` - Main application entry point
- `pages/` - Application pages
- `assets/` - UI components and styles

**Pages:**
- Eco-Bot App
- MVP Interface
- Zero Waste Challenge
- GBTS Interaction
- Group Chat Screen
- Eco Game

### 9. Security Layer (`/SecurityLayer`)
Authentication and authorization services.

**Key Files:**
- `authenticator.js` - User authentication

### 10. Real-Time Processing (`/RealTimeData`)
Real-time data processing and streaming.

**Key Files:**
- `realTimeProcessor.js` - Real-time data handler

## Data Flow

### User Interaction Flow
1. User interacts via Streamlit UI or direct chat
2. Request passes through API Gateway
3. Security Layer validates request
4. Request routed to appropriate agent/buddy
5. GBTS system manages conversation flow
6. Agents process request using tools/models
7. Response formatted and returned
8. Memory system stores interaction

### Agent Communication Flow
1. Agent initiates communication
2. Digital Twin validates action
3. GBTS manages conversation tree
4. Message passed to target agent(s)
5. Group chat coordination (if multi-agent)
6. Response aggregation
7. Memory persistence

### Data Storage Flow
1. Data validation
2. Blockchain verification (for facts)
3. P2P node distribution
4. Neural grid relationship mapping
5. Database persistence
6. Version tracking

## Key Technologies

- **Python**: Core backend logic, agents, ML models
- **JavaScript**: Frontend, visualizations, 3D interfaces
- **AutoGen**: Multi-agent framework
- **OpenAI GPT**: Language model backend
- **Streamlit**: Web UI framework
- **D3.js**: Data visualization
- **Three.js**: 3D visualization
- **Notion API**: External integration
- **NetworkX**: Graph operations for conversation trees

## Configuration

### Environment Variables
- `OPENAI_API_KEY` - OpenAI API access
- `OPENAI_ORGANIZATION` - OpenAI organization ID
- Database connection strings
- Notion API credentials

### LLM Configuration
Located in `/agents/config/llm_config.py`

Default settings:
- Temperature: 0.72
- Max tokens: 1500
- Top P: 1
- Frequency penalty: 0.5

## Deployment

### Docker Support
Docker configuration available in `/docker` directory.

### Development Mode
```bash
streamlit run streamlit_app/eco_bot_main.py
```

## Testing

Test suite located in `/tests` directory:
- Agent retrieval tests
- Conversation tree tests
- LLM configuration tests
- Database model tests

Run tests:
```bash
pytest
```

## Future Enhancements

- Enhanced blockchain integration
- Expanded P2P network capabilities
- Advanced neural memory grid algorithms
- Additional ML model integrations
- Mobile application support

## References

- [Main README](../README.md)
- [Scripts Documentation](./scripts/README.md)
- [Modules Documentation](./modules/README.md)
- [API Documentation](./api/README.md)
