#!/usr/bin/env python3
import os
import re
from pathlib import Path
from langchain_core.documents import Document

VAULT_DIR = "./vault"


def get_keywords(text):
    text = text.lower()
    words = re.findall(r"\b[a-z]{3,}\b", text)
    return set(words)


def load_and_index():
    docs = []
    keywords_index = {}

    for md_file in Path(VAULT_DIR).rglob("*.md"):
        try:
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()

            if not content.strip():
                continue

            doc = Document(
                page_content=content,
                metadata={"source": str(md_file), "title": md_file.stem},
            )
            docs.append(doc)

            keywords = get_keywords(content)
            for kw in keywords:
                if kw not in keywords_index:
                    keywords_index[kw] = []
                keywords_index[kw].append(len(docs) - 1)

        except Exception as e:
            print(f"Error: {e}")

    return docs, keywords_index


class KeywordRAG:
    def __init__(self):
        print("Loading vault...")
        self.docs, self.keywords_index = load_and_index()
        print(f"Indexed {len(self.docs)} documents")

    def query(self, question, top_k=3):
        q_keywords = get_keywords(question)

        scores = {}
        for kw in q_keywords:
            if kw in self.keywords_index:
                for idx in self.keywords_index[kw]:
                    if idx not in scores:
                        scores[idx] = 0
                    scores[idx] += 1

        sorted_idxs = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        top_idxs = [idx for idx, s in sorted_idxs[:top_k]]

        if not top_idxs:
            return "No relevant notes found.", []

        result = "I found these relevant notes in your vault:\n\n"
        for i, idx in enumerate(top_idxs, 1):
            d = self.docs[idx]
            result += f"📄 Note {i} ({d.metadata.get('title', 'Unknown')}):\n"
            result += d.page_content[:500] + "\n\n"

        result += "\nThese notes should contain information related to your question."

        return result, [self.docs[idx] for idx in top_idxs]

    def query_with_sources(self, question):
        answer, sources = self.query(question)
        return {"answer": answer, "sources": sources}


_rag_instance = None


def build_chain():
    global _rag_instance
    if _rag_instance is None:
        _rag_instance = KeywordRAG()
    return _rag_instance


if __name__ == "__main__":
    r = build_chain()
    print("\nTesting...")
    result = r.query_with_sources("Buddha")
    print(result["answer"][:500])
