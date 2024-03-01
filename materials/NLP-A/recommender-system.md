---
title: "NLP based recommender-system"
collection: teaching
type: "M.Sc course"
permalink: /materials/NLP-A/recommender-system
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2024-02-27
location: "Debrecen, Hungary"
---

# [Recommender System](https://www.kaggle.com/code/aishwaryasharma1992/recommender-system-using-huggingface-library#%F0%9F%8D%BF-The-Age-of-Recommendation-Systems)

```python
!pip install sentence-transformers
!pip install datasets
```

## Imports


```python
import ast # Importing this library for reading a column as dict, list instead of str
import pandas as pd
import seaborn as sns
from datasets import load_dataset
from sentence_transformers import util
from sentence_transformers import SentenceTransformer
```

## Load movie data

```python
movies = load_dataset("AiresPucrs/tmdb_5000_movies")
movies = pd.DataFrame(movies['train'])
movies.head()
```

```python
# Reading the file columns as lists & dictionaries instead of pandas DF
columns = ['genres','keywords','production_companies','production_countries','spoken_languages']
movies[columns] = movies[columns].applymap(lambda x : ast.literal_eval(str(x)))
```

```python
# Creating a function to extract the relevant data
def get_data(x, cols, dict):
    for col in cols:
        for i in range(len(x[col])):
            for j in range(len(x[col][i])):
                x[col][i][j] = x[col][i][j][dict]
    return x


movies = get_data(movies, columns,'name')
```

```python
# Converting multiple columns to numeric
numeric_columns = ['budget','id','popularity','revenue','runtime','vote_average','vote_count']
movies[numeric_columns] = movies[numeric_columns].apply(pd.to_numeric, errors = 'coerce')

movies.head(5)
```

## Credit data to movies

```python
credits = pd.read_csv("https://raw.githubusercontent.com/andandandand/CSV-datasets/master/tmdb_5000_credits.csv")
credits.head()
```


## Joining the Movies and Credits Dataset

```python
movies = pd.merge(movies, credits[['movie_id','cast', 'crew']],  left_on= "id", right_on = "movie_id", how = "left")
movies['overview'] = movies['overview'].astype(str)
movies.head()
```

## Exploratory Data Analysis

```python
# Finding the top 10 grossing movies in this dataset
# Before we can do that we will need to adjust the revenue numbers with inflation
import plotly.express as px

px.bar(movies.sort_values("revenue", ascending = False).head(10).reset_index(),
       x = "original_title",
       y = "revenue",
       title = "Highest Grossing Movies",
       color = "original_title",
       labels = {"original_title":"Movie Name","revenue":"Revenue (USD $)"})
```

```python
cor = movies.drop(["id","movie_id"], axis = 1).corr()

ax = sns.heatmap(
    cor,
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True,
    annot=True,
    annot_kws={"size": 12}
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
);
```

```python
movies["ROI"] = movies["revenue"]/movies["budget"]

movies[(movies["budget"] > 1000) & (movies["vote_count"] >500)].sort_values("ROI", ascending = False).head(10).reset_index()

px.line(movies[(movies["budget"] > 1000) & (movies["vote_count"] >500)].sort_values("ROI", ascending = False).head(20).reset_index(),
        x = "original_title",
        y = "ROI",
        title = "Movies with highest ROI",
        labels = {"original_title":"Movie Name","ROI":"ROI (USD $)"})
```

## Exploring relationships of Genres with Revenue & Ratings

```python
# Creating a function to find the relationship between genres and other different parameters
def genre_rshp(param, n):
    #We'll be only considering the Top n movies which have performed well either on the basis of revenue or ratings
    high = movies[movies["vote_count"] > 500].sort_values(param, ascending = False).head(n).reset_index()["genres"]
    high = high.apply(lambda x : ' '.join(x))
    # Split the strings into individual words and store them in a list
    words = []
    for row in high:
        words.extend(row.split())
    # Count the occurrences of each word using a dictionary
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    #Sorting the dictionary on the basis of genre occurences
    sorted_dict = dict(sorted(word_counts.items(), key=lambda x: x[1], reverse=True))
    # Creating a new pandas DataFrame with first five key-value pairs and sum of last six values
    new_df = pd.DataFrame(columns=['Genre', 'Count'])
    other = 0
    count = 0
    for key, value in sorted_dict.items():
        if count <= 5:
            new_df = new_df.append({'Genre': key, 'Count': value}, ignore_index=True)
            count += 1
        else:
            other += value
    new_df = new_df.append({'Genre': 'Other', 'Count': other}, ignore_index=True)
    fig = px.pie(new_df, values='Count', names='Genre',
             title= "Top generes related to the highest " + param)
    return fig

#Exploring the relationship of genres alongside revenue
fig2 = genre_rshp("revenue", 200)
fig2.show()
```

```python
#Exploring the relationship of genres alongside vote avergae/ movie rating
fig3 = genre_rshp("vote_average", 200)

fig3.show()
```

```python
#Exploring the relationship of genres alongside popularity metric
fig4 = genre_rshp("popularity", 200)

fig4.show()
```

## Function to Find Movies with Similar Overview

```python
# Loading the model for performing sentence similarity
model = SentenceTransformer('all-MiniLM-L6-v2')
overview_embeddings = model.encode(movies['overview'], show_progress_bar=True)

# Compute cosine similarity between all pairs
overview_cos_sim = util.cos_sim(overview_embeddings, overview_embeddings)
```

```python
def recommender(movie_name):
    result = pd.concat([movies["original_title"],
                        pd.DataFrame(overview_cos_sim[:,movies[movies["original_title"] == movie_name].index].numpy(),
                                     columns=['Overview'])],
                       axis = 1)
    result = result[result["Overview"] != 1]
    result = result.sort_values('Overview', ascending= False).head(10).reset_index(drop =  True)
    return result

recommender("The Dark Knight")
```

```python
recommender("Casino Royale")
```

```python
recommender("Shutter Island")
```

```python
recommender("My Name Is Khan")
```

```python
from IPython.display import YouTubeVideo
YouTubeVideo('u1xrNaTO1bI')
```