# Data Integration and Database Documentation

## Overview

The Data Integration module handles all database operations, external service integrations, and real-time data processing. It provides the persistence layer and external connectivity for the Eco-Bot system.

## Module Structure

```
data/
├── database/
│   └── utils/
│       ├── db_operations.py    # Database operations
│       └── setconn.py          # Connection setup
└── intergration/               # Note: spelled "intergration" in codebase
    ├── Async_AgentDB_notion.py # Async Notion sync
    ├── notion_connection_ops.js # Notion operations (JS)
    └── notion_integration.py   # Notion integration (Python)

RealTimeData/
└── realTimeProcessor.js        # Real-time data processing

APIGateway/
├── __init__.py
├── gbts_handler.py             # GBTS API handler
└── queryHandler.js             # Query processing
```

## Database Layer

### db_operations.py

**Purpose:** Core database operations and utilities.

**Key Functions:**

#### Connection Management
```python
def connect_db():
    """
    Establish database connection.
    
    Returns:
        Connection object
    """
    
def get_connection_pool():
    """
    Get connection pool for efficient connection reuse.
    
    Returns:
        ConnectionPool instance
    """
    
def close_connection(conn):
    """
    Safely close database connection.
    
    Args:
        conn: Connection object to close
    """
```

#### Query Operations
```python
def execute_query(query, params=None):
    """
    Execute SQL query safely with parameterization.
    
    Args:
        query (str): SQL query string
        params (tuple): Query parameters
        
    Returns:
        Query results
        
    Raises:
        DatabaseError: If query execution fails
    """
    
def batch_insert(table, records):
    """
    Efficiently insert multiple records.
    
    Args:
        table (str): Table name
        records (list): List of record dictionaries
        
    Returns:
        int: Number of records inserted
    """
    
def batch_update(table, records, key_field):
    """
    Update multiple records efficiently.
    
    Args:
        table (str): Table name
        records (list): Records to update
        key_field (str): Primary key field name
    """
```

#### Transaction Management
```python
def begin_transaction():
    """Start database transaction."""
    
def commit_transaction():
    """Commit current transaction."""
    
def rollback_transaction():
    """Rollback current transaction."""
    
@contextmanager
def transaction():
    """
    Context manager for transactions.
    
    Usage:
        with transaction():
            execute_query(...)
            execute_query(...)
    """
```

**Features:**
- Connection pooling for performance
- SQL injection prevention via parameterization
- Transaction support with rollback
- Batch operations for efficiency
- Error handling and logging
- Automatic connection cleanup

**Usage Example:**
```python
from data.database.utils.db_operations import execute_query, transaction

# Single query
results = execute_query(
    "SELECT * FROM agents WHERE role = %s",
    params=("recycling_expert",)
)

# Transaction
with transaction():
    execute_query("INSERT INTO logs (...) VALUES (...)", params)
    execute_query("UPDATE metrics SET count = count + 1")
```

### setconn.py

**Purpose:** Database connection configuration and setup.

**Configuration:**
```python
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 5432)),
    'database': os.getenv('DB_NAME', 'eco_bot'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'sslmode': os.getenv('DB_SSL_MODE', 'prefer'),
    'connect_timeout': int(os.getenv('DB_TIMEOUT', 10))
}

POOL_CONFIG = {
    'min_connections': 2,
    'max_connections': 10,
    'max_idle_time': 300,  # 5 minutes
    'max_lifetime': 3600   # 1 hour
}
```

**Functions:**
```python
def validate_config():
    """Validate database configuration."""
    
def test_connection():
    """Test database connectivity."""
    
def initialize_pool():
    """Initialize connection pool."""
```

**Environment Variables:**
```bash
# .env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=eco_bot
DB_USER=eco_admin
DB_PASSWORD=your_secure_password
DB_SSL_MODE=require
DB_TIMEOUT=10
```

## Notion Integration

### notion_integration.py

**Purpose:** Python interface for Notion API integration.

**Key Functions:**

#### Client Initialization
```python
def get_notion_client():
    """
    Initialize and return Notion client.
    
    Returns:
        notion_client.Client: Configured Notion client
        
    Raises:
        ValueError: If API key not found
    """
    
def validate_credentials():
    """Validate Notion API credentials."""
```

#### Database Operations
```python
def query_database(database_id, filter=None, sorts=None):
    """
    Query Notion database.
    
    Args:
        database_id (str): Notion database ID
        filter (dict): Optional filter criteria
        sorts (list): Optional sort criteria
        
    Returns:
        list: Query results
    """
    
def create_database_entry(database_id, properties):
    """
    Create new entry in Notion database.
    
    Args:
        database_id (str): Target database ID
        properties (dict): Entry properties
        
    Returns:
        dict: Created entry data
    """
```

