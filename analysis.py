import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# load our book database into the pandas dataframe
connection = sqlite3.connect("books.db")
df = pd.read_sql_query("SELECT * FROM BOOKS", connection) # df means dataframe
connection.close()

# # displaying the data
# print(df.head()) # prints the first 5 rows if not specified how many in the ()
# print(df.shape) # this prints out (number of rows, number of columns)
# print(df.describe()) # prints off mathmatical facts about the data
# print(df.dtypes) # this prints off the data type for each row

"""============================================================"""

# messing around with queries using some core Pandas Methods

# count all occurrences of '--insert what you want to count--' with .value_counts
#print(f"Number of specific star ratings:\n{df['rating'].value_counts()}")

# Aggregate queries using Pandas groupby() method
avg_by_rating = df.groupby('rating')['price'].mean()
# print(f"\nAverage price by rating:{avg_by_rating}\n")

# summary of multiple aggregate functions at once
def summary_of_aggregates():
    print(f"\nSummary of multiple aggregate functions at once:\n")
    sumamry = df.groupby('rating').agg(
        total_books = ('title', 'count'),
        avg_price = ('price', 'mean'),
        max_price = ('price', 'max')
    )
    print(sumamry)


# sorting values by column with sort_values()

#cheapest books first
cheapest = df.sort_values('price').head(10)
# print(f"\n========== Top 10 Cheapest books: =========== \n{cheapest[['title', 'price', 'rating']]}")

#most expensive books first
most_expensive = df.sort_values('price', ascending=False).head(10)
# print(f"\n========== Top 10 Most Expensive books: =========== \n{most_expensive[['title', 'price', 'rating']]}")

# Filering rows with conditions

#books with 5 star rating
five_stars = df[df['rating'] == 5] # need nested otherwise it returns True or False
#print(f"\n\n========== Books with 5-star ratings: ==========\n {five_stars}")

#books under £10 
cheap = df[df['price'] < 15.0]
#print(f"\n\n========== Books Under £15: ==========\n {cheap}")

# combining conditional statements
affordable_good_book = df[(df['price'] < 15.0) & (df['rating'] >= 4)]
#print(f"\n\n========== Books Under £15 with at least a 4 star rating: ==========\n {affordable_good_book}")

"""============================================================"""

# Creating charts from the dataset above

#creating a bar chart
def bar_chart_avg_price_by_rating():

    plt.figure(figsize=(8, 5))
    bars = plt.bar(avg_by_rating.index, avg_by_rating.values, color="blue", edgecolor="white")

    #creating the labels and title
    plt.xlabel("Star Rating Out Of 5", fontsize=12)
    plt.ylabel("Average Price (£)", fontsize=12)
    plt.title("Average Book Price by Star Rating", fontsize=14, fontweight="bold")
    plt.xticks([1,2,3,4,5])

    #adding value labels on top of each bar
    for bar, val in zip(bars, avg_by_rating.values):
        plt.ylabel("Average Price (£)", fontsize=12)
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, f"{val:.2f}", ha="center", va="bottom", fontsize=10)

    #plt.tight_layout()
    plt.savefig("Bar_chart_price_by_rating.png", dpi=150)
    plt.show()
    print("Bar chart saved as Bar_chart_price_by_rating.png")

# Creating a Histogram chart
def histogram_price_distribution():

    plt.figure(figsize=(8, 5))
    plt.hist(df['price'], bins=20, color='blue', edgecolor='white', alpha=0.85)

    plt.xlabel('Price (£)', fontsize=12)
    plt.ylabel('Number of Books', fontsize=12)
    plt.title('Distribution of Book Prices', fontsize=14, fontweight="bold")

    #add a vertical line at the average price
    avg = df['price'].mean()
    plt.axvline(avg, color='red', linestyle='--', linewidth=2, label=f'Mean:£{avg:.2f}')
    # plt.legend()

    plt.savefig("Histogram_chart_showing_price_distribution.png", dpi=150)
    plt.show()
    print("Histogram_chart_showing_price_distribution.png")




# print(book_data["genre"].value_counts()) # prints out the number of books in each genre to the terminal

# print(data.head())
# print(data.shape)
# print(data.describe())
# print(data.dtypes)
def scatter_plot_rating_by_genre():

    connection = sqlite3.connect('books.db')
    command = connection.cursor()
    book_data = pd.read_sql_query("""SELECT b.book_id, b.title, b.price, b.rating, g.genre
                            FROM books b
                            JOIN genres g
                            on b.genre_id = g.genre_id
                            """, connection)
    connection.close()

    scatter_plot = book_data.plot(title = "Number Of Star Rating by Genre", kind = 'scatter', x = 'rating', y = 'genre') 
    scatter_plot.get_figure().savefig("Scatter_plot_showing_rating_by_genre.png", dpi=150)
    plt.show()
    print("Scatter plot saved as Scatter_plot_showing_rating_by_genre.png")
