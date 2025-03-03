---
title: "Agent"
collection: teaching
type: "M.Sc course"
permalink: /materials/NLP-A/labor/agent
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2025-03-03
location: "Debrecen, Hungary"
---

## [Colab](https://colab.research.google.com/drive/1BY11_hBm4KjzFnJIu5P3NE6qFr_MlieN)

This labor demonstrates building a medical chatbot using the MedQuad dataset and the LlamaIndex library. It leverages a large language model (LLM) to understand and answer medical questions based on the information within the dataset.

## Theoretical Background:

- **MedQuad Dataset:** A medical question-answering dataset containing pairs of questions and answers related to various medical topics. It serves as the knowledge base for the chatbot.
- **LlamaIndex:** A framework designed to facilitate interactions with LLMs. It allows for indexing data, creating chatbots, and managing the context of conversations.
- **Large Language Models (LLMs):** Powerful models trained on vast amounts of text data, enabling them to understand natural language and generate human-like text. The chatbot utilizes an LLM to interpret user queries and formulate answers.
- **Vector Databases:** These databases store data as vectors, enabling efficient similarity search. LlamaIndex uses vector databases to index the MedQuad dataset for quick retrieval of relevant information.

## Notebook Workflow:

- **Installation and Imports:** Installs the necessary libraries (llama-index, llama-index-embeddings-huggingface, etc.) and imports required modules for data manipulation, embedding generation, and interaction with LLMs.
- **Data Loading:** Loads the MedQuad dataset from Hugging Face Datasets using Pandas.
- **Vector Database Creation:** Creates a vector database using LlamaIndex to store and index the MedQuad data. This allows for efficient retrieval of relevant information when answering user queries.
- **Chatbot Initialization:** Initializes a chatbot engine that uses the specified LLM and the created vector database. It also sets the system prompt to guide the chatbot's behavior and personality.
- **Chatbot Interaction:** Enters a loop that continuously prompts the user for questions and provides answers using the chatbot engine. The responses are streamed to provide a more interactive experience.
- **History Reset:** Clears the chat history after the interaction.

## Key Concepts:

- **Embedding Generation:** Converts text data into numerical vectors to represent their meaning and semantic relationships.
- **Similarity Search:** Retrieves information from the vector database that is semantically similar to the user's query.
- **Context Management:** Maintains the context of the conversation, allowing the chatbot to understand and respond to follow-up questions.


