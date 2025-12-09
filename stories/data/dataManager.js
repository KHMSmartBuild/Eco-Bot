/**
 * Eco-Bot Enhanced Data Manager
 * 
 * Provides advanced data management capabilities including:
 * - CRUD operations for story data
 * - Data persistence with localStorage
 * - Event-driven data updates
 * - Data caching and optimization
 * - Import/export functionality
 */

import { logger, LogCategory } from './logger.js';

/**
 * Event emitter for data changes
 */
class DataEventEmitter {
  constructor() {
    this.listeners = {};
  }
  
  on(event, callback) {
    if (!this.listeners[event]) {
      this.listeners[event] = [];
    }
    this.listeners[event].push(callback);
    return () => this.off(event, callback);
  }
  
  off(event, callback) {
    if (!this.listeners[event]) return;
    this.listeners[event] = this.listeners[event].filter(cb => cb !== callback);
  }
  
  emit(event, data) {
    if (!this.listeners[event]) return;
    this.listeners[event].forEach(callback => {
      try {
        callback(data);
      } catch (error) {
        logger.error(LogCategory.DATA, `Error in event listener for ${event}`, error);
      }
    });
  }
}

/**
 * Data cache for performance optimization
 */
class DataCache {
  constructor(maxSize = 100, ttl = 300000) { // 5 minutes default TTL
    this.cache = new Map();
    this.maxSize = maxSize;
    this.ttl = ttl;
  }
  
  set(key, value) {
    // Remove oldest entry if cache is full
    if (this.cache.size >= this.maxSize) {
      const firstKey = this.cache.keys().next().value;
      this.cache.delete(firstKey);
      logger.debug(LogCategory.DATA, `Cache evicted: ${firstKey}`);
    }
    
    this.cache.set(key, {
      value,
      timestamp: Date.now()
    });
    
    logger.debug(LogCategory.DATA, `Cache set: ${key}`);
  }
  
  get(key) {
    const entry = this.cache.get(key);
    
    if (!entry) {
      logger.debug(LogCategory.DATA, `Cache miss: ${key}`);
      return null;
    }
    
    // Check if entry has expired
    if (Date.now() - entry.timestamp > this.ttl) {
      this.cache.delete(key);
      logger.debug(LogCategory.DATA, `Cache expired: ${key}`);
      return null;
    }
    
    logger.debug(LogCategory.DATA, `Cache hit: ${key}`);
    return entry.value;
  }
  
  has(key) {
    return this.get(key) !== null;
  }
  
  delete(key) {
    const deleted = this.cache.delete(key);
    if (deleted) {
      logger.debug(LogCategory.DATA, `Cache deleted: ${key}`);
    }
    return deleted;
  }
  
  clear() {
    this.cache.clear();
    logger.info(LogCategory.DATA, 'Cache cleared');
  }
  
  getStats() {
    return {
      size: this.cache.size,
      maxSize: this.maxSize,
      ttl: this.ttl
    };
  }
}

/**
 * Storage adapter for data persistence
 */
class StorageAdapter {
  constructor(storageKey = 'eco-bot-data') {
    this.storageKey = storageKey;
    this.available = this.checkAvailability();
  }
  
  checkAvailability() {
    try {
      if (typeof localStorage === 'undefined') return false;
      const test = '__storage_test__';
      localStorage.setItem(test, test);
      localStorage.removeItem(test);
      return true;
    } catch (e) {
      return false;
    }
  }
  
  save(key, data) {
    if (!this.available) {
      logger.warn(LogCategory.DATA, 'localStorage not available, data not persisted');
      return false;
    }
    
    try {
      const storageData = this.loadAll() || {};
      storageData[key] = {
        data,
        savedAt: new Date().toISOString()
      };
      localStorage.setItem(this.storageKey, JSON.stringify(storageData));
      logger.info(LogCategory.DATA, `Data saved to storage: ${key}`);
      return true;
    } catch (error) {
      logger.error(LogCategory.DATA, `Failed to save data: ${key}`, error);
      return false;
    }
  }
  
  load(key) {
    if (!this.available) return null;
    
    try {
      const storageData = this.loadAll();
      const entry = storageData?.[key];
      if (entry) {
        logger.info(LogCategory.DATA, `Data loaded from storage: ${key}`);
        return entry.data;
      }
      return null;
    } catch (error) {
      logger.error(LogCategory.DATA, `Failed to load data: ${key}`, error);
      return null;
    }
  }
  
