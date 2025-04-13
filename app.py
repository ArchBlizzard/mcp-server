import logging
from flask import Flask, request, jsonify
from mcp.server import MCPServer
import config

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
mcp_server = MCPServer()

@app.route("/webhook", methods=["POST"])
def whatsapp_webhook():
    """Handle incoming WhatsApp messages"""
    try:
        # Extract message content from Twilio webhook
        incoming_msg = request.form.get("Body", "").strip()
        sender = request.form.get("From", "")
        
        # Check if it's a media message (voice note)
        num_media = int(request.form.get("NumMedia", 0))
        media_url = None
        
        if num_media > 0:
            media_url = request.form.get("MediaUrl0", "")
            media_type = request.form.get("MediaContentType0", "")
            
            if "audio" in media_type:
                # Handle voice message
                logger.info(f"Received voice message from {sender}")
                response = mcp_server.handle_voice_message(sender, media_url)
            else:
                # Unsupported media type
                response = "Sorry, I can only process text or voice messages."
        else:
            # Handle text message
            logger.info(f"Received text message from {sender}: {incoming_msg}")
            response = mcp_server.handle_text_message(sender, incoming_msg)
            
        return jsonify({"status": "success", "response": response})
    
    except Exception as e:
        logger.error(f"Error processing webhook: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/health", methods=["GET"])
def health_check():
    """Simple health check endpoint"""
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    logger.info(f"Starting MCP server on {config.HOST}:{config.PORT}")
    app.run(host=config.HOST, port=config.PORT, debug=True)