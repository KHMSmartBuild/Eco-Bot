# Eco-Bot Documentation

Welcome to the comprehensive documentation for the Eco-Bot project. This documentation covers all aspects of the system architecture, scripts, modules, and APIs.

## 📚 Documentation Structure

### Getting Started
- [Main README](../README.md) - Project overview and quick start
- [Architecture Overview](./ARCHITECTURE.md) - Complete system architecture
- [Contributing Guide](../CONTRIBUTING.md) - How to contribute
- [Code of Conduct](../CODE_OF_CONDUCT.md) - Community guidelines

### Core Documentation

#### 1. System Architecture
- **[Architecture Documentation](./ARCHITECTURE.md)** - Complete system design, data flows, and component interactions
  - High-level architecture diagram
  - Component descriptions
  - Data flow diagrams
  - Technology stack
  - Deployment architecture

#### 2. Scripts and Modules
- **[Scripts Overview](./scripts/README.md)** - Index of all scripts in the project
- **[Agents Module](./scripts/agents.md)** - Multi-agent system documentation
- **[GBTS Module](./scripts/gbts.md)** - Gaia-Bohm Thought Style system
- **[Eco-Buddies Module](./scripts/eco-buddies.md)** - User-facing chat and vision interfaces
- **[Streamlit Application](./scripts/streamlit-app.md)** - Web UI documentation
- **[Data Integration](./scripts/data-integration.md)** - Database and external integrations
- **[Utilities](./scripts/utilities.md)** - Helper scripts and tools

#### 3. API Documentation
- **[API Reference](./api/README.md)** - API endpoints and usage *(coming soon)*

#### 4. Module Documentation
- **[Module Index](./modules/README.md)** - Detailed module documentation *(coming soon)*

## 🗂️ Quick Reference

### By Component

| Component | Description | Documentation |
|-----------|-------------|---------------|
| **Agents** | Multi-agent orchestration system | [agents.md](./scripts/agents.md) |
| **GBTS** | Conversation tree management | [gbts.md](./scripts/gbts.md) |
| **Eco-Buddies** | User-facing chat interface | [eco-buddies.md](./scripts/eco-buddies.md) |
| **Streamlit App** | Web-based UI | [streamlit-app.md](./scripts/streamlit-app.md) |
| **Database** | Data persistence layer | [data-integration.md](./scripts/data-integration.md) |
| **API Gateway** | Request routing | [data-integration.md](./scripts/data-integration.md) |
| **Models** | ML model implementations | [models.md](./scripts/models.md) *(coming soon)* |
| **Security** | Authentication & authorization | [data-integration.md](./scripts/data-integration.md) |

### By File Type

| Type | Count | Documentation |
|------|-------|---------------|
| Python Scripts | ~60 | See individual module docs |
| JavaScript Scripts | ~25 | See individual module docs |
| Shell Scripts | ~3 | [utilities.md](./scripts/utilities.md) |
| Documentation Files | 6+ | This directory |

### By Use Case

#### For Developers
- [Architecture Documentation](./ARCHITECTURE.md) - Understand system design
- [Agents Module](./scripts/agents.md) - Work with agents
- [GBTS Module](./scripts/gbts.md) - Implement conversation flows
- [Data Integration](./scripts/data-integration.md) - Database operations

#### For DevOps
- [Utilities](./scripts/utilities.md) - Deployment and maintenance scripts
- [Architecture Documentation](./ARCHITECTURE.md) - Deployment architecture
- [Streamlit App](./scripts/streamlit-app.md) - Application deployment

#### For Contributors
- [Contributing Guide](../CONTRIBUTING.md) - Contribution guidelines
- [Scripts Overview](./scripts/README.md) - Script organization
- [Utilities](./scripts/utilities.md) - Development tools

#### For Users
- [Streamlit Application](./scripts/streamlit-app.md) - Using the web interface
- [Eco-Buddies Module](./scripts/eco-buddies.md) - Chat and interaction features

## 🎯 Common Tasks

### Setup and Installation
1. Clone repository: See [Main README](../README.md)
2. Install dependencies: `pip install -r requirements.txt`
3. Configure environment: Copy `.env.example` to `.env`
4. Initialize database: See [Data Integration](./scripts/data-integration.md)

### Running the Application
```bash
# Streamlit web app
streamlit run streamlit_app/eco_bot_main.py

# Chat interface
python eco_buddies/eco_chat.py

# Run tests
pytest
```

### Development
```bash
# Update requirements
python scripts/get_requirements.py
python scripts/Update_requirements.py

# Generate file structure
python scripts/file_structure_tree_updater.py

# Sync with Notion
python scripts/notion_update.py
```

## 📖 Documentation Conventions

### File Naming
- `README.md` - Index/overview files
- `ARCHITECTURE.md` - Architecture documentation
- `module-name.md` - Module-specific documentation
- `api-name.md` - API documentation

### Documentation Structure
Each module documentation includes:
1. **Overview** - Purpose and context
2. **Module Structure** - File organization
3. **Core Components** - Main classes/functions
4. **Usage Examples** - Code samples
5. **Configuration** - Setup and options
6. **Testing** - Test information
7. **Dependencies** - Required packages
8. **Related Documentation** - Cross-references

