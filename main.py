## import the necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

## initialize the webdriver
driver = webdriver.Chrome()

## navigate to the website
driver.get("https://www.scoir.com/")
