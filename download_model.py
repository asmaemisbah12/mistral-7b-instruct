"""
Download Mistral 7B Instruct v0.2 Q5_K_M GGUF to models/
"""
from pathlib import Path

from huggingface_hub import hf_hub_download

REPO_ID = "TheBloke/Mistral-7B-Instruct-v0.2-GGUF"
FILENAME = "mistral-7b-instruct-v0.2.Q5_K_M.gguf"
LOCAL_DIR = Path(__file__).parent / "models"

def main():
    LOCAL_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Downloading {FILENAME} from {REPO_ID}...")
    path = hf_hub_download(
        repo_id=REPO_ID,
        filename=FILENAME,
        local_dir=str(LOCAL_DIR),
        local_dir_use_symlinks=False,
    )
    print(f"Downloaded to: {path}")


if __name__ == "__main__":
    main()
