from selenium import webdriver
from time import sleep
import re
import sys

# Initialise browser and specify login details
browser = webdriver.Chrome(executable_path=r"D:\Projects\Trading\chromedriver.exe")
browser.implicitly_wait(10)
username = "USERNAME"
password = "PASSWORD"


# Open Trading212 and login
browser.get('https://live.trading212.com/')

username_field = browser.find_element_by_name("login[username]")
username_field.send_keys(username)
username_field = browser.find_element_by_name("login[password]")
username_field.send_keys(password)
login_button = browser.find_element_by_class_name("button-login")
login_button.click()
sleep(6) # wait for page to l   oad html

#Annoying pop up on Trading212 Invest
browser.maximize_window()


# Get page HTML source
cfd = "accountTradingType: 'CFD',"
source = browser.page_source


#Find out of invest or CFD 
if cfd in source:
    browser.quit() 
    sys.exit("CFD Page")


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

# Google search each stock
for stock in stocks:

    browser.execute_script('''window.open("https://www.google.com/search?q={} news","_blank");'''.format(stock))


