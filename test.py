import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

st.write("Here's the table that shows 1000 top movie based on IMDB rating:")
df = pd.read_csv(r'C:\Users\abdur\My Data\Data Science\Personal Project\Movie Recomendation\Top 1000 IMDb movies_FIX.csv')

column = ["Title", "Genre", "Star", "Director" ]

st.write(df[column])
option = st.selectbox(
    'Select your favorite movie',
    df['Title']
    )

for feature in column:
    df[feature] = df[feature].fillna('')

def get_important_features(data):
    important_features = []
    for i in range(0, data.shape[0]):
        important_features.append(data['Star'][i]+' '+data['Director'][i]+' '+data['Genre'][i]+' '+data['Title'][i])
        
    return important_features

df['important_features'] = get_important_features(df)

cm = CountVectorizer().fit_transform(df['important_features'])

cs = cosine_similarity(cm)

title = option

movie_id = df[df['Title'] == title]['Movie ID'].values[0]

scores = list(enumerate(cs[movie_id]))

sorted_scores = sorted(scores, key = lambda x:x[1], reverse = True)

sorted_scores = sorted_scores[1:]

j = 0 

jmax = st.slider("No. Movie recomendation", 1, 20)

if st.button('Show The Recomendation'):
    'The',jmax, ' most recommended movies to', option, 'are :'
    for item in sorted_scores:
             movie_title = df[df['Movie ID'] == item[0]]['Title'].values[0]
             st.write(j+1, movie_title)
             j = j+1
             if j>jmax-1:
                 break