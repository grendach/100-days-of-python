from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text
# print(website_html)
soup = BeautifulSoup(website_html, "html.parser")
# section_heading = soup.find(name="h3", class_="jsx-4245974604")
all_movies = soup.find_all(name="h3", class_="title") # not working with new version of site

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]
with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write()