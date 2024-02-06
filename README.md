#simple-webscraper

Quotes Scraper:
This python script 'quotes.scraper' is designed to scrape quotes from the website https://quotes.toscrape.com/. It is a multi-page quote scraper that scrapes the first three pages of quotes from the website. It utilizes BeautifulSoup for parsing and requests for making website requests.

Requirements:
- Python3
- BeautifulSoup
- requests

Script Details:
- The quotes_scraper function in the script takes a url as an input and scrapes quotes from multiple pages using a while loop.
- The function also handles parsing or request errors.
- The extracted quotes are printed in the console along with the page numbers thanks to the for loop used in the main body made to go through the first three pages while formatting the output.