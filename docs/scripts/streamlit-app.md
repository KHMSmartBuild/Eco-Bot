# Streamlit Application Documentation

## Overview

The Streamlit application provides a web-based user interface for interacting with Eco-Bot. It includes multiple pages for different functionalities, including chat, games, GBTS visualization, and system monitoring.

## Module Structure

```
streamlit_app/
├── __init__.py
├── eco_bot_main.py              # Main application entry point
├── pages/                       # Application pages
│   ├── __init__.py
│   ├── Eco-BotAPP.py           # Main Eco-Bot application page
│   ├── MVP.py                  # MVP interface
│   ├── ZeroWasteChallange.py   # Zero Waste Challenge page
│   ├── eco_bot_system.py       # System monitoring page
│   ├── eco_game_streamlit.py   # Eco game interface
│   ├── gbts_interaction_page.py # GBTS interaction page
│   └── groupchat_screen.py     # Group chat interface
└── assets/                      # UI assets
    ├── __init__.py
    ├── game/                   # Game assets
    │   └── game.js            # Game logic
    ├── images/                # Image assets
    │   ├── __init__.py
    │   └── interactive_avatar.js # Avatar interactions
    └── styles/                # Style components
        ├── __init__.py
        ├── Avatar.js          # Avatar styling
        ├── ChatArea.js        # Chat area styling
        └── ChatBox.js         # Chat box styling
```

## Main Application

### eco_bot_main.py

**Purpose:** Main entry point for the Streamlit application.

**Key Features:**
- Application initialization
- Page routing
- Session state management
- Global configuration

**Usage:**
```bash
streamlit run streamlit_app/eco_bot_main.py
```

**Configuration:**
```python
st.set_page_config(
    page_title="Eco-Bot",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)
```

**Session State:**
- User authentication
- Conversation history
- Current page
- User preferences

## Application Pages

### 1. Eco-BotAPP.py

**Purpose:** Main Eco-Bot application interface.

**Features:**
- Chat interface
- Image upload and analysis
- Voice input
- Conversation history
- Settings panel

**Layout:**
```
┌─────────────────────────────────────┐
│         Eco-Bot Header              │
├─────────────┬───────────────────────┤
│  Sidebar    │   Chat Area           │
│  - Settings │   - Messages          │
│  - History  │   - Input Box         │
│  - Tools    │   - Image Upload      │
│             │   - Voice Input       │
└─────────────┴───────────────────────┘
```

**Components:**
```python
# Chat interface
chat_container = st.container()
with chat_container:
    display_messages()
    user_input = st.text_input("Ask me about recycling...")
    
# Image upload
uploaded_file = st.file_uploader("Upload image", type=['jpg', 'png'])

# Voice input
audio_file = st.audio_input("Record your question")
```

### 2. MVP.py

**Purpose:** Minimal Viable Product interface for testing.

**Features:**
- Simplified chat interface
- Basic functionality testing
- Quick interactions
- Performance monitoring

**Use Case:**
- Development testing
- User acceptance testing
- Feature validation

### 3. ZeroWasteChallange.py

**Purpose:** Zero Waste Challenge game/tracker.

**Features:**
- Daily waste tracking
- Challenge goals
- Progress visualization
- Achievements
- Leaderboard

**Game Flow:**
1. User sets waste reduction goal
2. Daily check-ins with waste data
3. Track progress over time
4. Earn achievements
5. Compare with community

**Metrics:**
- Total waste reduced
- Recycling rate
- Composting percentage
- Carbon footprint reduction

**Visualization:**
```python
import plotly.express as px

# Progress chart
fig = px.line(
    waste_data,
    x='date',
    y='waste_kg',
    title='Your Waste Reduction Journey'
)
st.plotly_chart(fig)
```

### 4. eco_bot_system.py

**Purpose:** System monitoring and administration.

**Features:**
- Agent status monitoring
- Performance metrics
- Error logs
- System health
- Configuration management

**Metrics Displayed:**
- Active agents count
- Response times
- API usage
- Error rates
- User sessions

**Dashboard Sections:**
- System Overview
- Agent Performance
- API Statistics
- Error Logs
- Configuration

