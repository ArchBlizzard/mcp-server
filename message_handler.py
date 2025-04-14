import logging
from datetime import datetime
import config

logger = logging.getLogger(__name__)

class MessageHandler:
    def __init__(self):
        """Initialize the message handler"""
        self.conversation_history = config.CONVERSATION_HISTORY
        logger.info("Message handler initialized")
    
    def add_to_history(self, user_id, role, content):
        """
        Add a message to the conversation history
        
        Args:
            user_id: The user's identifier
            role: The role of the message sender (user or assistant)
            content: The message content
            
        Returns:
            bool: Success status
        """
        try:
            # Initialize conversation history for this user if it doesn't exist
            if user_id not in self.conversation_history:
                self.conversation_history[user_id] = []
            
            # Add the message to history
            self.conversation_history[user_id].append({
                "role": role,
                "content": content,
                "timestamp": datetime.now().isoformat()
            })
            
            # Limit history size (keep last 10 messages)
            if len(self.conversation_history[user_id]) > 10:
                self.conversation_history[user_id] = self.conversation_history[user_id][-10:]
            
            logger.info(f"Added message to history for user {user_id}")
            return True
            
        except Exception as e:
            logger.error(f"Error adding to history: {str(e)}")
            return False
    
    def get_conversation_context(self, user_id):
        """
        Get the conversation context for a user
        
        Args:
            user_id: The user's identifier
            
        Returns:
            list: Conversation context
        """
        try:
            # Return the conversation history in the format needed by Claude
            if user_id in self.conversation_history:
                # Format for Claude API
                claude_messages = []
                
                for msg in self.conversation_history[user_id]:
                    claude_messages.append({
                        "role": msg["role"],
                        "content": msg["content"]
                    })
                
                return claude_messages
            else:
                return []
                
        except Exception as e:
            logger.error(f"Error getting conversation context: {str(e)}")
            return []
    
    def clear_history(self, user_id):
        """
        Clear the conversation history for a user
        
        Args:
            user_id: The user's identifier
            
        Returns:
            bool: Success status
        """
        try:
            if user_id in self.conversation_history:
                self.conversation_history[user_id] = []
                logger.info(f"Cleared history for user {user_id}")
                return True
            else:
                logger.warning(f"No history found for user {user_id}")
                return False
                
        except Exception as e:
            logger.error(f"Error clearing history: {str(e)}")
            return False