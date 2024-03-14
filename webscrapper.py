import requests
from bs4 import BeautifulSoup

# URL of the IMDb website
url = 'https://www.imdb.com/chart/top/'

# Send a GET request to the URL
response = requests.get(url)
print(response)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the movie titles and ratings
movies = soup.find_all('td', class_='titleColumn')
ratings = soup.find_all('td', class_='ratingColumn imdbRating')

# Extract and print movie titles and ratings
for movie, rating in zip(movies, ratings):
    title = movie.a.text
    rating_value = rating.strong.text
    print("Movie: {} | Rating: {}".format(title, rating_value))