### 5. eco_game_streamlit.py

**Purpose:** Interactive environmental education game.

**Game Elements:**
- Quiz questions
- Sorting challenges
- Recycling simulations
- Points and rewards

**Example:**
```python
# Recycling sorting game
st.header("Sort the Items!")

items = ["Plastic Bottle", "Banana Peel", "Glass Jar", "Pizza Box"]
bins = ["Recycling", "Compost", "Trash"]

for item in items:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write(item)
    with col2:
        selection = st.selectbox("", bins, key=item)
        
if st.button("Check Answers"):
    score = calculate_score()
    st.success(f"Score: {score}/4")
```

### 6. gbts_interaction_page.py

**Purpose:** Interactive GBTS conversation tree visualization.

**Features:**
- Real-time tree visualization
- Node inspection
- Branch exploration
- Conversation replay
- Export capabilities

**Visualization:**
```python
import streamlit.components.v1 as components

# Embed D3.js visualization
components.html(
    gbts_visualization_html,
    height=600,
    scrolling=True
)
```

**Interactions:**
- Click nodes to view details
- Hover for quick info
- Zoom and pan
- Expand/collapse branches

### 7. groupchat_screen.py

**Purpose:** Multi-agent group chat interface.

**Features:**
- Multiple agent participation
- Real-time message updates
- Agent identification
- Conversation flow visualization

**Layout:**
```python
# Agent list sidebar
with st.sidebar:
    st.header("Active Agents")
    for agent in agents:
        st.write(f"🤖 {agent.name}")
        
# Chat area
chat_container = st.container()
with chat_container:
    for message in messages:
        st.chat_message(message.agent_name).write(message.content)
        
# Input
user_input = st.chat_input("Type your message...")
```

## Assets

### Game Assets

#### game.js

**Purpose:** Game logic and state management.

**Key Features:**
- Game state management
- Score tracking
- Level progression
- Animation handling

**Game Types:**
- Sorting game
- Quiz game
- Memory game
- Simulation game

### Image Assets

#### interactive_avatar.js

**Purpose:** Animated avatar for user interaction.

**Features:**
- Idle animations
- Speaking animations
- Emotion expressions
- Interactive responses

**States:**
- Idle
- Listening
- Thinking
- Speaking
- Success/Error feedback

### Style Components

#### Avatar.js

**Purpose:** Avatar styling and animations.

**CSS Classes:**
- `.avatar-container`
- `.avatar-image`
- `.avatar-animation`
- `.avatar-state-*`

#### ChatArea.js

**Purpose:** Chat area styling.

**CSS Layout:**
```css
.chat-area {
  display: flex;
  flex-direction: column;
  height: 100%;
  overflow-y: auto;
}

.message-container {
  padding: 10px;
  margin: 5px;
  border-radius: 8px;
}

.user-message {
  background: #e3f2fd;
  align-self: flex-end;
}

.bot-message {
  background: #f1f8e9;
  align-self: flex-start;
}
```

#### ChatBox.js

**Purpose:** Input chat box styling.

**Features:**
- Auto-resize
- Multi-line support
- Send button styling
- Attachment icons

## Page Navigation

### Sidebar Navigation

```python
# In eco_bot_main.py
def main():
    st.sidebar.title("Navigation")
    
    pages = {
        "🏠 Home": home_page,
        "💬 Chat": chat_page,
        "🎮 Game": game_page,
        "📊 GBTS": gbts_page,
        "👥 Group Chat": groupchat_page,
        "⚙️ System": system_page
    }
    
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    pages[selection]()
```

## Session Management

### User Sessions

```python
# Initialize session state
if 'user_id' not in st.session_state:
    st.session_state.user_id = generate_user_id()
    
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []
    
if 'preferences' not in st.session_state:
    st.session_state.preferences = default_preferences()
```

### State Persistence

```python
# Save state
def save_session():
    session_data = {
        'user_id': st.session_state.user_id,
        'history': st.session_state.conversation_history,
        'preferences': st.session_state.preferences
    }
    save_to_db(session_data)
    
# Load state
def load_session(user_id):
    session_data = load_from_db(user_id)
    st.session_state.update(session_data)
```

