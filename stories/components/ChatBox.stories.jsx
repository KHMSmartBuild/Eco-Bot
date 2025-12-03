import ChatBox from './ChatBox';

/**
 * ChatBox component for text input in the Eco-Bot chat interface.
 * Users can type messages to interact with eco-buddies and participate in conversations.
 */
export default {
  title: 'Components/ChatBox',
  component: ChatBox,
  parameters: {
    layout: 'centered',
    docs: {
      description: {
        component: `
The ChatBox component provides a text input area for users to communicate with Eco-Bot and eco-buddies.

## Features
- Multi-line text input
- Submit on Enter key
- Customizable placeholder
- Disabled state support
- Eco-themed styling variant

## Usage
\`\`\`jsx
import ChatBox from './ChatBox';

<ChatBox 
  placeholder="Ask Eco-Bot a question..."
  onSubmit={(message) => console.log('Sent:', message)}
/>
\`\`\`
        `,
      },
    },
  },
  tags: ['autodocs'],
  argTypes: {
    placeholder: {
      control: 'text',
      description: 'Placeholder text when input is empty',
    },
    value: {
      control: 'text',
      description: 'Current input value',
    },
    disabled: {
      control: 'boolean',
      description: 'Whether the input is disabled',
    },
    rows: {
      control: { type: 'range', min: 1, max: 10, step: 1 },
      description: 'Number of visible rows',
    },
    onChange: {
      action: 'changed',
      description: 'Called when text changes',
    },
    onSubmit: {
      action: 'submitted',
      description: 'Called when user presses Enter',
    },
  },
};

// Default ChatBox
export const Default = {
  args: {
    placeholder: 'Type your message...',
    rows: 3,
  },
};

// With eco-themed prompt
export const EcoPrompt = {
  args: {
    placeholder: 'Ask Eco-Bot about sustainability...',
    rows: 3,
  },
};

// Disabled state
export const Disabled = {
  args: {
    placeholder: 'Connection lost...',
    disabled: true,
    rows: 3,
  },
};

// Small single-line
export const SingleLine = {
  args: {
    placeholder: 'Quick message...',
    rows: 1,
  },
};

// Large multi-line for detailed messages
export const LargeInput = {
  args: {
    placeholder: 'Share your eco-mission details...',
    rows: 6,
  },
};

// Pre-filled with text
export const PreFilled = {
  args: {
    value: 'Hello Eco-Bot! Can you give me tips for reducing plastic waste?',
    rows: 3,
  },
};
