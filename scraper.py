import requests
from bs4 import BeautifulSoup

# LOOKIN AT THE GENERAL HTML STRUCTURE
# 'url' assigns the website we are looking at
# 'response' pulls the info from that website
# prints off their values and data
url = "https://books.toscrape.com" 
response = requests.get(url) 
#print(f"Status code = {response.status_code}") # hould be 200 if succesufl
#print(response.text[:500]) # prints the first 500 characters of HTML

"""========================================================================"""




# FINDING WHAT HTML TO LOOK FOR & PARSING HTML USING BeautifulSoup
# 'soup' looks through the HTML
# 'books' finds all book containers (each one has a <article> tag)
"""<article class="product_pod">
  <h3>
    <a href="..." title="A Light in the Attic">A Light in the Attic</a>
  </h3>
  <p class="price_color">£12.99</p>
  <p class="star-rating Three"></p>
</article>
"""
url = "https://books.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")
#print(soup.prettify())
#print(f"Found {len(books)} books on this page") # should print 20

"""========================================================================"""


# MAKING THE DATA LOOK NICE
def clean_price(price_text):
    return float(price_text.replace("Â£", ""))

def clean_rating(rating_word):
    rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    return rating_map.get(rating_word, 0)

"""========================================================================"""


# GETTING DATA FROM EACH INDIVIDUAL BOOK
# 'title' finds heading 'h3', then looks at 'a' where words = 'title'
# 'price_text' finds paragraph 'p' where class name = 'price color' and grabs the text
# rating_word finds paragraph 'p' where class name = 'star-rating' and grabs the last word of that
for book in books:
    title = book.h3.a['title']
    price_text = book.find('p', class_='price_color').text
    rating_word = book.find('p', class_='star-rating')['class'][1]
    print(f'{title} | {clean_price(price_text)} | {clean_rating(rating_word)}')
   
"""========================================================================"""