## Integration Examples

### With Eco-Buddies

```python
import streamlit as st
from eco_buddies.Eco_Bot import EcoBot_Vision
from eco_buddies.eco_chat import EcoChat

# Initialize bot
if 'chat_bot' not in st.session_state:
    st.session_state.chat_bot = EcoChat()
    
# Chat interaction
user_input = st.chat_input("Ask me anything...")
if user_input:
    response = st.session_state.chat_bot.send_message(user_input)
    st.session_state.conversation_history.append({
        'user': user_input,
        'bot': response
    })
```

### With GBTS

```python
from gbts.gbts import PromptTree
import streamlit.components.v1 as components

# Visualize conversation tree
tree = PromptTree()
# ... populate tree from conversation ...

# Render visualization
visualization_html = tree.to_html()
components.html(visualization_html, height=600)
```

### With Agents

```python
from agents.agent_classes import AgentClass

# Initialize agents for group chat
if 'agents' not in st.session_state:
    st.session_state.agents = [
        AgentClass(role="recycling_expert", llm_config=config),
        AgentClass(role="composting_expert", llm_config=config),
        AgentClass(role="zero_waste_expert", llm_config=config)
    ]
    
# Group chat
for agent in st.session_state.agents:
    with st.chat_message(agent.role):
        response = agent.respond(user_input)
        st.write(response)
```

## Customization

### Themes

```python
# Custom theme
st.markdown("""
<style>
    .stApp {
        background-color: #e8f5e9;
    }
    .stButton>button {
        background-color: #4caf50;
        color: white;
    }
</style>
""", unsafe_allow_html=True)
```

### Custom Components

```python
# Custom metric display
def eco_metric(label, value, delta=None):
    st.metric(
        label=label,
        value=value,
        delta=delta,
        delta_color="inverse"  # Green for decrease in waste
    )
    
eco_metric("Waste Reduced", "15 kg", "-5 kg this week")
```

## Performance Optimization

### Caching

```python
@st.cache_data
def load_recycling_data():
    # Load and cache recycling information
    return fetch_recycling_database()
    
@st.cache_resource
def initialize_bot():
    # Cache bot initialization
    return EcoChat()
```

### Lazy Loading

```python
# Load heavy components only when needed
if st.session_state.page == "gbts":
    load_gbts_visualization()
```

## Deployment

### Local Development

```bash
streamlit run streamlit_app/eco_bot_main.py
```

### Production Deployment

```bash
# With Docker
docker build -t eco-bot-streamlit .
docker run -p 8501:8501 eco-bot-streamlit

# With Streamlit Cloud
# Push to GitHub and connect repository
```

### Configuration

```toml
# .streamlit/config.toml
[server]
port = 8501
enableCORS = false
enableXsrfProtection = true

[theme]
primaryColor = "#4caf50"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"
```

## Testing

```python
# tests/test_streamlit_app.py
from streamlit.testing.v1 import AppTest

def test_main_page():
    at = AppTest.from_file("streamlit_app/eco_bot_main.py")
    at.run()
    assert not at.exception
    
def test_chat_interaction():
    at = AppTest.from_file("streamlit_app/pages/Eco-BotAPP.py")
    at.run()
    at.text_input[0].input("How do I recycle?")
    at.run()
    assert len(at.session_state.conversation_history) > 0
```

## Dependencies

```python
# requirements.txt
streamlit>=1.28.0
plotly>=5.17.0
pandas>=2.0.0
pillow>=10.0.0
```

## Future Enhancements

- [ ] Mobile-responsive design
- [ ] Dark mode support
- [ ] Multi-language interface
- [ ] Voice commands
- [ ] Real-time notifications
- [ ] Social features (sharing, leaderboards)
- [ ] Advanced analytics dashboard

## Related Documentation

- [Eco-Buddies Module](./eco-buddies.md)
- [GBTS Module](./gbts.md)
- [Agents Module](./agents.md)
- [Architecture Overview](../ARCHITECTURE.md)
