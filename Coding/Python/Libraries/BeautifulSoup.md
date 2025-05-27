---
color: var(--mk-color-teal)
sticker: lucide//soup
tags:
  - py-libraries
---
`pip install beautifulsoup4` - Specialized web scraping library

Quick access:
[[BeautifulSoup#Basic HTML parsing|Basic HTML parsing]]
[[BeautifulSoup#Find all command|Find all command]]
[[BeautifulSoup#Print the visible output of a tag only|Print the visible output of a tag only]]
[[BeautifulSoup#Get a specific attribute|Get a specific attribute]]

### Basic HTML parsing
~~~python
import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
print(soup)
~~~
`BeautifulSoup` relies on the [[Coding/Python/Libraries/requests]] library to get HTML data, which it can then parse using `html.parser`. We can directly print that data or use `print(soup.prettify())`, which adds indentation to make our HTML more readable.

### Find all command
`soup.find_all("tag", {"class":"value"})` - Finds all tags which *have a class with a certain value.* For example: `myLinks = soup.find_all("a", {"class":"css-1m051bw"})` will create a list of all `<a>` tags which have the class `css-1m051bw`.

### Print the visible output of a tag only
`variable.text` - Outputs the part of the tag that the user can see on the website. Useful for extracting only the user's preview of a link. 

### Get a specific attribute
`tag.get('href')` - Will get the value of the `href` tag from the `tag` variable. This can be used for any other attribute too.