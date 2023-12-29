# Importing the necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import csv                             # CSV module provides functionality to both read from and write to CSV files.

driver = Service('C:/Users/12267/chromedriver.exe')     # Setting up the ChromeDriver service
page = webdriver.Chrome(service=driver)                 # Creating a Chrome WebDriver instance
page.get("http://quotes.toscrape.com")                  # Opening the target website

page.find_element(By.LINK_TEXT, "Login").click()  # Clicking on the "Login" link
time.sleep(3)                                           # Pausing execution for 3 seconds to allow the page to load

# Locating username and password fields, and entering values
username = page.find_element(By.ID, "username")
password = page.find_element(By.ID, "password")
username.send_keys("admin")
my_password = input("Enter Password as 1234 ")
password.send_keys(my_password)

page.find_element(By.CSS_SELECTOR, "input.btn-primary").click()  # Clicking the login button



# Extracting all the quotes from the page using the specified HTML element and class attribute
quotes = page.find_elements(By.CLASS_NAME, "text")
# Extracting all the authors from the page using the specified HTML element and class attribute
authors = page.find_elements(By.CLASS_NAME, "author")


file = open("scraped_quotes1.csv", "w")                         # Opening a CSV file in write mode
csv_writer = csv.writer(file)                                  # Creating a CSV writer object
csv_writer.writerow(["QUOTES", "AUTHORS"])                     # Writing the header row to the CSV file

# Iterating through the extracted quotes and authors using a zip function
for quote, author in zip(quotes, authors):
    print(quote.text + " - " + author.text)          # Printing each quote and its corresponding author to the console
    csv_writer.writerow([quote.text, author.text])   # Writing each quote and its corresponding author to the CSV file
file.close()                                         # Closing the CSV file