  loadAll() {
    if (!this.available) return null;
    
    try {
      const data = localStorage.getItem(this.storageKey);
      return data ? JSON.parse(data) : {};
    } catch (error) {
      logger.error(LogCategory.DATA, 'Failed to load all data from storage', error);
      return {};
    }
  }
  
  remove(key) {
    if (!this.available) return false;
    
    try {
      const storageData = this.loadAll() || {};
      delete storageData[key];
      localStorage.setItem(this.storageKey, JSON.stringify(storageData));
      logger.info(LogCategory.DATA, `Data removed from storage: ${key}`);
      return true;
    } catch (error) {
      logger.error(LogCategory.DATA, `Failed to remove data: ${key}`, error);
      return false;
    }
  }
  
  clear() {
    if (!this.available) return false;
    
    try {
      localStorage.removeItem(this.storageKey);
      logger.info(LogCategory.DATA, 'Storage cleared');
      return true;
    } catch (error) {
      logger.error(LogCategory.DATA, 'Failed to clear storage', error);
      return false;
    }
  }
}

/**
 * Main Data Manager class
 */
export class DataManager {
  constructor(options = {}) {
    this.events = new DataEventEmitter();
    this.cache = new DataCache(options.cacheSize, options.cacheTTL);
    this.storage = new StorageAdapter(options.storageKey);
    this.collections = new Map();
    
    logger.info(LogCategory.DATA, 'DataManager initialized', options);
  }
  
  /**
   * Register a data collection
   */
  registerCollection(name, initialData = [], schema = null) {
    if (this.collections.has(name)) {
      logger.warn(LogCategory.DATA, `Collection already exists: ${name}`);
      return false;
    }
    
    this.collections.set(name, {
      data: [...initialData],
      schema,
      createdAt: new Date().toISOString(),
      modifiedAt: new Date().toISOString()
    });
    
    logger.info(LogCategory.DATA, `Collection registered: ${name}`, { itemCount: initialData.length });
    this.events.emit('collectionRegistered', { name, itemCount: initialData.length });
    
    return true;
  }
  
  /**
   * Get all items from a collection
   */
  getAll(collectionName) {
    const cacheKey = `collection:${collectionName}`;
    const cached = this.cache.get(cacheKey);
    
    if (cached) {
      return cached;
    }
    
    const collection = this.collections.get(collectionName);
    if (!collection) {
      logger.warn(LogCategory.DATA, `Collection not found: ${collectionName}`);
      return null;
    }
    
    this.cache.set(cacheKey, collection.data);
    return collection.data;
  }
  
  /**
   * Get a single item by ID
   */
  getById(collectionName, id) {
    const cacheKey = `item:${collectionName}:${id}`;
    const cached = this.cache.get(cacheKey);
    
    if (cached) {
      return cached;
    }
    
    const collection = this.collections.get(collectionName);
    if (!collection) {
      logger.warn(LogCategory.DATA, `Collection not found: ${collectionName}`);
      return null;
    }
    
    const item = collection.data.find(item => item.id === id);
    if (item) {
      this.cache.set(cacheKey, item);
    }
    
    return item || null;
  }
  
  /**
   * Add an item to a collection
   */
  add(collectionName, item) {
    const collection = this.collections.get(collectionName);
    if (!collection) {
      logger.error(LogCategory.DATA, `Cannot add to non-existent collection: ${collectionName}`);
      return null;
    }
    
    // Generate ID if not present
    const newItem = {
      ...item,
      id: item.id || `${collectionName}-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`,
      createdAt: new Date().toISOString()
    };
    
    collection.data.push(newItem);
    collection.modifiedAt = new Date().toISOString();
    
    // Invalidate cache
    this.cache.delete(`collection:${collectionName}`);
    
    logger.info(LogCategory.DATA, `Item added to ${collectionName}`, { id: newItem.id });
    this.events.emit('itemAdded', { collection: collectionName, item: newItem });
    
    return newItem;
  }
  
  /**
   * Update an item in a collection
   */
  update(collectionName, id, updates) {
    const collection = this.collections.get(collectionName);
    if (!collection) {
      logger.error(LogCategory.DATA, `Cannot update in non-existent collection: ${collectionName}`);
      return null;
    }
    
    const index = collection.data.findIndex(item => item.id === id);
    if (index === -1) {
      logger.warn(LogCategory.DATA, `Item not found: ${id} in ${collectionName}`);
      return null;
    }
    
    const updatedItem = {
      ...collection.data[index],
      ...updates,
      id, // Preserve original ID
      updatedAt: new Date().toISOString()
    };
    
    collection.data[index] = updatedItem;
    collection.modifiedAt = new Date().toISOString();
    
    // Invalidate cache
    this.cache.delete(`collection:${collectionName}`);
    this.cache.delete(`item:${collectionName}:${id}`);
    
    logger.info(LogCategory.DATA, `Item updated in ${collectionName}`, { id });
    this.events.emit('itemUpdated', { collection: collectionName, item: updatedItem });
    
    return updatedItem;
  }
  
