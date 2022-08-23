from bs4 import BeautifulSoup
import requests

URL = "https://www.timeout.com/film/best-movies-of-all-time"

response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
all_movies = soup.find_all(name="h3", class_="_h3_cuogz_1") # not working with new version of site


movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.writelines(movie+"\n")
