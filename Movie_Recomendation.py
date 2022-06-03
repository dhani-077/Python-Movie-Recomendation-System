import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv("Top 1000 IMDb movies.csv")

column = ["Star", "Director", "Genre", "Title"]

def get_important_features(data):
    important_features = []
    for i in range(0, data.shape[0]):
        important_features.append(data['Star'][i]+' '+data['Director'][i]+' '+data['Genre'][i]+' '+data['Title'][i])
        
    return important_features

df['important_features'] = get_important_features(df)

cm = CountVectorizer().fit_transform(df['important_features'])

cs = cosine_similarity(cm)

title = 'The Shawsank Redemption'

movie_id = df[df.Title == title]['Movie ID'].values[0]

scores = list(enumerate(cs[movie_id]))

sorted_scores = sorted(scores, key = lambda x:x[1], reverse = True)

sorted_scores = sorted_scores[1:]

j = 0

print('The 7 most recommended movies to', title, 'are:\n')
for item in sorted_scores:
    movie_title = df[df['Movie ID'] == item[0]]['Title'].values[0]
    print(j+1, movie_title)
    j = j+1
    if j>6:
        break
