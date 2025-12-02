import { describe, it, expect } from 'vitest';
import { 
  gbtsPrompts, 
  gbtsVisualizationData, 
  ecoBotPersonality, 
  ecoBuddies, 
  sampleConversations,
  validateGBTSData,
  transformConversationToGBTS 
} from '../stories/data/storyData';

describe('Story Data Management', () => {
  describe('gbtsPrompts', () => {
    it('should contain all GBTS stages', () => {
      const expectedStages = [
        'Seed of Inquiry',
        'Branches of Understanding',
        'Leaves of Application',
        'Roots of Connection',
        'Forest of Exploration',
        'Canopy of Synthesis',
        'Harvest of Wisdom'
      ];
      
      expectedStages.forEach(stage => {
        expect(gbtsPrompts).toHaveProperty(stage);
      });
    });

    it('should have prompt and guidance for each stage', () => {
      Object.values(gbtsPrompts).forEach(stage => {
        expect(stage).toHaveProperty('prompt');
        expect(stage).toHaveProperty('guidance');
        expect(stage).toHaveProperty('response_type');
        expect(stage.prompt).toBeTruthy();
        expect(stage.guidance).toBeTruthy();
      });
    });
  });

  describe('gbtsVisualizationData', () => {
    it('should have nodes and links arrays', () => {
      expect(gbtsVisualizationData).toHaveProperty('nodes');
      expect(gbtsVisualizationData).toHaveProperty('links');
      expect(Array.isArray(gbtsVisualizationData.nodes)).toBe(true);
      expect(Array.isArray(gbtsVisualizationData.links)).toBe(true);
    });

    it('should have valid node structure', () => {
      gbtsVisualizationData.nodes.forEach(node => {
        expect(node).toHaveProperty('id');
        expect(node).toHaveProperty('group');
        expect(typeof node.id).toBe('string');
        expect(typeof node.group).toBe('number');
      });
    });

    it('should have valid link structure', () => {
      gbtsVisualizationData.links.forEach(link => {
        expect(link).toHaveProperty('source');
        expect(link).toHaveProperty('target');
      });
    });
  });

  describe('ecoBotPersonality', () => {
    it('should have name and core values', () => {
      expect(ecoBotPersonality.name).toBe('EcoBot');
      expect(Array.isArray(ecoBotPersonality.core_values)).toBe(true);
      expect(ecoBotPersonality.core_values.length).toBeGreaterThan(0);
    });

    it('should have AI features', () => {
      expect(Array.isArray(ecoBotPersonality.AI_features)).toBe(true);
      expect(ecoBotPersonality.AI_features).toContain('Gaia Theory');
    });

    it('should have personality traits', () => {
      expect(ecoBotPersonality.personality_traits).toBeDefined();
      expect(Object.keys(ecoBotPersonality.personality_traits).length).toBeGreaterThan(0);
    });
  });

  describe('ecoBuddies', () => {
    it('should be an array of eco-buddies', () => {
      expect(Array.isArray(ecoBuddies)).toBe(true);
      expect(ecoBuddies.length).toBeGreaterThan(0);
    });

    it('should have required properties for each buddy', () => {
      ecoBuddies.forEach(buddy => {
        expect(buddy).toHaveProperty('id');
        expect(buddy).toHaveProperty('name');
        expect(buddy).toHaveProperty('avatar');
        expect(buddy).toHaveProperty('specialty');
      });
    });
  });

  describe('sampleConversations', () => {
    it('should have composting conversation', () => {
      expect(sampleConversations).toHaveProperty('composting');
      expect(Array.isArray(sampleConversations.composting)).toBe(true);
    });

    it('should have ecoMission conversation', () => {
      expect(sampleConversations).toHaveProperty('ecoMission');
      expect(Array.isArray(sampleConversations.ecoMission)).toBe(true);
    });

    it('should have valid message format', () => {
      sampleConversations.composting.forEach(msg => {
        expect(msg).toHaveProperty('role');
        expect(msg).toHaveProperty('content');
        expect(['user', 'assistant']).toContain(msg.role);
      });
    });
  });

  describe('validateGBTSData', () => {
    it('should validate correct data', () => {
      const result = validateGBTSData(gbtsVisualizationData);
      expect(result.valid).toBe(true);
    });

    it('should reject null data', () => {
      const result = validateGBTSData(null);
      expect(result.valid).toBe(false);
      expect(result.error).toBeDefined();
    });

    it('should reject data without nodes', () => {
      const result = validateGBTSData({ links: [] });
      expect(result.valid).toBe(false);
    });

    it('should reject data with empty nodes', () => {
      const result = validateGBTSData({ nodes: [], links: [] });
      expect(result.valid).toBe(false);
    });

    it('should reject data with invalid links', () => {
      const result = validateGBTSData({
        nodes: [{ id: 'A', group: 1 }],
        links: [{ source: 'A', target: 'B' }] // B doesn't exist
      });
      expect(result.valid).toBe(false);
    });
  });

  describe('transformConversationToGBTS', () => {
    it('should transform conversation to nodes and links', () => {
      const conversation = [
        { role: 'user', content: 'Hello' },
        { role: 'assistant', content: 'Hi there!' }
      ];
      
      const result = transformConversationToGBTS(conversation);
      
      expect(result.nodes).toHaveLength(2);
      expect(result.links).toHaveLength(1);
    });

    it('should create correct link structure', () => {
      const conversation = [
        { role: 'user', content: 'Message 1' },
        { role: 'assistant', content: 'Message 2' },
        { role: 'user', content: 'Message 3' }
      ];
      
      const result = transformConversationToGBTS(conversation);
      
      expect(result.nodes).toHaveLength(3);
      expect(result.links).toHaveLength(2);
      expect(result.links[0].source).toBe('msg-0');
      expect(result.links[0].target).toBe('msg-1');
    });

    it('should handle empty conversation', () => {
      const result = transformConversationToGBTS([]);
      
      expect(result.nodes).toHaveLength(0);
      expect(result.links).toHaveLength(0);
    });
  });
});
