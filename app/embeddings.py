from transformers import AutoTokenizer, AutoModel
import torch
from config import config

tokenizer = AutoTokenizer.from_pretrained(config.MODEL_ID)
model = AutoModel.from_pretrained(config.MODEL_ID)

def embed_text(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).cpu().numpy()
