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
                genre_id INTEGER,
                FOREIGN KEY (genre_id) REFERENCES genres(genre_id),
                CHECK (price >= 0)
                )
                """)

print("books table has been created!\n")
command.execute(""" CREATE TABLE IF NOT EXISTS genres
                (
                genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
                genre TEXT
                )
                """)
print("genre tabel has been created!\n")


# instert genre data into our genres table within the book database
def add_genres_to_table(all_genres):
    connection = sqlite3.connect('books.db')
    command = connection.cursor()

    unique_genres = set(all_genres)

    command.execute("DELETE FROM genres") # so we can run this multiple times and not overlap data
    command.execute("DELETE FROM sqlite_sequence WHERE name='genres'") # resets the auto counter back to 1

    for genre in unique_genres:
        command.execute("""
            INSERT INTO genres (genre)
            VALUES (?)
        """, (genre,))

    connection.commit()
    connection.close()

    print(f"Added {len(unique_genres)} genres to the genres table")

# instert book data into our books table within the book database
def add_books_to_table(all_books):
    connection = sqlite3.connect('books.db')
    command = connection.cursor()

    command.execute("DELETE FROM books")
    command.execute("DELETE FROM sqlite_sequence WHERE name='books'") # resets the auto counter back to 1

    for book in all_books:
        command.execute("""
            SELECT genre_id
            FROM genres
            WHERE genre = ?
        """, (book['genre'],))

        genre_id = command.fetchone()[0]

        command.execute("""
            INSERT INTO books (title, price, rating, genre_id)
            VALUES (?, ?, ?, ?)
        """, (book['title'], book['price'], book['rating'], genre_id))

    connection.commit()
    connection.close()

    print(f"Added {len(all_books)} books to the books table")

# for row in command.execute("""SELECT * FROM books b
#                            JOIN genres g
#                            on b.genre_id = g.genre_id
#                            WHERE g.genre_id = 1"""):
#     print(f"Genre ID: {row[0]} || Title: {row[1]}")

connection.commit()
connection.close()