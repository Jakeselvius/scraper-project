import sqlite3

# .fetchone() returns a 1 specified row as a tuple (ordered and unchangable value(s))
# .fetchall() returns all remaining rows of the last select statement 
# order of rows is:| BOOK_ID | TITLE | PRICE | RATING | GENRE_ID |
connection = sqlite3.connect('books.db') # opens the database
command = connection.cursor() # allows us to execute sql commands

# FIND HOW MANY BOOKS THERE ARE PER GENRE
def books_per_genre():
    connection = sqlite3.connect('books.db')
    command.execute(""" SELECT g.genre, COUNT(*) AS total_books
    FROM books b
    JOIN genres g
    ON b.genre_id = g.genre_id
    GROUP BY g.genre
    ORDER BY total_books DESC;""")
    books = command.fetchall()
    print("====================\nNumber-Of-Books-Per-Genre\n====================")
    for book in books:
        print(f"[Genre - {book[0]} | Price - £{book[1]}]\n{'-'*60}")
    connection.close()

# FIND THE AVG PRICE OF EACH BOOK PER GENRE
def avg_price_per_genre():
    connection = sqlite3.connect('books.db')
    command.execute("""SELECT g.genre, COUNT(*) AS total_books, AVG(b.price) AS average_price_per_genre
                    FROM books b
                    JOIN genres g
                    ON b.genre_id = b.genre_id
                    GROUP BY g.genre
                    ORDER BY b.price DESC """)
    books = command.fetchall()
    print("\n====================\nAvg Price-Of-Books-Per-Genre\n====================")
    for book in books:
        print(f"[Genre - {book[0]} | Quantity - {book[1]} | Avg Price - £{book[2]:.2f}]\n{'-'*60}")
    connection.close()

# FIND THE MOST EXPENSIVE BOOK PER GENRE
def max_price_per_genre():
    connection = sqlite3.connect('books.db')
    command.execute("""SELECT g.genre, MAX(b.price) AS most_expensive
                    FROM books b
                    JOIN genres g
                    ON b.genre_id = g.genre_id
                    GROUP BY g.genre
                     """)
    books = command.fetchall()
    print("\n====================\nMost-Expensive-Books-Per-Genre\n====================")
    for book in books:
        print(f"[Genre - {book[0]} | Most expensive - £{book[1]:.2f}]\n{'-'*60}")
    connection.close()


# FIND THE LEAST EXPENSIVE BOOK PER GENRE
def min_price_per_genre():
    connection = sqlite3.connect('books.db')
    command.execute("""SELECT g.genre, MIN(b.price) AS least_expensive
                    FROM books b
                    JOIN genres g
                    ON b.genre_id = g.genre_id
                    GROUP BY g.genre
                     """)
    books = command.fetchall()
    print("\n====================\nLease-Expensive-Books-Per-Genre\n====================")
    for book in books:
        print(f"[Genre - {book[0]} | Least expensive - £{book[1]:.2f}]\n{'-'*60}")
    connection.close()

# AVERAGE RATING OF EACH GENRE
def average_rating_per_genre():
    connection = sqlite3.connect('books.db')
    command.execute("""SELECT g.genre, AVG(b.rating) AS average_rating
                    FROM books b
                    JOIN genres g
                    ON b.genre_id = g.genre_id
                    GROUP BY g.genre
                     """)
    books = command.fetchall()
    print("\n====================\nLease-Expensive-Books-Per-Genre\n====================")
    for book in books:
        print(f"[Genre - {book[0]} | Average rating - {book[1]:.2f}]\n{'-'*60}")
    connection.close()

