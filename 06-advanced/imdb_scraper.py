"""
IMDB Top 250 Movies Scraper — Learning Web Scraping
Author: Gökhan Arda Borulu
Topic: Web Scraping, BeautifulSoup, Requests, HTML Parsing

Scrapes IMDB's Top 250 movies page and filters by rating.
Demonstrates web scraping with requests and BeautifulSoup.

Note: IMDB may change their HTML structure over time.
      This is an educational exercise in web scraping concepts.
"""

import requests
from bs4 import BeautifulSoup


def scrape_imdb_top_movies(min_rating: float) -> None:
    """Scrape IMDB Top 250 and print movies above the given rating."""
    url = "http://www.imdb.com/chart/top"

    try:
        response = requests.get(url, timeout=15)
        soup = BeautifulSoup(response.content, "html.parser")

        titles = soup.find_all("td", {"class": "titleColumn"})
        ratings = soup.find_all("td", {"class": "ratingColumn imdbRating"})

        found = 0
        for title_tag, rating_tag in zip(titles, ratings):
            title = title_tag.text.strip().replace("\n", " ")
            rating = rating_tag.text.strip().replace("\n", "")

            try:
                if float(rating) > min_rating:
                    found += 1
                    print(f"⭐ {rating} — {title}")
            except ValueError:
                continue

        print(f"\n📊 {min_rating} üzerinde {found} film bulundu.")

    except requests.RequestException as e:
        print(f"❌ Bağlantı hatası: {e}")


if __name__ == "__main__":
    print("=" * 40)
    print("  🎬 IMDB TOP 250 FILM ARAMA")
    print("=" * 40)

    try:
        threshold = float(input("Minimum rating giriniz (örn: 8.5): "))
        scrape_imdb_top_movies(threshold)
    except ValueError:
        print("Lütfen geçerli bir rating giriniz.")
