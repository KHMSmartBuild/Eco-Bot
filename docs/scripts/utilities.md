# Utilities and Helper Scripts Documentation

## Overview

This document covers utility scripts and helper functions used throughout the Eco-Bot project. These scripts provide support for development, maintenance, and operational tasks.

## Scripts Location

```
scripts/
├── Update_requirements.py       # Update requirements.txt
├── addFolders.bat              # Windows folder creation utility
├── eco_bot_personality.js      # Personality configuration
├── file_structure_tree_updater.py  # Generate file structure tree
├── get_requirements.py         # Extract requirements from code
└── notion_update.py            # Update Notion integration
```

## Core Utility Scripts

### 1. file_structure_tree_updater.py

**Purpose:** Generate a tree structure visualization of the project file system.

**Author:** Kyle  
**Version:** 1.0  
**Location:** `/scripts/file_structure_tree_updater.py`

**Functionality:**
```python
def scan_directory(path, prefix=''):
    """
    Recursively scan directory and build tree structure.
    
    Args:
        path (str): Directory path to scan
        prefix (str): Prefix for tree formatting
        
    Returns:
        str: Formatted tree structure
    """
```

**Key Features:**
- Recursive directory scanning
- Respects `.gitignore` patterns
- Excludes virtual environments and `.env` files
- Formatted tree output
- Sorted directory listing

**Output:**
Generates `debug_data/file_structure_tree.txt` with structure like:
```
+-- agents
    +-- __init__.py
    +-- agent_classes.py
    +-- assistants
        +-- __init__.py
        +-- assistant_retrevial.py
        +-- group_chat.py
```

**Usage:**
```bash
python scripts/file_structure_tree_updater.py
```

**Configuration:**
```python
# Excluded items
excluded = ['eco-bot_env', '.env', '__pycache__', '.git']

# Output location
output_file = 'debug_data/file_structure_tree.txt'
```

**Use Cases:**
- Documentation generation
- Project structure visualization
- Code review preparation
- Onboarding new developers

### 2. get_requirements.py

**Purpose:** Extract Python package requirements from code files.

**Functionality:**
- Scans Python files for imports
- Identifies external packages
- Generates requirements list
- Excludes standard library modules

**Key Features:**
```python
def extract_imports(file_path):
    """Extract all import statements from Python file."""
    
def is_external_package(package_name):
    """Check if package is external (not stdlib)."""
    
def generate_requirements():
    """Generate requirements.txt from codebase."""
```

**Usage:**
```bash
python scripts/get_requirements.py
```

**Output:**
Updates or creates `requirements.txt` with discovered dependencies.

**Example Output:**
```
openai>=1.0.0
streamlit>=1.28.0
autogen>=0.1.0
opencv-python>=4.8.0
pandas>=2.0.0
```

### 3. Update_requirements.py

**Purpose:** Update requirements.txt with latest package versions.

**Functionality:**
- Read current requirements
- Check for latest versions
- Update version numbers
- Preserve version constraints

**Key Features:**
```python
def check_latest_version(package_name):
    """Query PyPI for latest version."""
    
def update_requirements_file():
    """Update all packages to latest versions."""
    
def validate_compatibility():
    """Check for version conflicts."""
```

**Usage:**
```bash
python scripts/Update_requirements.py

# With options
python scripts/Update_requirements.py --check-only
python scripts/Update_requirements.py --backup
```

**Safety Features:**
- Creates backup before updating
- Validates compatibility
- Preserves pinned versions
- Logs all changes

### 4. notion_update.py

**Purpose:** Sync project data with Notion workspace.

**Functionality:**
- Update Notion databases
- Sync task lists
- Update documentation
- Track project metrics

**Key Features:**
```python
def connect_notion():
    """Establish Notion API connection."""
    
def update_task_database():
    """Sync tasks with Notion database."""
    
def update_documentation():
    """Push documentation updates to Notion."""
```

**Configuration:**
```python
# .env
NOTION_API_KEY=your_notion_key
NOTION_DATABASE_ID=your_database_id
```

**Usage:**
```bash
python scripts/notion_update.py

# Update specific database
python scripts/notion_update.py --database tasks

# Sync all
python scripts/notion_update.py --sync-all
```

**Sync Operations:**
- Task status updates
- Documentation synchronization
- Metric tracking
- Team updates

### 5. eco_bot_personality.js

**Purpose:** Define and configure Eco-Bot personality traits.

**Configuration Structure:**
```javascript
const ecoBot_personality = {
  traits: {
    enthusiasm: 0.8,      // How enthusiastic about eco topics
    formality: 0.4,       // Level of formality
    humor: 0.6,           // Use of humor
    empathy: 0.9,         // Empathetic responses
    directness: 0.7       // How direct/concise
  },
  
  communication_style: {
    greeting: "friendly",
    encouragement: "high",
    educational_tone: "conversational",
    error_handling: "supportive"
  },
  
  knowledge_focus: {
    recycling: 1.0,
    composting: 0.9,
    zero_waste: 0.95,
    climate_change: 0.85,
    sustainability: 0.9
  },
  
  interaction_preferences: {
    question_depth: "thorough",
    example_usage: "frequent",
    link_provision: "when_helpful",
    follow_up_questions: "encouraged"
  }
};
```

**Usage:**
```javascript
import ecoBot_personality from './scripts/eco_bot_personality.js';

// Apply personality to responses
function generateResponse(query, personality) {
  // Adjust tone based on personality traits
  const enthusiasm = personality.traits.enthusiasm;
  const humor = personality.traits.humor;
  
  // Generate response...
}
```

**Customization:**
Modify personality for different contexts:
- Kid-friendly mode: Higher enthusiasm, simpler language
- Professional mode: Higher formality, more technical
- Beginner mode: More educational, more examples

