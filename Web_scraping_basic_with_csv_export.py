# Importing the necessary libraries

from bs4 import BeautifulSoup   # BeautifulSoup is a library for pulling data out of HTML and XML files.
import requests                 # Requests is a simple HTTP library for making requests to URLs.
import csv                      # CSV module provides functionality to both read from and write to CSV files.


scrape_page = requests.get("http://quotes.toscrape.com")      # Making a GET request to the specified URL
page = BeautifulSoup(scrape_page.text, "html.parser") # Creating a BeautifulSoup object to parse the HTML content

# Extracting all the quotes from the page using the specified HTML element and class attribute
quotes = page.findAll("span", attrs={"class": "text"})

# Extracting all the authors from the page using the specified HTML element and class attribute
authors = page.findAll("small", attrs={"class": "author"})


file = open("scraped_quotes.csv", "w")                         # Opening a CSV file in write mode
csv_writer = csv.writer(file)                                  # Creating a CSV writer object
csv_writer.writerow(["QUOTES", "AUTHORS"])                     # Writing the header row to the CSV file

# Iterating through the extracted quotes and authors using a zip function
for quote, author in zip(quotes, authors):
    print(quote.text + " - " + author.text)          # Printing each quote and its corresponding author to the console
    csv_writer.writerow([quote.text, author.text])   # Writing each quote and its corresponding author to the CSV file
file.close()                                         # Closing the CSV file

