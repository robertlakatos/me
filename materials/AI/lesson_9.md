---
title: "9. Gyakorlat"
collection: teaching
type: "B.Sc course"
permalink: /materials/AI/lesson_9
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2024-04-08
location: "Debrecen, Hungary"
---

## Adathalmaz

```python
from sklearn.datasets import fetch_openml
mnist = fetch_openml(name="mnist_784")
```

```python
print(mnist.keys())
```

```python
data = mnist.data
labels = mnist.target
```

```python
# 70000 darab 784 (28x28) jellemzővel leírható kép
data.shape
```

```python
data
```

```python
import matplotlib.pyplot as plt

def viz(test_img, test_label, size=(28, 28)):
    plt.imshow(test_img.reshape(size[0], size[1]), cmap="Greys")
    plt.axis('off')
    plt.title(str(test_label))
    plt.show()
```

```python
import numpy as np

choice = np.random.choice(np.arange(data.shape[0]+1))
# Teszt kép kiválasztása
test_img = data.iloc[choice].values
# Teszt label kiválasztása
test_label = mnist.target.iloc[choice]
viz(test_img, test_label)
```

### Normalizáció

<img src="https://robertlakatos.github.io/me/materials/AI/images/norm.jpg" alt="normalization">

```python
def normalize(x):
    return (x - np.min(x)) / (np.max(x) - np.min(x))
```

```python
n_data = normalize(data.values)
n_data.shape
```

### One-hot

<img src="https://robertlakatos.github.io/me/materials/AI/images/one_hot.png" alt="one hot">

```python
def one_hot_encode(x: np.ndarray, num_labels: int) -> np.ndarray:
    return np.eye(num_labels)[x]
```

### Tanuló és teszt adatok

```python
train_test_split_no = int(n_data.shape[0] * 0.8)
train_test_split_no
```

```python
X_train = n_data[:train_test_split_no]
y_train = labels[:train_test_split_no].values.astype(int)
y_train = one_hot_encode(y_train, 10)

X_train.shape, y_train
```

```python
X_test = n_data[train_test_split_no:]
y_test = labels[train_test_split_no:].values.astype(int)
y_test = one_hot_encode(y_test, 10)

X_test.shape
```

## Hogyan tudjuk elképzelni?

### Neuronok

<img src="https://robertlakatos.github.io/me/materials/AI/images/nn_3.png" alt="neural network 3">

### Agyunk mint hálózat

<img src="https://robertlakatos.github.io/me/materials/AI/images/nn_4.jpg" alt="neural network 4">

### Egy rétegű neurális hálók

<img src="https://robertlakatos.github.io/me/materials/AI/images/nn_1.png" alt="neural network 1">

### Több rétegű neurális hálózat

<img src="https://robertlakatos.github.io/me/materials/AI/images/nn_2.png" alt="neural network 2">

### Neurális hálózat koncepció

<img src="https://robertlakatos.github.io/me/materials/AI/images/nn_5.png" alt="neural network 5">

### Aktivácuós függvények

<img src="https://robertlakatos.github.io/me/materials/AI/images/soft_max.png" alt="soft max">

<img src="https://robertlakatos.github.io/me/materials/AI/images/relu.png" alt="relu">

## Egyszerű neurális hálózat pythonban

```python
import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Input((X_train.shape[1])),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(10, activation="softmax")
    ]
)
```

```python
model.summary()
```

```python
for layer in model.get_weights():
    print(layer.shape)
```

```python
tf.keras.utils.plot_model(
    model,
    show_shapes=True,
    show_dtype=True,
    show_layer_names=True,
    expand_nested=True,
    dpi=96,
    layer_range=None,
    show_layer_activations=True)
```

```python
model.compile(
    optimizer="adam", 
    loss="categorical_crossentropy", 
    metrics=["accuracy"]
)
```

```python
x = tf.ones((3, X_train.shape[1]))
model(x)
```

### Tanulás

```python
model.fit(X_train, y_train, epochs=5, batch_size=32)
```

### Kiértékelés

```python
model.evaluate(X_test, y_test)
```

```python
choice = np.random.choice(np.arange(X_test.shape[0]+1))
p = model.predict(np.array([X_test[choice]]))
viz(X_test[choice], np.argmax(p))
```