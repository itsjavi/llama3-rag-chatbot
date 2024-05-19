from transformers import pipeline
from config import config

generation_pipeline = pipeline("text-generation", model=config.MODEL_ID)

def generate_response(query, context):
    input_text = f"Context: {context}\n\nQuestion: {query}\nAnswer:"
    response = generation_pipeline(input_text, max_length=200, num_return_sequences=1)
    return response[0]['generated_text']
