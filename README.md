# RAG Chatbot with LangChain, OLlama and Llama3

This project demonstrates how to use these technologies together to create a chatbot that can answer questions about a webpage.

## Pre-requisites

- Python 3.11 or higher
- OLlama server running

## Setup

1. Create a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:
   ```bash
   python3 main.py
   ```

## Usage

Send a POST request to the `/chat` endpoint with a JSON payload containing the query.

Example:

```json
{
  "query": "Where is the function to calculate the costs of the orders?"
}
```
