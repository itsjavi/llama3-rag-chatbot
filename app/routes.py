from flask import request, jsonify
from app import app
from app.retrieval import retrieve_code_snippets
from app.generation import generate_response

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    query = data.get('query')
    retrieved_code = retrieve_code_snippets(query)
    context = " ".join(retrieved_code)
    response = generate_response(query, context)
    return jsonify({'response': response})
