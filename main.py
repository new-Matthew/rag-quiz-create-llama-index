from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core import Settings
from fastapi import FastAPI
from controller import generate_quiz


app = FastAPI()

app.include_router(generate_quiz.router)

Settings.llm = Ollama(model="llama3.1:8b-instruct-q2_K", temperature=0.1, request_timeout=60*60, json_mode=True)
Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")