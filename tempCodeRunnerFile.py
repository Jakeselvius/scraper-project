    for book, genre in zip(all_books, all_genres):
        print(F"Title: {book['title']} | Price: {book['price']} | Rating: {book['rating']} | Genre: {genre}\n")
        