### Code Examples
Code examples follow this format:
```python
# Clear description of what the example does
from module import Class

# Setup
instance = Class()

# Usage
result = instance.method()

# Expected output
# Output: expected_value
```

## 🔍 Finding Information

### Search by Topic
- **Authentication** → [Data Integration](./scripts/data-integration.md) (Security Layer)
- **Chat Interface** → [Eco-Buddies](./scripts/eco-buddies.md)
- **Conversation Trees** → [GBTS Module](./scripts/gbts.md)
- **Database Operations** → [Data Integration](./scripts/data-integration.md)
- **Vision Processing** → [Eco-Buddies](./scripts/eco-buddies.md) (EcoBot_Vision)
- **Web Interface** → [Streamlit App](./scripts/streamlit-app.md)
- **Agent Communication** → [Agents Module](./scripts/agents.md)

### Search by Technology
- **Python** → All module documentation
- **JavaScript** → [GBTS](./scripts/gbts.md), [Streamlit Assets](./scripts/streamlit-app.md)
- **D3.js** → [GBTS Visualizations](./scripts/gbts.md)
- **Three.js** → [GBTS 3D Visualization](./scripts/gbts.md)
- **Streamlit** → [Streamlit App](./scripts/streamlit-app.md)
- **OpenAI API** → [Agents](./scripts/agents.md), [Eco-Buddies](./scripts/eco-buddies.md)
- **Notion API** → [Data Integration](./scripts/data-integration.md)

## 🛠️ Development Workflow

### 1. Understanding the Codebase
```
Start: Architecture Documentation → Module Documentation → Specific Scripts
```

### 2. Making Changes
```
Read Module Docs → Check Examples → Implement → Test → Document
```

### 3. Adding New Features
```
Design → Document → Implement → Test → Update Docs → Submit PR
```

## 📝 Documentation Standards

### Docstring Format (Python)
```python
def function_name(param1, param2):
    """
    Brief description of function.
    
    Longer description if needed. Explain purpose, behavior,
    and any important details.
    
    Args:
        param1 (type): Description of param1
        param2 (type): Description of param2
        
    Returns:
        type: Description of return value
        
    Raises:
        ErrorType: When this error occurs
        
    Example:
        >>> function_name("value1", "value2")
        expected_output
    """
```

### JSDoc Format (JavaScript)
```javascript
/**
 * Brief description of function.
 * 
 * Longer description if needed.
 * 
 * @param {type} param1 - Description of param1
 * @param {type} param2 - Description of param2
 * @returns {type} Description of return value
 * @throws {ErrorType} When this error occurs
 * 
 * @example
 * functionName("value1", "value2");
 * // Returns: expected_output
 */
function functionName(param1, param2) {
  // Implementation
}
```

## 🔄 Keeping Documentation Updated

### When to Update Documentation
- Adding new features
- Modifying existing functionality
- Fixing bugs that affect documented behavior
- Changing configuration options
- Adding new dependencies
- Changing file structure

### Documentation Review Checklist
- [ ] Code changes documented
- [ ] Examples updated
- [ ] Configuration changes noted
- [ ] Related docs cross-referenced
- [ ] Breaking changes highlighted
- [ ] Migration guides added (if needed)

## 🤝 Contributing to Documentation

### How to Contribute
1. Identify documentation gaps
2. Create/update relevant documentation
3. Follow documentation standards
4. Submit pull request
5. Respond to review feedback

### Documentation Priorities
1. **Critical** - Core functionality, architecture
2. **High** - Frequently used features, setup
3. **Medium** - Advanced features, utilities
4. **Low** - Edge cases, experimental features

## 📞 Getting Help

### Resources
- **Issues** - [GitHub Issues](https://github.com/KHMSmartBuild/Eco-Bot/issues)
- **Discussions** - [GitHub Discussions](https://github.com/KHMSmartBuild/Eco-Bot/discussions)
- **Email** - [info@KHMSmartBuild](mailto:info@KHMSmartBuild)

### Common Questions
Check the relevant module documentation:
- Setup questions → [Main README](../README.md)
- Architecture questions → [Architecture](./ARCHITECTURE.md)
- Feature questions → Specific module docs
- API questions → [API Documentation](./api/README.md)

## 📊 Documentation Metrics

### Coverage
- ✅ Core architecture documented
- ✅ Major modules documented
- ✅ Key scripts documented
- ⏳ API documentation in progress
- ⏳ Advanced features documentation in progress

### Last Updated
This documentation structure was created on 2023-10-29 and should be kept up to date with code changes.

## 🗺️ Documentation Roadmap

### Completed
- [x] Architecture documentation
- [x] Core module documentation
- [x] Scripts documentation
- [x] Navigation structure

### In Progress
- [ ] API reference documentation
- [ ] Advanced module documentation
- [ ] Tutorial and guides

### Planned
- [ ] Video tutorials
- [ ] Interactive examples
- [ ] API playground
- [ ] Architecture decision records (ADRs)

## License

This documentation is part of the Eco-Bot project and follows the same license as the main project. See [LICENSE](../LICENSE) for details.

---

**Note:** This documentation is a living document and will be updated as the project evolves. If you find any discrepancies or areas for improvement, please contribute!
