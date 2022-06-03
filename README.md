# Python Movie Recomendation System
* Creating a movie recomendation system using python.
* Scraped 1000 movie list from imdb using BeautifulSoup.
* Make recomendation system based on Movie Title, Genre, Cast, and Director.
* Built a Web App using streamlit.

# Code and Resource Used
* **Python Version:** 3.9.7
* **Packages:** pandas, numpy, sklearn, bs4, streamlit
* **Scraper Github:** https://github.com/Reljod/Python-Data-Scraping-IMDb-Movie-site-using-BeautifulSoup-Series-1-
* **Movie Recomendation System:** https://www.youtube.com/watch?v=ueKXSupHz6Q
* **Streamlit Production:** https://docs.streamlit.io/library/get-started

# Web Scraping
I'm using a Web Scrap github repo from the link above to scrap top 1000 movie title from IMDB. From each movie I got the following:
* Movie ID
* Title
* Year of Realase
* Watch Time
* Genre
* Director
* Star
* Movie Rating
* Votes
* Description

# Data Cleaning
After scraping the data above I cleaned it up. I made the following changes and created the following variables:
* Grouping a column consist of the data that will be used for model building:
* * Title
* * Genre
* * Cast
* * Director
* Check for any missing value from the column above
* Fill the missing value if any using fillna('')

# Building Recomendation System
First I transform a column that has been grouped to vector using CountVectorizer from sklearn library. This will transform text from the column to integer type data. It will identify all the text from each column and count it.

Then I'm building the recomendation system using cosine_similarity. With this library I'm try to match a movie selection with text from the column above.

# Productionization
In this step I build a streamlit web app. The app take the movie of your choice and the number of movie that you want to be recomended.

