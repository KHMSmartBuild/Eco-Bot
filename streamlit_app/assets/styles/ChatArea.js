import React from 'react';
import Avatar from './Avatar';
import './ChatArea.css'; 

function ChatArea(props) {
    return (
        <div className="chat-area">
            <Avatar src="../assets/images/eco-bot.png" alt="Eco-Bot" />
            <div className="messages">
                {props.children}
            </div>
        </div>
    );
}

export default ChatArea;
