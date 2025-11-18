# Agents Module Documentation

## Overview

The Agents module implements a multi-agent system using the AutoGen framework. It provides the core infrastructure for agent creation, communication, and coordination within the Eco-Bot system.

## Module Structure

```
agents/
├── __init__.py
├── agent_classes.py           # Core agent class definitions
├── agents_table.csv           # Agent configuration data
├── assistants/                # Specialized assistant agents
│   ├── __init__.py
│   ├── assistant_retrevial.py # Assistant retrieval logic
│   └── group_chat.py          # Group chat coordination
├── config/                    # Configuration files
│   ├── __init__.py
│   ├── config_setup.py        # Environment and config setup
│   ├── llm_config.py          # LLM configuration
│   └── OAI_CONFIG_LIST.js     # OpenAI config (JS version)
└── tools/                     # Agent tools and functions
    ├── __init__.py
    └── functions/
        ├── gbts_parse.py      # GBTS parsing utilities
        ├── get_recycling_info.py  # Recycling information tool
        └── post_tiktok.py     # TikTok posting integration
```

## Core Components

### 1. agent_classes.py

**Purpose:** Defines the core agent classes and orchestration logic.

**Key Classes:**

#### AgentClass
Main orchestrator for the multi-agent system.

```python
class AgentClass:
    def __init__(self, role, llm_config):
        """
        Initialize agent system.
        
        Args:
            role: Agent role definition
            llm_config: LLM configuration dictionary
        """
```

**Attributes:**
- `group_chat`: GroupChat instance for multi-agent coordination
- `understanding_agent`: Agent for comprehension tasks
- `task_master`: Agent for task distribution
- `main_safety_agent`: Safety and moderation agent
- `digital_twin`: Associated digital twin agent

#### GeneralManager
User proxy agent for managing agent interactions.

**Sub-agents:**
- Understanding Agent
- Task Master
- Main Safety Agent

**Dependencies:**
- `autogen` - AutoGen framework
- `openai` - OpenAI API
- `dotenv` - Environment configuration
- `dt.digital_twin` - Digital Twin integration

**Configuration:**
```python
config = {
    "api_key": openai.api_key,
    "engine": "gpt-3",
    "temperature": 0.72,
    "max_tokens": 1500,
    "top_p": 1,
    "frequency_penalty": 0.5,
}
```

**Usage:**
```python
from agents.agent_classes import AgentClass

# Initialize agent system
agent_system = AgentClass(
    role="eco_assistant",
    llm_config=llm_config
)
```

### 2. Assistants

#### assistant_retrevial.py

**Purpose:** Implements assistant retrieval and management logic.

**Key Features:**
- Assistant discovery
- Capability matching
- Dynamic assistant selection

**Usage:**
Used internally by the agent system to find and assign appropriate assistants for tasks.

#### group_chat.py

**Purpose:** Manages group chat sessions between multiple agents.

**Key Features:**
- Multi-agent coordination
- Message routing
- Conversation state management
- Turn-based communication

**Integration:**
Works with AutoGen's GroupChat and GroupChatManager classes.

### 3. Configuration

#### config_setup.py

**Purpose:** Environment and configuration initialization.

**Key Functions:**
- Load environment variables
- Validate API keys
- Initialize configuration objects

**Environment Variables:**
- `OPENAI_API_KEY` - OpenAI API key
- `OPENAI_ORGANIZATION` - OpenAI organization ID

#### llm_config.py

**Purpose:** LLM-specific configuration management.

**Configuration Options:**
- Model selection
- Temperature settings
- Token limits
- Frequency/presence penalties
- Response formatting

**Default Configuration:**
```python
{
    "temperature": 0.72,
    "max_tokens": 1500,
    "top_p": 1,
    "frequency_penalty": 0.5,
}
```

### 4. Tools

Agent tools extend agent capabilities with specific functions.

#### gbts_parse.py

**Purpose:** Parse and process GBTS (Gaia-Bohm Thought Style) structures.

**Key Functions:**
- Parse GBTS tree structures
- Extract conversation flows
- Validate GBTS format

**Integration:**
Used by agents to understand and navigate GBTS conversation trees.

#### get_recycling_info.py

**Purpose:** Retrieve recycling information for materials.

**Key Functions:**
- Query recycling databases
- Material classification
- Recycling guidelines

**Example:**
```python
from agents.tools.functions.get_recycling_info import get_recycling_info

info = get_recycling_info("plastic bottle")
# Returns recycling instructions and facilities
```

#### post_tiktok.py

**Purpose:** Integration for posting content to TikTok.

**Key Functions:**
- Content formatting
- TikTok API integration
- Post scheduling

## Agent Communication Flow

1. **User Request** → General Manager receives request
2. **Task Analysis** → Understanding Agent analyzes task
3. **Task Distribution** → Task Master assigns to appropriate agents
4. **Safety Check** → Main Safety Agent validates actions
5. **Digital Twin Validation** → Digital Twin confirms agent actions
6. **Execution** → Agents execute tasks using tools
7. **Response Aggregation** → Results combined and formatted
8. **Response Delivery** → Final response returned to user

## Usage Examples

### Basic Agent Initialization

```python
from agents.agent_classes import AgentClass
from agents.config.llm_config import get_llm_config

# Get configuration
llm_config = get_llm_config()

# Create agent system
eco_agent = AgentClass(
    role="environmental_advisor",
    llm_config=llm_config
)
```

### Group Chat Setup

```python
from agents.assistants.group_chat import setup_group_chat

# Initialize group chat with multiple agents
group_chat = setup_group_chat(
    agents=[agent1, agent2, agent3],
    max_round=10
)

# Start conversation
group_chat.initiate_chat("How can we reduce carbon emissions?")
```

### Using Agent Tools

```python
from agents.tools.functions.get_recycling_info import get_recycling_info

# Get recycling information
result = get_recycling_info("aluminum can")
print(result)  # Recycling guidelines and facilities
```

## Testing

Tests located in `/tests/`:
- `agent_retrevial_tests.py` - Tests assistant retrieval
- `llm_config_test.py` - Tests configuration setup

Run tests:
```bash
pytest tests/agent_retrevial_tests.py
pytest tests/llm_config_test.py
```

## Configuration Best Practices

1. **API Keys**: Store in `.env` file, never commit
2. **Temperature**: Adjust based on use case (creative vs. factual)
3. **Max Tokens**: Balance between response quality and cost
4. **Frequency Penalty**: Prevent repetitive responses

## Dependencies

```python
# Core
autogen>=0.1.0
openai>=1.0.0
python-dotenv>=0.19.0

# Agent-specific
networkx>=2.6.0  # For conversation graphs
```

## Error Handling

Common errors and solutions:

1. **Missing API Key**
   ```
   Error: OPENAI_API_KEY not found
   Solution: Set in .env file
   ```

2. **Agent Communication Timeout**
   ```
   Error: Agent did not respond within timeout
   Solution: Increase timeout in group_chat config
   ```

3. **Tool Execution Failure**
   ```
   Error: Tool function failed
   Solution: Check tool dependencies and inputs
   ```

## Future Enhancements

- [ ] Enhanced agent learning capabilities
- [ ] Persistent agent memory across sessions
- [ ] Advanced task delegation algorithms
- [ ] Multi-modal agent capabilities
- [ ] Agent performance monitoring

## Related Documentation

- [Digital Twin Module](./digital-twin.md)
- [GBTS Module](./gbts.md)
- [Architecture Overview](../ARCHITECTURE.md)
