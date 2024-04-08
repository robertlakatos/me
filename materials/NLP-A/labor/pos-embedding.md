---
title: "Position Embedding"
collection: teaching
type: "M.Sc course"
permalink: /materials/NLP-A/labor/pos-embedding
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2024-02-27
location: "Debrecen, Hungary"
---

## Transformer architektúra

<img src="https://www.tensorflow.org/images/tutorials/transformer/transformer.png" alt="Transformer">

Ábra 1: Transformer architektúra. Forrás: [www.tensorflow.org](https://www.tensorflow.org/text/tutorials/transformer).

## Beágyazó és pozíciókódoló rétegek

<img src="https://www.tensorflow.org/images/tutorials/transformer/PositionalEmbedding.png" alt="Transformer">

Ábra 2: Beágyazó és pozíciókódoló rétegek. Forrás: [www.tensorflow.org](https://www.tensorflow.org/text/tutorials/transformer).

## Pozició Embedding

- A modellben használt figyelemrétegek bemenetüket vektorok halmazának tekintik, sorrend nélkül. Mivel a modell nem tartalmaz visszatérő vagy konvolúciós rétegeket.Valamilyen módra van szüksége a szórend azonosítására, különben a beviteli sorozatot egy zsáknyi szópéldányként látná, a hogyan vagy, hogy vagy, hogy vagy és így tovább, megkülönböztethetetlenek.

- A Transformer egy "pozíciós kódolást" ad hozzá a beágyazási vektorokhoz. Különböző frekvenciákon (a sorozaton keresztül) szinuszokat és koszinuszokat használ. A definíció szerint a közeli elemeknek hasonló pozíciókódolásuk lesz.

## Pozició alapú beágyazás formula.

<img src="https://i.stack.imgur.com/67ADh.png">

Ábra 6: Pozició alapú beágyazás formula.: [stackoverflow](https://i.stack.imgur.com/67ADh.png).

```python
import numpy as np
import tensorflow as tf

def positional_encoding(length, depth):
  depth = depth/2

  positions = np.arange(length)[:, np.newaxis]     # (seq, 1)
  depths = np.arange(depth)[np.newaxis, :]/depth   # (1, depth)

  angle_rates = 1 / (10000**depths)         # (1, depth)
  angle_rads = positions * angle_rates      # (pos, depth)

  pos_encoding = np.concatenate([np.sin(angle_rads), np.cos(angle_rads)],axis=-1)

  return tf.cast(pos_encoding, dtype=tf.float32)
```

```python
import matplotlib.pyplot as plt

pos_encoding = positional_encoding(length=2048, depth=512)

print(pos_encoding.shape)

plt.pcolormesh(pos_encoding.numpy().T, cmap='RdBu')
plt.ylabel('Mélység (dimenzió szám)')
plt.xlabel('Pozició')
plt.colorbar()
plt.show()
```

```python
class PositionalEmbedding(tf.keras.layers.Layer):
  def __init__(self, vocab_size, d_model):
    super().__init__()
    self.d_model = d_model
    self.embedding = tf.keras.layers.Embedding(vocab_size, d_model, mask_zero=True) 
    self.pos_encoding = positional_encoding(length=2048, depth=d_model)

  def compute_mask(self, *args, **kwargs):
    return self.embedding.compute_mask(*args, **kwargs)

  def call(self, x):
    length = tf.shape(x)[1]
    x = self.embedding(x)
    # Ez a tényező határozza meg a beágyazás és a pozitonális_kódolás relatív skáláját.
    x *= tf.math.sqrt(tf.cast(self.d_model, tf.float32))
    x = x + self.pos_encoding[tf.newaxis, :length, :]
    return x
```

```python
embed_pt = PositionalEmbedding(vocab_size=100, d_model=512)
embed_en = PositionalEmbedding(vocab_size=100, d_model=512)

pt_emb = embed_pt(pt)
en_emb = embed_en(en)
```

```python
en_emb._keras_mask
```

### Mondatok beágyazás transformerrel vagy hogyan működik a semantikus kereső?

```python
!pip install transformers
!pip install -U sentence-transformers
```

```python
from sentence_transformers import util
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
```

```python
sentences = ["I'm happy", "I'm full of happiness"]

embedding_1= model.encode(sentences[0], convert_to_tensor=True)
embedding_2 = model.encode(sentences[1], convert_to_tensor=True)

util.pytorch_cos_sim(embedding_1, embedding_2)
```