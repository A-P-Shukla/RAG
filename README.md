# RAG: Advanced Retrieval-Augmented Generation with LangGraph

This repository serves as a comprehensive collection of examples and implementations demonstrating advanced techniques in Retrieval-Augmented Generation (RAG), primarily leveraging the [LangGraph](https://langchain-ai.github.io/langgraph/) framework. It explores various facets of building intelligent, stateful, and agentic LLM applications, moving beyond traditional RAG approaches.

## Key Features and Concepts Explored

This project delves into several critical areas of modern RAG and LLM application development:

-   **Agentic RAG**: Implementations showcasing how to build RAG systems that can evaluate retrieved documents, reformulate queries, and self-correct, enabling more robust and intelligent information retrieval.
-   **LangGraph Workflows**: Extensive examples of using LangGraph to construct cyclic graphs for complex agent behaviors, including conditional edges, state management, and human-in-the-loop processes.
-   **Contextual Retrieval**: Demonstrations of different retrieval strategies, including basic vector store lookups, late chunking, and optimizing for long context windows.
-   **Multi-Agent Systems**: Advanced patterns for orchestrating multiple AI agents to collaborate on tasks such as research, analysis, and report generation.
-   **Output Parsing and Monitoring**: Techniques for structured output from LLMs and integrating monitoring tools like LangSmith for observability.
-   **Error Handling and Cost Optimization**: Strategies for building resilient LLM applications and managing token usage efficiently.
-   **Multimodal RAG**: Introduction to RAG systems that can process and retrieve information from various data types beyond just text.

## Installation

To set up the project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/A-P-Shukla/RAG.git
    cd RAG
    ```

2.  **Install dependencies:**
    This project uses `uv` for dependency management. If you don't have `uv` installed, you can install it via `pip`:
    ```bash
    pip install uv
    ```
    Then, install the project dependencies:
    ```bash
    uv pip install -e .
    ```
    Alternatively, you can use `pip` directly:
    ```bash
    pip install -r requirements.txt # (if requirements.txt exists, otherwise install from pyproject.toml)
    ```
    Based on `pyproject.toml`, the key dependencies include:
    -   `langchain`
    -   `langchain-community`
    -   `langchain-anthropic`
    -   `langchain-openai`
    -   `langgraph`
    -   `python-dotenv`
    -   `bs4`
    -   `pypdf`
    -   `langchain-ollama`
    -   `langchain-chroma`
    -   `rank-bm25`
    -   `langgraph-checkpoint-sqlite`
    -   `pytest`
    -   `fastapi`
    -   `uvicorn`

3.  **Environment Variables:**
    Create a `.env` file in the root directory and add your API keys for OpenAI, Anthropic, or any other services used in the examples. For instance:
    ```
    OPENAI_API_KEY="your_openai_api_key"
    ANTHROPIC_API_KEY="your_anthropic_api_key"
    # Add other keys as needed
    ```

## Usage

Each Python file in the root directory typically represents a self-contained example or lesson. To run an example, navigate to the project root and execute the desired script:

```bash
python 04_agentic_rag.py
```

Some notable examples include:

-   `main.py`: A basic setup test for OpenAI and Anthropic LLMs.
-   `04_agentic_rag.py`: Demonstrates an agentic RAG workflow with query rewriting and document grading.
-   `langgraph_core.py`: Introduces fundamental LangGraph concepts through various examples.
-   `rag_pipeline.py`: Showcases different RAG pipeline variations, including basic, cited, and structured output RAG.
-   `multi_agent_research_system.py`: A comprehensive example of a multi-agent research system using LangGraph.

## Project Structure

The repository is organized with individual Python files, each focusing on a specific RAG or LangGraph concept. Image files (`.png`) are included to visualize graph structures where applicable.

```
RAG/
├── 01_long_context_vs_rag.py
├── 02_contextual_retrieval.py
├── 03_late_chunking.py
├── 04_agentic_rag.py
├── 05_graphrag_intro.py
├── 06_multimodal_rag.py
├── README.md
├── advanced_rag.py
├── agent_communication.py
├── ... (other Python files for various examples)
├── graph.png
├── graph_2.png
├── graph_3.png
├── graph_code.png
├── graph_complex.png
├── graph_new.png
├── graph_newest.png
├── research_graph.png
├── pyproject.toml
├── uv.lock
└── main.py
```

## Contributing

Contributions are welcome! If you have an example of an advanced RAG technique or a LangGraph pattern that fits the scope of this repository, feel free to open a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE). (Note: A `LICENSE` file is not explicitly present in the repository, but this is a common default for open-source projects. If a specific license is intended, please add a `LICENSE` file.)
