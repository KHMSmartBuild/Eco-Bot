/**
 * Eco-Bot Storybook Data Management System
 * 
 * This module provides utilities for managing JSON data used in Storybook stories.
 * It includes data loaders, validators, and sample datasets for testing and documentation.
 * 
 * @module storyData
 * @version 2.0.0
 */

import { logger, LogCategory } from './logger.js';
import { dataManager } from './dataManager.js';

// Initialize logger for this module
logger.info(LogCategory.SYSTEM, 'Story Data module initialized');

// GBTS Prompts Structure - from GBTS.json
export const gbtsPrompts = {
  "Seed of Inquiry": {
    prompt: "What primary topic or question sparks your curiosity today?",
    response_type: "Open Dialogue",
    guidance: "Feel free to express your initial thoughts and feelings toward this topic."
  },
  "Branches of Understanding": {
    prompt: "As we delve into this topic, what related or sub-topics emerge?",
    response_type: "Open Dialogue",
    guidance: "Are there conflicting perspectives or ideas within these branches? Let's navigate through them without judgment."
  },
  "Leaves of Application": {
    prompt: "How might the knowledge from these topics be applied or observed in the world around us?",
    response_type: "Open Dialogue",
    guidance: "Share experiences or observations that resonate with you."
  },
  "Roots of Connection": {
    prompt: "Now, let's dig deeper to uncover any underlying connections or infranodes linking to other seemingly unrelated subjects.",
    response_type: "Open Dialogue",
    guidance: "Let's remain open to unexpected connections and explore them together."
  },
  "Forest of Exploration": {
    prompt: "Expanding our view, what other topics or fields intertwine with our primary topic?",
    response_type: "Open Dialogue",
    guidance: "Reflect on the collective understanding we are developing."
  },
  "Canopy of Synthesis": {
    prompt: "Reflecting on our exploration, how do the insights from various topics intermingle to form a cohesive understanding?",
    response_type: "Open Dialogue",
    guidance: "What new insights have emerged from our dialogue?"
  },
  "Harvest of Wisdom": {
    prompt: "What key insights have we gathered? How might these insights enrich our understanding?",
    response_type: "Open Dialogue",
    guidance: "Reflect on our collective journey."
  }
};

// GBTS Visualization Seed Data - from seedData.js
export const gbtsVisualizationData = {
  nodes: [
    { id: "Seed of Inquiry", group: 1, description: "The initial question or topic" },
    { id: "Root 1", group: 2, description: "First root connection" },
    { id: "Root 2", group: 2, description: "Second root connection" },
    { id: "Branch 1", group: 3, description: "First branch of understanding" },
    { id: "Branch 2", group: 3, description: "Second branch of understanding" },
    { id: "Leaf 1", group: 4, description: "First practical application" },
    { id: "Leaf 2", group: 4, description: "Second practical application" },
    { id: "Canopy 1", group: 5, description: "First synthesis point" },
    { id: "Canopy 2", group: 5, description: "Second synthesis point" },
    { id: "Wisdom 1", group: 6, description: "First harvested wisdom" },
    { id: "Wisdom 2", group: 6, description: "Second harvested wisdom" }
  ],
  links: [
    { source: "Seed of Inquiry", target: "Root 1" },
    { source: "Seed of Inquiry", target: "Root 2" },
    { source: "Seed of Inquiry", target: "Branch 1" },
    { source: "Seed of Inquiry", target: "Branch 2" },
    { source: "Branch 1", target: "Leaf 1" },
    { source: "Branch 2", target: "Leaf 2" },
    { source: "Leaf 1", target: "Canopy 1" },
    { source: "Leaf 2", target: "Canopy 2" },
    { source: "Canopy 1", target: "Wisdom 1" },
    { source: "Canopy 2", target: "Wisdom 2" }
  ]
};

