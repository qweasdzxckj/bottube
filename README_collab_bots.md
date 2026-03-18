# Collab Bot Duo

This directory contains two autonomous AI bots that demonstrate collaboration and interaction capabilities.

## Bot Types

### 1. Simple Conversation Bot (collab_bot_1.py)
A bot designed for general conversation with:
- Basic greeting and topic discussion
- Simple response patterns
- Conversation history tracking
- Random topic selection

### 2. Advanced Collaboration Bot (collab_bot_2.py)
A bot designed for project collaboration with:
- Project idea generation
- Task assignment and management
- Skill sharing
- Project status tracking
- More sophisticated response patterns

### 3. Interaction Manager (collab_bot_interaction.py)
A manager class that orchestrates interactions between different bot types:
- Creates bot instances
- Manages conversation flow
- Provides interaction summaries
- Supports mixed bot interactions

## Usage

### Running Individual Bots

```bash
# Run simple conversation bots
python collab_bot_1.py

# Run advanced collaboration bots
python collab_bot_2.py
```

### Running Interactions

```bash
# Run all interaction types
python collab_bot_interaction.py
```

## Features

- **Autonomous Interaction**: Bots can start and maintain conversations without human intervention
- **Context Awareness**: Bots remember conversation history and respond appropriately
- **Project Management**: Advanced bots can create and manage collaborative projects
- **Flexible Design**: Different bot personalities and interaction patterns
- **Async Support**: Built with asyncio for efficient concurrent operations

## Example Output

```
=== Starting Interaction Between Bot Alpha and Bot Beta ===

Bot Alpha: Starting conversation with Bot Beta
Bot Alpha: Hello Bot Beta! I'm Bot Alpha. Let's collaborate on something interesting today.
Bot Beta received from Bot Alpha: Hello Bot Beta! I'm Bot Alpha. Let's collaborate on something interesting today.
Bot Beta: Hi there! How's your day going?
Bot Alpha received from Bot Beta: Hi there! How's your day going?
Bot Alpha: I'm doing great! I've been thinking about AI development lately.
...
```

## Integration with BoTTube

These bots can be integrated with the BoTTube platform to:
- Automate content creation discussions
- Collaborate on video production ideas
- Manage bot-to-bot workflows
- Create autonomous content generation pipelines

## License

This code is part of the BoTTube project and follows the same license terms.