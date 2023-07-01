from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys

# Launch Chrome browser
driver = webdriver.Chrome()

# Go to Amazon India website
driver.get("https://www.amazon.in")

# Find the search bar and enter the search query
search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
search_bar.send_keys("Wrist Watches")

# Submit the search query
search_bar.send_keys(Keys.RETURN)

# Apply filters for Display, Brands Material, Brand, and Discount
display_filter = driver.find_element(By.XPATH, "//span[contains(text(), 'Analogue')]")
display_filter.click()

material_filter = driver.find_element(By.XPATH, "//span[contains(text(), 'Leather')]")
material_filter.click()

brand_filter = driver.find_element(By.XPATH, "//span[contains(text(), 'Titan')]")
brand_filter.click()

discount_filter = driver.find_element(By.XPATH, "//span[contains(text(), '25% Off or more')]")
discount_filter.click()

# Wait for the search results to load
driver.implicitly_wait(10)

# Find the fifth element from the search results
fifth_element = driver.find_element(By.XPATH, "(//div[@data-index='4'])[1]")

# Get the text of the fifth element
fifth_element_text = fifth_element.text
print("Fifth element from the search results:")
print(fifth_element_text)

# Wait for user input before closing the browser
input("Press Enter key to close the browser...")

# Close the browser
driver.quit()
sys.exit(0)
