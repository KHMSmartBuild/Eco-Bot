# Eco-Buddies Module Documentation

## Overview

The Eco-Buddies module provides the user-facing interface for Eco-Bot, implementing chat functionality, vision capabilities, and user interaction management. This is where users directly interact with the environmental AI assistant.

## Module Structure

```
eco_buddies/
├── __init__.py
├── Eco_Bot.py           # Vision-based Eco-Bot implementation
├── Eco_Buddies.py       # Main Eco-Buddies orchestration
├── eco_chat.py          # Chat interface implementation
├── eco_bot_mvp.js       # JavaScript MVP implementation
├── utils/               # Utility modules
│   └── logging_setup.py # Logging configuration
└── tools/               # Eco-Buddies tools
    └── whisper_module.py # Audio transcription (Whisper)
```

## Core Components

### 1. Eco_Bot.py

**Purpose:** Vision-based Eco-Bot implementation using GPT-4 Vision.

**Key Class:**

#### EcoBot_Vision

Main class for image-based environmental analysis and guidance.

```python
class EcoBot_Vision:
    """
    Eco-Bot chat bot using OpenAI's GPT-4 Vision for image processing.
    """
    
    def __init__(self):
        """Initialize Eco-Bot Vision with conversation history."""
        super().__init__()
        self.conversation_history = []
```

**Key Methods:**

##### run_image()
Process and analyze images for environmental insights.

```python
def run_image(self):
    """
    Runs the image processing on the user-specified image.
    
    Returns:
        None
    
    TODO:
        - Prompt the user to input the image file path.
        - Process the image using GPT-4 Vision
        - Return environmental analysis
    """
```

**Use Cases:**
- Identify recyclable materials in images
- Analyze waste composition
- Verify proper recycling practices
- Detect environmental issues
- Provide visual guidance

**Dependencies:**
- `openai` - GPT-4 Vision API
- `cv2` - OpenCV for image processing
- `PIL` - Python Imaging Library
- `base64` - Image encoding
- `numpy` - Numerical operations

**Example Usage:**
```python
from eco_buddies.Eco_Bot import EcoBot_Vision

# Initialize vision bot
bot = EcoBot_Vision()

# Process an image
result = bot.run_image()
# Bot analyzes image and provides environmental guidance
```

**Image Processing Pipeline:**
1. Load image from path
2. Encode image to base64
3. Send to GPT-4 Vision API
4. Receive analysis
5. Format response
6. Update conversation history

**Supported Image Formats:**
- JPEG
- PNG
- WebP
- GIF (first frame)

**Features:**
- Real-time image analysis
- Conversation history tracking
- Multi-turn image discussions
- Environmental context awareness

### 2. Eco_Buddies.py

**Purpose:** Main orchestration for Eco-Buddies system.

**Key Features:**
- Coordinate multiple Eco-Bot instances
- Manage user sessions
- Route requests to appropriate handlers
- Aggregate responses

**Architecture:**
```
Eco_Buddies
    ├── Vision Module (Eco_Bot.py)
    ├── Chat Module (eco_chat.py)
    ├── Audio Module (whisper_module.py)
    └── Session Management
```

**Responsibilities:**
- User session lifecycle
- Module coordination
- Response aggregation
- Error handling

### 3. eco_chat.py

**Purpose:** Text-based chat interface for Eco-Bot.

**Key Features:**
- Natural language processing
- Context-aware responses
- Multi-turn conversations
- Environmental knowledge integration

**Chat Flow:**
1. User sends text message
2. Message processed for intent
3. Context retrieved from history
4. Agent generates response
5. Response formatted and returned
6. History updated

**Example:**
```python
from eco_buddies.eco_chat import EcoChat

# Initialize chat
chat = EcoChat()

# Send message
response = chat.send_message("How can I reduce plastic waste?")
print(response)
# "Here are 5 ways to reduce plastic waste: ..."
```

**Supported Intents:**
- Recycling questions
- Waste reduction advice
- Environmental facts
- Eco-friendly alternatives
- Sustainability tips

### 4. eco_bot_mvp.js

