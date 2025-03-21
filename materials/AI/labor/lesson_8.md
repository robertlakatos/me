---
title: "Gyakorlat 8."
collection: teaching
type: "B.Sc course"
permalink: /materials/AI/labor/lesson_8
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2024-04-02
location: "Debrecen, Hungary"
---

## Adatok letöltése

```python
import pandas as pd
import tensorflow_datasets as tfds
from tqdm import tqdm

# Adathalmaz letöltése
dataset_train = tfds.load('imdb_reviews', split='train', shuffle_files=True)
dataset_test = tfds.load('imdb_reviews', split='test', shuffle_files=True)
```

```python
def convert_to_df(dataset):
    data = [{ 'text': item['text'].numpy().decode('utf-8'), 'label': item['label'].numpy() } for item in tqdm(dataset)]
    return pd.DataFrame(data)

df_train = convert_to_df(dataset_train)
df_test = convert_to_df(dataset_test)
```

```python
df_train.hist()
```

```python
df_test.hist()
```

```python
def sentiment(value):
    if(value == 1):
        return "positive"
    else:
        return "negative"

df_train["sentiment"] = [None] * len(df_train)
df_train["sentiment"] = df_train["label"].apply(sentiment)
df_test["sentiment"] = [None] * len(df_test)
df_test["sentiment"] = df_test["label"].apply(sentiment)

df_train.head()
```

## Adattiszítás

```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')

STOPWORDS = stopwords.words("english")

STOPWORDS[:10]
```

```python
from bs4 import BeautifulSoup

def remove_html_tags(text):
    soup = BeautifulSoup(text, 'html.parser')
    text = soup.get_text()
    
    return text
```

```python
df_train["text"] = df_train["text"].apply(remove_html_tags)
```

```python
nltk.download('punkt')

tokenized_reviews = df_train["text"].apply(lambda review_text: word_tokenize(review_text.replace("\n","").lower()))

tokenized_reviews.head()
```

```python
d = dict()

for review in tqdm(tokenized_reviews):
    for word in review:
        if word not in STOPWORDS and word.isalpha():
            d[word] = d.get(word, 0) + 1
```

```python
d = sorted(d.items(), key=lambda item: item[1], reverse=True)
d[:10]
```

```python
DESIRED_VOCAB_SIZE = 4000

VOCAB = [k for k,v in d[:DESIRED_VOCAB_SIZE]]
word_table = pd.DataFrame({"word": VOCAB})
word_table.head(10)
```

## Naive Bayes

### Bayes tétel

<img src="https://robertlakatos.github.io/me/materials/AI/images/bayes.png" alt="bayes">

### Teljes eseményrendszer

Az eseménytér felbontása olyan diszjunkt részhalmazokra, melyek együttesen lefedik a teljes eseményteret. 

<img src="https://robertlakatos.github.io/me/materials/AI/images/bayes_telj.png" alt="bayes">

### Kódoljuk le

```python
dict_freqs = {"positive": {}, "negative": {}}
```

```python
VOCAB_IDX = {}
for i in range(0, len(word_table["word"].values)):
    VOCAB_IDX[word_table["word"].values[i]] = i

for idx in range(df_train.shape[0]):
    review = df_train.iloc[idx]["text"]
    sentiment = df_train.iloc[idx]["sentiment"]
    
    for word in review.split(" "):
        if word in VOCAB_IDX:
            dict_freqs[sentiment][word] = dict_freqs[sentiment].get(word, 0) + 1
```

```python
print("story idx:", VOCAB_IDX["story"])
```

```python
print("positive good", dict_freqs["positive"]["good"])
print("negative good", dict_freqs["negative"]["good"])
print("negative bad", dict_freqs["negative"]["bad"])
print("positive bad", dict_freqs["positive"]["bad"])
```

```python
total_positive = sum(dict_freqs["positive"].values())

word_table["positive"] = [(dict_freqs["positive"].get(w, 0) + 1) / (total_positive + len(VOCAB))  for w in word_table["word"]]
```

```python
total_negative = sum(dict_freqs["negative"].values())

word_table["negative"] = [(dict_freqs["negative"].get(w, 0) + 1) / (total_negative + len(VOCAB))  for w in word_table["word"]]
```

```python
word_table.head()
```

```python
import numpy as np

word_table["ratio"] = np.log(word_table["positive"] / word_table["negative"])
word_table = word_table.set_index("word")

word_table
```

```python
word_table["ratio"].describe()
```

## Előrejelzés

```python
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

STOPWORDS = stopwords.words("english")

def predict_for_review_raw(review):
    _input = remove_html_tags(review)
    _input = word_tokenize(_input.lower())

    word_table_words = word_table.index

    return sum([word_table["ratio"].loc[token] for token in _input if token in word_table_words])
```

```python
predict_for_review_raw("This movie sucks.")
```

```python
predict_for_review_raw("This movie was fantastic!")
```

```python
def predict_for_review(review):
    return int(predict_for_review_raw(review) > 0)

```

```python
preds = df_train["text"].apply(predict_for_review)
```

```python
def get_accuracy(preds, real):
    return sum(preds == real) / len(real)
```

```python
real = (df_train["sentiment"] == "positive").astype(int)
print(f"Training set accuracy: {get_accuracy(preds, real)}")
```

```python
preds_test = df_test["text"].apply(predict_for_review)
real_test = (df_test["sentiment"] == "positive").astype(int)
print(f"Test set accuracy: {get_accuracy(preds_test, real_test)}")
```

### Determinizmus vagy véletlen?

#### József Attila: Eszmélet

"Akár egy halom hasított fa,<br>
hever egymáson a világ,<br>
szorítja, nyomja, összefogja<br>
egyik dolog a másikát<br>
s így mindenik determinált.<br>
Csak ami nincs, annak van bokra,<br>
csak ami lesz, az a virág,<br>
ami van, széthull darabokra."<br>

...<br><br>

"Én fölnéztem az est alól<br>
az egek fogaskerekére -<br>
csilló véletlen szálaiból<br>
törvényt szőtt a mult szövőszéke<br>
és megint fölnéztem az égre<br>
álmaim gőzei alól<br>
s láttam, a törvény szövedéke<br>
mindíg fölfeslik valahol."<br>


<iframe width="560" height="315" src="https://www.youtube.com/embed/0uF9W2jlCns?si=gUxPMCHdY4P1oIy_&amp;start=169" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>