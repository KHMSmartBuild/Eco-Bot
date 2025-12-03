import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import './StoryFrame.css';

/**
 * StoryFrame Component
 * 
 * A dynamic story frame component designed to be populated by multi-agents.
 * Each frame can contain:
 * - Title/Chapter heading
 * - Narrative text
 * - Illustration placeholder or image
 * - Character/Agent attribution
 * - Interactive elements
 * 
 * This component supports dynamic content injection from the Eco-Bot multi-agent system.
 */
function StoryFrame({
  id,
  title,
  chapter,
  content,
  illustration,
  illustrationAlt,
  agent,
  agentAvatar,
  timestamp,
  mood,
  interactive,
  onInteraction,
  children,
  variant,
  loading
}) {
  const [isExpanded, setIsExpanded] = useState(false);
  const [animationState, setAnimationState] = useState('idle');

  useEffect(() => {
    if (loading) {
      setAnimationState('loading');
    } else {
      setAnimationState('ready');
    }
  }, [loading]);

  const handleInteraction = (action) => {
    if (onInteraction) {
      onInteraction({ frameId: id, action, timestamp: new Date().toISOString() });
    }
  };

  const moodStyles = {
    curious: { borderColor: '#4CAF50', backgroundColor: '#E8F5E9' },
    excited: { borderColor: '#FF9800', backgroundColor: '#FFF3E0' },
    thoughtful: { borderColor: '#2196F3', backgroundColor: '#E3F2FD' },
    wise: { borderColor: '#9C27B0', backgroundColor: '#F3E5F5' },
    playful: { borderColor: '#E91E63', backgroundColor: '#FCE4EC' },
    default: { borderColor: '#607D8B', backgroundColor: '#ECEFF1' }
  };

  const currentMoodStyle = moodStyles[mood] || moodStyles.default;

  return (
    <article 
      className={`story-frame story-frame--${variant} ${loading ? 'story-frame--loading' : ''}`}
      style={currentMoodStyle}
      data-frame-id={id}
      data-mood={mood}
    >
      {/* Header Section */}
      <header className="story-frame__header">
        {chapter && (
          <span className="story-frame__chapter">Chapter {chapter}</span>
        )}
        {title && (
          <h2 className="story-frame__title">{title}</h2>
        )}
        {timestamp && (
          <time className="story-frame__timestamp" dateTime={timestamp}>
            {new Date(timestamp).toLocaleDateString()}
          </time>
        )}
      </header>

      {/* Illustration Section */}
      <div className="story-frame__illustration">
        {loading ? (
          <div className="story-frame__placeholder story-frame__placeholder--loading">
            <div className="story-frame__spinner"></div>
            <span>Agent is creating illustration...</span>
          </div>
        ) : illustration ? (
          <img 
            src={illustration} 
            alt={illustrationAlt || `Illustration for ${title}`}
            className="story-frame__image"
          />
        ) : (
          <div className="story-frame__placeholder">
            <svg className="story-frame__placeholder-icon" viewBox="0 0 100 100">
              <rect x="10" y="10" width="80" height="60" fill="none" stroke="currentColor" strokeWidth="2"/>
              <circle cx="30" cy="30" r="8" fill="currentColor"/>
              <path d="M10 70 L40 45 L60 60 L90 35" fill="none" stroke="currentColor" strokeWidth="2"/>
            </svg>
            <span>Illustration Placeholder</span>
            <small>Ready for agent-generated content</small>
          </div>
        )}
      </div>

      {/* Content Section */}
      <div className={`story-frame__content ${isExpanded ? 'story-frame__content--expanded' : ''}`}>
        {loading ? (
          <div className="story-frame__content-loading">
            <div className="story-frame__text-skeleton"></div>
            <div className="story-frame__text-skeleton"></div>
            <div className="story-frame__text-skeleton story-frame__text-skeleton--short"></div>
          </div>
        ) : (
          <>
            <p className="story-frame__text">{content}</p>
            {children}
          </>
        )}
      </div>

      {/* Agent Attribution */}
      {agent && (
        <footer className="story-frame__footer">
          <div className="story-frame__agent">
            {agentAvatar && (
              <img 
                src={agentAvatar} 
                alt={`${agent} avatar`}
                className="story-frame__agent-avatar"
              />
            )}
            <span className="story-frame__agent-name">Narrated by {agent}</span>
          </div>
        </footer>
      )}

      {/* Interactive Elements */}
      {interactive && (
        <div className="story-frame__actions">
          <button 
            className="story-frame__action-btn"
            onClick={() => {
              setIsExpanded(!isExpanded);
              handleInteraction('expand');
            }}
          >
            {isExpanded ? 'Show Less' : 'Read More'}
          </button>
          <button 
            className="story-frame__action-btn story-frame__action-btn--secondary"
            onClick={() => handleInteraction('regenerate')}
          >
            🔄 Regenerate
          </button>
          <button 
            className="story-frame__action-btn story-frame__action-btn--secondary"
            onClick={() => handleInteraction('share')}
          >
            📤 Share
          </button>
        </div>
      )}
    </article>
  );
}

StoryFrame.propTypes = {
  /** Unique identifier for the frame */
  id: PropTypes.string.isRequired,
  /** Title of the story frame */
  title: PropTypes.string,
  /** Chapter number */
  chapter: PropTypes.number,
  /** Main narrative content */
  content: PropTypes.string,
  /** URL for the illustration image */
  illustration: PropTypes.string,
  /** Alt text for the illustration */
  illustrationAlt: PropTypes.string,
  /** Name of the agent/narrator */
  agent: PropTypes.string,
  /** Avatar URL for the agent */
  agentAvatar: PropTypes.string,
  /** Timestamp for the frame creation */
  timestamp: PropTypes.string,
  /** Mood/theme of the frame affecting styling */
  mood: PropTypes.oneOf(['curious', 'excited', 'thoughtful', 'wise', 'playful', 'default']),
  /** Whether interactive controls should be shown */
  interactive: PropTypes.bool,
  /** 
   * Callback for user interactions
   * @param {Object} event - The interaction event
   * @param {string} event.frameId - ID of the frame
   * @param {string} event.action - Action type ('expand', 'regenerate', 'share')
   * @param {string} event.timestamp - ISO timestamp of the interaction
   */
  onInteraction: PropTypes.func,
  /** Additional content to render */
  children: PropTypes.node,
  /** Visual variant of the frame */
  variant: PropTypes.oneOf(['default', 'featured', 'compact', 'full-width']),
  /** Loading state */
  loading: PropTypes.bool
};

StoryFrame.defaultProps = {
  mood: 'default',
  variant: 'default',
  interactive: false,
  loading: false
};

export default StoryFrame;
