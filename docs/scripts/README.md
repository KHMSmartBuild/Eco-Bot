# Scripts Documentation

This directory contains documentation for all scripts in the Eco-Bot project.

## Overview

The Eco-Bot project contains 88 script files across various modules. This documentation provides detailed information about each script's purpose, functionality, and usage.

## Directory Structure

### Core Modules

#### 1. [Agents Module](./agents.md)
Multi-agent system implementation using AutoGen framework.
- Agent class definitions
- Assistant agents
- Configuration and setup
- Agent tools and functions

#### 2. [GBTS Module](./gbts.md)
Gaia-Bohm Thought Style system for conversation management.
- Conversation tree implementation
- Visualization components
- Frontend and backend layers
- Data processing

#### 3. [Eco-Buddies Module](./eco-buddies.md)
User-facing chatbot and interaction components.
- Main Eco-Bot implementation
- Chat interfaces
- Vision capabilities
- Utility functions

#### 4. [Models Module](./models.md)
Machine learning model definitions.
- Eco-Bot models
- Vision models
- Audio processing models
- Digital Twin models

#### 5. [API Gateway](./api-gateway.md)
API routing and request handling.
- GBTS handlers
- Query processors

#### 6. [Data Integration](./data-integration.md)
Database and external service integrations.
- Database operations
- Notion integration
- Async processing

#### 7. [Streamlit Application](./streamlit-app.md)
Web-based user interface.
- Main application
- Page components
- Assets and styling

#### 8. [Security Layer](./security.md)
Authentication and authorization.
- User authentication
- Access control

#### 9. [Utility Scripts](./utilities.md)
Helper scripts and utilities.
- File structure updater
- Requirements management
- Notion updates
- Development tools

## Quick Reference

### Python Scripts
Total: ~60 Python files

Key entry points:
- `streamlit_app/eco_bot_main.py` - Main Streamlit application
- `eco_buddies/Eco_Bot.py` - Eco-Bot vision implementation
- `agents/agent_classes.py` - Agent system core
- `gbts/gbts.py` - GBTS system core

### JavaScript Scripts
Total: ~25 JavaScript files

Key entry points:
- `gbts/eco_bot3D.js` - 3D visualization
- `gbts/visualizations/gbtsVisualization.js` - GBTS visualization
- `eco_buddies/eco_bot_mvp.js` - MVP implementation

### Shell Scripts
Total: ~3 shell files

Utility scripts for development and deployment.

## Script Categories

### 1. Application Entry Points
Scripts that serve as main entry points for applications:
- `streamlit_app/eco_bot_main.py`
- `eco_buddies/Eco_Bot.py`
- `eco_buddies/eco_chat.py`

### 2. Core Logic
Core business logic implementations:
- `agents/agent_classes.py`
- `gbts/gbts.py`
- `dt/digital_twin.py`

### 3. Data Processing
Data handling and processing scripts:
- `data/database/utils/db_operations.py`
- `data/intergration/Async_AgentDB_notion.py`
- `RealTimeData/realTimeProcessor.js`

### 4. Visualization
UI and visualization components:
- `gbts/visualizations/gbtsVisualization.js`
- `gbts/visualizations/Frontend/dashboardRenderer.js`
- `streamlit_app/assets/game/game.js`

### 5. Configuration
Configuration and setup scripts:
- `agents/config/config_setup.py`
- `agents/config/llm_config.py`

### 6. Testing
Test scripts:
- `tests/agent_retrevial_tests.py`
- `tests/conversation_tree.test.js`
- `tests/llm_config_test.py`

### 7. Utilities
Helper and utility scripts:
- `scripts/file_structure_tree_updater.py`
- `scripts/get_requirements.py`
- `scripts/Update_requirements.py`
- `scripts/notion_update.py`

## Usage Guidelines

### Running Scripts

#### Python Scripts
```bash
# Run with Python 3
python script_name.py

# Or with virtual environment
source env/bin/activate
python script_name.py
```

#### JavaScript Scripts
```bash
# Run with Node.js
node script_name.js
```

#### Streamlit Applications
```bash
streamlit run streamlit_app/eco_bot_main.py
```

### Environment Setup

Most scripts require environment variables:
```bash
# Copy .env.example to .env
cp .env.example .env

# Edit .env with your API keys
OPENAI_API_KEY=your_key_here
OPENAI_ORGANIZATION=your_org_here
```

### Dependencies

Install Python dependencies:
```bash
pip install -r requirements.txt
```

Install JavaScript dependencies:
```bash
npm install
```

## Script Naming Conventions

- **Python**: `snake_case.py`
- **JavaScript**: `camelCase.js` or `kebab-case.js`
- **Classes**: PascalCase
- **Functions**: snake_case (Python) or camelCase (JavaScript)

## Documentation Standards

Each script should include:
1. Module-level docstring explaining purpose
2. Function/method docstrings with parameters and return values
3. Inline comments for complex logic
4. Usage examples where appropriate

## Contributing

When adding new scripts:
1. Follow naming conventions
2. Add comprehensive docstrings
3. Update relevant documentation files
4. Add tests if applicable
5. Update this index

## Related Documentation

- [Architecture Documentation](../ARCHITECTURE.md)
- [Module Documentation](../modules/README.md)
- [API Documentation](../api/README.md)
