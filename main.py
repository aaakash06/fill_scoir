## import the necessary libraries
import os
import time
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
wait = WebDriverWait(driver, 4)

# Find the text input by name and type a value
email_input = driver.find_element(By.NAME, "email")
email_input.send_keys(os.getenv("EMAIL"))

password_input = driver.find_element(By.NAME, "password")
password_input.send_keys(os.getenv("PASSWORD"))

## find the login button

login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))

## click the login button
login_button.click()

wait = WebDriverWait(driver, 4)


## wait for the login page to load
apply_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/student/app-profile"]')))
apply_button.click()

# wait.until(EC.url_contains("app-profile"))

# wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/student/app-profile?stage=&amp;prospectId=676dd01f1f50748393d76963"]')))


## after selecting a college
## community based org
time.sleep(10)
driver.find_element(By.XPATH, '//*[@id="cbo-information"]/div[1]/div[3]/div/div[2]/button').click()
driver.find_element(By.XPATH, '//*[@id="cbo-information"]/div[1]/div[3]/div/div[2]/button').click()
## high school coursework 
driver.find_element(By.XPATH, '//*[@id="app-main-content"]/div/div/div/div[2]/div/div[1]/ul/div[6]/div/div/div/ul/a[4]').click()
# driver.find_element(By.XPATH, '//*[@id="cbo-information"]/div[1]/div[3]/div/div[2]/button').click()

# driver.find_element(By.XPATH, "//a[@href='#']").click()
# driver.find_element(By.CLASS_NAME, "jss-158").click()
# driver.find_elements(By.TAG_NAME, "button")[1].click()


# ## find the login button and click it
# login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
# login_button.click()

# ## wait for the home page to load
# wait.until(EC.url_contains("home"))
time.sleep(100)

## close the browser
driver.quit()

