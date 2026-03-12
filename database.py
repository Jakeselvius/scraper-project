import sqlite3

"""First step is to create a connection to an existing db
if none exist, the name inputted will be cerated as one"""

connection = sqlite3.connect('books.db') # connects to existing db, creates one of none exist
command = connection.cursor() # this allows us to run a command like CREATE TABLE, INSERT, UPDATE etc...

"""Now lets create 2 tables, 1 for book data containing book_id, title, price, rating
and a 2nd table that holds book_id, genre, total_per_genre"""
command.execute(""" CREATE TABLE IF NOT EXISTS books (
                book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                price REAL,
                rating INTEGER,
                CHECK (price >= 0)
                )
                """)

print("books table has been created!\n")
command.execute(""" CREATE TABLE IF NOT EXISTS genres
                (
                book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                genre TEXT
                )
                """)
print("genre tabel has been created!\n")


# instert book data into our books table
def add_books_to_table(all_books):
    connection = sqlite3.connect('books.db')
    command = connection.cursor()

    command.execute(""" DELETE FROM books """) #delete any existing data so we can re-run the progeram
    command.execute("DELETE FROM sqlite_sequence WHERE name='books'")
    
    for book in all_books:
        command.execute(""" INSERT INTO books 
                        (title, price, rating)
                        VALUES (?,?,?)
                        """, (book['title'], book['price'], book['rating']))
    connection.commit()
    connection.close()
    print(f"Added {len(all_books)} books to the 'books' table")

def add_genres_to_table(all_genres):
    connection = sqlite3.connect('books.db')
    command = connection.cursor()

    command.execute("""DELETE FROM genres""")
    command.execute("DELETE FROM sqlite_sequence WHERE name='genres'") # resets the autoincrement id back to 1 
    for genre in all_genres:
        command.execute(""" INSERT INTO genres
                        (genre)
                        VALUES (?) 
                        """, (genre['genre'],))
    connection.commit()
    connection.close()
    print(f"Added {len(all_genres)} to the genres table")

# for row in command.execute("""SELECT * FROM genres"""):
#     print(row)

# connection.commit()
# connection.close()