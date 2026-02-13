/**
 * Eco-Bot Storybook Logger
 * 
 * A comprehensive logging utility for the Storybook data management system.
 * Provides structured logging with different levels, timestamps, and context.
 */

// Log levels
export const LogLevel = {
  DEBUG: 'debug',
  INFO: 'info',
  WARN: 'warn',
  ERROR: 'error'
};

// Log categories for filtering
export const LogCategory = {
  DATA: 'data',
  VALIDATION: 'validation',
  TRANSFORMATION: 'transformation',
  COMPONENT: 'component',
  VISUALIZATION: 'visualization',
  SYSTEM: 'system'
};

/**
 * Logger configuration
 */
const config = {
  enabled: true,
  minLevel: LogLevel.DEBUG,
  includeTimestamp: true,
  includeCategory: true,
  maxLogHistory: 100,
  persistToStorage: false
};

/**
 * In-memory log storage for debugging and analysis
 */
const logHistory = [];

/**
 * Format a log entry with timestamp and metadata
 */
const formatLogEntry = (level, category, message, data = null) => {
  const entry = {
    timestamp: new Date().toISOString(),
    level,
    category,
    message,
    data
  };
  
  return entry;
};

/**
 * Get the console method for a log level
 */
const getConsoleMethod = (level) => {
  switch (level) {
    case LogLevel.DEBUG:
      return console.debug;
    case LogLevel.INFO:
      return console.info;
    case LogLevel.WARN:
      return console.warn;
    case LogLevel.ERROR:
      return console.error;
    default:
      return console.log;
  }
};

/**
 * Check if a log level should be displayed
 */
const shouldLog = (level) => {
  if (!config.enabled) return false;
  
  const levels = [LogLevel.DEBUG, LogLevel.INFO, LogLevel.WARN, LogLevel.ERROR];
  const minIndex = levels.indexOf(config.minLevel);
  const currentIndex = levels.indexOf(level);
  
  return currentIndex >= minIndex;
};

/**
 * Format the log output for console
 */
const formatConsoleOutput = (entry) => {
  const parts = [];
  
  if (config.includeTimestamp) {
    parts.push(`[${entry.timestamp}]`);
  }
  
  parts.push(`[${entry.level.toUpperCase()}]`);
  
  if (config.includeCategory) {
    parts.push(`[${entry.category}]`);
  }
  
  parts.push(entry.message);
  
  return parts.join(' ');
};

/**
 * Main logging function
 */
const log = (level, category, message, data = null) => {
  if (!shouldLog(level)) return;
  
  const entry = formatLogEntry(level, category, message, data);
  
  // Store in history
  logHistory.push(entry);
  if (logHistory.length > config.maxLogHistory) {
    logHistory.shift();
  }
  
  // Output to console
  const consoleMethod = getConsoleMethod(level);
  const formattedMessage = formatConsoleOutput(entry);
  
  if (data !== null) {
    consoleMethod(formattedMessage, data);
  } else {
    consoleMethod(formattedMessage);
  }
  
  // Persist to storage if enabled
  if (config.persistToStorage && typeof localStorage !== 'undefined') {
    try {
      localStorage.setItem('eco-bot-logs', JSON.stringify(logHistory.slice(-50)));
    } catch (e) {
      // Storage might be full or unavailable
    }
  }
  
  return entry;
};

/**
 * Logger API
 */
export const logger = {
  // Convenience methods for each level
  debug: (category, message, data) => log(LogLevel.DEBUG, category, message, data),
  info: (category, message, data) => log(LogLevel.INFO, category, message, data),
  warn: (category, message, data) => log(LogLevel.WARN, category, message, data),
  error: (category, message, data) => log(LogLevel.ERROR, category, message, data),
  
  // Category-specific loggers
  data: {
    debug: (message, data) => log(LogLevel.DEBUG, LogCategory.DATA, message, data),
    info: (message, data) => log(LogLevel.INFO, LogCategory.DATA, message, data),
    warn: (message, data) => log(LogLevel.WARN, LogCategory.DATA, message, data),
    error: (message, data) => log(LogLevel.ERROR, LogCategory.DATA, message, data)
  },
  
  validation: {
    debug: (message, data) => log(LogLevel.DEBUG, LogCategory.VALIDATION, message, data),
    info: (message, data) => log(LogLevel.INFO, LogCategory.VALIDATION, message, data),
    warn: (message, data) => log(LogLevel.WARN, LogCategory.VALIDATION, message, data),
    error: (message, data) => log(LogLevel.ERROR, LogCategory.VALIDATION, message, data)
  },
  
  visualization: {
    debug: (message, data) => log(LogLevel.DEBUG, LogCategory.VISUALIZATION, message, data),
    info: (message, data) => log(LogLevel.INFO, LogCategory.VISUALIZATION, message, data),
    warn: (message, data) => log(LogLevel.WARN, LogCategory.VISUALIZATION, message, data),
    error: (message, data) => log(LogLevel.ERROR, LogCategory.VISUALIZATION, message, data)
  },
  
  // Configuration
  configure: (options) => {
    Object.assign(config, options);
    logger.info(LogCategory.SYSTEM, 'Logger configuration updated', options);
  },
  
  // Enable/disable logging
  enable: () => {
    config.enabled = true;
    console.info('[Logger] Logging enabled');
  },
  
  disable: () => {
    config.enabled = false;
    console.info('[Logger] Logging disabled');
  },
  
  // Set minimum log level
  setLevel: (level) => {
    config.minLevel = level;
    console.info(`[Logger] Minimum log level set to: ${level}`);
  },
  
  // Get log history
  getHistory: (options = {}) => {
    let history = [...logHistory];
    
    if (options.level) {
      history = history.filter(entry => entry.level === options.level);
    }
    
    if (options.category) {
      history = history.filter(entry => entry.category === options.category);
    }
    
    if (options.since) {
      const sinceDate = new Date(options.since);
      history = history.filter(entry => new Date(entry.timestamp) >= sinceDate);
    }
    
    if (options.limit) {
      history = history.slice(-options.limit);
    }
    
    return history;
  },
  
  // Clear log history
  clearHistory: () => {
    logHistory.length = 0;
    logger.info(LogCategory.SYSTEM, 'Log history cleared');
  },
  
  // Export logs as JSON
  exportLogs: () => {
    return JSON.stringify(logHistory, null, 2);
  },
  
  // Get statistics
  getStats: () => {
    const stats = {
      total: logHistory.length,
      byLevel: {},
      byCategory: {}
    };
    
    Object.values(LogLevel).forEach(level => {
      stats.byLevel[level] = logHistory.filter(e => e.level === level).length;
    });
    
    Object.values(LogCategory).forEach(category => {
      stats.byCategory[category] = logHistory.filter(e => e.category === category).length;
    });
    
    return stats;
  }
};

export default logger;
