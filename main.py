import requests
from bs4 import BeautifulSoup

page = requests.get(
    "http://dataquestio.github.io/web-scraping-pages/simple.html")

soup = BeautifulSoup(page.content, 'html.parser')
# .prettify() : to print out the HTML content of the page, and format it nicelt
print(soup.prettify())
