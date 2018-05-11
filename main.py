import requests
from bs4 import BeautifulSoup

page = requests.get(
    "http://dataquestio.github.io/web-scraping-pages/simple.html")

soup = BeautifulSoup(page.content, 'html.parser')
# .prettify() : to print out the HTML content of the page, and format it nicelt
print(soup.prettify())


print("*"*50)
# .children => go one level deep
# returns a list generator/list_iterator object, so you need to call `list` to iterate through and evaluate and return a list
print(soup.children)
# list(list_iterator obejct) => return a type of `list``
print(list(soup.children))
# To find the type of each element in the list
typeOfEachElement = [type(item) for item in list(soup.children)]

# to select the `html` tag and its children by taking the third item in the list
html = list(soup.children)[2]
# To find the children inside the `html` tag
htmlChildren = list(html.children)
# To dive into the `body`
body = htmlChildren[3]
# To get/isolate the `p` tag
p = list(body.children)[1]
# once you have isolated the tag, can use `get_text` to extract all of the text inside the tag
print(p.get_text())
