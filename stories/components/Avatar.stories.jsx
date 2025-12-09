import React from 'react';
import Avatar from './Avatar';

/**
 * Avatar component for displaying user/bot profile images.
 * This component is used throughout the Eco-Bot application for eco-buddies
 * and user representations.
 */
export default {
  title: 'Components/Avatar',
  component: Avatar,
  parameters: {
    layout: 'centered',
    docs: {
      description: {
        component: `
The Avatar component displays profile images for eco-buddies and users in the Eco-Bot application.

## Features
- Customizable size
- Circular or custom shape
- Responsive image handling
- Accessibility support with alt text

## Usage
\`\`\`jsx
import Avatar from './Avatar';

<Avatar src="/path/to/image.png" alt="Eco Bot" size={100} />
\`\`\`
        `,
      },
    },
  },
  tags: ['autodocs'],
  argTypes: {
    src: {
      control: 'text',
      description: 'Image source URL',
    },
    alt: {
      control: 'text',
      description: 'Alternative text for accessibility',
    },
    size: {
      control: { type: 'range', min: 30, max: 200, step: 10 },
      description: 'Size of the avatar in pixels',
    },
    className: {
      control: 'text',
      description: 'Additional CSS classes',
    },
  },
};

// Default Avatar
export const Default = {
  args: {
    src: 'https://api.dicebear.com/7.x/bottts/svg?seed=ecobot',
    alt: 'Eco Bot Avatar',
    size: 100,
  },
};

// Small Avatar
export const Small = {
  args: {
    src: 'https://api.dicebear.com/7.x/bottts/svg?seed=ecobuddy1',
    alt: 'Small Eco Buddy',
    size: 50,
  },
};

// Large Avatar
export const Large = {
  args: {
    src: 'https://api.dicebear.com/7.x/bottts/svg?seed=ecobuddy2',
    alt: 'Large Eco Buddy',
    size: 150,
  },
};

// Eco-themed Avatar with border
export const EcoThemed = {
  args: {
    src: 'https://api.dicebear.com/7.x/bottts/svg?seed=ecothemed',
    alt: 'Eco Themed Avatar',
    size: 100,
    className: 'avatar-eco',
  },
};

// Multiple Eco Buddies showcase
export const EcoBuddiesGallery = {
  render: () => (
    <div style={{ display: 'flex', gap: '20px', flexWrap: 'wrap', justifyContent: 'center' }}>
      <Avatar src="https://api.dicebear.com/7.x/bottts/svg?seed=buddy1" alt="Eco Buddy 1" size={80} />
      <Avatar src="https://api.dicebear.com/7.x/bottts/svg?seed=buddy2" alt="Eco Buddy 2" size={80} />
      <Avatar src="https://api.dicebear.com/7.x/bottts/svg?seed=buddy3" alt="Eco Buddy 3" size={80} />
      <Avatar src="https://api.dicebear.com/7.x/bottts/svg?seed=buddy4" alt="Eco Buddy 4" size={80} />
    </div>
  ),
  parameters: {
    docs: {
      description: {
        story: 'A gallery showcasing multiple Eco Buddies avatars used in the Eco-Bot group chat.',
      },
    },
  },
};
