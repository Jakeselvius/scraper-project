# import sqlite3

# # .fetchone() returns a 1 specified row as a tuple (ordered and unchangable value(s))
# # .fetchall() returns all remaining rows of the last select statement 
# # order of rows is: TITLE | PRICE | RATING


# connection = sqlite3.connect("books.db")
# cursor = connection.cursor()

# # --- Query 1: How many books do we have? ---
# cursor.execute("""SELECT COUNT(*) FROM BOOKS""")
# count = cursor.fetchone()[0]  # retrieves the data from the first position in the row we selected
# print(f"Total books: {count}")


# # --- Query 2: What is the average price? ---
# cursor.execute("""SELECT AVG(PRICE) FROM BOOKS""")
# avg_price = cursor.fetchone()[0]
# print(f"Average price: £{avg_price:.2f}")

# # --- Query 3: Top 5 cheapest books with 5 stars ---
# cursor.execute("""SELECT TITLE, PRICE, RATING 
#                FROM BOOKS 
#                WHERE RATING = 5 
#                ORDER BY PRICE ASC
#                LIMIT 5
#                """)
# results = cursor.fetchall()
# print("\nTop 5 cheapest 5-star books:")
# for row in results:
#     print(f"{row[0]} - £{row[1]:.2f}")

# # --- Query 4: Average price by rating ---
# cursor.execute("""SELECT RATING, AVG(PRICE) AS ave_price, COUNT(*) AS count
#                 FROM BOOKS
#                GROUP BY RATING 
#                ORDER BY RATING DESC
#                """)
# results = cursor.fetchall()
# print("Average price by star rating: ")
# for row in results:
#     print(f"{row[0]} stars: £{row[1]:.2f} avg ({row[2]} books)")

# connection.close()