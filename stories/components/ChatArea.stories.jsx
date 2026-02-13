import ChatArea from './ChatArea';

// Sample conversation data
const sampleConversation = [
  { role: 'user', content: 'Hello Eco-Bot! Can you explain composting?' },
  { role: 'assistant', content: 'Hello! 🌱 Composting is nature\'s way of recycling organic matter into nutrient-rich soil. It\'s like giving your food scraps a second life!' },
  { role: 'user', content: 'What can I compost at home?' },
  { role: 'assistant', content: 'Great question! You can compost fruit and vegetable scraps, coffee grounds, eggshells, yard waste, and paper products. Avoid meat, dairy, and oily foods as they can attract pests.' },
];

const gbtsConversation = [
  { role: 'user', content: 'explain how i can make my own compost' },
  { role: 'assistant', content: 'Seed of Inquiry: The question you\'ve posed is about creating your own compost. This is a fantastic initiative! Composting is an excellent way to recycle organic waste.' },
  { role: 'assistant', content: 'Branches of Understanding: Creating compost involves several related topics including waste types suitable for composting, the composting process itself, and the balance of green and brown materials.' },
  { role: 'assistant', content: 'Leaves of Application: Applying this knowledge involves setting up your composting system - whether it\'s a compost heap, bin, or tumbler.' },
];

/**
 * ChatArea component combines Avatar and message display for conversations
 * with eco-buddies in the Eco-Bot application.
 */
export default {
  title: 'Components/ChatArea',
  component: ChatArea,
  parameters: {
    layout: 'centered',
    docs: {
      description: {
        component: `
The ChatArea component displays conversations between users and eco-buddies, combining the Avatar component with a message display area.

## Features
- Avatar integration
- Message history display
- User and bot message styling
- Smooth animations
- Scrollable message area

## GBTS Integration
This component integrates with the Gaia-Bohm Thought Style (GBTS) system, displaying conversations that follow the GBTS prompt tree structure:
- Seed of Inquiry
- Branches of Understanding  
- Leaves of Application
- Roots of Connection
- Forest of Exploration
- Canopy of Synthesis
- Harvest of Wisdom

## Usage
\`\`\`jsx
import ChatArea from './ChatArea';

const messages = [
  { role: 'user', content: 'Hello!' },
  { role: 'assistant', content: 'Hi there! How can I help?' }
];

<ChatArea 
  avatarSrc="/eco-bot.png"
  avatarAlt="Eco Bot"
  userName="Eco-Bot"
  messages={messages}
/>
\`\`\`
        `,
      },
    },
  },
  tags: ['autodocs'],
  argTypes: {
    avatarSrc: {
      control: 'text',
      description: 'Avatar image URL',
    },
    avatarAlt: {
      control: 'text',
      description: 'Avatar alt text',
    },
    userName: {
      control: 'text',
      description: 'Display name',
    },
    messages: {
      control: 'object',
      description: 'Array of message objects',
    },
  },
};

// Default ChatArea with sample conversation
export const Default = {
  args: {
    avatarSrc: 'https://api.dicebear.com/7.x/bottts/svg?seed=ecobot',
    avatarAlt: 'Eco Bot',
    userName: 'Eco-Bot',
    messages: sampleConversation,
  },
};

// GBTS-style conversation
export const GBTSConversation = {
  args: {
    avatarSrc: 'https://api.dicebear.com/7.x/bottts/svg?seed=gbts',
    avatarAlt: 'GBTS Bot',
    userName: 'Eco-Bot (GBTS Mode)',
    messages: gbtsConversation,
  },
  parameters: {
    docs: {
      description: {
        story: 'Demonstrates a conversation following the Gaia-Bohm Thought Style (GBTS) structure.',
      },
    },
  },
};

// Empty state
export const Empty = {
  args: {
    avatarSrc: 'https://api.dicebear.com/7.x/bottts/svg?seed=empty',
    avatarAlt: 'Eco Bot',
    userName: 'Eco-Bot',
    messages: [],
  },
};

// Single message
export const SingleMessage = {
  args: {
    avatarSrc: 'https://api.dicebear.com/7.x/bottts/svg?seed=single',
    avatarAlt: 'Eco Bot',
    userName: 'Welcome Bot',
    messages: [
      { role: 'assistant', content: 'Welcome to Eco-Bot! 🌍 How can I help you on your sustainability journey today?' },
    ],
  },
};

// Long conversation with scroll
export const LongConversation = {
  args: {
    avatarSrc: 'https://api.dicebear.com/7.x/bottts/svg?seed=long',
    avatarAlt: 'Eco Bot',
    userName: 'Eco-Bot',
    messages: [
      ...sampleConversation,
      { role: 'user', content: 'How long does composting take?' },
      { role: 'assistant', content: 'Typically, composting takes 2-3 months with active management, or 6-12 months for passive composting. The key factors are temperature, moisture, and regular turning.' },
      { role: 'user', content: 'What about indoor composting?' },
      { role: 'assistant', content: 'Indoor composting is perfect for apartment dwellers! You can use vermicomposting (with worms), bokashi bins, or electric composters. They\'re compact and don\'t produce strong odors when done correctly.' },
      { role: 'user', content: 'Thanks for all the information!' },
      { role: 'assistant', content: 'You\'re welcome! 🌱 Remember, every bit of composting helps reduce landfill waste and creates amazing soil. Happy composting!' },
    ],
  },
};
