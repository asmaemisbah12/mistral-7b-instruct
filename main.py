from fastapi import FastAPI
from pydantic import BaseModel
from llama_cpp import Llama

app = FastAPI()

llm = Llama(
    model_path="models/mistral-7b-instruct-v0.2.Q5_K_M.gguf",
    n_threads=8,
)


class Prompt(BaseModel):
    prompt: str


@app.post("/generate")
def generate(data: Prompt):
    output = llm(data.prompt, max_tokens=200)
    return {"response": output["choices"][0]["text"]}
