import React from 'react';
import PropTypes from 'prop-types';
import Avatar from './Avatar';
import './ChatArea.css';

/**
 * ChatArea component combines Avatar and message display
 * Used for showing conversations between users and eco-buddies
 */
function ChatArea({ children, avatarSrc, avatarAlt, messages, userName }) {
  return (
    <div className="chat-area">
      <div className="chat-header">
        <Avatar src={avatarSrc} alt={avatarAlt || "Avatar"} size={60} />
        {userName && <span className="user-name">{userName}</span>}
      </div>
      <div className="messages">
        {messages && messages.map((msg, index) => (
          <div 
            key={index} 
            className={`message ${msg.role === 'user' ? 'message-user' : 'message-bot'}`}
          >
            <span className="message-role">{msg.role}:</span>
            <span className="message-content">{msg.content}</span>
          </div>
        ))}
        {children}
      </div>
    </div>
  );
}

ChatArea.propTypes = {
  /** Additional content to render in the messages area */
  children: PropTypes.node,
  /** Avatar image source URL */
  avatarSrc: PropTypes.string.isRequired,
  /** Avatar alt text */
  avatarAlt: PropTypes.string,
  /** Array of message objects with role and content */
  messages: PropTypes.arrayOf(
    PropTypes.shape({
      role: PropTypes.string.isRequired,
      content: PropTypes.string.isRequired,
    })
  ),
  /** Display name for the user/bot */
  userName: PropTypes.string,
};

ChatArea.defaultProps = {
  avatarAlt: 'Avatar',
  messages: [],
};

export default ChatArea;
