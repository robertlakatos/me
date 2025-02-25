---
title: "Vectore Store"
collection: teaching
type: "M.Sc course"
permalink: /materials/NLP-A/labor/vector-store
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2025-02-25
location: "Debrecen, Hungary"
---

## [Colab](https://drive.google.com/file/d/1Zf2OESutr4QaZK5prOY4tF3sIDgjDVIO)

## What is Semantic Search?

Semantic search is an advanced retrieval technique that goes beyond simple keyword matching by understanding the meaning and context of queries. Unlike traditional lexical search methods, which rely on exact word matches, semantic search leverages vector representations of text, allowing it to find relevant documents even when different words or phrases are used. This is particularly useful in natural language processing (NLP) applications, such as question-answering systems, recommendation engines, and knowledge retrieval.

At its core, semantic search involves:
    - **Text Embedding:** Converting text into dense vector representations using pre-trained language models.
    - **Indexing:** Storing these vectors in a searchable structure.
    - **Querying:** Transforming user queries into vectors and retrieving the most semantically similar results using a similarity metric like cosine similarity or dot product.
    - **Post-processing & Ranking:** Refining results using additional filtering, reranking, or metadata constraints.

## Semantic Search with LlamaIndex

LlamaIndex (formerly known as GPT Index) is a powerful library designed to facilitate the integration of Large Language Models (LLMs) with structured and unstructured data sources. It provides an efficient framework for indexing, storing, and retrieving information for semantic search applications.

### Vectorization in LlamaIndex

LlamaIndex relies on embedding models to convert textual data into vector representations. It supports multiple embedding providers such as OpenAI, Hugging Face, and Cohere. The general process of vectorization in LlamaIndex includes:

1. **Data Ingestion:**
    - Raw text, PDFs, databases, or APIs are ingested into LlamaIndex.
    - The text is split into chunks (e.g., using recursive chunking or fixed-size splitting) to improve retrieval performance.
2. **Embedding Generation:**
    - Each text chunk is passed through an embedding model to generate a high-dimensional vector representation.
    - Popular models include OpenAI’s text-embedding-ada-002 or sentence transformers like all-MiniLM-L6-v2.
3. **Index Construction:**
    - The generated embeddings are stored in a vector database or in-memory index.
    - LlamaIndex supports integrations with vector databases like FAISS, ChromaDB, Pinecone, and Weaviate.

### Query Execution in LlamaIndex

When a user submits a query, LlamaIndex follows these steps:
1. **Query Vectorization:** The query text is transformed into an embedding vector using the same model that was used for indexing.
2. **Similarity Search:** The system performs a nearest-neighbor search in the vector database, retrieving the most similar document chunks.
3. **Contextual Augmentation & RAG:** 
    - Retrieved text snippets are passed to an LLM to generate responses in a Retrieval-Augmented Generation (RAG) workflow. 
    - This allows LLMs to provide more accurate and context-aware answers based on retrieved knowledge.
4. **Response Generation & Ranking:**
    - Additional ranking or reranking methods can be applied to refine search results.
    - Metadata filters and hybrid search (combining keyword and vector search) can be used for more precise retrieval.

## LlamaIndex-Specific Features for Semantic Search

LlamaIndex provides several features that enhance semantic search efficiency:

- **Multi-level Indexing:** Combines different indexing techniques (vector, keyword, and hierarchical) for improved retrieval.
- **Structured Query Engine:** Supports querying structured databases (SQL) alongside unstructured text.
- **Hybrid Search:** Combines semantic search with traditional keyword-based retrieval for better precision.
- **LLM-powered Query Expansion:** Automatically reformulates queries for improved recall.

By leveraging LlamaIndex, developers can build scalable and efficient semantic search applications that integrate seamlessly with LLMs and external data sources.

## Most important NLP and AI packages!

- [LlamaIndex](https://docs.llamaindex.ai/en/stable/)
- [Huggingface](https://huggingface.co/)

## [Colab](https://colab.research.google.com/drive/17PNZn6S4BxkTQBi81ytuFKSA193TifPy#scrollTo=t94J2jg6CsXq)