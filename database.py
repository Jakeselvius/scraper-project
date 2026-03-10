import sqlite3

# creates my 'books' database if it doesnt exist
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

# creates the books table and makes sure it doesnt already exist
cursor.execute("""
               CREATE TABLE IF NOT EXISTS books (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT NOT NULL,
               price REAL NOT NULL,
               rating INTEGER NOT NULL
               )
               """)
conn.commit()
conn.close()
print("Database created!")


def save_books_to_db(books):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM books") # clears old data so when I re-run i wont get duplicates

    for book in books:
        cursor.execute("""
                       INSERT INTO books (title, price, rating)
                       VALUES (?,?,?)
                    """, (book["title"], book["price"], book["rating"]))
    conn.commit()
    conn.close()
    print(f"Saved {len(books)} books to the database")
        