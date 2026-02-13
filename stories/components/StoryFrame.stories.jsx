import React from 'react';
import StoryFrame from './StoryFrame';
import './StoryFrame.css';

/**
 * StoryFrame - Dynamic Story Frame for Multi-Agent Content
 * 
 * The StoryFrame component is designed to be populated dynamically by the Eco-Bot
 * multi-agent system. Each frame can display story content with illustrations,
 * agent attribution, and interactive elements.
 * 
 * ## Key Features
 * - **Dynamic Content**: Ready for agent-generated text and illustrations
 * - **Mood-Based Theming**: Visual styling adapts to content mood
 * - **Loading States**: Built-in skeleton loading for async content
 * - **Interactive Controls**: Expand, regenerate, and share actions
 * - **Agent Attribution**: Shows which Eco-Buddy narrated the content
 * 
 * ## Multi-Agent Integration
 * 
 * The StoryFrame is designed to receive content from different Eco-Bot agents:
 * 
 * ```javascript
 * // Example: Agent populating a story frame
 * const frameData = await agent.generateStoryFrame({
 *   topic: "composting",
 *   mood: "curious",
 *   includeIllustration: true
 * });
 * 
 * <StoryFrame
 *   id={frameData.id}
 *   title={frameData.title}
 *   content={frameData.content}
 *   illustration={frameData.illustration}
 *   agent={frameData.agentName}
 *   mood={frameData.mood}
 * />
 * ```
 */
export default {
  title: 'Components/StoryFrame',
  component: StoryFrame,
  parameters: {
    layout: 'centered',
    docs: {
      description: {
        component: `
# StoryFrame Component

A dynamic story frame component designed to be populated by the Eco-Bot multi-agent system.

## Purpose

The StoryFrame serves as a container for story content that can be dynamically generated 
by various Eco-Bot agents. It provides:

- Visual consistency across different story chapters
- Loading states for async content generation
- Mood-based theming that reflects the story's emotional tone
- Interactive controls for user engagement
- Agent attribution to show which Eco-Buddy created the content

## Usage with Multi-Agents

\`\`\`jsx
// The DataManager can store and retrieve story frames
import { dataManager } from './data/storyData';

// Register a collection for story frames
dataManager.registerCollection('storyFrames', []);

// Agent generates and stores a frame
const newFrame = dataManager.add('storyFrames', {
  title: "The Journey Begins",
  content: "Once upon a time in the forest...",
  mood: "curious",
  agent: "Eco-Bot"
});

// Listen for new frames
dataManager.on('itemAdded', ({ collection, item }) => {
  if (collection === 'storyFrames') {
    // Render the new frame
  }
});
\`\`\`
        `
      }
    }
  },
  tags: ['autodocs'],
  argTypes: {
    id: {
      control: 'text',
      description: 'Unique identifier for the frame'
    },
    title: {
      control: 'text',
      description: 'Title of the story frame'
    },
    chapter: {
      control: { type: 'number', min: 1, max: 20 },
      description: 'Chapter number'
    },
    content: {
      control: 'text',
      description: 'Main narrative content'
    },
    illustration: {
      control: 'text',
      description: 'URL for illustration image'
    },
    agent: {
      control: 'text',
      description: 'Name of the narrating agent'
    },
    agentAvatar: {
      control: 'text',
      description: 'Avatar URL for the agent'
    },
    mood: {
      control: { type: 'select' },
      options: ['curious', 'excited', 'thoughtful', 'wise', 'playful', 'default'],
      description: 'Mood/theme affecting visual styling'
    },
    variant: {
      control: { type: 'select' },
      options: ['default', 'featured', 'compact', 'full-width'],
      description: 'Visual variant of the frame'
    },
    interactive: {
      control: 'boolean',
      description: 'Show interactive controls'
    },
    loading: {
      control: 'boolean',
      description: 'Show loading state'
    }
  }
};

// Default story frame
export const Default = {
  args: {
    id: 'frame-1',
    title: 'The Seed of Curiosity',
    chapter: 1,
    content: 'In the heart of a lush forest, where ancient trees whispered secrets to the wind, a young sapling began to wonder about the world beyond its roots. This is where our journey into environmental awareness begins...',
    agent: 'Eco-Bot',
    agentAvatar: 'https://api.dicebear.com/7.x/bottts/svg?seed=ecobot',
    mood: 'curious',
    interactive: true
  }
};

// With illustration
export const WithIllustration = {
  args: {
    id: 'frame-2',
    title: 'The Forest Awakens',
    chapter: 2,
    content: 'As dawn breaks over the canopy, creatures of all sizes emerge to play their part in the great cycle of nature. Each has a role, each has a purpose.',
    illustration: 'https://images.unsplash.com/photo-1448375240586-882707db888b?w=800&auto=format&fit=crop',
    illustrationAlt: 'A misty forest at dawn',
    agent: 'Energy Buddy',
    agentAvatar: 'https://api.dicebear.com/7.x/bottts/svg?seed=energy',
    mood: 'excited',
    interactive: true
  }
};