### 6. addFolders.bat

**Purpose:** Windows batch script for creating project folder structure.

**Functionality:**
```batch
@echo off
mkdir agents
mkdir gbts
mkdir eco_buddies
mkdir models
mkdir data
mkdir streamlit_app
mkdir tests
echo Folders created successfully!
```

**Usage:**
```batch
# Windows
addFolders.bat

# Create custom structure
addFolders.bat --custom
```

**Features:**
- Quick project setup
- Consistent structure
- Error handling
- Confirmation messages

## Additional Utility Modules

### Database Utilities

**Location:** `data/database/utils/`

#### db_operations.py

**Purpose:** Common database operations.

**Key Functions:**
```python
def connect_db():
    """Establish database connection."""
    
def execute_query(query, params):
    """Execute SQL query safely."""
    
def batch_insert(table, records):
    """Batch insert records."""
    
def get_connection_pool():
    """Get connection pool instance."""
```

**Features:**
- Connection pooling
- Query parameterization (SQL injection prevention)
- Transaction management
- Error handling and retry logic

#### setconn.py

**Purpose:** Set up database connections.

**Configuration:**
```python
DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}
```

### Logging Utilities

**Location:** `eco_buddies/utils/logging_setup.py`

**Purpose:** Centralized logging configuration.

**Key Features:**
```python
def setup_logging(name, level='INFO', log_file=None):
    """
    Configure logging for module.
    
    Args:
        name: Logger name
        level: Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Optional file output
        
    Returns:
        Logger instance
    """
```

**Log Format:**
```python
FORMAT = '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
```

**Usage:**
```python
from eco_buddies.utils.logging_setup import setup_logging

logger = setup_logging(__name__)
logger.info("Starting process")
logger.error("Error occurred", exc_info=True)
```

## Development Utilities

### Testing Helpers

**Purpose:** Helper functions for testing.

**Common Functions:**
```python
def create_test_data():
    """Generate test data."""
    
def mock_api_response():
    """Mock external API responses."""
    
def setup_test_db():
    """Set up test database."""
    
def cleanup_test_data():
    """Clean up after tests."""
```

### Debug Utilities

**Location:** `debug/`

**Purpose:** Debugging and troubleshooting tools.

**Contents:**
- Debug logs
- Performance metrics
- Error traces
- Test outputs

## Integration Utilities

### Notion Integration

**Location:** `data/intergration/`

#### notion_integration.py

**Purpose:** Python interface for Notion API.

**Key Functions:**
```python
def get_notion_client():
    """Initialize Notion client."""
    
def query_database(database_id, filter=None):
    """Query Notion database."""
    
def create_page(parent, properties):
    """Create new Notion page."""
    
def update_page(page_id, properties):
    """Update existing page."""
```

#### notion_connection_ops.js

**Purpose:** JavaScript interface for Notion API.

**Key Functions:**
```javascript
async function connectNotion() {
  // Initialize Notion client
}

async function syncData(data) {
  // Sync data to Notion
}

async function fetchPages(databaseId) {
  // Retrieve pages from database
}
```

#### Async_AgentDB_notion.py

**Purpose:** Asynchronous agent database sync with Notion.

**Key Features:**
- Async operations
- Batch processing
- Error recovery
- Progress tracking

**Usage:**
```python
import asyncio
from data.intergration.Async_AgentDB_notion import sync_agents

# Sync agent data
asyncio.run(sync_agents())
```

## Best Practices

### 1. Error Handling

```python
import logging

logger = logging.getLogger(__name__)

try:
    result = perform_operation()
except Exception as e:
    logger.error(f"Operation failed: {e}", exc_info=True)
    # Handle gracefully
```

### 2. Configuration Management

```python
from dotenv import load_dotenv
import os

load_dotenv()

# Use environment variables
API_KEY = os.getenv('API_KEY')
if not API_KEY:
    raise ValueError("API_KEY not found in environment")
```

### 3. Logging

```python
# Use appropriate log levels
logger.debug("Detailed diagnostic info")
logger.info("General information")
logger.warning("Warning messages")
logger.error("Error messages")
logger.critical("Critical failures")
```

### 4. Documentation

```python
def utility_function(param1, param2):
    """
    Brief description of function.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When invalid input provided
    """
```

## Maintenance Scripts

### Daily Tasks
- Log rotation
- Database cleanup
- Cache clearing
- Backup verification

### Weekly Tasks
- Dependency updates check
- Performance analysis
- Error log review
- Documentation updates

### Monthly Tasks
- Full system backup
- Security audit
- Dependency updates
- Performance optimization

## Common Operations

### Update Dependencies
```bash
python scripts/get_requirements.py
python scripts/Update_requirements.py
pip install -r requirements.txt
```

### Generate Documentation
```bash
python scripts/file_structure_tree_updater.py
# Manual: Update docs based on structure
```

### Sync with Notion
```bash
python scripts/notion_update.py --sync-all
```

### Database Maintenance
```python
from data.database.utils.db_operations import cleanup_old_records

cleanup_old_records(days=30)
```

## Troubleshooting

### Common Issues

1. **Import Errors**
   - Check virtual environment activation
   - Verify requirements installed
   - Check Python path

2. **Database Connection Errors**
   - Verify credentials in .env
   - Check database server status
   - Test network connectivity

3. **Notion Sync Failures**
   - Validate API key
   - Check database permissions
   - Verify network access

## Future Utilities

- [ ] Automated testing utilities
- [ ] Performance monitoring scripts
- [ ] Deployment automation
- [ ] Code quality checks
- [ ] Security scanning tools

## Related Documentation

- [Architecture Overview](../ARCHITECTURE.md)
- [Agents Module](./agents.md)
- [Data Integration](./data-integration.md)
