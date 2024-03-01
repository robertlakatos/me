---
title: "Python Basics (refresher)"
collection: teaching
type: "M.Sc course"
permalink: /materials/NLP-A/python
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2024-02-27
location: "Debrecen, Hungary"
---

## Variables

```python
foo = 5
```

```python
print(foo)
```

```python
bar = 2

print(foo + bar)
print(foo * bar)
print(foo / bar)
print(foo // bar)
print(foo % bar)
print(foo == bar)
print(2 == 2)
```

```python
bar = "Hello"
```

```python
print(bar)
```

```python
name = "Adam"
print("Hello", name)
```

```python
print("Hello " + name + "!")
```

```python
print("Hello", name, "!")
```

```python
print(f"Hello, {name}!")
```

```python
foo = "FoO"
print(foo)
```

```python
print("original:\t", foo)
print("lower():\t", foo.lower())
print("upper():\t", foo.upper())
print("capitalize():\t", foo.capitalize())
```

```python
foo = True
bar = False

print(foo)
print(foo and bar)
print(foo or bar)
print(not foo)
```

## Compound types

### Lists

```python
l = [1, 2, 3, 4, 5]
```

```python
print(l)
```

```python
l = [1, "a", "abcdefgh", 2.5]
```

```python
print(l)
```

```python
l.append(5)
```

```python
print(l)
```

```python
l.pop()
```

```python
print(l)
```

```python
l.pop(1)
```

```python
print(l)
```

```python
l = []
```

```python
l.append(1)
l.append("apple")
l.append(2.5)
```

```python
print(l)
```

```python
range(1, 10)
```

```python
l = list(range(1, 10))
```

```python
print(l)
```

```python
print(l[0])
```

```python
print(l[0:2])
```

```python
print(l[2:])
```

```python
print(l[-1])
```

```python
print(l[-2:])
```

```python
print(l[:-2])
```

```python
print("Before:", l)
l[-2:] = ["quick", "maths"]
print("After:", l)
```

### Tuples

```python
t = (1, 2)
```

```python
print(t[0])
```

```python
t2 = (1, 2, "apple")
```

```python
print(t2)
```

```python
print(t2[-2:])
```

```python
t2[0] = "banana"
```

### Sets

```python
s = set()
```

```python
s.add(1)
```

```python
print(s)
```

```python
s.add(1)
```

```python
print(s)
```

```python
s.remove(1)
```

```python
print(s)
```

```python
s.add(1)
s.add("apple")
```

### Dictionaries

```python
d = dict()
```

```python
d["foo"] = "bar"
```

```python
print(d)
```

```python
print(d["foo"])
```

```python
print(d["foo2"])
```

```python
print(d.get("foo2"))
```

```python
print(d.get("foo2", "bar2"))
```

## Control flow

```python
n = 10

if n % 2 == 0:
    print("The number is even.")
else:
    print("The number is not even.")
```

```python
n = 11

if n % 2 == 0:
    print("The number is even.")
elif n % 3 == 0:
    print("The number can be divided by 3.")
else:
    print("The number is not even and cannot be divided by 3.")
```

```python
for i in range(10):
    print(i)
```

```python
for i in range(10):
    print(i, end="")
```

```python
for i in range(10):
    print(i, end=",")
```

```python
for i in range(1, 10 + 1):
    print(i)
```

```python
l = range(10)

for i in range(len(l)):
    print(l[i])
```

```python
for item in l:
    print(item)
```

```python
s = {1,2, 3} # or s = set([1, 2, 3])

for item in s:
    print(item, end=";")
```

```python
d = {
    "name": "John Smith",
    "age": 25,
    "height": 182,
    "weight": 82
}

for key, value in d.items():
    print(key, "->", value)

print("-" * 20)

for key in d:
    print(d[key])
```

```python
n = 10

while n > 0:
    print(n)
    n -= 1

print("---")
print(n)
print("---")

while n < 10:
    print(n ** 2)
    n += 1
```

## Functions

```python
def my_function(x, y):
    return x + y

print(my_function(2, 3))
```

```python
def greet_person(name):
    print(f"Hello, {name}!")

greet_person(name="David")
```

## Packages

```python
import math

n = 10.5

print("ceil(): \t", math.ceil(n))
print("floor(): \t", math.floor(n))
print("sqrt(): \t", math.sqrt(n))
```