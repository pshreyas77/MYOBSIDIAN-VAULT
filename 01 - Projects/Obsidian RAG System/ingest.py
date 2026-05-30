#!/usr/bin/env python3
import os
import hashlib
import numpy as np
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings


class SimpleHashEmbeddings(Embeddings):
    def __init__(self, dim: int = 384):
        self.dim = dim

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return [self.embed_query(t) for t in texts]

    def embed_query(self, text: str) -> list[float]:
        hash_obj = hashlib.sha256(text.encode())
        hash_bytes = hash_obj.digest()
        np.random.seed(int.from_bytes(hash_bytes[:4], "big"))
        vec = np.random.randn(self.dim)
        vec = vec / np.linalg.norm(vec)
        return vec.tolist()


EMBEDDINGS = SimpleHashEmbeddings(dim=384)

VAULT_DIR = "./vault"
CHROMA_DB_DIR = "./chroma_db"
CHUNK_SIZE = 512
CHUNK_OVERLAP = 64


def load_markdown_files(vault_dir: str) -> list:
    documents = []
    md_files = list(Path(vault_dir).rglob("*.md"))
    print(f"Found {len(md_files)} markdown files")

    for md_file in md_files:
        try:
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()
            if content.strip():
                doc = Document(
                    page_content=content,
                    metadata={"source": str(md_file), "title": md_file.stem},
                )
                documents.append(doc)
        except Exception as e:
            print(f"Error loading {md_file}: {e}")

    return documents


def index_vault() -> int:
    print(f"Starting indexing of vault at: {VAULT_DIR}")

    os.makedirs(VAULT_DIR, exist_ok=True)
    os.makedirs(CHROMA_DB_DIR, exist_ok=True)

    if not os.path.exists(VAULT_DIR):
        print(f"Error: Vault directory not found at {VAULT_DIR}")
        return 0

    documents = load_markdown_files(VAULT_DIR)

    if not documents:
        print("No documents loaded - check vault directory")
        return 0

    print(f"Loaded {len(documents)} documents")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
        is_separator_regex=False,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Created {len(chunks)} chunks")

    print("Creating vector store...")
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=EMBEDDINGS,
        persist_directory=CHROMA_DB_DIR,
    )

    count = vectorstore._collection.count()
    print(f"Successfully indexed {count} chunks to ChromaDB")
    return count


if __name__ == "__main__":
    index_vault()
