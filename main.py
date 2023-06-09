from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
response.raise_for_status()
markup = response.text

soup = BeautifulSoup(markup, "html.parser")
movies = soup.select(".listicle-item picture img")
titles = [f"{index+1}) {movie.get('alt')}" for index, movie in enumerate(movies[::-1])]
#print(titles)

with open("movies.txt", mode="w") as file:
    for movie in titles:
        file.write(f"{movie}\n")