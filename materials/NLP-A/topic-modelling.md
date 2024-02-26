---
title: "Topic Modelling"
collection: teaching
type: "M.Sc course"
permalink: /materials/NLP-A/topic-modelling
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2024
location: "Debrecen, Hungary"
---

```python
!pip install wordcloud
!pip install pyLDAvis
!pip install datasets
!pip install numpy==1.23.0
!pip install bertopic
```

## Load data

```python
import pandas as pd
from datasets import load_dataset

news = load_dataset("rungalileo/20_Newsgroups_Fixed")
news = pd.DataFrame(news['train'])
news = news.dropna()
print(news.info())
news.head()
```

```python
import nltk

nltk.download("stopwords")
nltk.download('punkt')
nltk.download('wordnet')
```

```python
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()
w_n_lemmatizer = WordNetLemmatizer()

stop_words = set(stopwords.words("english"))

news["text"] = news["text"].apply(lambda row: row.lower())
news["text"] = news["text"].apply(lambda row: " ".join([word for word in word_tokenize(row) if not word in stop_words and word.isalpha()]))
news["text"] = news["text"].apply(lambda row: " ".join([w_n_lemmatizer.lemmatize(word) for word in word_tokenize(row)]))
news["text"] = news["text"].apply(stemmer.stem)

news.head()
```

## Wordcloud

```python
from wordcloud import WordCloud

long_string = ','.join(news["text"].values)

wordcloud = WordCloud(background_color="white",
                      max_words=1000,
                      contour_width=3,
                      contour_color='steelblue')

wordcloud.generate(long_string)

wordcloud.to_image()
```

## LDA

```python
import gensim.corpora as corpora

data_words = [item.split() for item in news["text"].values]

id2word = corpora.Dictionary(data_words)

print(id2word)
```

```python
corpus = [id2word.doc2bow(text) for text in data_words]

print(corpus[:1][0][:30])
```

```python
import gensim

num_topics = 10

lda_model = gensim.models.LdaMulticore(corpus=corpus,
                                       id2word=id2word,
                                       num_topics=10)

lda_model.print_topics()
```

```python
import os
import pickle
import pyLDAvis
import pyLDAvis.gensim_models


pyLDAvis.enable_notebook()

LDAvis_data_filepath = os.path.join('lda_'+str(num_topics))

LDAvis_prepared = pyLDAvis.gensim_models.prepare(lda_model, corpus, id2word)
with open(LDAvis_data_filepath, 'wb') as f:
    pickle.dump(LDAvis_prepared, f)

with open(LDAvis_data_filepath, 'rb') as f:
    LDAvis_prepared = pickle.load(f)
    pyLDAvis.save_html(LDAvis_prepared, 'lda_'+ str(num_topics) +'.html')

LDAvis_prepared
```

## [BERTopic](https://huggingface.co/datasets/huggingface/documentation-images/resolve/2d1113254a370972470d42e122df150f3551cc07/blog/BERTopic/bertopic_overview.mp4)

```python
from bertopic import BERTopic

topic_model = BERTopic()
topics, probs = topic_model.fit_transform(news["text"].values)
```

```python
topic_model.get_topic_info()
```

```python
topic_model.get_topic(10)
```

```python
topic_model.get_document_info(news["text"].values)
```