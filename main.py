from scraper import scrape_page
from queries import *
from analysis import *


if __name__ == "__main__":
    bar_chart_avg_price_by_rating()
    histogram_price_distribution()
    scatter_plot_rating_by_genre()
    # scrape_page(1)
    # books_per_genre()
    # avg_price_per_genre()
    # max_price_per_genre()
    # min_price_per_genre()
    # average_rating_per_genre()