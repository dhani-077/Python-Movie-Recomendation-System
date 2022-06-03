#importing the libraries needed 
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

#Declaring the headers 
headers = {"Accept-Language": "en-US,en;q=0.5"}

#Make Movie ID
ids = np.arange(0,1000)
movie_id = []
for y in ids:
    movie_id.append(int(y))

#declaring the list of empty variables, So that we can append the data overall

movie_name = []
year = []
time=[]
ganre=[]
rating=[]
metascore =[]
directors = []
stars = []
votes = []
gross = []
description = []

#creating an array of values and passing it in the url for dynamic webpages
pages = np.arange(1,1000,100)

#the whole core of the script
for page in pages:
    page = requests.get("https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start="+str(page)+"&ref_=adv_nxt")
    soup = BeautifulSoup(page.text, 'html.parser')
    movie_data = soup.findAll('div', attrs = {'class': 'lister-item mode-advanced'})
    for store in movie_data:
        name = store.h3.a.text
        movie_name.append(name)
        
        year_of_release = store.h3.find('span', class_ = "lister-item-year text-muted unbold").text
        year.append(year_of_release)
        
        runtime = store.p.find("span", class_ = 'runtime').text
        time.append(runtime)
        
        movie_genre = store.find("span", class_ = 'genre').text.rstrip().replace('\n', '').split(",")
        movie_genre = ''.join(map(str,movie_genre))
        ganre.append(movie_genre)
        
        rate = store.find('div', class_ = "inline-block ratings-imdb-rating").text.replace('\n', '')
        rating.append(rate)
        
        meta = store.find('span', class_ = "metascore").text if store.find('span', class_ = "metascore") else "****"
        metascore.append(meta)
        
        nama = store.find('p', attrs = {'class': ""})
        try:
            actor = nama.text.replace('\n',"").split("|")
            actor = [x.strip() for x in actor]
            actor = [actor[i].replace(j, "") for i,j in enumerate(["Director:", "Stars:"])]
            directors.append(actor[0])
            aktor = [x.strip() for x in actor[1].split(",")]
            aktor = ' '.join(map(str,aktor))
            stars.append(aktor)
        except:
            actor = nama.text.replace("\n","").strip()
            directors.append(np.nan)
            aktor = [x.strip() for x in actor.split(",")]
            aktor = ' '.join(map(str,aktor))
            stars.append(aktor)
        
        value = store.find_all('span', attrs = {'name': "nv"})
        
        vote = value[0].text
        votes.append(vote)
        
        grosses = value[1].text if len(value)>1 else '%^%^%^'
        gross.append(grosses)
        
        describe = store.find_all('p', class_ = 'text-muted')
        description_ = describe[1].text.replace('\n', '') if len(describe) >1 else '*****'
        description.append(description_)
        
#creating a dataframe 
movie_list = pd.DataFrame({ "Movie ID": movie_id, "Title": movie_name, "Year of Release" : year, "Watch Time": time, "Genre": ganre, "Director": directors, "Star": stars, "Movie Rating": rating, "Meatscore of movie": metascore, "Votes" : votes, "Gross": gross, "Description": description  })
movie_list.to_csv("Top 1000 IMDb movies_FIX.csv",index=False)
