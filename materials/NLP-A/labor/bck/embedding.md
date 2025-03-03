---
title: "Embedding"
collection: teaching
type: "M.Sc course"
permalink: /materials/NLP-A/labor/embedding
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2024-02-27
location: "Debrecen, Hungary"
---

```python
!pip install datasets
!pip install transformers
```

## Transformer architektúra

<img src="https://www.tensorflow.org/images/tutorials/transformer/transformer.png" alt="Transformer">

Ábra 1: Transformer architektúra. Forrás: [www.tensorflow.org](https://www.tensorflow.org/text/tutorials/transformer).

## Beágyazó és pozíciókódoló rétegek

<img src="https://www.tensorflow.org/images/tutorials/transformer/PositionalEmbedding.png" alt="Transformer">

Ábra 2: Beágyazó és pozíciókódoló rétegek. Forrás: [www.tensorflow.org](https://www.tensorflow.org/text/tutorials/transformer).

## Beágyazás

### CBOW, Skip-gramm

<img src="https://wiki.pathmind.com/images/wiki/word2vec_diagrams.png">

Ábra 3: CBOW, Skip-gramm. Forrás: [wiki.pathmind.com](https://wiki.pathmind.com/images/wiki/word2vec_diagrams.png).

### Word2Vec CBOW

<img src="https://miro.medium.com/v2/resize:fit:1400/0*3DFDpaXoglalyB4c.png">

Ábra 4: Word2Vec CBOW. Forrás: [medium](https://miro.medium.com/v2/resize:fit:1400/0*3DFDpaXoglalyB4c.png).

### Miért használjuk a beágyazást?

<img src="https://miro.medium.com/v2/resize:fit:2000/1*SYiW1MUZul1NvL1kc1RxwQ.png">

Ábra 5: Miért használjuk a beágyazást? Forrás: [medium](https://miro.medium.com/v2/resize:fit:2000/1*SYiW1MUZul1NvL1kc1RxwQ.png).

```python
from datasets import load_dataset

dataset = load_dataset("imdb")
dataset
```

```python
corpus = [text for text in dataset["train"]["text"]][:5000]
len(corpus)
```

```python
corpus[0]
```

### Lemmatizáció

```python
import nltk

nltk.download('wordnet')
nltk.download('stopwords')
```

```python
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

stop_words = set(stopwords.words('english'))
w_n_lemmatizer = WordNetLemmatizer()

words = ['kites', 'babies', 'dogs', 'flying', 'smiling',
         'driving', 'died', 'tried', 'feet']

for word in words:
    print(word + "\t" + w_n_lemmatizer.lemmatize(word))
```

```python
from tqdm import tqdm
from nltk.tokenize import word_tokenize

nltk.download('punkt')

corpus_cleaned = []

for document in tqdm(corpus):
  tmp = []
  for word in word_tokenize(document.lower()):
    if not word in stop_words and word.isalnum():
      tmp.append(w_n_lemmatizer.lemmatize(word))

  corpus_cleaned.append(tmp)
```

```python
len(corpus_cleaned), corpus_cleaned[0]
```

```python
from gensim.models import Word2Vec

w2v_model = Word2Vec(vector_size=10,
                     window=5,
                     min_count=1)
```

```python
w2v_model.build_vocab(corpus_cleaned)
w2v_model.corpus_count
```

```python
w2v_model.train(corpus_cleaned,
                total_examples=w2v_model.corpus_count,
                epochs=30)
```

```python
w2v_model.wv.save_word2vec_format("word2vec.vec")
```

```python
w2v_model.wv.most_similar(positive=["film"])
```

```python
w2v_model.wv.most_similar(negative=["good"])
```

### [projector.tensorflow.org](https://projector.tensorflow.org/)

```python
with open("word2vec.vec", "r") as f:
    tmp = f.read().split("\n")

with open("word2vec.tsv", "w") as t:
    for i in range(1,len(tmp)):
        splited = tmp[i].split(" ")
        t.write("\t".join(splited[1:]) + "\n")

with open("meta.tsv", "w") as m:
    for i in range(1,len(tmp)):
        splited = tmp[i].split(" ")
        m.write(splited[0] + "\n")
```