import { describe, it, expect, beforeEach, vi } from 'vitest';
import { DataManager, dataManager } from '../stories/data/dataManager.js';

// Mock console methods to avoid noisy output during tests
vi.spyOn(console, 'debug').mockImplementation(() => {});
vi.spyOn(console, 'info').mockImplementation(() => {});
vi.spyOn(console, 'warn').mockImplementation(() => {});
vi.spyOn(console, 'error').mockImplementation(() => {});

describe('DataManager', () => {
  let manager;

  beforeEach(() => {
    manager = new DataManager();
  });

  describe('collection management', () => {
    it('should register a new collection', () => {
      const result = manager.registerCollection('test', [{ id: '1', name: 'Item 1' }]);
      expect(result).toBe(true);
    });

    it('should not register duplicate collections', () => {
      manager.registerCollection('test', []);
      const result = manager.registerCollection('test', []);
      expect(result).toBe(false);
    });

    it('should get all items from a collection', () => {
      const initialData = [
        { id: '1', name: 'Item 1' },
        { id: '2', name: 'Item 2' }
      ];
      manager.registerCollection('test', initialData);
      const items = manager.getAll('test');
      expect(items).toHaveLength(2);
    });

    it('should return null for non-existent collection', () => {
      const result = manager.getAll('nonexistent');
      expect(result).toBeNull();
    });
  });

  describe('CRUD operations', () => {
    beforeEach(() => {
      manager.registerCollection('items', [
        { id: '1', name: 'Item 1' },
        { id: '2', name: 'Item 2' }
      ]);
    });

    it('should get item by ID', () => {
      const item = manager.getById('items', '1');
      expect(item).toBeDefined();
      expect(item.name).toBe('Item 1');
    });

    it('should return null for non-existent item', () => {
      const item = manager.getById('items', 'nonexistent');
      expect(item).toBeNull();
    });

    it('should add a new item', () => {
      const newItem = manager.add('items', { name: 'Item 3' });
      expect(newItem).toBeDefined();
      expect(newItem.id).toBeDefined();
      expect(newItem.name).toBe('Item 3');
      expect(newItem.createdAt).toBeDefined();
    });

    it('should preserve provided ID when adding', () => {
      const newItem = manager.add('items', { id: 'custom-id', name: 'Custom Item' });
      expect(newItem.id).toBe('custom-id');
    });

    it('should update an existing item', () => {
      const updated = manager.update('items', '1', { name: 'Updated Item 1' });
      expect(updated).toBeDefined();
      expect(updated.name).toBe('Updated Item 1');
      expect(updated.updatedAt).toBeDefined();
    });

    it('should preserve ID when updating', () => {
      const updated = manager.update('items', '1', { id: 'different-id', name: 'Updated' });
      expect(updated.id).toBe('1'); // Original ID preserved
    });

    it('should return null when updating non-existent item', () => {
      const result = manager.update('items', 'nonexistent', { name: 'Test' });
      expect(result).toBeNull();
    });

    it('should remove an item', () => {
      const result = manager.remove('items', '1');
      expect(result).toBe(true);
      expect(manager.getById('items', '1')).toBeNull();
    });

    it('should return false when removing non-existent item', () => {
      const result = manager.remove('items', 'nonexistent');
      expect(result).toBe(false);
    });
  });

  describe('query', () => {
    beforeEach(() => {
      manager.registerCollection('products', [
        { id: '1', name: 'Apple', category: 'fruit', price: 1.5 },
        { id: '2', name: 'Banana', category: 'fruit', price: 0.75 },
        { id: '3', name: 'Carrot', category: 'vegetable', price: 0.5 },
        { id: '4', name: 'Broccoli', category: 'vegetable', price: 1.25 }
      ]);
    });

    it('should query items with predicate', () => {
      const fruits = manager.query('products', item => item.category === 'fruit');
      expect(fruits).toHaveLength(2);
      expect(fruits.every(item => item.category === 'fruit')).toBe(true);
    });

    it('should query items by price', () => {
      const cheap = manager.query('products', item => item.price < 1);
      expect(cheap).toHaveLength(2);
    });

    it('should return empty array for non-matching query', () => {
      const expensive = manager.query('products', item => item.price > 10);
      expect(expensive).toHaveLength(0);
    });

    it('should return empty array for non-existent collection', () => {
      const result = manager.query('nonexistent', () => true);
      expect(result).toEqual([]);
    });
  });

  describe('export and import', () => {
    beforeEach(() => {
      manager.registerCollection('test', [
        { id: '1', name: 'Item 1' }
      ]);
    });

    it('should export all data as JSON', () => {
      const exported = manager.exportAll();
      expect(() => JSON.parse(exported)).not.toThrow();
      const data = JSON.parse(exported);
      expect(data).toHaveProperty('test');
    });

    it('should import data from JSON', () => {
      const importData = {
        imported: {
          data: [{ id: '1', name: 'Imported Item' }],
          createdAt: new Date().toISOString()
        }
      };
      const result = manager.importData(JSON.stringify(importData));
      expect(result).toBe(true);
      expect(manager.getAll('imported')).toBeDefined();
    });

    it('should handle invalid JSON on import', () => {
      const result = manager.importData('invalid json');
      expect(result).toBe(false);
    });
  });

  describe('statistics', () => {
    it('should provide statistics about collections', () => {
      manager.registerCollection('col1', [{ id: '1' }, { id: '2' }]);
      manager.registerCollection('col2', [{ id: '1' }]);
      
      const stats = manager.getStats();
      expect(stats.totalItems).toBe(3);
      expect(stats.collections).toHaveProperty('col1');
      expect(stats.collections).toHaveProperty('col2');
      expect(stats.collections.col1.itemCount).toBe(2);
      expect(stats.collections.col2.itemCount).toBe(1);
    });
  });

  describe('events', () => {
    it('should emit event when collection is registered', () => {
      const callback = vi.fn();
      manager.on('collectionRegistered', callback);
      manager.registerCollection('test', []);
      expect(callback).toHaveBeenCalled();
    });

    it('should emit event when item is added', () => {
      manager.registerCollection('test', []);
      const callback = vi.fn();
      manager.on('itemAdded', callback);
      manager.add('test', { name: 'New Item' });
      expect(callback).toHaveBeenCalled();
    });

    it('should emit event when item is updated', () => {
      manager.registerCollection('test', [{ id: '1', name: 'Item' }]);
      const callback = vi.fn();
      manager.on('itemUpdated', callback);
      manager.update('test', '1', { name: 'Updated' });
      expect(callback).toHaveBeenCalled();
    });

    it('should emit event when item is removed', () => {
      manager.registerCollection('test', [{ id: '1', name: 'Item' }]);
      const callback = vi.fn();
      manager.on('itemRemoved', callback);
      manager.remove('test', '1');
      expect(callback).toHaveBeenCalled();
    });
  });

  describe('clear', () => {
    it('should clear all data', () => {
      manager.registerCollection('test1', [{ id: '1' }]);
      manager.registerCollection('test2', [{ id: '2' }]);
      manager.clear();
      expect(manager.getAll('test1')).toBeNull();
      expect(manager.getAll('test2')).toBeNull();
    });
  });
});

describe('Singleton dataManager', () => {
  it('should be an instance of DataManager', () => {
    expect(dataManager).toBeInstanceOf(DataManager);
  });
});
