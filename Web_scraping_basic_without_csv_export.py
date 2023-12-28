# Importing the necessary libraries

from bs4 import BeautifulSoup   # BeautifulSoup is a library for pulling data out of HTML and XML files.
import requests                 # Requests is a simple HTTP library for making requests to URLs.

scrape_page = requests.get("http://quotes.toscrape.com")      # Making a GET request to the specified URL
page = BeautifulSoup(scrape_page.text, "html.parser") # Creating a BeautifulSoup object to parse the HTML content

# Extracting all the quotes from the page using the specified HTML element and class attribute
quotes = page.findAll("span", attrs={"class": "text"})

# Extracting all the authors from the page using the specified HTML element and class attribute
authors = page.findAll("small", attrs={"class": "author"})

# Iterating through the extracted quotes and authors using a zip function
for quote, author in zip(quotes, authors):
    print(quote.text + " - " + author.text)          # Printing each quote and its corresponding author to the console

