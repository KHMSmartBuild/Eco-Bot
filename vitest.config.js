import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  test: {
    globals: true,
    environment: 'node',
    include: [
      'tests/storyData.test.js', 
      'tests/storybook.test.js',
      'tests/logger.test.js',
      'tests/dataManager.test.js',
      'tests/serviceContainer.test.js'
    ],
    exclude: ['node_modules', 'storybook-static', 'tests/conversation_tree.test.js'],
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
      exclude: ['node_modules/', 'storybook-static/', '.storybook/'],
    },
  },
});
