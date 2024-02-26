---
title: "Pipeline"
collection: teaching
type: "M.Sc course"
permalink: /NLP-A/pipeline
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2024
location: "Debrecen, Hungary"
---

### Mi az NLP?

- Az NLP (Natural Language Processing) a nyelvészet és a gépi tanulás területe, amely az emberi nyelvvel megértésére összpontosít.
- Az NLP-feladatok célja nemcsak az egyes szavak egyenkénti megértése, hanem a szavak kontextusának megértése.

### Leggyakoribb NLP feladatok

- Mondatok osztályozása:
    - Szentiment (hangulat) analízis,
    - Kategorizálás, például egy e-mail spam-e?
    - Mondat nyelvtanilag helyes-e
    - Két mondat logikailag összefügg-e vagy sem
- Az egyes szavak osztályozása egy mondatban: A mondat grammatikai összetevőinek (főnév, ige, melléknév) vagy a megnevezett entitások (személy, hely, szervezet) azonosítása.
- Szöveges tartalom generálása:
    - Prompt kitöltése automatikusan generált szöveggel
    - Szöveg üres részeinek kitöltése maszkolt szavakkal
- Válasz kinyerése egy szövegből: Adott egy kérdés és egy kontextus, a kérdésre adott válasz kinyerése a szövegkörnyezetben megadott információk alapján.
- Új mondat generálása beviteli szövegből: Szöveg fordítása másik nyelvre, szöveg összefoglalása.
- Multimodális és komplex megoldások
    - Prompt engineering
    - Képek generálása
    - Chat

### Az NLP azonban nem korlátozódik írott szövegre. Megbirkózik a beszédfelismerés és a számítógépes látás összetett kihívásaival is, például hangminta átiratának vagy képleírásának létrehozásával!

## Legfontosabb ML csomagok

- [PyTorch](https://pytorch.org/)
- [Tensorflow](https://www.tensorflow.org/)
- [Keras](https://keras.io/)
- ### [Huggingface](https://huggingface.co/)

## Pipline and Examples

### Dependencies

```python
!pip install transformers
!pip install sentencepiece
```

### Working with pipelines

```python
from transformers import pipeline
```

```python
classifier = pipeline("sentiment-analysis")
classifier("I've been waiting for a HuggingFace course my whole life.")
```

```python
classifier(["I've been waiting for a HuggingFace course my whole life.", "I hate this so much!"])
```

### Zero-shot classification

```python
classifier = pipeline("zero-shot-classification")
classifier(
    "This is a course about the Transformers library",
    candidate_labels=["education", "politics", "business"],
)
```

### Text generation

```python
generator = pipeline("text-generation")
generator("In this course, we will teach you how to")
```

```python
generator = pipeline("text-generation", model="distilgpt2")
generator(
    "In this course, we will teach you how to",
    max_length=30,
    num_return_sequences=2,
)
```

### Mask filling

```python
unmasker = pipeline("fill-mask")
unmasker("This course will teach you all about <mask> models.", top_k=2)
```

### Named entity recognition

```python
ner = pipeline("ner", grouped_entities=True)
ner("My name is Sylvain and I work at Hugging Face in Brooklyn.")
```

### Question answering

```python
question_answerer = pipeline("question-answering")
question_answerer(
    question="Where do I work?",
    context="My name is Sylvain and I work at Hugging Face in Brooklyn",
)
```

### Summarization

```python
summarizer = pipeline("summarization")
summarizer(
    """
    America has changed dramatically during recent years. Not only has the number of
    graduates in traditional engineering disciplines such as mechanical, civil,
    electrical, chemical, and aeronautical engineering declined, but in most of
    the premier American universities engineering curricula now concentrate on
    and encourage largely the study of engineering science. As a result, there
    are declining offerings in engineering subjects dealing with infrastructure,
    the environment, and related issues, and greater concentration on high
    technology subjects, largely supporting increasingly complex scientific
    developments. While the latter is important, it should not be at the expense
    of more traditional engineering.

    Rapidly developing economies such as China and India, as well as other
    industrial countries in Europe and Asia, continue to encourage and advance
    the teaching of engineering. Both China and India, respectively, graduate
    six and eight times as many traditional engineers as does the United States.
    Other industrial countries at minimum maintain their output, while America
    suffers an increasingly serious decline in the number of engineering graduates
    and a lack of well-educated engineers.
"""
)
```

### Translation

```python
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")
translator("Ce cours est produit par Hugging Face.")
```

## [Mi az a Transformer?](https://arxiv.org/pdf/1706.03762.pdf)

<img src="https://www.comingsoon.net/wp-content/uploads/sites/3/2023/06/Watch-the-Transformers-Movies-Before-Rise-of-the-Beasts.jpg?resize=1024,576" alt="Transformers">

Ábra 1: Transformers. Forrás: [Comingsoon](https://www.comingsoon.net/guides/news/1293620-do-i-need-to-watch-the-transformers-movies-before-rise-of-the-beasts).

### Leghíresebb transformer architektúrák

- 2018. június: A GPT, az első előre betanított Transformer modell, amelyet különféle NLP-feladatok finomhangolására használnak, és a legmodernebb eredményeket érte el
- 2018. október: A BERT, egy másik nagy, előre betanított modell, amelyet a mondatok jobb összefoglalására terveztek (erről a következő fejezetben olvashat bővebben!)
- 2019. február: GPT-2, a GPT továbbfejlesztett (és nagyobb) változata, amelyet etikai aggályok miatt nem adtak ki azonnal nyilvánosan
- 2019. október: DistilBERT, a BERT desztillált változata, amely 60%-kal gyorsabb, 40%-kal könnyebb a memóriában, és továbbra is megőrzi a BERT teljesítményének 97%-át
- 2019. október: BART és T5, két nagy, előre betanított modell, amelyek ugyanazt az architektúrát használják, mint az eredeti Transformer modell (az első, amelyik ezt megtette)
- 2020. május, GPT-3, a GPT-2 még nagyobb verziója, amely finomhangolás nélkül (úgynevezett zero-shot learning) számos feladaton jól teljesít.
- 2022. március, GPT-3.5, a GPt-2 még nagyobb verziója és nagyobb, mint a GPT-3, valamint ez a hálózati bázis az első chatGPT-hez
- 2023. márcis, GPT-4


### Nagy nyelvi modellek és méreteik

<img src="https://i0.wp.com/thelowdown.momentum.asia/wp-content/uploads/2023/03/LLMs-featured-img.jpg?resize=1024%2C512&ssl=1" alt="LLM-ek">

Ábra 2: Nagy nyelvi modellek. Forrás: [thelowdown](https://thelowdown.momentum.asia/the-emergence-of-large-language-models-llms/).


### First Transformer

<img src="https://www.tensorflow.org/images/tutorials/transformer/transformer.png" alt="Transformer architektúra">

Ábra 3: Transformer architektúra. Forrás: [Google AI Blog](https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html).