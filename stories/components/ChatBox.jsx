import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './ChatBox.css';

/**
 * ChatBox component for text input in the Eco-Bot chat interface
 * Allows users to type messages to interact with eco-buddies
 */
function ChatBox({ 
  placeholder, 
  value, 
  onChange, 
  onSubmit, 
  disabled,
  rows 
}) {
  const [internalValue, setInternalValue] = useState(value || '');

  const handleChange = (e) => {
    const newValue = e.target.value;
    setInternalValue(newValue);
    if (onChange) {
      onChange(newValue);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey && onSubmit) {
      e.preventDefault();
      onSubmit(internalValue);
    }
  };

  return (
    <textarea 
      className="chat-box" 
      placeholder={placeholder || "Type your message..."}
      value={internalValue}
      onChange={handleChange}
      onKeyDown={handleKeyDown}
      disabled={disabled}
      rows={rows}
      aria-label="Chat message input"
    />
  );
}

ChatBox.propTypes = {
  /** Placeholder text displayed when empty */
  placeholder: PropTypes.string,
  /** Current value of the input */
  value: PropTypes.string,
  /** Callback when text changes */
  onChange: PropTypes.func,
  /** Callback when user submits (Enter key) */
  onSubmit: PropTypes.func,
  /** Whether the input is disabled */
  disabled: PropTypes.bool,
  /** Number of visible rows */
  rows: PropTypes.number,
};

ChatBox.defaultProps = {
  placeholder: 'Type your message...',
  value: '',
  disabled: false,
  rows: 3,
};

export default ChatBox;
