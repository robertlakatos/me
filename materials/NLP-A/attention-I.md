---
title: "Attention I."
collection: teaching
type: "M.Sc course"
permalink: /materials/NLP-A/attention-I
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2024-02-27
location: "Debrecen, Hungary"
---

## Alap (base) és kereszt (cross) figyelem

## Transformer architektúra

<img src="https://www.tensorflow.org/images/tutorials/transformer/transformer.png" alt="Transformer">

Ábra 1: Transformer architektúra. Forrás: [www.tensorflow.org](https://www.tensorflow.org/text/tutorials/transformer).

### Miért fontosak a transzformátorok?

- A transzformátorok kiválóak a szekvenciális adatok, például a természetes nyelv modellezésében.

- A visszatérő neurális hálózatokkal (RNN) ellentétben a transzformátorok párhuzamosíthatók. Ezáltal hatékonyak olyan hardvereken, mint a GPU-k és a TPU-k. Ennek fő oka az, hogy a Transformers az ismétlődést a figyelemre cserélte, és a számítások egyidejűleg is megtörténhetnek. A fóliakimenetek párhuzamosan is számíthatók, az RNN-hez hasonló sorozat helyett.

- Ellentétben az RNN-ekkel (mint a seq2seq, 2014 ) vagy a konvolúciós neurális hálózatokkal (CNN-ekkel) (például a ByteNet ), a transzformátorok képesek megragadni a távoli vagy nagy hatótávolságú kontextusokat és függőségeket az adatokban a bemeneti vagy kimeneti szekvenciák távoli pozíciói között. Így hosszabb kapcsolatokat lehet megtanulni. A figyelem lehetővé teszi, hogy minden hely hozzáférjen az egyes rétegek teljes bemenetéhez, míg az RNN-ekben és a CNN-ekben az információnak sok feldolgozási lépésen kell keresztülmennie ahhoz, hogy nagy távolságra mozogjon, ami megnehezíti a tanulást.

-A transzformátorok nem tesznek feltételezéseket az adatok időbeli/térbeli kapcsolatairól. Ez ideális objektumok (például StarCraft egységek ) feldolgozásához.

<img src="https://www.tensorflow.org/images/tutorials/transformer/encoder_self_attention_distribution.png" alt="Transformer">

Ábra 2: Az „it” szó kódoló önfigyelem eloszlása ​​egy angol-francia fordításra képzett Transformer 5.-6. rétegében (a nyolc figyelemfej egyike). Forrás: [www.Google Blog](https://blog-research-google.translate.goog/2017/08/transformer-novel-neural-network.html?_x_tr_sl=en&_x_tr_tl=hu&_x_tr_hl=hu&_x_tr_pto=wapp).

## Attention rétegek

<img src="https://www.tensorflow.org/images/tutorials/transformer/BaseAttention.png" alt="Transformer">

Ábra 3: Attention rétegek. Forrás: [www.tensorflow.org](https://www.tensorflow.org/text/tutorials/transformer).

```python
import tensorflow as tf

class BaseAttention(tf.keras.layers.Layer):
  def __init__(self, **kwargs):
    super().__init__()
    self.mha = tf.keras.layers.MultiHeadAttention(**kwargs)
    self.layernorm = tf.keras.layers.LayerNormalization()
    self.add = tf.keras.layers.Add()
```

## Query, Key, Value

```python
d = {'color': 'blue', 'age': 22, 'type': 'pickup'}
result = d['color']
```

## Fuzzy , differenciálható , vektorizált szótár keresés

<img src="https://www.tensorflow.org/images/tutorials/transformer/BaseAttention-new.png" alt="Transformer">

Ábra 4: Query, Key, Value. Forrás: [www.tensorflow.org](https://www.tensorflow.org/text/tutorials/transformer).

```python
import tensorflow as tf

layer = tf.keras.layers.MultiHeadAttention(num_heads=2, key_dim=2)
target = tf.keras.Input(shape=[8, 16])
source = tf.keras.Input(shape=[4, 16])
output_tensor, weights = layer(query=target,
                               value=source,
                               return_attention_scores=True)

output_tensor.shape, weights.shape
```

## Multi Head Attention

<img src="https://www.researchgate.net/publication/351019792/figure/fig1/AS:1014991599726592@1619004263146/Multi-Head-Attention-consists-of-several-Scaled-Dot-Product-Attention-layers-running.png" alt="Transformer">

Ábra 5: Multi Head Attention. Forrás: [www.researchgate.net](https://www.researchgate.net).

## Globális Önfigyelem réteg

A globális önfigyelés azt jelenti, hogy minden bemeneti token számára figyelmet számolunk ki a többi bemeneti tokenre. Az alapvető Transformer modellben a self-attention mechanizmus egy globális önfigyelést használ, ami azt jelenti, hogy minden tokennek van súlya, amely megmutatja, milyen mértékben figyel az összes többi tokenre a bemeneti szekvenciában. Ennek a mechanizmusnak a célja az összes lehetséges kapcsolat figyelembevétele, ami fontos lehet a feldolgozott szekvencia számára.

<img src="https://www.tensorflow.org/images/tutorials/transformer/SelfAttention.png" alt="Transformer">

Ábra 6: A globális önfigyelmi réteg. Forrás: [www.tensorflow.org](https://www.tensorflow.org/text/tutorials/transformer).

+ Ez a réteg felelős a kontextusszekvencia feldolgozásáért és az információ terjesztéséért annak hosszában
+ Mivel a szövegkörnyezeti sorrend rögzített a fordítás generálása közben, az információ mindkét irányban áramolhat.
+ A transzformátorok és az önfigyelem előtt a modellek általában RNN-eket vagy CNN-eket használtak ehhez a feladathoz:
+ Az RNN-nek és a CNN-nek azonban megvannak a korlátai:
    + Az RNN lehetővé teszi az információ áramlását a sorozaton keresztül, de számos feldolgozási lépésen keresztül jut el oda (korlátozza a gradiens áramlását). Ezeket az RNN lépéseket egymás után kell futtatni, így az RNN kevésbé tudja kihasználni a modern párhuzamos eszközök előnyeit.
    + A CNN-ben minden helyszín párhuzamosan feldolgozható, de ez csak korlátozott befogadó mezőt biztosít. A receptív mező csak lineárisan növekszik a CNN rétegek számával. Számos konvolúciós réteget kell egymásra raknia, hogy információt továbbítson a szekvencián (a Wavenet csökkenti ezt a problémát dilatált konvolúciókkal).
+ A globális önfigyelem réteg viszont lehetővé teszi, hogy minden sorozatelem közvetlenül hozzáférjen minden más szekvenciaelemhez, csak néhány művelettel, és az összes kimenet párhuzamosan számítható.

<img src="https://www.tensorflow.org/images/tutorials/transformer/SelfAttention-new-full.png" alt="Transformer">

Ábra 7: A Globális önfigyelem réteg. Forrás: [www.tensorflow.org](https://www.tensorflow.org/text/tutorials/transformer).

```python
class GlobalSelfAttention(BaseAttention):
  def call(self, x):
    attn_output = self.mha(
        query=x,
        value=x,
        key=x)
    x = self.add([x, attn_output])
    x = self.layernorm(x)
    return x
```

```python
sample_gsa = GlobalSelfAttention(num_heads=2, key_dim=512)
```