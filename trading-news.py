from selenium import webdriver
from time import sleep
import re

# Initialise browser and specify login details
browser = webdriver.Chrome(executable_path=r"YOUR PATH TO \chromedriver.exe")
browser.implicitly_wait(10)
username = "USERNAME"
password = "EMAIL"


# Open Trading212 and login
browser.get('https://live.trading212.com/')

username_field = browser.find_element_by_name("login[username]")
username_field.send_keys(username)
username_field = browser.find_element_by_name("login[password]")
username_field.send_keys(password)
login_button = browser.find_element_by_class_name("button-login")
login_button.click()
sleep(6) # wait for page to l load html

#Annoying pop up on Trading212 Invest
browser.maximize_window()

continue_button = browser.find_element_by_class_name("custom-button")
continue_button.click()

# Get page HTML source
source = browser.page_source


#Annoying trading212 pop up 
continue_button = browser.find_element_by_class_name("custom-button")
continue_button.click()

# Find regex, for any stock
stock_regex = re.compile(r'<td data-column-id="name" class="name">[a-zA-Z ]+')
holdings = stock_regex.findall(source)

# Extract name of stock from html
stocks = []
for holding in holdings:
    stock = holding.replace('<td data-column-id="name" class="name">', "")
    stocks.append(stock)


for stock in stocks:

    browser.execute_script('''window.open("https://www.google.com/search?q={} news","_blank");'''.format(stock))