**Purpose:** JavaScript MVP implementation for web integration.

**Key Features:**
- Client-side chat interface
- Real-time communication
- Browser-based interactions
- API integration

**Integration:**
- Connects to Python backend
- Handles UI interactions
- Manages client state
- Formats displays

**Example:**
```javascript
import EcoBotMVP from './eco_buddies/eco_bot_mvp.js';

// Initialize
const ecoBot = new EcoBotMVP({
  apiEndpoint: '/api/chat',
  containerId: 'chat-container'
});

// Start chat
ecoBot.initialize();
```

### 5. Tools

#### whisper_module.py

**Purpose:** Audio transcription using OpenAI Whisper.

**Key Features:**
- Speech-to-text conversion
- Multi-language support
- Real-time transcription
- Audio file processing

**Supported Formats:**
- MP3
- WAV
- M4A
- FLAC

**Usage:**
```python
from eco_buddies.tools.whisper_module import transcribe_audio

# Transcribe audio file
text = transcribe_audio("recording.mp3")
print(text)
# "How can I recycle batteries?"
```

**Use Cases:**
- Voice commands
- Audio message processing
- Accessibility features
- Multilingual support

**Configuration:**
```python
whisper_config = {
    "model": "whisper-1",
    "language": "en",
    "response_format": "text"
}
```

### 6. Utils

#### logging_setup.py

**Purpose:** Configure logging for Eco-Buddies module.

**Key Features:**
- Structured logging
- Log rotation
- Multiple log levels
- Context tracking

**Log Levels:**
- DEBUG - Detailed diagnostic info
- INFO - General informational messages
- WARNING - Warning messages
- ERROR - Error messages
- CRITICAL - Critical failures

**Configuration:**
```python
from eco_buddies.utils.logging_setup import setup_logging

# Initialize logging
logger = setup_logging(
    name="eco_buddies",
    level="INFO",
    log_file="eco_buddies.log"
)

# Use logger
logger.info("User started chat session")
logger.error("Failed to process image", exc_info=True)
```

**Log Format:**
```
2023-10-29 12:00:00 [INFO] eco_buddies.chat: User message received
2023-10-29 12:00:01 [DEBUG] eco_buddies.vision: Processing image...
2023-10-29 12:00:02 [INFO] eco_buddies.chat: Response sent
```

## Integration with Other Modules

### With Agents Module
```python
from agents.agent_classes import AgentClass
from eco_buddies.Eco_Bot import EcoBot_Vision

# Create agent
agent = AgentClass(role="vision", llm_config=config)

# Create vision bot with agent
vision_bot = EcoBot_Vision()
# Use agent for advanced reasoning
```

### With GBTS Module
```python
from gbts.gbts import PromptTree
from eco_buddies.eco_chat import EcoChat

# Create chat with GBTS integration
chat = EcoChat()
tree = PromptTree()

# Track conversation in GBTS tree
# Enable advanced conversation management
```

### With Streamlit App
```python
import streamlit as st
from eco_buddies.Eco_Bot import EcoBot_Vision

# Streamlit integration
uploaded_file = st.file_uploader("Upload image")
if uploaded_file:
    bot = EcoBot_Vision()
    result = bot.run_image(uploaded_file)
    st.write(result)
```

## Usage Examples

### Basic Chat Session

```python
from eco_buddies.eco_chat import EcoChat

# Start chat
chat = EcoChat()

# Multi-turn conversation
messages = [
    "What items can I recycle?",
    "What about plastic bags?",
    "Where can I drop them off?"
]

for msg in messages:
    response = chat.send_message(msg)
    print(f"User: {msg}")
    print(f"Bot: {response}\n")
```

### Vision Analysis

```python
from eco_buddies.Eco_Bot import EcoBot_Vision
import cv2

# Initialize vision bot
vision_bot = EcoBot_Vision()

# Load and analyze image
image_path = "waste_photo.jpg"
analysis = vision_bot.run_image(image_path)

print(analysis)
# "This image shows mixed recyclables and trash.
#  The plastic bottle should go in recycling bin.
#  The food wrapper should go in trash..."
```

