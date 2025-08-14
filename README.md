# Financial Data Analytics Agent 📊

An AI-powered, multi-modal agent I developed from concept to completion to democratize financial analysis. This tool allows users to ask complex questions in natural language and receive synthesized insights from both structured data (CSVs) and unstructured data (images of financial charts).

## Overview

The Financial Data Analytics Agent is a proof-of-concept for an advanced analytical tool that empowers users to conduct sophisticated financial analysis with ease. The agent is designed to solve the problem of fragmented data analysis, where insights are hidden across different data formats. By ingesting both CSV files and images of financial charts, it removes the need for manual, time-intensive analysis by a skilled professional.

Users can upload their data, and through a conversational interface, ask complex questions to generate insights, perform statistical analysis, and create visualizations. My role was as the sole developer, owning the project end-to-end. This involved architecting the multi-modal RAG system, building the agentic workflow, and developing the full user-facing evaluation front-end.

## Features ✨

  * **Multi-Modal Analysis:** Ingests and analyzes both structured (CSV) and unstructured (images of charts) data.
  * **CSV Data Upload & Management:** Users can upload multiple CSV files for analysis.
  * **Interactive Data Dictionary:**
      * View and edit descriptions for uploaded datasets.
      * View metadata such as features, coverage, and usage notes.
  * **Conversational AI for Data Analysis:**
      * Chat with an AI agent (powered by GPT-4o) to ask questions about the data.
      * The AI can perform data manipulation, statistical analysis, and generate insights using Python.
  * **Interactive Plotly Visualizations:**
      * The AI agent generates interactive charts using Plotly based on user requests.
  * **Code Execution & Debugging:**
      * A debug tab shows the AI's thought process, the Python code executed, and its output.
  * **Stateful Conversations:** LangGraph manages the agent's state, allowing for follow-up questions and iterative analysis.

## Tech Stack 🛠️

  * **Backend:** Python
  * **AI/ML Frameworks & Architecture:**
      * LangGraph for the core agentic workflow and intelligent query routing.
      * Langchain-OpenAI (for GPT-4o).
      * Multi-Modal RAG System combining a **BLIP-2** vision model with a **Fusion-in-Decoder (FiD)** architecture.
  * **Data Handling & Analysis:**
      * Pandas
      * Scikit-learn
  * **Visualization:** Plotly
  * **Frontend:** Streamlit
  * **Utilities:** python-dotenv

## How It Works 🧠

The application is architected as a multi-modal agent capable of reasoning over different data types.

1.  **Frontend (Streamlit):**
      * The user interacts with the application through a Streamlit dashboard.
      * They upload CSV files and images, and can update data descriptions in the `data_dictionary.json`.
      * User queries from the chat input are sent to the backend.
2.  **Backend (LangGraph Agent):**
      * A LangGraph state machine intelligently routes user queries. Based on the query and data, it decides whether to analyze structured data, unstructured data, or both.
3.  **Multi-Modal RAG System:**
      * For questions involving images, a **BLIP-2 vision model** processes the visual data to extract relevant information.
      * This visual information is combined with text-based data from CSVs and the user's query within a **Fusion-in-Decoder (FiD) architecture**, allowing the LLM to synthesize insights from both sources.
4.  **Tool Execution:**
      * The agent uses a `complete_python_task` tool to execute LLM-generated Python code for data analysis (Pandas) and plotting (Plotly).
      * The tool executes the code, captures outputs, and persists variables and figures across turns in the conversation.
5.  **Response to User:**
      * The tool's output is returned to the LLM, which generates a natural language response.
      * Generated Plotly figures are displayed directly in the Streamlit chat interface.

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

4.  **Set up your OpenAI API Key:**

      * Create a `.env` file in the project's root directory.
      * Add your OpenAI API key to the `.env` file:
        ```env
        OPENAI_API_KEY="your_openai_api_key_here"
        ```

## Usage ▶️

1.  Navigate to the `FinancialDataAnalyticsAgent` directory.

2.  Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

    The application will open in your web browser, typically at `http://localhost:8501`.

      * **Data Management Tab:** Upload your CSV files and images.
      * **Chat Interface Tab:** Select the files you want to analyze and ask the AI questions.
      * **Debug Tab:** View the thought process, executed code, and outputs from the AI agent.

## Future Enhancements (Ideas) 💡

  * More advanced data preprocessing options directly in the UI.
  * User authentication and persistent storage of analysis sessions.
  * Ability to save and export generated code notebooks.
  * Enhanced error handling and feedback for user queries.
