# Voice-Enabled MCP Server
An MCP server connecting Claude AI with ElevenLabs for voice enabled conversation capabilities.

## Quick Setup
### Prerequisites
- Claude Desktop
- ElevenLabs API key
- Python 3.8+

### Installation

1. Install `uv` package manager:
```python
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Install the MCP server:
```python
uv pip install elevenlabs-mcp
```

3. Configure Claude Desktop:
   - Go to Settings > Developer > Edit Config
   - Add to `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "ElevenLabs": {
      "command": "uvx",
      "args": ["elevenlabs-mcp"],
      "env": {
        "ELEVENLABS_API_KEY": "YOUR_API_KEY"
      }
    }
  }
}
```

**Windows users:** Enable Developer Mode via Help > Enable Developer Mode

## Usage

1. Launch Claude Desktop
2. After successful integration, you'll see a developer sign indicating 19 available ElevenLabs MCP tools
3. Start a voice conversation with ElevenLabs by stating your preferred voice ID
4. The AI will now respond to your queries using the selected ElevenLabs voice, powered by Claude's intelligence
5. You can have natural voice conversations, asking questions and receiving spoken responses

## Demo

[Watch the demo](https://drive.google.com/file/d/1Vy-r1D8sR04FSJgS6KFespOZdVgMPrPK/view?usp=sharing)
