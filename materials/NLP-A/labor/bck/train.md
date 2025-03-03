---
title: "Train"
collection: teaching
type: "M.Sc course"
permalink: /materials/NLP-A/labor/train
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2024-02-27
location: "Debrecen, Hungary"
---

## Függőségek

```python
!pip install datasets
!pip install transformers==4.28.0
!pip install evaluate
```

## Erőforrások ellenőrzése

```python
!nvidia-smi
```

```python
import torch

torch.cuda.is_available(), torch.cuda.device_count(), torch.cuda.current_device()
```

### Az adathalmaz: [financial_phrasebank](https://huggingface.co/datasets/financial_phrasebank)

```python
from datasets import load_dataset

dataset = load_dataset("financial_phrasebank", 'sentences_allagree')
```

```python
dataset["train"][100]
```

```python
set([item["label"] for item in dataset["train"]])
```

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
```

```python
def tokenize_function(examples):
    return tokenizer(examples["sentence"], padding="max_length", truncation=True)

tokenized_datasets = dataset.map(tokenize_function, batched=True)
```

```python
small_train_dataset = tokenized_datasets["train"].shuffle(seed=42).select(range(1000))
small_eval_dataset = tokenized_datasets["train"].shuffle(seed=42).select(range(1000,1200)) 
```

```python
small_train_dataset, small_eval_dataset 
```

```python
print(small_train_dataset[0]["sentence"])
print(small_train_dataset[0]["label"])
print(small_train_dataset[0]["input_ids"])
print(small_train_dataset[0]["attention_mask"])
```

```python
print(small_eval_dataset[0]["sentence"])
print(small_eval_dataset[0]["label"])
print(small_eval_dataset[0]["input_ids"])
print(small_eval_dataset[0]["attention_mask"]) 
```

```python
from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased-finetuned-sst-2-english",
    ignore_mismatched_sizes=True,
    num_labels=3)
```

## Mérés

<img src="https://www.researchgate.net/publication/336402347/figure/fig3/AS:812472659349505@1570719985505/Calculation-of-Precision-Recall-and-Accuracy-in-the-confusion-matrix.ppm" alt="ACC">

Ábra 1: Pontosság. Forrás: [researchgate](https://www.researchgate.net/publication/336402347/figure/fig3/AS:812472659349505@1570719985505/Calculation-of-Precision-Recall-and-Accuracy-in-the-confusion-matrix.ppm).

<img src="https://oncologymedicalphysics.com/wp-content/uploads/2021/04/Precision-vs-Accuracy-OMP.png" alt="PvP">

Ábra 2: Pontosság és precizitás. Forrás: [oncologymedicalphysics](https://oncologymedicalphysics.com/wp-content/uploads/2021/04/Precision-vs-Accuracy-OMP.png).

```python
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score

y_true = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
y_pred = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
```

```python
from sklearn.metrics import confusion_matrix

TP, FP, FN, TN = confusion_matrix(y_true, y_pred, labels=[0, 1]).ravel()

# True Positive (TP) : The prediction was positive and the real sample was also positive.
print("True Positive (TP):", TP)
# True Negative (TN) : The prediction was negative and the real sample was also negative.
print("True Negative (TN):", TN)
# False Positive (FP) : The prediction was positive and the real sample was also negative.
print("False Positive (FP):", FP)
# False Negative (FN) : The prediction was negative and the real sample was also positive.
print("False Negative (FN):", FN)
```

```python
# Recall (R) = TP / (TP + FN)
print(recall_score(y_true, y_pred))

# Precizitás (P) = TP / (TP + FP)
print(precision_score(y_true, y_pred))

# Accuracy (A) = (TP + TN) / (TP + TN + FP + FN) - Correct classificaton / all classifications
print(accuracy_score(y_true, y_pred))

# F1 = 2 * P * R / (P + R)
print(f1_score(y_true, y_pred))
```

```python
import numpy as np
import evaluate

metric = evaluate.load("accuracy")
```

```python
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)
```

## Tanítás/képzés

<img src="https://tropeaka.com/cdn/shop/articles/main_image_d517c79f-4ec7-4946-bb5e-db7e80623e85_1080x.jpg?v=1571697737" alt="Train">

Ábra 3: Training. Forrás: [tropeaka](https://tropeaka.com/cdn/shop/articles/main_image_d517c79f-4ec7-4946-bb5e-db7e80623e85_1080x.jpg?v=1571697737).

```python
from transformers import TrainingArguments, Trainer

training_args = TrainingArguments(
    output_dir="test_trainer",
    evaluation_strategy="epoch",
    num_train_epochs=2
    )
```

```python
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=small_train_dataset,
    eval_dataset=small_eval_dataset,
    compute_metrics=compute_metrics,
)
```

```python
trainer.train()
```

```python
from transformers import pipeline

model_old = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
pipeline_old = pipeline("text-classification", model=model_old, tokenizer=tokenizer)
```

```python
text = small_eval_dataset[0:10]["sentence"]
labels = small_eval_dataset[0:10]["label"]
text, labels
```

```python
pipeline_old(text)
```

```python
device = "cuda:0" if torch.cuda.is_available() else "cpu"
device
```

```python
model_cpu = model.to("cpu")
```

```python
pipeline_new = pipeline("text-classification", model=model_cpu, tokenizer=tokenizer)
```

```python
print(labels)
pipeline_new(text)
```

### Pipeline nélkül (Hardcore verzió :D)

```python
import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

tokenizer_hc = DistilBertTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
model_hc = model

inputs = tokenizer(text, return_tensors="pt",padding=True,truncation=True)
with torch.no_grad():
    logits = model_hc(**inputs).logits

predicted_class_ids = [l.argmax().item() for l in logits]
predicted_class_ids, labels
```