title = "The Great Gatsby"
price = 12.99
rating = 4
in_stock = True

books = ["Gatsby", "1984", "Dune"]
prices = [12.99, 8.50, 15.00]
books.append("Hobbit")

print("=====================================================\n")
for book in books:
    print(book)


book_dict = {"title": "Hobbit", "price": 8.50, "rating": 5}
print(book_dict["title"])
print(book_dict["price"])

all_books = [
    {"title":"Hobbit", "price": 8.50, "rating": 5},
    {"title": "Dune", "price": 15.00, "rating": 4},
    {"title": "Gatsby", "price": 12.99, "rating": 3}
]

# Loops through every book in 'all_books' and prints its info
for book in all_books:
    print(f"Book: {book['title']}, Price: {book['price']}, Rating: {book['rating']}")




def greet_user(name):
    message = "Hello, " + name + "!"
    return message

result = greet_user("Jake")
print(result + '\n')

# returns a dictionary of the book we made
def create_book(title, price, rating) -> dict: 
    return {"title": title, "price": price, "rating": rating}

# print out our book
def print_book(book) ->str:
    print(f" {book['title']} - ${book['price']} - Rating: {book['rating']}/5")

books = [
    create_book("The Hobbit", 9.99, 5),
    create_book("Dune", 15.00, 4),
    create_book("Harry Potter", 8.50, 5),
    create_book("Gatsby", 12.99, 3),
    create_book("Brave New World", 7.25, 4)
]
print("=====================================================")
print("\nAll books")
for book in books:
    print_book(book)

print("\n=====================================================")
# Find the chepest book
cheapest = min(books, key=lambda b: b["price"]) # lamda: referene to books, look at price
total = sum(price["price"] for price in books)
average = total / len(books)

print(f"\nCheapest: {cheapest['title']} - ${cheapest['price']:.2f}")
print(f"Average Price: ${average:.2f}\n")
print("=====================================================")
