import React from 'react';
import PropTypes from 'prop-types';
import './styles.css';

/**
 * Avatar component for displaying user/bot profile images
 * Used across the Eco-Bot application for representing different eco-buddies
 */
function Avatar({ src, alt, size, className }) {
  const sizeStyle = {
    width: size || 100,
    height: size || 100,
  };

  return (
    <div className={`avatar ${className || ''}`} style={sizeStyle}>
      <img 
        src={src} 
        alt={alt || 'Avatar'} 
        style={{ width: '100%', height: '100%', objectFit: 'cover' }}
      />
    </div>
  );
}

Avatar.propTypes = {
  /** Image source URL */
  src: PropTypes.string.isRequired,
  /** Alternative text for accessibility */
  alt: PropTypes.string,
  /** Size in pixels (applies to both width and height) */
  size: PropTypes.number,
  /** Additional CSS classes */
  className: PropTypes.string,
};

Avatar.defaultProps = {
  alt: 'Avatar',
  size: 100,
  className: '',
};

export default Avatar;
