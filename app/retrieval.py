import os
import faiss
import numpy as np
from app.embeddings import embed_text

repo_dir = 'data/repository'
code_exts = [".md", ".mdx", ".ts", ".tsx", ".js", ".jsx", ".cjs", ".mjs", ".mts", ".css", ".scss"]
excluded_dirs = ["node_modules", "dist", "build", "target", ".git"]

def load_code_files(folder_path):
    code_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if any(excluded_dir in root for excluded_dir in excluded_dirs):
                continue
            if file.endswith(tuple(code_exts)):
                with open(os.path.join(root, file), 'r') as f:
                    code_files.append(tuple([file, f.read()]))
                    # code_files.append(tuple([os.path.join(root, file), f.read()]))
    return code_files

def create_faiss_index(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index

def embed_code_files(code_files):
    # embeddings = [embed_text(code) for code in code_files] # This is the original line
    # embed the code with the file name:
    embeddings = [embed_text(f"///file: {code[0]}\n\n{code[1]}") for code in code_files]
    return np.vstack(embeddings)

code_files = load_code_files(repo_dir)
code_file_embeddings = embed_code_files(code_files)
faiss_index = create_faiss_index(code_file_embeddings)

def retrieve_code_snippets(query, k=5):
    query_embedding = embed_text(query)
    distances, indices = faiss_index.search(query_embedding, k)
    return [code_files[i] for i in indices[0]]
