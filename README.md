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
