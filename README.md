## this code base is not currently working more of a mess then a code base but a piece of art in the making non the less
# Eco-Bot
EcoBot is envisioned as an interactive, educational, and engaging AI bot focused on promoting ecological and environmental awareness and actions. It's designed to navigate users through a rich, exploratory journey within the realms of environmental knowledge, utilizing a unique approach, potentially named the Gaia-Bohm Thought Style (GBTS)

# README

## Eco-Bot

Eco-Bot is a multi-agent system project aimed at enhancing communication and understanding among agents and their digital twins using a Gaia-Bohm Thought Style (GBTS) guided prompt tree system.

## Hybrid Decentralized Memory System with Truth Datacore

Eco-Bot integrates a revolutionary Hybrid Decentralized Memory System to enhance its data storage, retrieval, and validation capabilities. This system combines the trustworthiness of blockchain technology with the adaptability of P2P networks and the contextual richness of neural grids.

### System Components:

- **Blockchain-Based Truth Datacore:** An immutable database of verified facts, ensuring data integrity through consensus and efficient retrieval through categorization.
- **P2P Information Nodes:** Storage for transient and agent-specific data, facilitating data exchange within the network.
- **Neural Memory Grid Overlay:** Provides context between various data pieces, enhancing understanding and relevance.

### Special Features:

- **Specialized Librarian Agents:** Enhance data retrieval, fact-checking, and bias mitigation.
- **Versioning System:** Manages dynamic, evolving facts, ensuring transparency and historical context.

### Benefits:

- **Trustworthiness:** Reliability through an immutable database.
- **Combat Misinformation:** A robust defense against false data.
- **Clear Data Distinction:** Differentiates between verified and auxiliary data.

## Table of Contents

1. Installation
2. Usage
3. Project Structure
4. Testing
5. Deployment
6. Contributing
7. License
8. Contact

## Installation

1. **Clone the repository**:
    
    ```bash
    git clone [Repository Link]
    cd Eco-Bot
    ```
    
2. **Set up a virtual environment** (optional, but recommended):
    
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```
    
3. **Install the dependencies**:
    
    ```bash
    pip install -r requirements.txt
    ```
    
4. **Set up the database**:
    - Instructions for setting up the database...

## Usage

1. **Start the Streamlit app**:
    
    ```bash
    streamlit run streamlit_app/app.py
    ```
    
2. **Interacting with the system**:
    - Instructions for interacting with the system...

## Project Structure

- `agents/`: Contains the classes and logic for agents and digital twin agents.
- `gbts/`: Contains the classes and logic for managing the GBTS and prompt tree system.
- `streamlit_app/`: Contains the Streamlit application code for monitoring and management.
- ... (other directories and files)

## Testing

Run the test suite using the following commands:

```bash
# Run all tests
npm run test

# Run tests in watch mode
npm run test:watch

# Run tests with coverage
npm run test:coverage

# Run Python tests
pytest
```

## 📚 Storybook Component Library

Eco-Bot includes a fully-documented Storybook component library for developing, testing, and showcasing UI components.

### Running Storybook

Start the Storybook development server:

```bash
npm run storybook
```

This will open Storybook at `http://localhost:6006`.

### Building Storybook

Build a static version for deployment:

```bash
npm run build-storybook
```

The output will be in the `storybook-static/` directory.

### Component Categories

#### Components
Core UI components used throughout the application:
- **Avatar** - Displays eco-buddy profile images with customizable sizes
- **ChatBox** - Text input component for user messages
- **ChatArea** - Combined avatar and message display for conversations

#### Visualizations
Interactive data visualizations:
- **GBTSTree** - Tree visualization of the Gaia-Bohm Thought Style conversation structure

### JSON Data Management

The Storybook uses a centralized JSON data management system located in `stories/data/storyData.js` that provides:

- **GBTS Prompts** - Structured prompts for each GBTS stage
- **Visualization Data** - Node and link data for tree visualizations
- **Eco-Bot Personality** - Character traits and behaviors
- **Sample Conversations** - Example dialogues for testing

Example usage:
```javascript
import { 
  gbtsVisualizationData, 
  ecoBuddies, 
  validateGBTSData 
} from './stories/data/storyData';

// Validate data before use
const result = validateGBTSData(myData);
if (result.valid) {
  // Use the data
}
```

### GBTS Structure

The Gaia-Bohm Thought Style structures conversations as a growing tree:

1. 🌱 **Seed of Inquiry** - The initial question
2. 🌿 **Branches of Understanding** - Related sub-topics
3. 🍃 **Leaves of Application** - Practical applications
4. 🌳 **Roots of Connection** - Deep underlying connections
5. 🌲 **Forest of Exploration** - Broader related topics
6. 🌴 **Canopy of Synthesis** - Integration of insights
7. 🌾 **Harvest of Wisdom** - Key takeaways

## Deployment
Todo:
Instructions for deploying the project using Docker, etc...

## Contributing

Information about how others can contribute to the project...

## License

Information about the project's license...

## Contact

Your Name – [info@KHMSmartBuild](mailto:info@KHMSmartBuild)

Project Link: [Eco-Bot]