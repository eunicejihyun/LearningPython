from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep

IG_UN = "your@gmail.com"
IG_PW = "your_password"
TARGET_UN = "debaysounds"
chrome_driver_path = r"C:\Users\YourPath\Desktop\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
IG_URL = "https://www.instagram.com/"
driver.get(IG_URL)
sleep(2)

# Login ________________________________________________________________________________________________________________
un_field = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
pw_field = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
un_field.send_keys(IG_UN)
pw_field.send_keys(IG_PW)
pw_field.send_keys(Keys.ENTER)
sleep(2)

# Checking to see if there is a request to save some info
try:
    not_now = driver.find_element(By.XPATH, "//*[contains(text(), 'Not Now')]")
    not_now.click()
except NoSuchElementException:
    print("No save request")
sleep(1)

# Dealing with another pop up
try:
    not_now = driver.find_element(By.XPATH, "//*[contains(text(), 'Not Now')]")
    not_now.click()
except NoSuchElementException:
    print("No save request")
sleep(2)

# Navigate to page _____________________________________________________________________________________________________
driver.get(f"{IG_URL}{TARGET_UN}/")
sleep(2)

# Click on followers
follower_count = driver.find_element(By.PARTIAL_LINK_TEXT, " followers")
follower_count.click()
sleep(2)

# Get list of followers
follower_list = driver.find_elements_by_css_selector("li button")
sleep(2)

# Follow accounts
for account in follower_list:
    try:
        account.click()
        sleep(1)
    except ElementClickInterceptedException:
        cancel_button = driver.find_element(By.XPATH, "//*[contains(text(), 'Cancel')]")
        cancel_button.click()
