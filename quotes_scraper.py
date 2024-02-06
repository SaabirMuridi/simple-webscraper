from bs4 import BeautifulSoup
import requests


def quotes_scraper(url):
    #variable will hold scraped content
    quotes = []
    while url:
        try:
            #request response from url
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            #content extraction from current page
            current_page_quotes = soup.select('.quote span.text')
            quotes.extend(current_page_quotes)

            #finds next page using the sites 'next' button
            next_page_link = soup.select_one('li.next a')
            url = next_page_link['href'] if next_page_link else None
        except Exception as e:
            print("Error:", e)
            break
            
    return quotes

if __name__ == "__main__":
    base_url = "https://quotes.toscrape.com/page/{}/"
    for page_number in range(1,4):
        url = base_url.format(page_number)
        quotes = quotes_scraper(url)
        print(f"Quotes from page {page_number}:")
        for quote in quotes:
            print("-", quote.text.strip())