#### Page Operations
```python
def create_page(parent, properties, children=None):
    """
    Create new Notion page.
    
    Args:
        parent (dict): Parent page/database
        properties (dict): Page properties
        children (list): Optional child blocks
        
    Returns:
        dict: Created page data
    """
    
def update_page(page_id, properties):
    """
    Update existing Notion page.
    
    Args:
        page_id (str): Page ID to update
        properties (dict): Updated properties
    """
    
def archive_page(page_id):
    """Archive a Notion page."""
```

#### Block Operations
```python
def append_blocks(page_id, blocks):
    """
    Append blocks to page.
    
    Args:
        page_id (str): Target page ID
        blocks (list): Blocks to append
    """
    
def update_block(block_id, content):
    """Update block content."""
```

**Configuration:**
```python
# .env
NOTION_API_KEY=your_notion_integration_key
NOTION_DATABASE_ID=your_database_id
NOTION_PAGE_ID=your_page_id
```

**Usage Example:**
```python
from data.intergration.notion_integration import (
    get_notion_client,
    query_database,
    create_page
)

# Initialize client
client = get_notion_client()

# Query database
results = query_database(
    database_id="abc123",
    filter={
        "property": "Status",
        "select": {"equals": "Active"}
    }
)

# Create page
new_page = create_page(
    parent={"database_id": "abc123"},
    properties={
        "Name": {"title": [{"text": {"content": "New Task"}}]},
        "Status": {"select": {"name": "In Progress"}}
    }
)
```

### Async_AgentDB_notion.py

**Purpose:** Asynchronous synchronization between agent database and Notion.

**Key Features:**
- Async/await operations
- Batch processing
- Error recovery
- Progress tracking
- Conflict resolution

**Key Functions:**
```python
async def sync_agents_to_notion():
    """
    Sync agent data to Notion database.
    
    Returns:
        dict: Sync results (success, failed, skipped)
    """
    
async def sync_notion_to_agents():
    """Sync Notion changes back to agent database."""
    
async def bidirectional_sync():
    """Perform two-way synchronization."""
    
async def handle_conflicts(local_data, remote_data):
    """Resolve sync conflicts."""
```

**Sync Strategy:**
```python
SYNC_CONFIG = {
    'batch_size': 50,
    'max_retries': 3,
    'retry_delay': 5,  # seconds
    'conflict_resolution': 'latest_wins',  # or 'manual'
    'sync_interval': 300  # 5 minutes
}
```

**Usage:**
```python
import asyncio
from data.intergration.Async_AgentDB_notion import sync_agents_to_notion

async def main():
    results = await sync_agents_to_notion()
    print(f"Synced: {results['success']}")
    print(f"Failed: {results['failed']}")
    print(f"Skipped: {results['skipped']}")

asyncio.run(main())
```

### notion_connection_ops.js

**Purpose:** JavaScript interface for Notion operations.

**Key Functions:**
```javascript
async function connectNotion() {
  /**
   * Initialize Notion client.
   * @returns {Client} Notion client instance
   */
}

async function queryDatabase(databaseId, options = {}) {
  /**
   * Query Notion database.
   * @param {string} databaseId - Database ID
   * @param {Object} options - Query options (filter, sorts)
   * @returns {Array} Query results
   */
}

async function createPage(parentId, properties) {
  /**
   * Create new page in Notion.
   * @param {string} parentId - Parent database/page ID
   * @param {Object} properties - Page properties
   * @returns {Object} Created page
   */
}

async function batchUpdate(updates) {
  /**
   * Batch update multiple pages.
   * @param {Array} updates - Array of update operations
   * @returns {Object} Update results
   */
}
```

**Dependencies:**
```json
{
  "@notionhq/client": "^2.2.14"
}
```

**Usage:**
```javascript
import { connectNotion, queryDatabase } from './data/intergration/notion_connection_ops.js';

// Initialize
const notion = await connectNotion();

// Query
const results = await queryDatabase('database_id', {
  filter: {
    property: 'Status',
    select: { equals: 'Active' }
  }
});
```

## API Gateway

### gbts_handler.py

**Purpose:** Handle GBTS-related API requests.

**Key Endpoints:**
```python
def handle_conversation_request(request):
    """
    Process conversation tree request.
    
    Args:
        request: API request object
        
    Returns:
        Response with conversation data
    """
    
def handle_node_creation(request):
    """Create new conversation node."""
    
def handle_tree_traversal(request):
    """Traverse conversation tree."""
    
def handle_visualization_request(request):
    """Generate visualization data."""
```

**Request/Response Format:**
```python
# Request
{
    'action': 'create_node',
    'data': {
        'role': 'user',
        'message': 'How do I recycle plastic?',
        'parent_id': 'node_123'
    }
}

# Response
{
    'success': True,
    'node_id': 'node_456',
    'tree_path': ['node_1', 'node_123', 'node_456']
}
```

### queryHandler.js

**Purpose:** Process and route API queries.

