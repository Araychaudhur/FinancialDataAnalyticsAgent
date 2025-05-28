# Financial Data Analytics Agent 📊

An interactive data analysis and visualization tool that allows users to upload CSV data, chat with an AI assistant to perform analyses, and generate insights using Python, Streamlit, Langchain (LangGraph), and Plotly.

## Overview

The Financial Data Analytics Agent empowers users, especially those with limited programming experience, to explore and understand their financial datasets. Users can upload their data, define metadata, and then use a conversational interface to ask questions, request analyses, and generate visualizations. The backend leverages a Large Language Model (GPT-4o) orchestrated by LangGraph to interpret user requests and execute Python code for analysis and plotting.

## Features ✨

* **CSV Data Upload & Management:** Users can upload multiple CSV files for analysis.
* **Interactive Data Dictionary:**
    * View and edit descriptions for uploaded datasets, stored in `data_dictionary.json`.
    * View metadata such as features, coverage, and usage notes.
* **Conversational AI for Data Analysis:**
    * Chat with an AI agent (powered by GPT-4o via Langchain) to ask questions about the data.
    * The AI can perform data manipulation, statistical analysis, and generate insights using Python (Pandas, Scikit-learn).
* **Interactive Plotly Visualizations:**
    * The AI agent generates interactive charts using Plotly based on user requests.
    * Visualizations are displayed directly in the chat interface.
* **Code Execution & Debugging:**
    * The AI uses a `complete_python_task` tool to execute generated Python code in a REPL environment.
    * A debug tab shows intermediate outputs, including the AI's thought process, the Python code executed, and its output.
* **Stateful Conversations:** LangGraph manages the agent's state, allowing for follow-up questions and iterative analysis.

## Tech Stack 🛠️

* **Backend:** Python
* **AI/ML Frameworks:**
    * Langchain & LangGraph
    * Langchain-OpenAI (for GPT-4o)
* **Data Handling & Analysis:**
    * Pandas
    * Scikit-learn (available for use by the agent)
* **Visualization:** Plotly
* **Frontend:** Streamlit
* **Utilities:** python-dotenv

## How It Works 🧠

1.  **Frontend (Streamlit):**
    * The user interacts with the application through a Streamlit interface (`visualization_agent.py`).
    * They upload CSV files and can update their descriptions in the `data_dictionary.json`.
    * User queries from the chat input are sent to the `PythonChatBot`.
2.  **Backend (PythonChatBot & LangGraph):**
    * The `PythonChatBot` (`Pages/backend.py`) initializes and runs a LangGraph state machine.
    * The `AgentState` (`Pages/graph/state.py`) holds the conversation messages, input data details, intermediate outputs, and paths to generated images.
3.  **LLM Interaction (LangGraph Nodes):**
    * The `call_model` node (`Pages/graph/nodes.py`) formats the input (including data summaries and chat history) and invokes the OpenAI GPT-4o model with a system prompt (`Pages/prompts/prompt.md`).
    * The LLM decides if it needs to execute Python code using the `complete_python_task` tool.
4.  **Tool Execution:**
    * If the model decides to use the tool, the `route_to_tools` node directs the flow to the `call_tools` node.
    * The `call_tools` node invokes `complete_python_task` (`Pages/graph/tools.py`) with the LLM-generated Python code.
    * The `complete_python_task` tool executes the code, captures output (including Plotly figures which are pickled), and returns results. Variables and Plotly figures can persist across tool calls within the session.
5.  **Response to User:**
    * The tool's output is returned to the LLM, which then generates a natural language response for the user.
    * Generated Plotly figures are displayed in the Streamlit chat interface.

## Setup and Installation ⚙️

1.  **Clone the repository:**
    ```bash
    git clone [Your GitHub Repository Link Here]
    cd FinancialDataAnalyticsAgent
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *This installs pandas, streamlit, langchain-core, scikit-learn, plotly, langchain, langgraph, langchain-openai, python-dotenv, and langchain_experimental.*

4.  **Set up your OpenAI API Key:**
    * Create a `.env` file in the `FinancialDataAnalyticsAgent` directory.
    * Add your OpenAI API key to the `.env` file:
        ```env
        OPENAI_API_KEY="your_openai_api_key_here"
        ```
        The application loads this using `python-dotenv`.

## Usage ▶️

1.  Navigate to the `FinancialDataAnalyticsAgent` directory.
2.  Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```
    The application will open in your web browser, typically at `http://localhost:8501`.

    * **Data Management Tab:** Upload your CSV files. Selected files can be analyzed in the Chat Interface. You can also provide or update descriptions for your datasets here.
    * **Chat Interface Tab:** Once files are selected, ask the AI questions about your data or request analyses and visualizations.
    * **Debug Tab:** View the thought process, executed code, and outputs from the AI agent for troubleshooting or understanding its actions.

## Future Enhancements (Ideas) 💡
* More advanced data preprocessing options directly in the UI.
* User authentication and persistent storage of analysis sessions.
* Ability to save and export generated code notebooks.
* Enhanced error handling and feedback for user queries.