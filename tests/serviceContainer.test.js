import { describe, it, expect, beforeEach, vi } from 'vitest';
import { ServiceContainer, ServiceLifecycle, container } from '../stories/data/serviceContainer.js';

// Mock console methods
vi.spyOn(console, 'debug').mockImplementation(() => {});
vi.spyOn(console, 'info').mockImplementation(() => {});
vi.spyOn(console, 'warn').mockImplementation(() => {});
vi.spyOn(console, 'error').mockImplementation(() => {});

describe('ServiceContainer', () => {
  let serviceContainer;

  beforeEach(() => {
    serviceContainer = new ServiceContainer();
  });

  describe('registration', () => {
    it('should register a singleton service', () => {
      serviceContainer.registerSingleton('testService', () => ({ value: 42 }));
      expect(serviceContainer.has('testService')).toBe(true);
    });

    it('should register a transient service', () => {
      serviceContainer.registerTransient('transientService', () => ({ value: Math.random() }));
      expect(serviceContainer.has('transientService')).toBe(true);
    });

    it('should register an instance directly', () => {
      const instance = { name: 'TestInstance' };
      serviceContainer.registerInstance('instanceService', instance);
      expect(serviceContainer.resolve('instanceService')).toBe(instance);
    });

    it('should warn when overwriting a service', () => {
      serviceContainer.register('myService', () => ({}));
      serviceContainer.register('myService', () => ({}));
      // Should not throw
      expect(serviceContainer.has('myService')).toBe(true);
    });
  });

  describe('resolution', () => {
    it('should resolve a singleton service', () => {
      serviceContainer.registerSingleton('singleton', () => ({ id: Date.now() }));
      
      const first = serviceContainer.resolve('singleton');
      const second = serviceContainer.resolve('singleton');
      
      expect(first).toBe(second);
    });

    it('should resolve a transient service with new instances', () => {
      let counter = 0;
      serviceContainer.registerTransient('transient', () => ({ count: ++counter }));
      
      const first = serviceContainer.resolve('transient');
      const second = serviceContainer.resolve('transient');
      
      expect(first.count).not.toBe(second.count);
    });

    it('should throw for unregistered service', () => {
      expect(() => serviceContainer.resolve('nonexistent')).toThrow();
    });

    it('should return null for tryResolve on unregistered service', () => {
      const result = serviceContainer.tryResolve('nonexistent');
      expect(result).toBeNull();
    });
  });

  describe('dependencies', () => {
    it('should resolve dependencies', () => {
      serviceContainer.registerSingleton('dep1', () => ({ value: 10 }));
      serviceContainer.registerSingleton('dep2', () => ({ value: 20 }));
      serviceContainer.register('main', (d1, d2) => ({
        sum: d1.value + d2.value
      }), {
        lifecycle: ServiceLifecycle.SINGLETON,
        dependencies: ['dep1', 'dep2']
      });

      const main = serviceContainer.resolve('main');
      expect(main.sum).toBe(30);
    });

    it('should detect circular dependencies', () => {
      serviceContainer.register('a', (b) => ({ b }), {
        dependencies: ['b']
      });
      serviceContainer.register('b', (a) => ({ a }), {
        dependencies: ['a']
      });

      expect(() => serviceContainer.resolve('a')).toThrow(/Circular dependency/);
    });

    it('should throw if dependency not found', () => {
      serviceContainer.register('service', (missing) => ({ missing }), {
        dependencies: ['missingDep']
      });

      expect(() => serviceContainer.resolve('service')).toThrow();
    });
  });

  describe('scopes', () => {
    it('should create a scope', () => {
      const scope = serviceContainer.createScope('testScope');
      expect(scope.name).toBe('testScope');
    });

    it('should cache scoped services within a scope', () => {
      let counter = 0;
      serviceContainer.register('scoped', () => ({ count: ++counter }), {
        lifecycle: ServiceLifecycle.SCOPED
      });

      serviceContainer.createScope('scope1');
      const first = serviceContainer.resolve('scoped');
      const second = serviceContainer.resolve('scoped');

      expect(first.count).toBe(second.count);
    });

    it('should dispose a scope', () => {
      const scope = serviceContainer.createScope('disposableScope');
      scope.dispose();
      // Should not throw
      expect(true).toBe(true);
    });
  });

  describe('service info', () => {
    it('should return service info', () => {
      serviceContainer.registerSingleton('infoService', () => ({}), ['dep1']);
      const info = serviceContainer.getServiceInfo('infoService');
      
      expect(info).toBeDefined();
      expect(info.name).toBe('infoService');
      expect(info.lifecycle).toBe(ServiceLifecycle.SINGLETON);
    });

    it('should return null for non-existent service', () => {
      const info = serviceContainer.getServiceInfo('nonexistent');
      expect(info).toBeNull();
    });

    it('should list registered services', () => {
      serviceContainer.register('service1', () => ({}));
      serviceContainer.register('service2', () => ({}));
      
      const services = serviceContainer.getRegisteredServices();
      expect(services).toContain('service1');
      expect(services).toContain('service2');
    });
  });

  describe('statistics', () => {
    it('should return container statistics', () => {
      serviceContainer.registerSingleton('s1', () => ({}));
      serviceContainer.registerTransient('t1', () => ({}));
      serviceContainer.resolve('s1'); // Instantiate singleton

      const stats = serviceContainer.getStats();
      
      expect(stats.totalServices).toBe(2);
      expect(stats.byLifecycle.singleton).toBe(1);
      expect(stats.byLifecycle.transient).toBe(1);
      expect(stats.instantiatedSingletons).toBe(1);
    });
  });

  describe('clear', () => {
    it('should clear all services', () => {
      serviceContainer.register('service1', () => ({}));
      serviceContainer.register('service2', () => ({}));
      
      serviceContainer.clear();
      
      expect(serviceContainer.has('service1')).toBe(false);
      expect(serviceContainer.has('service2')).toBe(false);
    });
  });
});

describe('Default container singleton', () => {
  it('should be a ServiceContainer instance', () => {
    expect(container).toBeInstanceOf(ServiceContainer);
  });
});
