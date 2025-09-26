# AI Agent Mastery Project

This project is the starting point for building a conversational AI agent. The goal is to begin with a simple, runnable agent and iteratively add capabilities.

This README describes **Iteration 1: The Core Conversation Loop**. For the full development plan, see `PLANNING.md`.

## Features (Iteration 1)

- Basic, turn-by-turn conversation with an LLM.
- Terminal-based chat interface.
- Simple configuration for connecting to different LLM providers.

## Project Structure

```
ai-agent-mastery/
├── .env.example               # Example environment variables
├── requirements.txt           # Project dependencies
├── README.md                  # This project documentation
├── PLANNING.md                # The development plan
├── TASK.md                    # Implementation tasks
├── agent.py                   # Main agent implementation
├── cli.py                     # Terminal user interface
└── tests/                     # Test directory
    └── test_agent.py          # Agent tests
```

## Setup and Usage

### Prerequisites

- Python 3.11+

### 1. Environment Setup

1.  **Clone the repository** (if you haven't already).

2.  **Create and activate a virtual environment:**
    ```bash
    # Navigate to the project directory
    cd ai-agent-mastery

    # Create a virtual environment
    python -m venv venv

    # Activate the virtual environment
    # On Windows:
    # venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure your environment:**
    Create a `.env` file by copying the example file:
    ```bash
    # On Windows:
    # copy .env.example .env
    # On macOS/Linux:
    cp .env.example .env
    ```
    Then, edit the `.env` file with your LLM provider's details.

### 2. Configure the LLM

Fill in the `.env` file with the correct values for your LLM provider.

```
# Base URL for the OpenAI compatible instance
# e.g., https://api.openai.com/v1 or http://localhost:11434/v1 for Ollama
LLM_BASE_URL=

# API key for your LLM provider
LLM_API_KEY=

# The specific LLM you want to use
# e.g., gpt-4o-mini or llama3
LLM_CHOICE=
```

### 3. Run the Agent

Start the agent's command-line interface:

```bash
python cli.py
```

You can now chat with the agent in your terminal. To exit, type `exit`.

## Future Iterations

The next steps, as outlined in `PLANNING.md`, include:
- **Iteration 2:** Adding a web search tool.
- **Iteration 3:** Adding conversational memory.
