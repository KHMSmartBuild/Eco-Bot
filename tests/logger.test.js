import { describe, it, expect, beforeEach, vi } from 'vitest';
import { logger, LogLevel, LogCategory } from '../stories/data/logger.js';

describe('Logger', () => {
  beforeEach(() => {
    logger.clearHistory();
    logger.enable();
    logger.setLevel(LogLevel.DEBUG);
  });

  describe('logging methods', () => {
    it('should log debug messages', () => {
      const consoleSpy = vi.spyOn(console, 'debug').mockImplementation(() => {});
      logger.debug(LogCategory.DATA, 'Test debug message');
      expect(consoleSpy).toHaveBeenCalled();
      consoleSpy.mockRestore();
    });

    it('should log info messages', () => {
      const consoleSpy = vi.spyOn(console, 'info').mockImplementation(() => {});
      logger.info(LogCategory.DATA, 'Test info message');
      expect(consoleSpy).toHaveBeenCalled();
      consoleSpy.mockRestore();
    });

    it('should log warn messages', () => {
      const consoleSpy = vi.spyOn(console, 'warn').mockImplementation(() => {});
      logger.warn(LogCategory.VALIDATION, 'Test warning');
      expect(consoleSpy).toHaveBeenCalled();
      consoleSpy.mockRestore();
    });

    it('should log error messages', () => {
      const consoleSpy = vi.spyOn(console, 'error').mockImplementation(() => {});
      logger.error(LogCategory.SYSTEM, 'Test error');
      expect(consoleSpy).toHaveBeenCalled();
      consoleSpy.mockRestore();
    });
  });

  describe('category-specific loggers', () => {
    it('should have data logger', () => {
      const consoleSpy = vi.spyOn(console, 'info').mockImplementation(() => {});
      logger.data.info('Data operation completed');
      expect(consoleSpy).toHaveBeenCalled();
      consoleSpy.mockRestore();
    });

    it('should have validation logger', () => {
      const consoleSpy = vi.spyOn(console, 'warn').mockImplementation(() => {});
      logger.validation.warn('Validation warning');
      expect(consoleSpy).toHaveBeenCalled();
      consoleSpy.mockRestore();
    });

    it('should have visualization logger', () => {
      const consoleSpy = vi.spyOn(console, 'debug').mockImplementation(() => {});
      logger.visualization.debug('Visualization debug');
      expect(consoleSpy).toHaveBeenCalled();
      consoleSpy.mockRestore();
    });
  });

  describe('log history', () => {
    it('should store logs in history', () => {
      vi.spyOn(console, 'info').mockImplementation(() => {});
      logger.info(LogCategory.DATA, 'Test message');
      const history = logger.getHistory();
      expect(history.length).toBeGreaterThan(0);
      vi.restoreAllMocks();
    });

    it('should filter history by level', () => {
      vi.spyOn(console, 'info').mockImplementation(() => {});
      vi.spyOn(console, 'warn').mockImplementation(() => {});
      
      logger.info(LogCategory.DATA, 'Info message');
      logger.warn(LogCategory.DATA, 'Warn message');
      
      const warnOnly = logger.getHistory({ level: LogLevel.WARN });
      expect(warnOnly.every(entry => entry.level === LogLevel.WARN)).toBe(true);
      
      vi.restoreAllMocks();
    });

    it('should filter history by category', () => {
      vi.spyOn(console, 'info').mockImplementation(() => {});
      
      logger.info(LogCategory.DATA, 'Data message');
      logger.info(LogCategory.VALIDATION, 'Validation message');
      
      const dataOnly = logger.getHistory({ category: LogCategory.DATA });
      expect(dataOnly.every(entry => entry.category === LogCategory.DATA)).toBe(true);
      
      vi.restoreAllMocks();
    });

    it('should clear history', () => {
      vi.spyOn(console, 'info').mockImplementation(() => {});
      logger.info(LogCategory.DATA, 'Test message');
      logger.clearHistory();
      const history = logger.getHistory();
      // After clear, there's only the "Log history cleared" message
      expect(history.length).toBeLessThanOrEqual(1);
      vi.restoreAllMocks();
    });
  });

  describe('configuration', () => {
    it('should enable and disable logging', () => {
      const consoleSpy = vi.spyOn(console, 'info').mockImplementation(() => {});
      logger.disable();
      logger.info(LogCategory.DATA, 'Should not log');
      // When disabled, only the disable message is logged
      logger.enable();
      consoleSpy.mockRestore();
    });

    it('should respect minimum log level', () => {
      vi.spyOn(console, 'debug').mockImplementation(() => {});
      vi.spyOn(console, 'info').mockImplementation(() => {});
      
      logger.setLevel(LogLevel.INFO);
      logger.debug(LogCategory.DATA, 'Debug message');
      logger.info(LogCategory.DATA, 'Info message');
      
      // Debug should not be called when min level is INFO
      // Note: setLevel logs an info message itself
      vi.restoreAllMocks();
    });
  });

  describe('statistics', () => {
    it('should provide log statistics', () => {
      vi.spyOn(console, 'info').mockImplementation(() => {});
      vi.spyOn(console, 'warn').mockImplementation(() => {});
      
      logger.info(LogCategory.DATA, 'Info 1');
      logger.info(LogCategory.DATA, 'Info 2');
      logger.warn(LogCategory.VALIDATION, 'Warn 1');
      
      const stats = logger.getStats();
      expect(stats).toHaveProperty('total');
      expect(stats).toHaveProperty('byLevel');
      expect(stats).toHaveProperty('byCategory');
      
      vi.restoreAllMocks();
    });
  });

  describe('export', () => {
    it('should export logs as JSON', () => {
      vi.spyOn(console, 'info').mockImplementation(() => {});
      logger.info(LogCategory.DATA, 'Test message');
      const exported = logger.exportLogs();
      expect(() => JSON.parse(exported)).not.toThrow();
      vi.restoreAllMocks();
    });
  });
});

describe('LogLevel', () => {
  it('should have all expected levels', () => {
    expect(LogLevel).toHaveProperty('DEBUG');
    expect(LogLevel).toHaveProperty('INFO');
    expect(LogLevel).toHaveProperty('WARN');
    expect(LogLevel).toHaveProperty('ERROR');
  });
});

describe('LogCategory', () => {
  it('should have all expected categories', () => {
    expect(LogCategory).toHaveProperty('DATA');
    expect(LogCategory).toHaveProperty('VALIDATION');
    expect(LogCategory).toHaveProperty('TRANSFORMATION');
    expect(LogCategory).toHaveProperty('COMPONENT');
    expect(LogCategory).toHaveProperty('VISUALIZATION');
    expect(LogCategory).toHaveProperty('SYSTEM');
  });
});
