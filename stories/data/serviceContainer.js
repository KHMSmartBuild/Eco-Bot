/**
 * Eco-Bot Service Container
 * 
 * Implements a simple dependency injection container for the Eco-Bot system.
 * This allows for:
 * - Loose coupling between components
 * - Easy testing with mock services
 * - Runtime configuration of services
 * - Singleton and factory patterns
 * 
 * @module ServiceContainer
 * @version 1.0.0
 */

import { logger, LogCategory } from './logger.js';

/**
 * Service lifecycle types
 */
export const ServiceLifecycle = {
  SINGLETON: 'singleton',  // Single instance shared across all requests
  TRANSIENT: 'transient',  // New instance for each request
  SCOPED: 'scoped'         // Single instance per scope
};

/**
 * Service registration metadata
 */
class ServiceRegistration {
  constructor(name, factory, lifecycle, dependencies = []) {
    this.name = name;
    this.factory = factory;
    this.lifecycle = lifecycle;
    this.dependencies = dependencies;
    this.instance = null;
    this.registeredAt = new Date().toISOString();
  }
}

/**
 * Main Service Container class
 */
export class ServiceContainer {
  constructor() {
    this.services = new Map();
    this.scopes = new Map();
    this.currentScope = null;
    
    logger.info(LogCategory.SYSTEM, 'ServiceContainer initialized');
  }

  /**
   * Register a service with the container
   * 
   * @param {string} name - Service name/identifier
   * @param {Function} factory - Factory function to create the service
   * @param {Object} options - Registration options
   * @param {string} options.lifecycle - Service lifecycle (singleton, transient, scoped)
   * @param {string[]} options.dependencies - Names of dependent services
   */
  register(name, factory, options = {}) {
    const {
      lifecycle = ServiceLifecycle.SINGLETON,
      dependencies = []
    } = options;

    if (this.services.has(name)) {
      logger.warn(LogCategory.SYSTEM, `Service '${name}' is being overwritten`);
    }

    const registration = new ServiceRegistration(name, factory, lifecycle, dependencies);
    this.services.set(name, registration);

    logger.info(LogCategory.SYSTEM, `Service registered: ${name}`, { lifecycle, dependencies });

    return this;
  }

  /**
   * Register a singleton service (shorthand)
   */
  registerSingleton(name, factory, dependencies = []) {
    return this.register(name, factory, {
      lifecycle: ServiceLifecycle.SINGLETON,
      dependencies
    });
  }

  /**
   * Register a transient service (shorthand)
   */
  registerTransient(name, factory, dependencies = []) {
    return this.register(name, factory, {
      lifecycle: ServiceLifecycle.TRANSIENT,
      dependencies
    });
  }

  /**
   * Register an instance directly (for pre-created objects)
   */
  registerInstance(name, instance) {
    const registration = new ServiceRegistration(name, () => instance, ServiceLifecycle.SINGLETON);
    registration.instance = instance;
    this.services.set(name, registration);

    logger.info(LogCategory.SYSTEM, `Service instance registered: ${name}`);

    return this;
  }

  /**
   * Resolve a service by name
   * 
   * @param {string} name - Service name to resolve
   * @returns {*} The resolved service instance
   */
  resolve(name) {
    const registration = this.services.get(name);

    if (!registration) {
      logger.error(LogCategory.SYSTEM, `Service not found: ${name}`);
      throw new Error(`Service '${name}' is not registered`);
    }

    // Check for circular dependencies
    const resolving = new Set();
    return this._resolveWithDependencies(registration, resolving);
  }