// Loading state
export const Loading = {
  args: {
    id: 'frame-loading',
    title: 'Creating Your Story...',
    loading: true,
    mood: 'default'
  },
  parameters: {
    docs: {
      description: {
        story: 'Shows the loading state while an agent is generating content. This includes skeleton loaders for both text and illustration.'
      }
    }
  }
};

// Placeholder (no content yet)
export const Placeholder = {
  args: {
    id: 'frame-placeholder',
    title: 'Awaiting Agent Content',
    chapter: 3,
    content: 'This frame is ready to receive dynamically generated content from an Eco-Bot agent. The illustration placeholder shows where generated imagery will appear.',
    mood: 'default',
    interactive: false
  },
  parameters: {
    docs: {
      description: {
        story: 'An empty frame ready to be populated by multi-agent content. The illustration placeholder indicates where agent-generated images will be displayed.'
      }
    }
  }
};

// Thoughtful mood
export const ThoughtfulMood = {
  args: {
    id: 'frame-thoughtful',
    title: 'Roots of Connection',
    chapter: 4,
    content: 'Deep beneath the surface, a hidden network connects all living things. The mycorrhizal network - nature\'s internet - allows trees to share nutrients and information. What can we learn from this ancient wisdom?',
    agent: 'Compost Buddy',
    agentAvatar: 'https://api.dicebear.com/7.x/bottts/svg?seed=compost',
    mood: 'thoughtful',
    interactive: true
  }
};

// Wise mood
export const WiseMood = {
  args: {
    id: 'frame-wise',
    title: 'Harvest of Wisdom',
    chapter: 7,
    content: 'And so we arrive at the end of our journey, richer in understanding. The lessons of nature are simple yet profound: balance, cooperation, and respect for all living things. This wisdom is now yours to carry forward.',
    agent: 'Water Buddy',
    agentAvatar: 'https://api.dicebear.com/7.x/bottts/svg?seed=water',
    mood: 'wise',
    interactive: true
  }
};

// Playful mood
export const PlayfulMood = {
  args: {
    id: 'frame-playful',
    title: 'The Eco-Challenge!',
    content: '🌱 Ready for an adventure? Your mission this week: Find three ways to reduce waste in your daily life! Can you spot the recyclables hiding in plain sight? Let\'s turn this into a game!',
    agent: 'Eco-Bot',
    agentAvatar: 'https://api.dicebear.com/7.x/bottts/svg?seed=ecobot',
    mood: 'playful',
    interactive: true
  }
};

// Compact variant
export const CompactVariant = {
  args: {
    id: 'frame-compact',
    title: 'Quick Eco-Tip',
    content: 'Did you know? A single mature tree can absorb up to 48 pounds of carbon dioxide per year!',
    mood: 'excited',
    variant: 'compact',
    interactive: false
  }
};

// Featured variant
export const FeaturedVariant = {
  args: {
    id: 'frame-featured',
    title: 'Featured Story: The Ocean\'s Secret',
    chapter: 1,
    content: 'Beneath the waves lies a world of wonder. The ocean, covering 71% of our planet, holds mysteries yet to be discovered. Join us on an underwater adventure as we explore the delicate balance of marine ecosystems and learn how we can protect these precious waters.',
    illustration: 'https://images.unsplash.com/photo-1518837695005-2083093ee35b?w=800&auto=format&fit=crop',
    illustrationAlt: 'Underwater ocean scene',
    agent: 'Water Buddy',
    agentAvatar: 'https://api.dicebear.com/7.x/bottts/svg?seed=water',
    mood: 'curious',
    variant: 'featured',
    interactive: true
  }
};

// Multiple frames in a story sequence
export const StorySequence = {
  render: () => (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '24px', maxWidth: '800px' }}>
      <StoryFrame
        id="seq-1"
        title="The Journey Begins"
        chapter={1}
        content="In a world where nature and technology dance together, a curious young explorer sets out to discover the secrets of sustainable living."
        mood="curious"
        agent="Eco-Bot"
        agentAvatar="https://api.dicebear.com/7.x/bottts/svg?seed=ecobot"
      />
      <StoryFrame
        id="seq-2"
        title="Into the Green"
        chapter={2}
        content="Our hero encounters the guardians of the forest - wise beings who teach the ancient art of composting and recycling."
        mood="thoughtful"
        agent="Compost Buddy"
        agentAvatar="https://api.dicebear.com/7.x/bottts/svg?seed=compost"
      />
      <StoryFrame
        id="seq-3"
        title="The Harvest"
        chapter={3}
        content="With newfound knowledge, the explorer returns home, ready to share the wisdom of sustainability with the world."
        mood="wise"
        agent="Eco-Bot"
        agentAvatar="https://api.dicebear.com/7.x/bottts/svg?seed=ecobot"
        interactive={true}
      />
    </div>
  ),
  parameters: {
    docs: {
      description: {
        story: 'Shows how multiple StoryFrames can be combined to create a sequential narrative, each potentially generated by different Eco-Bot agents.'
      }
    }
  }
};
