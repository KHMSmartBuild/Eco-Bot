/** @type { import('@storybook/react-vite').Preview } */
const preview = {
  parameters: {
    controls: {
      matchers: {
       color: /(background|color)$/i,
       date: /Date$/i,
      },
    },
    docs: {
      toc: true,
    },
    backgrounds: {
      default: 'light',
      values: [
        { name: 'light', value: '#F5F7F9' },
        { name: 'dark', value: '#1a1a1a' },
        { name: 'eco-green', value: '#e8f5e9' },
      ],
    },
  },
  globalTypes: {
    theme: {
      description: 'Eco-Bot theme',
      defaultValue: 'eco',
      toolbar: {
        title: 'Theme',
        icon: 'paintbrush',
        items: ['eco', 'spring', 'summer', 'autumn', 'winter'],
        dynamicTitle: true,
      },
    },
  },
};

export default preview;