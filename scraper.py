import requests
from bs4 import BeautifulSoup

# LOOKIN AT THE GENERAL HTML STRUCTURE
# 'url' assigns the website we are looking at
# 'response' pulls the info from that website
# prints off their values and data
url = "https://books.toscrape.com" 
response = requests.get(url) 
print(f"Status code = {response.status_code}") # hould be 200 if succesufl
print(response.text[:500]) # prints the first 500 characters of HTML

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
print(f"Found {len(books)} books on this page") # should print 20

"""========================================================================"""



