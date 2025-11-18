# Modules Documentation

## Overview

This directory contains detailed documentation for each module in the Eco-Bot system. Each module has its own dedicated documentation file with comprehensive information about its structure, functionality, and usage.

## Available Modules

### Core Modules
- [Agents Module](../scripts/agents.md) - Multi-agent orchestration system
- [GBTS Module](../scripts/gbts.md) - Gaia-Bohm Thought Style conversation management
- [Eco-Buddies Module](../scripts/eco-buddies.md) - User-facing chat and vision interface
- [Digital Twin Module](./digital-twin.md) *(coming soon)* - Digital twin agent implementation

### Application Modules
- [Streamlit Application](../scripts/streamlit-app.md) - Web-based user interface
- [Models Module](./models.md) *(coming soon)* - Machine learning models

### Infrastructure Modules
- [Data Integration](../scripts/data-integration.md) - Database and external integrations
- [API Gateway](./api-gateway.md) *(coming soon)* - API routing and handling
- [Security Layer](./security.md) *(coming soon)* - Authentication and authorization

### Supporting Modules
- [Utilities](../scripts/utilities.md) - Helper scripts and tools
- [Testing](./testing.md) *(coming soon)* - Testing infrastructure

## Module Structure

Each module documentation follows this structure:

### 1. Overview
- Purpose and goals
- Key features
- Dependencies

### 2. Architecture
- Component diagram
- File structure
- Class hierarchy

### 3. Core Components
- Main classes and functions
- Interfaces and APIs
- Data structures

### 4. Usage
- Installation and setup
- Configuration
- Code examples
- Best practices

### 5. Integration
- Integration points
- External dependencies
- Inter-module communication

### 6. Testing
- Test structure
- Running tests
- Test coverage

### 7. Troubleshooting
- Common issues
- Error handling
- Debugging tips

## Quick Reference

| Module | Primary Language | Entry Point | Documentation |
|--------|-----------------|-------------|---------------|
| Agents | Python | `agents/agent_classes.py` | [agents.md](../scripts/agents.md) |
| GBTS | Python/JavaScript | `gbts/gbts.py` | [gbts.md](../scripts/gbts.md) |
| Eco-Buddies | Python/JavaScript | `eco_buddies/Eco_Bot.py` | [eco-buddies.md](../scripts/eco-buddies.md) |
| Streamlit App | Python | `streamlit_app/eco_bot_main.py` | [streamlit-app.md](../scripts/streamlit-app.md) |
| Data | Python/JavaScript | `data/database/utils/` | [data-integration.md](../scripts/data-integration.md) |

## Module Dependencies

```
Streamlit App
    ├── Eco-Buddies
    │   ├── Agents
    │   │   ├── Digital Twin
    │   │   └── GBTS
    │   └── Models
    ├── GBTS
    └── API Gateway
        ├── Security Layer
        └── Data Integration
```

## Getting Started

1. **For New Developers:**
   - Start with [Architecture Documentation](../ARCHITECTURE.md)
   - Read module documentation for areas you'll work on
   - Review code examples in each module

2. **For Contributors:**
   - Check [Contributing Guide](../../CONTRIBUTING.md)
   - Review relevant module documentation
   - Follow coding standards in each module

3. **For Users:**
   - Start with [Streamlit Application](../scripts/streamlit-app.md)
   - Review [Eco-Buddies Module](../scripts/eco-buddies.md) for features

## Documentation Status

| Module | Status | Last Updated | Coverage |
|--------|--------|--------------|----------|
| Agents | ✅ Complete | 2023-10-29 | 95% |
| GBTS | ✅ Complete | 2023-10-29 | 95% |
| Eco-Buddies | ✅ Complete | 2023-10-29 | 95% |
| Streamlit App | ✅ Complete | 2023-10-29 | 90% |
| Data Integration | ✅ Complete | 2023-10-29 | 90% |
| Utilities | ✅ Complete | 2023-10-29 | 85% |
| Digital Twin | ⏳ In Progress | - | 0% |
| Models | ⏳ In Progress | - | 0% |
| API Gateway | ⏳ In Progress | - | 0% |
| Security | ⏳ In Progress | - | 0% |

## Contributing to Module Documentation

When adding or updating module documentation:

1. Follow the standard structure outlined above
2. Include code examples for all major features
3. Document all public APIs
4. Add cross-references to related modules
5. Update this index file

## Related Documentation

- [Main Documentation Index](../README.md)
- [Architecture Overview](../ARCHITECTURE.md)
- [Scripts Documentation](../scripts/README.md)
- [API Documentation](../api/README.md)
