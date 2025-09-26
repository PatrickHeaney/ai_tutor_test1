# AI Agent Mastery Project Tasks

This document outlines the specific implementation tasks for building the AI Agent, organized by iteration as defined in `PLANNING.md`.

## Iteration 1: The Core Conversation Loop

### Project Setup
- [ ] Create initial `requirements.txt` file.
- [ ] Create `.env.example` with `LLM_BASE_URL`, `LLM_API_KEY`, and `LLM_CHOICE`.
- [ ] Create the initial file structure (`agent.py`, `cli.py`, `tests/`).

### Agent Core (`agent.py`)
- [ ] Implement a basic agent class or function that can communicate with an LLM.
- [ ] Load LLM configuration from environment variables.
- [ ] Create a function to handle a single conversational turn (user input -> LLM response).

### Terminal UI (`cli.py`)
- [ ] Create the main application entry point.
- [ ] Implement a `while` loop to continuously accept user input.
- [ ] Call the agent with the user's input and print the response.
- [ ] Add a way for the user to exit the application (e.g., typing 'exit').

### Testing (`tests/test_agent.py`)
- [ ] Configure `pytest`.
- [ ] Write a unit test to verify the agent can be initialized.
- [ ] Write a unit test to check the conversation loop (mocking the LLM call).

### Documentation
- [ ] Update `README.md` with basic setup and usage instructions for running the terminal UI.

---

## Iteration 2: Adding Web Search (Future)
- [ ] ...

## Iteration 3: Adding Memory (Future)
- [ ] ...

