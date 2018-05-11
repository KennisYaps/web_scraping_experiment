import requests
from bs4 import BeautifulSoup

ids_classes_page = requests.get(
    "http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")

soup = BeautifulSoup(ids_classes_page.content, 'html.parser')
print(soup.prettify())
print("-"*100)
# Search for any `p` tag that has the "class outer-text":
p_class_outerText = soup.find_all('p', class_="outer-text")

# Search for any tag that has the "class outer-text":
outerText = soup.find_all(class_="outer-text")

# search for elements by id
id_first = soup.find_all(id="first")
print(id_first)