  /**
   * Remove an item from a collection
   */
  remove(collectionName, id) {
    const collection = this.collections.get(collectionName);
    if (!collection) {
      logger.error(LogCategory.DATA, `Cannot remove from non-existent collection: ${collectionName}`);
      return false;
    }
    
    const index = collection.data.findIndex(item => item.id === id);
    if (index === -1) {
      logger.warn(LogCategory.DATA, `Item not found: ${id} in ${collectionName}`);
      return false;
    }
    
    const removedItem = collection.data.splice(index, 1)[0];
    collection.modifiedAt = new Date().toISOString();
    
    // Invalidate cache
    this.cache.delete(`collection:${collectionName}`);
    this.cache.delete(`item:${collectionName}:${id}`);
    
    logger.info(LogCategory.DATA, `Item removed from ${collectionName}`, { id });
    this.events.emit('itemRemoved', { collection: collectionName, item: removedItem });
    
    return true;
  }
  
  /**
   * Query items with filters
   */
  query(collectionName, predicate) {
    const collection = this.collections.get(collectionName);
    if (!collection) {
      logger.warn(LogCategory.DATA, `Collection not found: ${collectionName}`);
      return [];
    }
    
    const results = collection.data.filter(predicate);
    logger.debug(LogCategory.DATA, `Query executed on ${collectionName}`, { resultCount: results.length });
    
    return results;
  }
  
  /**
   * Save collection to persistent storage
   */
  persist(collectionName) {
    const collection = this.collections.get(collectionName);
    if (!collection) {
      logger.error(LogCategory.DATA, `Cannot persist non-existent collection: ${collectionName}`);
      return false;
    }
    
    return this.storage.save(collectionName, collection);
  }
  
  /**
   * Load collection from persistent storage
   */
  restore(collectionName) {
    const stored = this.storage.load(collectionName);
    if (!stored) {
      logger.warn(LogCategory.DATA, `No stored data found for: ${collectionName}`);
      return false;
    }
    
    this.collections.set(collectionName, stored);
    logger.info(LogCategory.DATA, `Collection restored from storage: ${collectionName}`);
    this.events.emit('collectionRestored', { name: collectionName });
    
    return true;
  }
  
  /**
   * Export all data as JSON
   */
  exportAll() {
    const exportData = {};
    
    this.collections.forEach((collection, name) => {
      exportData[name] = collection;
    });
    
    logger.info(LogCategory.DATA, 'Data exported', { collectionCount: this.collections.size });
    
    return JSON.stringify(exportData, null, 2);
  }
  
  /**
   * Import data from JSON
   */
  importData(jsonString, merge = false) {
    try {
      const importData = JSON.parse(jsonString);
      
      Object.entries(importData).forEach(([name, collection]) => {
        if (merge && this.collections.has(name)) {
          const existing = this.collections.get(name);
          existing.data = [...existing.data, ...collection.data];
          existing.modifiedAt = new Date().toISOString();
        } else {
          this.collections.set(name, collection);
        }
      });
      
      logger.info(LogCategory.DATA, 'Data imported', { 
        collectionCount: Object.keys(importData).length,
        merge 
      });
      
      this.events.emit('dataImported', { collectionCount: Object.keys(importData).length });
      
      return true;
    } catch (error) {
      logger.error(LogCategory.DATA, 'Failed to import data', error);
      return false;
    }
  }
  
  /**
   * Get statistics about all collections
   */
  getStats() {
    const stats = {
      collections: {},
      totalItems: 0,
      cacheStats: this.cache.getStats()
    };
    
    this.collections.forEach((collection, name) => {
      stats.collections[name] = {
        itemCount: collection.data.length,
        createdAt: collection.createdAt,
        modifiedAt: collection.modifiedAt
      };
      stats.totalItems += collection.data.length;
    });
    
    return stats;
  }
  
  /**
   * Subscribe to data events
   */
  on(event, callback) {
    return this.events.on(event, callback);
  }
  
  /**
   * Clear all data and cache
   */
  clear() {
    this.collections.clear();
    this.cache.clear();
    logger.info(LogCategory.DATA, 'All data cleared');
    this.events.emit('dataCleared');
  }
}

// Create and export a singleton instance
export const dataManager = new DataManager();

export default DataManager;
