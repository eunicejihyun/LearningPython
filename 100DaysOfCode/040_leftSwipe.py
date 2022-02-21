from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


# FUNCTIONS ____________________________________________________________________________________________________________


def bot_check():
    """ Checks to see if the site thinks we're using a bot... Acts accordingly. """
    sleep(2)
    try:
        captcha = driver.find_element(By.NAME, "captcha")
    except NoSuchElementException:
        pass
    else:
        answer = input("Type what you see: ")
        captcha.send_keys(answer)
        button = driver.find_element(By.XPATH,
                                     '//*[@id="main"]/div/div[1]/div[2]/main/div/div[4]/form/div[2]/button/span/span/span')
        button.click()
        type_number()


def type_number():
    """ Checks to see if the site wants the user to type their phone number. Acts accordingly. """
    try:
        enter_number = driver.find_element(By.ID, "phone")
    except NoSuchElementException:
        pass
    else:
        enter_number.send_keys(US_phone_number)
        continue_button = driver.find_element(By.XPATH,
                                              '//*[@id="main"]/div/div[1]/div[2]/main/div/div[3]/form/div[4]/button/span/span/span')
        continue_button.click()


def check_ad():
    """ Checks to see if Bumble is advertising. Acts accordingly. """
    try:
        ad_close = driver.find_element(By.CLASS_NAME, "dialog__close")
    except NoSuchElementException:
        pass
    else:
        ad_close.click()


# Open Google Chrome with chromedriver
chrome_driver_path = r"C:\Users\YOUR_DRIVER_PATH\Desktop\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
url = "https://bumble.com/app/"
driver.get(url)

# Clicks on button to continue with phone number
sleep(2)
use_cell = driver.find_element(By.XPATH,
                               '//*[@id="main"]/div/div[1]/div[2]/main/div/div[3]/form/div[3]/div/span/span/span')
use_cell.click()

# Get user's phone number
US_phone_number = input("What is your phone number? ")
type_number()
bot_check()

# Authentication with phone
code = input("What is the 6-digit code you received? ")
code_field = driver.find_element(By.CLASS_NAME, "text-field__input")
code_field.send_keys(code)
bot_check()

# "Swipes" left on 10 matches
for x in range(10):
    sleep(2)
    check_ad()
    pass_button = driver.find_element(By.CSS_SELECTOR, "span[data-qa-icon-name='floating-action-no']")
    hover = ActionChains(driver).move_to_element(pass_button)
    hover.perform()
    sleep(1)
    pass_button.click()

# Closes the browser
driver.quit()
