print(f"Total books collected: {len(all_books)}")
for book in all_books:
    print("================================================================\n")
    print(f"Title: {book["title"]} | Price: {book["price"]} | Rating: {book['rating']}\n")
print("================================================================\n")