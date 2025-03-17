---
title: "Recurent Neural Network"
collection: teaching
type: "M.Sc course"
permalink: /materials/NLP-A/labor/recurent-neural-network
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2025-03-17
location: "Debrecen, Hungary"
---

## [Colab](https://colab.research.google.com/drive/1aMlFLC8rAZm68qincUte6fNQvawUBTY4)

## What is an RNN, specifically an LSTM?

- RNNs are a type of neural network designed to handle sequential data, like text or time series. They have a "memory" that allows them to retain information from previous steps in the sequence, which is crucial for understanding context.
- LSTMs (Long Short-Term Memory) are a special kind of RNN that address the "vanishing gradient" problem, which hindered the ability of traditional RNNs to learn long-range dependencies in sequences. LSTMs have a more complex internal structure with "gates" that control the flow of information, allowing them to better capture and retain important information over longer sequences.

## Why are LSTMs important in NLP?

- ** Contextual Understanding:**  LSTMs excel at capturing the relationships between words in a sentence or document, enabling them to understand the context of words and phrases. This is essential for tasks like sentiment analysis, machine translation, and text generation.
- ** Handling Long Sequences:**  Their ability to learn long-range dependencies makes them well-suited for processing lengthy text documents, where the meaning of a word might depend on information presented much earlier in the text.
- ** Sequence-to-Sequence Tasks:**  LSTMs can be used to map one sequence to another, which is fundamental for tasks like machine translation (translating a sentence from one language to another) or text summarization (condensing a longer text into a shorter summary).

**In simpler terms:** Think of an LSTM as a powerful reader that can remember the important parts of a story as it reads, allowing it to understand the overall plot and meaning better than a simple reader who only focuses on the current sentence. This "memory" and contextual understanding make LSTMs a valuable tool for NLP tasks where grasping the meaning of text is crucial.

## In the notebook:

### 1. Load Data
- Imports the pandas library for data manipulation.
- Defines a dictionary splits to hold the paths to the training, testing, and unsupervised data files in Parquet format.
- Loads the IMDB movie review dataset using pd.read_parquet from Hugging Face Datasets. It loads the training and testing data into separate Pandas DataFrames (df_imdb_train, df_imdb_test).
- Prints information about the training and testing DataFrames using df.info().
- Splits the testing data into validation and testing sets using train_test_split from sklearn.model_selection with a 20% test size and a random state of 42 for reproducibility.
- Prints the sizes of the validation and testing sets.

### 2. Tokenization (Create Dictionary)

- Imports necessary libraries from tokenizers for tokenization: Tokenizer, WordPiece, WordPieceTrainer, and Whitespace.
- Creates a Tokenizer object using the WordPiece model and sets the unknown token to [UNK].
- Initializes a WordPieceTrainer to train the tokenizer with a vocabulary size of 5000, a minimum frequency of 2, and special tokens.
- Defines a data_generator function to iterate over the text data for training the tokenizer.
- Trains the tokenizer using the training data (df_imdb_train['text']) and the trainer.
- Saves the trained tokenizer to a file named "tokenizer-wp-imdb.json".
- Encodes a sample text using the tokenizer and prints the resulting tokens and their IDs.
- Calculates the number of tokens for each text in the training, testing, and validation sets using the tokenizer and stores it in a new column named "count_of_tokens".
- Displays descriptive statistics of the training DataFrame using df.describe().
- Creates a histogram of the "count_of_tokens" column in the training DataFrame.
- Filters the training, testing, and validation DataFrames to keep only texts with 512 tokens or fewer.
- Prints the lengths of the filtered DataFrames.

### 3. Prepare to Train

- Enables padding and truncation for the tokenizer, ensuring all sequences have a length of 512.
- Defines a function encode_text to encode a batch of texts using the tokenizer.
- Creates a custom TextDataset class to handle the text data and labels.
- Creates DataLoader instances for the training, validation, and testing sets to handle batching and shuffling of data.

### 4. Define and Train Model

- Defines a TextClassifier model using PyTorch, consisting of an embedding layer, an LSTM layer, a fully connected layer, and dropout for regularization.
- Initializes the model, loss function (CrossEntropyLoss), and optimizer (Adam).
- Moves the model to the appropriate device (CUDA if available, otherwise CPU).
- Defines a function calculate_accuracy to evaluate the model's accuracy on a given dataset.
- Trains the model for 5 epochs, iterating over the training data in batches and updating the model's parameters using the optimizer.
- Calculates and prints the training loss and validation accuracy after each epoch.

### 5. Evaluate Model

- Selects 10 random samples from the test set for evaluation.
- Performs inference on the selected samples using the trained model and stores the predicted labels.
- Prints the tokens, true labels, and predicted labels for each sample.
- Calculates and prints the test accuracy of the model on the entire test set.


