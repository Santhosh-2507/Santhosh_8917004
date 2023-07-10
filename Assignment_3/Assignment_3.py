# Assignment 3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

#Setting up the webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.bestbuy.ca/en-ca")

time.sleep(3)

#Finding the search bar and entering text
search_bar = driver.find_element("name", "search")
search_bar.send_keys("men-watches")

#Getting the page displayed using the keyword entered
search_bar.send_keys(Keys.RETURN)
time.sleep(5)

assert "men-watches" in driver.title

#sorting the products using highest rated
sort_select = Select(driver.find_element("id","Sort"))
sort_select.select_by_visible_text("Highest Rated")
time.sleep(5)

#Filtering the option with the product availability to get it shipped
filter_checkbox = driver.find_element("id","facetFilter-Get it Shipped")
filter_checkbox.click()
time.sleep(3)

#Selecting the product from the list
product_list = driver.find_element("xpath","//*[@class='productItemName_3IZ3c']")
product_list.click()
time.sleep(8)

#Clicking through the rating option
product_rating = driver.find_element("xpath","(//button[@id='rating-link'])[1]")
product_rating.click()
time.sleep(5)

#Toggling on the verfied purchase option button
rating_checkbox = driver.find_element("xpath","//*[@class='x-toggle-switch toggleSwitch_2ZtVX']")
rating_checkbox.click()
time.sleep(3)

#Attempting to write the own review
product_review = driver.find_element("xpath","(//span[@class='content_3Dbgg'][normalize-space()='Write Your Review'])[2]")
product_review.click()
time.sleep(4)

driver.close()