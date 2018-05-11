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

print("*"*50)
# What we did above was useful for figuring out how to navigate a page, but it took a lot of commands to do something fairly simple. If we want to extract a single tag, we can instead use the `find_all` method, which will find all the instances of a tag on a page.

# .find_all('p') => returns a list of find all the instances of a `p` on a page.
# p = [<p>Here is some simple content for this page.</p>]
all_p = soup.find_all('p')
# extractTextInP = ['Here is some simple content for this page.']
extractTextInP = [text.get_text() for text in all_p]

# .find() => return the first instance of a tag
# first_p = <p>Here is some simple content for this page.</p>
first_p = soup.find('p')


