import requests
from bs4 import BeautifulSoup
from database import add_books_to_table, add_genres_to_table
import time

""" My goal here is to go into the first URL, get that HTML data, find the second URL 
(this inlcudes all data about the book, not just serface level info) and pull book info from this URL instead

The first URL will gather the data for my genre table/parse the books per page, 
the second URL will gather data about each specific book
"""

# 'search_url' will be used to look through each book
# 'search_response' pulls data from the page with the list of books
# 'search_soup' is the HTML for 'search_url'
# 'book_urls' will be used to look at the specific url data tied to that book
# 'book_response' pulls data from the book url
# 'book_soup' is the HTML for each url in 'book_url'
search_url = "https://books.toscrape.com/"
search_response = requests.get(search_url)
search_soup = BeautifulSoup(search_response.text, "html.parser")
book_urls = [book.find('a')['href'] for book in search_soup.find_all('article', class_='product_pod')]

book_response = None
book_soup = None
title = None
price = None
rating = None
genre = None

books = [] # list of all books
genres = [] # list of all genres
"""
Now that ive gotten all my book url's, we need to pull info off of each book_url.
We want, Title, Price, Rating, Genre
I will also add 2 small functions: 
1, to strip units from price and 2, convert rating from string word to an int number
"""

# deletes the units
def clean_price(price):
    return float(price.replace("Â£",""))

# converts string words to int numbers
def clean_rating(rating_word):
    translation = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
    return translation.get(rating_word)

for url in book_urls:
    url = "https://books.toscrape.com/" + url
    book_response = requests.get(url)
    book_soup = BeautifulSoup(book_response.text, 'html.parser')
    title = book_soup.find('h1').get_text()
    price = book_soup.find('p', class_='price_color').get_text()
    price = clean_price(price)
    rating = book_soup.find('p', class_='star-rating')['class'][1]
    rating = clean_rating(rating)
    genre = book_soup.find("ul", class_="breadcrumb").find_all("a")[2].get_text()
    books.append({'title': title, 'price': price, 'rating': rating})
    genres.append({'genre': genre})
    
    
add_books_to_table(books)
add_genres_to_table(genres)


for book, genre in zip(books, genres):
    print(F"Title: {book['title']} | Price: {book['price']} | Rating: {book['rating']} | Genre: {genre['genre']}\n")
    



