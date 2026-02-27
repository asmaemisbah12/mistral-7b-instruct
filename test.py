from llama_cpp import Llama

llm = Llama(
    model_path="models/mistral-7b-instruct-v0.2.Q5_K_M.gguf",
    n_threads=8,  # adjust to your CPU cores
)

output = llm(
    "Explain artificial intelligence in one short sentence.",
    max_tokens=100,
)

print(output["choices"][0]["text"])
