---
title: "Feed-Foward Layer. Dense Neural Network in the Trasnformer"
collection: teaching
type: "M.Sc course"
permalink: /materials/NLP-A/labor/feed-foward
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2024-02-27
location: "Debrecen, Hungary"
---

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

## Feed Forward rétegek (Klassikus Mélye Neurális háló)

A transzformátor ezt a pontonkénti előrecsatoló hálózatot is tartalmazza mind a kódolóban, mind a dekódolóban.

1. <b>Átalakítás a pozíciók között:</b> A PWFFN réteg először bemeneti reprezentációkat kap, amelyeket különböző pozíciókban az input szekvencián belül szeretné átalakítani. Az átalakítás pozíció alapján történik, tehát az egyes pozíciókhoz tartozó reprezentációk függetlenek egymástól. Ez segít a modelleknek abban, hogy megőrizzék a szekvenciákban lévő pozícióspecifikus információkat.
2. <b>Nemlineáris átalakítás:</b> Miután a bemeneti reprezentációkat pozíciós alapon átformálták, a PWFFN réteg egy nemlineáris aktiváló függvényen (általában ReLU) vezet át. Ez segít a modellnek abban, hogy komplexabb és nemlineáris kapcsolatokat ismerjen fel a tokenek között.
3. <b>Összekapcsolás és reprezentáció-változás:</b> Végül a PWFFN réteg a kimeneti reprezentációkat kapja meg. Ezek a kimeneti reprezentációk már kifejezőbbek és tartalmazhatnak olyan mintázatokat vagy jellemzőket, amelyek segítenek a modelleknek jobban megérteni a bemeneti szekvenciákat és feladatokat.

<img src="https://www.tensorflow.org/images/tutorials/transformer/FeedForward.png" alt="Transformer">

Ábra 3: Attention rétegek. Forrás: [www.tensorflow.org](https://www.tensorflow.org/text/tutorials/transformer).

```python
import tensorflow as tf

class FeedForward(tf.keras.layers.Layer):
  def __init__(self, d_model, dff, dropout_rate=0.1):
    super().__init__()
    self.seq = tf.keras.Sequential([
      tf.keras.layers.Dense(dff, activation='relu'),
      tf.keras.layers.Dense(d_model),
      tf.keras.layers.Dropout(dropout_rate)
    ])
    self.add = tf.keras.layers.Add()
    self.layer_norm = tf.keras.layers.LayerNormalization()

  def call(self, x):
    x = self.add([x, self.seq(x)])
    x = self.layer_norm(x) 
    return x
```

```python
sample_ffn = FeedForward(512, 2048)
```
