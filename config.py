import os

class Config:
    MODEL_ID='huggingface/llama3'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = True

config = Config()
