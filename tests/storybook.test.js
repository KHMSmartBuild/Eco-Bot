import { describe, it, expect } from 'vitest';
import React from 'react';

// Test component exports
describe('Component Exports', () => {
  it('should export Avatar component', async () => {
    const { default: Avatar } = await import('../stories/components/Avatar');
    expect(Avatar).toBeDefined();
    expect(typeof Avatar).toBe('function');
  });

  it('should export ChatBox component', async () => {
    const { default: ChatBox } = await import('../stories/components/ChatBox');
    expect(ChatBox).toBeDefined();
    expect(typeof ChatBox).toBe('function');
  });

  it('should export ChatArea component', async () => {
    const { default: ChatArea } = await import('../stories/components/ChatArea');
    expect(ChatArea).toBeDefined();
    expect(typeof ChatArea).toBe('function');
  });

  it('should export GBTSTree component', async () => {
    const { default: GBTSTree } = await import('../stories/visualizations/GBTSTree');
    expect(GBTSTree).toBeDefined();
    expect(typeof GBTSTree).toBe('function');
  });
});

// Test story exports
describe('Story Exports', () => {
  it('should export Avatar stories', async () => {
    const stories = await import('../stories/components/Avatar.stories');
    expect(stories.default).toBeDefined();
    expect(stories.default.title).toBe('Components/Avatar');
    expect(stories.Default).toBeDefined();
    expect(stories.Small).toBeDefined();
    expect(stories.Large).toBeDefined();
    expect(stories.EcoThemed).toBeDefined();
  });

  it('should export ChatBox stories', async () => {
    const stories = await import('../stories/components/ChatBox.stories');
    expect(stories.default).toBeDefined();
    expect(stories.default.title).toBe('Components/ChatBox');
    expect(stories.Default).toBeDefined();
    expect(stories.Disabled).toBeDefined();
  });

  it('should export ChatArea stories', async () => {
    const stories = await import('../stories/components/ChatArea.stories');
    expect(stories.default).toBeDefined();
    expect(stories.default.title).toBe('Components/ChatArea');
    expect(stories.Default).toBeDefined();
    expect(stories.GBTSConversation).toBeDefined();
  });

  it('should export GBTSTree stories', async () => {
    const stories = await import('../stories/visualizations/GBTSTree.stories');
    expect(stories.default).toBeDefined();
    expect(stories.default.title).toBe('Visualizations/GBTSTree');
    expect(stories.Default).toBeDefined();
    expect(stories.ComplexTree).toBeDefined();
  });
});

// Test story args
describe('Story Args Configuration', () => {
  it('Avatar stories should have required args', async () => {
    const stories = await import('../stories/components/Avatar.stories');
    expect(stories.Default.args).toBeDefined();
    expect(stories.Default.args.src).toBeDefined();
    expect(stories.Default.args.alt).toBeDefined();
  });

  it('ChatBox stories should have placeholder arg', async () => {
    const stories = await import('../stories/components/ChatBox.stories');
    expect(stories.Default.args).toBeDefined();
    expect(stories.Default.args.placeholder).toBeDefined();
  });

  it('ChatArea stories should have messages arg', async () => {
    const stories = await import('../stories/components/ChatArea.stories');
    expect(stories.Default.args).toBeDefined();
    expect(stories.Default.args.messages).toBeDefined();
    expect(Array.isArray(stories.Default.args.messages)).toBe(true);
  });

  it('GBTSTree stories should have data arg', async () => {
    const stories = await import('../stories/visualizations/GBTSTree.stories');
    expect(stories.Default.args).toBeDefined();
    expect(stories.Default.args.data).toBeDefined();
    expect(stories.Default.args.data.nodes).toBeDefined();
    expect(stories.Default.args.data.links).toBeDefined();
  });
});
