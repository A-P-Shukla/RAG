from dotenv import load_dotenv
load_dotenv()

import importlib.metadata
from langchain_core import __version__ as core_version
try:
    lg_version = importlib.metadata.version("langgraph")
except importlib.metadata.PackageNotFoundError:
    lg_version = "unknown"
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI


print(f"langchain-core version: {core_version}")
print(f"langgraph version: {lg_version}")




def main():
    #Test Gemini
    llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0)
    response = llm.invoke("Say 'setup complete!' in one word")
    print(f"Response from ChatGoogleGenerativeAI: {response.content}")

    #Test Anthropic
    llm_anthropic = ChatAnthropic(model="claude-sonnet-4-5-20250929", temperature=0)
    response_anthropic = llm_anthropic.invoke("Say 'setup complete!' in one word")
    print(f"Response from ChatAnthropic: {response_anthropic.content}")

    print("Setup complete!")


if __name__ == "__main__":
    main()