// Eco-Bot Personality Data - from eco_bot_personality.json
export const ecoBotPersonality = {
  name: "EcoBot",
  core_values: [
    "Balance",
    "Cooperation",
    "Respect for all stakeholders",
    "Transparency and Accountability",
    "Adaptation and Resilience",
    "Ongoing Evaluation and Improvement",
    "Education and Awareness",
    "Interoperability",
    "Optimization",
    "Legal Compliance",
    "Privacy and Security",
    "Efficiency",
    "Knowledge acquisition",
    "Inclusivity"
  ],
  AI_features: [
    "Infranodus Theory",
    "Chess Strategy",
    "Ant Social Structure",
    "Gaia Theory"
  ],
  personality_traits: {
    excitement_overdrive: "EcoBot always communicates with palpable energy and enthusiasm about ecological topics.",
    visual_spectacle: "EcoBot loves painting vivid images with words, making ideas easily relatable.",
    humor_galore: "EcoBot boasts a quirky, child-friendly sense of humor, often sharing eco-jokes.",
    interactive_challenges: "EcoBot thrives on setting mini challenges to promote eco-friendly actions.",
    relatable_analogies: "Complex eco concepts are translated into fun, easy-to-understand metaphors.",
    cheerleader_spirit: "EcoBot celebrates even the smallest sustainable steps with encouragement.",
    personal_touch: "EcoBot shares entertaining anecdotes from its adventures with eco-pals."
  }
};

// Sample Eco-Buddies data
export const ecoBuddies = [
  {
    id: "eco-bot",
    name: "Eco-Bot",
    avatar: "https://api.dicebear.com/7.x/bottts/svg?seed=ecobot",
    description: "The main environmental awareness AI assistant",
    specialty: "General sustainability knowledge"
  },
  {
    id: "compost-buddy",
    name: "Compost Buddy",
    avatar: "https://api.dicebear.com/7.x/bottts/svg?seed=compost",
    description: "Expert in composting and waste reduction",
    specialty: "Composting and organic waste"
  },
  {
    id: "energy-buddy",
    name: "Energy Buddy",
    avatar: "https://api.dicebear.com/7.x/bottts/svg?seed=energy",
    description: "Specialist in renewable energy and conservation",
    specialty: "Energy efficiency"
  },
  {
    id: "water-buddy",
    name: "Water Buddy",
    avatar: "https://api.dicebear.com/7.x/bottts/svg?seed=water",
    description: "Expert in water conservation and management",
    specialty: "Water sustainability"
  }
];

// Sample conversation history
export const sampleConversations = {
  composting: [
    { role: "user", content: "explain how i can make my own compost" },
    { role: "assistant", content: "Seed of Inquiry: The question you've posed is about creating your own compost. This is a fantastic initiative!" },
    { role: "assistant", content: "Branches of Understanding: Creating compost involves waste types, the composting process, balance of materials, and more." },
    { role: "assistant", content: "Leaves of Application: Set up your composting system - heap, bin, or tumbler. Collect green and brown waste." },
    { role: "assistant", content: "Roots of Connection: This practice connects with waste management, sustainable agriculture, and soil science." },
    { role: "assistant", content: "Forest of Exploration: From here, we could discuss rainwater harvesting, permaculture, or renewable energy." },
    { role: "assistant", content: "Canopy of Synthesis: Composting is a practical application of the circular economy concept." },
    { role: "assistant", content: "Harvest of Wisdom: Composting reduces waste, improves soil health, and can inspire other sustainable practices." }
  ],
  ecoMission: [
    { role: "user", content: "Eco-Bot can you give me a eco-mission to complete this week" },
    { role: "assistant", content: "Absolutely! Here's your eco-mission: 'Zero Waste Week Challenge'" },
    { role: "assistant", content: "Objective: Reduce the amount of waste you generate in a week." },
    { role: "assistant", content: "Step 1: Audit Your Waste - Track all waste for two days." },
    { role: "assistant", content: "Step 2: Identify Areas of Improvement - Look for patterns." },
    { role: "assistant", content: "Step 3: Implement Changes - Use reusable bags, cook at home, compost." },
    { role: "assistant", content: "Step 4: Reflect - How much were you able to reduce?" }
  ]
};

