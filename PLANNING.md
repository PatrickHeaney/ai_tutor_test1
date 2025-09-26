
# AI Agent Mastery Project Planning

This document outlines the plan for building an AI agent, starting with a minimal, conversational core and iteratively adding features.

## Iterative Development Plan

The project will follow an iterative development model. Each iteration delivers a runnable, testable version of the agent with increasing capabilities, ensuring continuous feedback and progress.

### Iteration 1: The Core Conversation Loop
*   **Goal**: Create the simplest possible, runnable agent.
*   **Functionality**: A user can start a terminal UI, have a basic conversation with the agent (no tools, no memory), and the agent will respond using an LLM.
*   **Testing**: Unit tests for agent/UI initialization. User testing to confirm a basic conversation is possible.

### Iteration 2: Adding Web Search
*   **Goal**: Give the agent its first tool to access external knowledge.
*   **Functionality**: The agent can answer questions about recent events or topics outside its training data.
*   **Testing**: Unit tests for the web search tool. User testing to confirm the agent uses the tool correctly.

### Iteration 3: Adding Memory
*   **Goal**: Make the agent stateful and conversational.
*   **Functionality**: The agent can remember information from earlier in the same conversation.
*   **Testing**: Unit tests for memory integration. User testing by asking the agent to recall previously mentioned facts.

## System Architecture (Iteration 1)

For the first iteration, the architecture is minimal:

```
+-----------------+
|  Terminal UI    |
+--------+--------+
         |
+--------v--------+
|    AI Agent     |
| (LLM Wrapper)   |
+-----------------+
```

### Key Components (Iteration 1):

1.  **AI Agent**: A simple wrapper around an LLM to handle conversation.
2.  **Terminal User Interface**: A basic command-line interface for user interaction.

## Environment Configuration

The system will use environment variables for configuration. For Iteration 1, only the LLM configuration is needed.

```python
# Base URL for the OpenAI compatible instance
LLM_BASE_URL=

# API key for your LLM provider
LLM_API_KEY=

# The LLM you want to use for the agents.
LLM_CHOICE=
```

## File Structure (Iteration 1)

```
ai-agent-mastery/
├── .env.example               # Example environment variables
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
├── PLANNING.md                # This planning document
├── TASK.md                    # Implementation tasks
├── agent.py                   # Main agent implementation
├── cli.py                     # Terminal user interface
└── tests/                     # Test directory
    └── test_agent.py          # Agent tests
```

## Testing Strategy

Testing will focus on the components relevant to each iteration. For Iteration 1, this includes unit tests for the agent's initialization and basic response generation.