**Key Functions:**
```javascript
async function handleQuery(query) {
  /**
   * Main query handler.
   * @param {Object} query - Query object
   * @returns {Object} Query results
   */
}

function routeQuery(query) {
  /**
   * Route query to appropriate handler.
   * @param {Object} query - Query to route
   * @returns {Promise} Handler promise
   */
}

function validateQuery(query) {
  /**
   * Validate query structure and parameters.
   * @param {Object} query - Query to validate
   * @returns {boolean} Validation result
   */
}

function formatResponse(data, error = null) {
  /**
   * Format API response.
   * @param {*} data - Response data
   * @param {Error} error - Optional error
   * @returns {Object} Formatted response
   */
}
```

**Query Types:**
- Agent queries
- GBTS tree queries
- Data retrieval queries
- Update queries
- Search queries

## Real-Time Data Processing

### realTimeProcessor.js

**Purpose:** Process real-time data streams.

**Key Features:**
- WebSocket support
- Event streaming
- Data aggregation
- Real-time analytics

**Key Functions:**
```javascript
class RealTimeProcessor {
  constructor(config) {
    /**
     * Initialize real-time processor.
     * @param {Object} config - Configuration
     */
  }
  
  async processStream(stream) {
    /**
     * Process data stream.
     * @param {Stream} stream - Data stream
     */
  }
  
  async aggregateData(timeWindow) {
    /**
     * Aggregate data over time window.
     * @param {number} timeWindow - Time window in ms
     */
  }
  
  emit(event, data) {
    /**
     * Emit real-time event.
     * @param {string} event - Event name
     * @param {*} data - Event data
     */
  }
}
```

**Usage:**
```javascript
import RealTimeProcessor from './RealTimeData/realTimeProcessor.js';

const processor = new RealTimeProcessor({
  batchSize: 100,
  flushInterval: 1000
});

processor.processStream(dataStream);
processor.on('aggregated', (data) => {
  console.log('Aggregated data:', data);
});
```

## Security Layer

### authenticator.js

**Purpose:** User authentication and authorization.

**Key Functions:**
```javascript
async function authenticateUser(credentials) {
  /**
   * Authenticate user credentials.
   * @param {Object} credentials - User credentials
   * @returns {Object} Authentication result with token
   */
}

async function validateToken(token) {
  /**
   * Validate authentication token.
   * @param {string} token - JWT token
   * @returns {boolean} Validation result
   */
}

async function refreshToken(oldToken) {
  /**
   * Refresh expired token.
   * @param {string} oldToken - Existing token
   * @returns {string} New token
   */
}

function checkPermissions(user, resource, action) {
  /**
   * Check user permissions.
   * @param {Object} user - User object
   * @param {string} resource - Resource name
   * @param {string} action - Action to perform
   * @returns {boolean} Permission granted
   */
}
```

## Best Practices

### Database Operations
```python
# Use connection pooling
from data.database.utils.db_operations import get_connection_pool

pool = get_connection_pool()

# Always use parameterized queries
execute_query(
    "SELECT * FROM users WHERE id = %s",
    params=(user_id,)  # Never: f"... WHERE id = {user_id}"
)

# Use transactions for related operations
with transaction():
    create_record(...)
    update_related(...)
```

### Error Handling
```python
import logging

logger = logging.getLogger(__name__)

try:
    result = query_database(...)
except DatabaseError as e:
    logger.error(f"Database error: {e}", exc_info=True)
    # Handle gracefully
except Exception as e:
    logger.critical(f"Unexpected error: {e}", exc_info=True)
    raise
```

### Async Operations
```python
import asyncio

async def sync_data():
    try:
        await sync_agents_to_notion()
    except Exception as e:
        logger.error(f"Sync failed: {e}")
        # Implement retry logic

# Run with proper event loop management
asyncio.run(sync_data())
```

## Testing

```python
# tests/test_database.py
import pytest
from data.database.utils.db_operations import execute_query

def test_query_execution():
    result = execute_query("SELECT 1")
    assert result is not None

def test_transaction_rollback():
    with pytest.raises(Exception):
        with transaction():
            execute_query("INSERT ...")
            raise Exception("Test rollback")
    # Verify data not inserted
```

## Dependencies

```python
# Python
psycopg2-binary>=2.9.0  # PostgreSQL
notion-client>=2.0.0
aiohttp>=3.8.0
python-dotenv>=0.19.0

# JavaScript
@notionhq/client: ^2.2.14
winston: ^3.11.0  # Logging
```

## Future Enhancements

- [ ] Redis caching layer
- [ ] GraphQL API support
- [ ] Event sourcing implementation
- [ ] Advanced query optimization
- [ ] Multi-database support
- [ ] Real-time collaboration features

## Related Documentation

- [Architecture Overview](../ARCHITECTURE.md)
- [Agents Module](./agents.md)
- [Utilities](./utilities.md)