### Voice Interaction

```python
from eco_buddies.tools.whisper_module import transcribe_audio
from eco_buddies.eco_chat import EcoChat

# Transcribe voice input
audio_file = "user_question.mp3"
text = transcribe_audio(audio_file)

# Process with chat
chat = EcoChat()
response = chat.send_message(text)

print(f"User (voice): {text}")
print(f"Bot: {response}")
```

### Complete Eco-Buddies Session

```python
from eco_buddies.Eco_Buddies import EcoBuddies
from eco_buddies.utils.logging_setup import setup_logging

# Setup logging
logger = setup_logging("eco_buddies_session")

# Initialize Eco-Buddies
eco_buddies = EcoBuddies()

# Start session
session = eco_buddies.start_session(user_id="user_123")

# Text interaction
response = session.chat("How do I compost?")
logger.info(f"Chat response: {response}")

# Vision interaction
image_result = session.analyze_image("compost_bin.jpg")
logger.info(f"Vision analysis: {image_result}")

# Voice interaction
audio_text = session.transcribe_audio("question.mp3")
voice_response = session.chat(audio_text)
logger.info(f"Voice response: {voice_response}")

# End session
session.end()
```

## Configuration

### Environment Variables

```bash
# .env file
OPENAI_API_KEY=your_api_key_here
OPENAI_ORGANIZATION=your_org_id_here
ECO_BOT_LOG_LEVEL=INFO
ECO_BOT_MAX_HISTORY=100
```

### Chat Configuration

```python
chat_config = {
    "model": "gpt-4",
    "temperature": 0.7,
    "max_tokens": 500,
    "system_prompt": "You are an environmental assistant...",
    "max_history": 50
}
```

### Vision Configuration

```python
vision_config = {
    "model": "gpt-4-vision-preview",
    "max_image_size": 20 * 1024 * 1024,  # 20MB
    "supported_formats": ["jpg", "png", "webp"],
    "detail": "high"
}
```

## Error Handling

### Common Errors

1. **Missing API Key**
```python
# Error: OpenAI API key not found
# Solution: Set OPENAI_API_KEY in .env
```

2. **Image Too Large**
```python
# Error: Image file too large
# Solution: Resize image before processing
```

3. **Unsupported Audio Format**
```python
# Error: Audio format not supported
# Solution: Convert to MP3 or WAV
```

### Error Recovery

```python
from eco_buddies.eco_chat import EcoChat

chat = EcoChat()

try:
    response = chat.send_message(message)
except Exception as e:
    logger.error(f"Chat error: {e}")
    response = "I'm sorry, I encountered an error. Please try again."
```

## Performance Optimization

### Caching Responses
```python
from functools import lru_cache

@lru_cache(maxsize=100)
def get_recycling_info(item):
    # Cache common queries
    return fetch_recycling_info(item)
```

### Batching Requests
```python
# Process multiple images in batch
images = ["img1.jpg", "img2.jpg", "img3.jpg"]
results = vision_bot.batch_process(images)
```

### Session Management
```python
# Reuse sessions for multiple requests
session = chat.create_session()
for msg in messages:
    session.send(msg)
session.close()
```

## Testing

```bash
# Run Eco-Buddies tests
pytest tests/ -k eco_buddies

# Test chat functionality
pytest tests/test_eco_chat.py

# Test vision processing
pytest tests/test_eco_vision.py
```

## Dependencies

```python
# requirements.txt
openai>=1.0.0
opencv-python>=4.8.0
Pillow>=10.0.0
numpy>=1.24.0
python-dotenv>=0.19.0
```

## Future Enhancements

- [ ] Multi-modal interactions (text + image + audio simultaneously)
- [ ] Personalized user profiles and preferences
- [ ] Integration with IoT devices
- [ ] Augmented reality features
- [ ] Gamification elements
- [ ] Social sharing features
- [ ] Offline mode support

## Related Documentation

- [Agents Module](./agents.md)
- [GBTS Module](./gbts.md)
- [Streamlit App](./streamlit-app.md)
- [Architecture Overview](../ARCHITECTURE.md)