  /**
   * Internal method to resolve a service with its dependencies
   */
  _resolveWithDependencies(registration, resolving) {
    if (resolving.has(registration.name)) {
      logger.error(LogCategory.SYSTEM, `Circular dependency detected: ${registration.name}`);
      throw new Error(`Circular dependency detected for service '${registration.name}'`);
    }

    resolving.add(registration.name);

    // Return cached instance for singletons
    if (registration.lifecycle === ServiceLifecycle.SINGLETON && registration.instance !== null) {
      resolving.delete(registration.name);
      return registration.instance;
    }

    // Check scoped instances
    if (registration.lifecycle === ServiceLifecycle.SCOPED && this.currentScope) {
      const scopedInstance = this.scopes.get(this.currentScope)?.get(registration.name);
      if (scopedInstance !== undefined) {
        resolving.delete(registration.name);
        return scopedInstance;
      }
    }

    // Resolve dependencies
    const dependencies = registration.dependencies.map(depName => {
      const depRegistration = this.services.get(depName);
      if (!depRegistration) {
        throw new Error(`Dependency '${depName}' not found for service '${registration.name}'`);
      }
      return this._resolveWithDependencies(depRegistration, resolving);
    });

    // Create instance
    const instance = registration.factory(...dependencies);

    // Cache based on lifecycle
    if (registration.lifecycle === ServiceLifecycle.SINGLETON) {
      registration.instance = instance;
    } else if (registration.lifecycle === ServiceLifecycle.SCOPED && this.currentScope) {
      if (!this.scopes.has(this.currentScope)) {
        this.scopes.set(this.currentScope, new Map());
      }
      this.scopes.get(this.currentScope).set(registration.name, instance);
    }

    resolving.delete(registration.name);

    logger.debug(LogCategory.SYSTEM, `Service resolved: ${registration.name}`, { lifecycle: registration.lifecycle });

    return instance;
  }

  /**
   * Try to resolve a service, returning null if not found
   */
  tryResolve(name) {
    try {
      return this.resolve(name);
    } catch {
      return null;
    }
  }

  /**
   * Check if a service is registered
   */
  has(name) {
    return this.services.has(name);
  }

  /**
   * Create a new scope for scoped services
   */
  createScope(scopeName = `scope-${Date.now()}`) {
    this.currentScope = scopeName;
    this.scopes.set(scopeName, new Map());
    
    logger.debug(LogCategory.SYSTEM, `Scope created: ${scopeName}`);

    return {
      name: scopeName,
      dispose: () => this.disposeScope(scopeName)
    };
  }

  /**
   * Dispose a scope and its cached instances
   */
  disposeScope(scopeName) {
    if (this.scopes.has(scopeName)) {
      this.scopes.delete(scopeName);
      if (this.currentScope === scopeName) {
        this.currentScope = null;
      }
      logger.debug(LogCategory.SYSTEM, `Scope disposed: ${scopeName}`);
    }
  }

  /**
   * Get all registered service names
   */
  getRegisteredServices() {
    return Array.from(this.services.keys());
  }

  /**
   * Get service registration info
   */
  getServiceInfo(name) {
    const registration = this.services.get(name);
    if (!registration) return null;

    return {
      name: registration.name,
      lifecycle: registration.lifecycle,
      dependencies: registration.dependencies,
      hasInstance: registration.instance !== null,
      registeredAt: registration.registeredAt
    };
  }

  /**
   * Get container statistics
   */
  getStats() {
    const stats = {
      totalServices: this.services.size,
      byLifecycle: {
        singleton: 0,
        transient: 0,
        scoped: 0
      },
      activeScopes: this.scopes.size,
      instantiatedSingletons: 0
    };

    this.services.forEach(reg => {
      stats.byLifecycle[reg.lifecycle]++;
      if (reg.lifecycle === ServiceLifecycle.SINGLETON && reg.instance !== null) {
        stats.instantiatedSingletons++;
      }
    });

    return stats;
  }

  /**
   * Clear all services (useful for testing)
   */
  clear() {
    this.services.clear();
    this.scopes.clear();
    this.currentScope = null;
    logger.info(LogCategory.SYSTEM, 'ServiceContainer cleared');
  }
}

// Create and export a default container instance
export const container = new ServiceContainer();

/**
 * Decorator-style function for auto-registration
 * Usage: withInjection(['dep1', 'dep2'], MyComponent)
 */
export function withInjection(dependencies, Component) {
  return function InjectedComponent(props) {
    const resolvedDeps = dependencies.reduce((acc, dep) => {
      acc[dep] = container.resolve(dep);
      return acc;
    }, {});

    return Component({ ...props, ...resolvedDeps });
  };
}

export default container;