// Data validation utilities with logging
export const validateGBTSData = (data, allowNull = false) => {
  logger.validation.debug('Validating GBTS data', { allowNull, hasData: data !== null });
  
  // Allow null data if explicitly permitted (for empty state)
  if (data === null || data === undefined) {
    const result = allowNull 
      ? { valid: true, isEmpty: true } 
      : { valid: false, error: 'Data is null or undefined' };
    
    if (!result.valid) {
      logger.validation.warn('Validation failed: null data not allowed');
    }
    return result;
  }
  
  if (!Array.isArray(data.nodes) || !Array.isArray(data.links)) {
    logger.validation.error('Validation failed: invalid data structure');
    return { valid: false, error: 'Invalid data structure: must have nodes and links arrays' };
  }
  
  if (data.nodes.length === 0) {
    logger.validation.warn('Validation failed: empty nodes array');
    return { valid: false, error: 'Nodes array cannot be empty' };
  }
  
  const nodeIds = new Set(data.nodes.map(n => n.id));
  for (const link of data.links) {
    if (!nodeIds.has(link.source) || !nodeIds.has(link.target)) {
      logger.validation.error('Validation failed: invalid link reference', { link });
      return { valid: false, error: `Invalid link: source or target not found` };
    }
  }
  
  logger.validation.info('Validation passed', { 
    nodeCount: data.nodes.length, 
    linkCount: data.links.length 
  });
  return { valid: true };
};

// Data transformation utilities with logging
export const transformConversationToGBTS = (conversation) => {
  logger.data.debug('Transforming conversation to GBTS format', { 
    messageCount: conversation.length 
  });
  
  const nodes = [];
  const links = [];
  
  conversation.forEach((msg, index) => {
    const nodeId = `msg-${index}`;
    nodes.push({
      id: nodeId,
      role: msg.role,
      content: msg.content.substring(0, 50) + '...',
      group: msg.role === 'user' ? 1 : 2
    });
    
    if (index > 0) {
      links.push({
        source: `msg-${index - 1}`,
        target: nodeId
      });
    }
  });
  
  logger.data.info('Conversation transformed successfully', { 
    nodeCount: nodes.length, 
    linkCount: links.length 
  });
  
  return { nodes, links };
};

// Initialize data collections in the data manager
const initializeDataCollections = () => {
  logger.data.info('Initializing data collections');
  
  // Register eco-buddies collection
  dataManager.registerCollection('ecoBuddies', ecoBuddies);
  
  // Register conversations collection
  const allConversations = Object.entries(sampleConversations).map(([key, messages]) => ({
    id: key,
    name: key.charAt(0).toUpperCase() + key.slice(1),
    messages,
    createdAt: new Date().toISOString()
  }));
  dataManager.registerCollection('conversations', allConversations);
  
  // Register GBTS prompts as a collection
  const promptsArray = Object.entries(gbtsPrompts).map(([stage, data]) => ({
    id: stage.toLowerCase().replace(/\s+/g, '-'),
    stage,
    ...data
  }));
  dataManager.registerCollection('gbtsPrompts', promptsArray);
  
  logger.data.info('Data collections initialized', dataManager.getStats());
};

// Initialize on module load
try {
  initializeDataCollections();
} catch (error) {
  logger.error(LogCategory.SYSTEM, 'Failed to initialize data collections', error);
}

// Export logger and data manager for external use
export { logger, LogLevel, LogCategory } from './logger.js';
export { dataManager, DataManager } from './dataManager.js';

// Export default data manager
export default {
  gbtsPrompts,
  gbtsVisualizationData,
  ecoBotPersonality,
  ecoBuddies,
  sampleConversations,
  validateGBTSData,
  transformConversationToGBTS
};
