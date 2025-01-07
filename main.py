## import the necessary libraries
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

## load the environment variables
load_dotenv()

## initialize the webdriver
driver = webdriver.Chrome()

## navigate to the website
driver.get("https://app.scoir.com/signin")

## wait for the page to load
wait = WebDriverWait(driver, 10)

## find the login button
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-primary']")))

## click the login button
login_button.click()

## wait for the login page to load
wait.until(EC.url_contains("login"))

## find the username and password input fields
username_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")

## enter the username and password
username_input.send_keys(os.getenv("EMAIL"))
password_input.send_keys(os.getenv("PASSWORD"))

## find the login button and click it
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

## wait for the home page to load
wait.until(EC.url_contains("home"))

## close the browser
driver.quit()

