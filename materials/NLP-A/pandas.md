---
title: "Pandas Intro (short)"
collection: teaching
type: "M.Sc course"
permalink: /materials/NLP-A/pandas
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2024-02-27
location: "Debrecen, Hungary"
---

## Basics

### [Pandas](https://pandas.pydata.org/)

```python
# !pip install pandas
```

```python
import pandas as pd
```

```python
df = pd.read_csv("https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/titanic_train.csv")
```

```python
df.head()
```

```python
df.head(2)
```

```python
df.tail()
```

```python
df.info()
```

```python
df.describe()
```

```python
df.to_numpy()
```

## Extracting information

```python
df["Name"].head()
```

```python
df[0:5]
```

```python
df.loc[:5, ["Name"]]
```

```python
type(df.loc[:5, ["Name"]])
```

```python
df.loc[:5, "Name"]
```

```python
type(df.loc[:5, "Name"])
```

```python
df.iloc[:5]
```

```python
df.iloc[4]
```

```python
type(df.iloc[4])
```

```python
df.iloc[:3, -2:]
```

```python
df[df["Pclass"] == 3]
```

```python
df["Pclass"] == 3
```

```python
df.head(1)
```

## Setting values

```python
df.at[0, "Age"]
```

```python
df.at[0, "Age"] = 10
```

```python
df.head(1)
```

```python
df.iat[0, 2] = 1
```

```python
df.head(1)
```

### Beware of referencing a dataframe!

```python
df2 = df
```

```python
df2.iat[0, 2] = 0
```

```python
df2.head(1)
```

```python
df.head(1)
```

```python
df.iat[0, 2] = 1
```

```python
df2.head(1)
```

```python
df.head(1)
```

### Use the .copy() function to solve this problem!

```python
df2 = df.copy()
```

```python
df2.iat[0, 2] = 0
```

```python
df2.head(1)
```

```python
df.head(1)
```

```python
df.iat[0, 2] = 2
```

```python
df.head(1)
```

```python
df2.head(1)
```

```python
df.iat[0, 2] = 1
```

```python
df.describe()
```

```python
df["Survived"].value_counts()
```

```python
df["Pclass"].value_counts()
```

```python
df["PassengerId"].plot()
```

```python
df["Survived"].value_counts().head(5).plot()
```

```python
df["Survived"].value_counts().head(5).plot(kind="bar")
```

```python
df["Pclass"].value_counts().plot(kind="bar")
```