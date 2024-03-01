---
title: "Numpy and Matplotlib"
collection: teaching
type: "M.Sc course"
permalink: /materials/NLP-A/numpy-and-matplotlib
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2024-02-27
location: "Debrecen, Hungary"
---

## Matplotlib

```python
!pip install matplotlib
```

```python
import matplotlib.pyplot as plt
import matplotlib as mpl

```

```python
plt.plot(range(10), range(10))
plt.show()
```

```python
mpl.style.use("seaborn")
```

```python
plt.plot(range(10), range(10))
plt.show()
```

```python
xs = range(1, 10 + 1)
ys = [x**2 for x in xs]
```

```python
plt.plot(xs, ys)
plt.xticks([5, 10])
plt.yticks([25, 50, 75, 100])
```

```python
plt.plot(xs, ys, color="orange")
plt.plot(xs, [5 * x for x in xs], color="green")
plt.xlabel("n")
plt.ylabel("n**2")
plt.legend(["quadratic function", "linear function"])
plt.title("Title")
```

```python
plt.hist(range(100), bins=5, rwidth=0.5)
```

```python
plt.boxplot([[1, 2, 3, 7], [1, 3, 4, 5], [3, 4, 5, 11]])
```

## Numpy

```python
import numpy as np
```

```python
a = np.array([1,2,3])
```

```python
a
```

### But why?

```python
%%timeit

my_list = list(range(1000000))

my_list = [2 * i for i in my_list]
```

```python
!dir
```

### [magic-timeit](https://ipython.org/ipython-doc/dev/interactive/magics.html#magic-timeit)

```python
%%timeit

my_array = np.zeros(1000000)

my_array *= 2
```

```python
sizes = 10 ** np.array(range(1, 7+1))
sizes
```

```python
from timeit import timeit
from tqdm import tqdm

times_list = []
times_numpy = []

for size in tqdm(sizes):
    _input = list(range(size))

    times_list.append(timeit(lambda: [2 * element for element in _input], number=100))

for size in tqdm(sizes):
    _input = np.array(range(size))

    times_numpy.append(timeit(lambda: 2 * _input, number=100))
```

```python
plt.plot(sizes, times_list, color="cyan")
plt.plot(sizes, times_numpy, color="orange")
plt.legend(["list", "numpy"], prop={"size": 16})
plt.xlabel("number of elements")
plt.ylabel("seconds")
plt.xscale("log")
plt.show()
```

```python
print(times_list)
print(times_numpy)
print([l/n for l, n in zip(times_list, times_numpy)])
```

### The basics

```python
a = np.array([1, 2, 3])

print("a:\t", a)
print("shape:\t", a.shape)
print("dim:\t", a.ndim)
print("dtype:\t", a.dtype)
```

```python
b = np.array([1, 2, 3], dtype=np.int8)
```

```python
print("b:\t", b)
print("shape:\t", b.shape)
print("dim:\t", b.ndim)
print("dtype:\t", b.dtype)
```

```python
print("size of a (in bytes): ", a.nbytes)
print("size of b (in bytes): ", b.nbytes)
```

```python
c = np.array([0.5, 0.75, 1.0])

print("c:\t", c)
print("dtype:\t", c.dtype)
```

```python
a = np.ones(10)
print(a)
```

```python
a = np.zeros(3)
print(a)
```

```python
d = np.arange(10)
print(d)
```

```python
d2 = np.arange(10).reshape(2, 5)
print(d2)
```

```python
print(d2[0])
```

```python
print(d2[0][2])
```

```python
e = np.linspace(0, 10, 11)
print(e)
```

```python
f = np.linspace(0, 10, 101)
print(f)
```

### Basic operations

```python
a = np.array([1, 2, 3])
b = np.array([3, 2, 1])

print(a - b)
print(a + b)
print(2 * a)
print(a ** 2)
print(a < 2)
print(np.sin(a))
print(np.sqrt(a))
print(np.log2(a))
```

```python
a += b
print(a)

a -= b
print(a)
```

```python
a = np.array([1, 2, 3])
b = a

b[0] = 10

print(a)
print(b)
```

```python
a = np.array([1, 2, 3])
b = a.copy()

b[0] = 10

print(a)
print(b)
```

### Matrix operations

```python
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[1, 2, 3, 4], [4, 3, 2, 1], [0, 1, 2, 3]])

C = np.matmul(A, B)
D = A @ B

print("A:", A.shape)
print("B:", B.shape)
print("2A:\n", 2 * A)
print("C:\n", C)
print("C shape:", C.shape)
print("D:\n", D)
print("D shape:", D.shape)
```
```