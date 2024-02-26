---
title: "Attention II."
collection: teaching
type: "M.Sc course"
permalink: /materials/NLP-A/attention-II
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2024
location: "Debrecen, Hungary"
---

## Globális (global) és ok-okozati (casual) önfigyelem

## Transformer architektúra

<img src="https://www.tensorflow.org/images/tutorials/transformer/transformer.png" alt="Transformer">

Ábra 1: Transformer architektúra. Forrás: [www.tensorflow.org](https://www.tensorflow.org/text/tutorials/transformer).

### Miért fontosak a transzformátorok?

- A transzformátorok kiválóak a szekvenciális adatok, például a természetes nyelv modellezésében.

- A visszatérő neurális hálózatokkal (RNN) ellentétben a transzformátorok párhuzamosíthatók. Ezáltal hatékonyak olyan hardvereken, mint a GPU-k és a TPU-k. Ennek fő oka az, hogy a Transformers az ismétlődést a figyelemre cserélte, és a számítások egyidejűleg is megtörténhetnek. A fóliakimenetek párhuzamosan is számíthatók, az RNN-hez hasonló sorozat helyett.

- Ellentétben az RNN-ekkel (mint a seq2seq, 2014 ) vagy a konvolúciós neurális hálózatokkal (CNN-ekkel) (például a ByteNet ), a transzformátorok képesek megragadni a távoli vagy nagy hatótávolságú kontextusokat és függőségeket az adatokban a bemeneti vagy kimeneti szekvenciák távoli pozíciói között. Így hosszabb kapcsolatokat lehet megtanulni. A figyelem lehetővé teszi, hogy minden hely hozzáférjen az egyes rétegek teljes bemenetéhez, míg az RNN-ekben és a CNN-ekben az információnak sok feldolgozási lépésen kell keresztülmennie ahhoz, hogy nagy távolságra mozogjon, ami megnehezíti a tanulást.

-A transzformátorok nem tesznek feltételezéseket az adatok időbeli/térbeli kapcsolatairól. Ez ideális objektumok (például StarCraft egységek ) feldolgozásához.

<img src="https://www.tensorflow.org/images/tutorials/transformer/encoder_self_attention_distribution.png" alt="Transformer">

Ábra 2: Az „it” szó kódoló önfigyelem eloszlása ​​egy angol-francia fordításra képzett Transformer 5.-6. rétegében (a nyolc figyelemfej egyike).. Forrás: [www.Google Blog](https://blog-research-google.translate.goog/2017/08/transformer-novel-neural-network.html?_x_tr_sl=en&_x_tr_tl=hu&_x_tr_hl=hu&_x_tr_pto=wapp).

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

```python
## Fuzzy , differenciálható , vektorizált szótár keresés

<img src="https://www.tensorflow.org/images/tutorials/transformer/BaseAttention-new.png" alt="Transformer">

Ábra 4: Query, Key, Value. Forrás: [www.tensorflow.org](https://www.tensorflow.org/text/tutorials/transformer).
```

## Multi Head Attention

<img src="https://www.researchgate.net/publication/351019792/figure/fig1/AS:1014991599726592@1619004263146/Multi-Head-Attention-consists-of-several-Scaled-Dot-Product-Attention-layers-running.png" alt="Transformer">

Ábra 5: Multi Head Attention. Forrás: [www.researchgate.net](https://www.researchgate.net).

## Ok-okozati önfigyelem réteg

Az ok-okozati önfigyelés során egy token csak az előtte lévő tokenekre figyel, vagyis az időben előtte levő információkra. Ezt például időben sorban történő szekvenciák feldolgozására használják, például szövegekben, ahol a szavak sorrendje fontos. A causal self attention segít a modelleknek megérteni az idősorrendi kapcsolatokat és az időbeli összefüggéseket.

<img src="https://www.tensorflow.org/images/tutorials/transformer/CausalSelfAttention.png" alt="Transformer">

Ábra 8: A alkalmi önfigyelm réteg. Forrás: [www.tensorflow.org](https://www.tensorflow.org/text/tutorials/transformer).

<img src="https://www.tensorflow.org/images/tutorials/transformer/CausalSelfAttention-new-full.png" alt="Transformer">

Ábra 9: A alkalmi önfigyelm réteg. Forrás: [www.tensorflow.org](https://www.tensorflow.org/text/tutorials/transformer).

+ Az ok-okozati maszk biztosítja, hogy minden hely csak az előtte lévő helyekhez férhessen hozzá.
+ A maradék kapcsolatokat az egyszerűség kedvéért itt is kihagytuk.
+ Ennek a rétegnek a kompaktabb ábrázolása a következő lenne.
+ A korai sorozatelemek kimenete nem függ a későbbi elemektől, így nem számít, hogy a réteg alkalmazása előtt vagy után vágja-e le az elemeket.

```python
class CausalSelfAttention(BaseAttention):
  def call(self, x):
    attn_output = self.mha(
        query=x,
        value=x,
        key=x,
        use_causal_mask = True)
    x = self.add([x, attn_output])
    x = self.layernorm(x)
    return x
```

```python
sample_csa = CausalSelfAttention(num_heads=2, key_dim=512)
```

## A kereszt figyelemi réteg

A kereszteződő önfigyelésnél az input egyik része figyel a másik részre. Például, ha egy fordítás modellt használunk, a fordító rendszernek figyelmet kell fordítania a forrásnyelvű szavakra és az ezekhez tartozó fordításokra. A cross self attention lehetővé teszi a modellek számára, hogy kapcsolatot építsenek ki két különböző szekvencia között, és segítségével a forrásinformációkat a célinformációval összevetik.

<img src="https://www.tensorflow.org/images/tutorials/transformer/CrossAttention.png" alt="Transformer">

Ábra 6: A keresztfigyelem réteg. Forrás: [www.tensorflow.org](https://www.tensorflow.org/text/tutorials/transformer).

<img src="https://www.tensorflow.org/images/tutorials/transformer/CrossAttention-new-full.png" alt="Transformer">

Ábra 7: A keresztfigyelem réteg. Forrás: [www.tensorflow.org](https://www.tensorflow.org/text/tutorials/transformer).

```python
class CrossAttention(BaseAttention):
  def call(self, x, context):
    attn_output, attn_scores = self.mha(
        query=x,
        key=context,
        value=context,
        return_attention_scores=True)

    # Gyorsítótárazza a figyelempontszámokat későbbi ábrázoláshoz.
    self.last_attn_scores = attn_scores

    x = self.add([x, attn_output])
    x = self.layernorm(x)

    return x
```

```python
sample_ca = CrossAttention(num_heads=2, key_dim=512)
```

<img src="https://www.tensorflow.org/images/tutorials/transformer/attention_map_portuguese.png" alt="Transformer">

Ábra 8: Vizualizált figyelemsúlyok. Forrás: [www.Google Blog](https://blog-research-google.translate.goog/2017/08/transformer-novel-neural-network.html?_x_tr_sl=en&_x_tr_tl=hu&_x_tr_hl=hu&_x_tr_pto=wapp).