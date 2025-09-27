
import asyncio
from agent import get_agent_response

async def main():
    """
    Main function to run the command-line interface for the agent.
    """
    print("AI Agent CLI")
    print("------------")
    print("Type 'exit' or 'quit' to end the conversation.")

    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break

            print("\nAI is thinking...")
            response = await get_agent_response(user_input)
            print(f"\nAI: {response}")

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
