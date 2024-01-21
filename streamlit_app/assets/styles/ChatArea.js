import React from 'react';
import Avatar from './Avatar';
import './styles.css'; 

/**
 * Render the ChatArea component.
 *
 * @param {object} props - The properties passed to the component, including the avatar source.
 * @return {JSX.Element} The rendered component.
 */
function ChatArea({ children, avatarSrc, avatarAlt }) {
    return (
        <div className="chat-area">
            <Avatar src={avatarSrc} alt={avatarAlt || "Avatar"} />
            <div className="messages">
                {children}
            </div>
        </div>
    );
}

export default ChatArea;
