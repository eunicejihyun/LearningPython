from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = r"C:\Users\Eunice Kim\Desktop\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

TWITTER_EMAIL = "yourusername"
TWITTER_PASSWORD = "yourpassword"

SPEED_TEST = "https://www.google.com/search?q=internet+speed+test"
TWITTER = "https://twitter.com/i/flow/login"

driver.get(SPEED_TEST)
sleep(2)

run_button = driver.find_element(By.ID, "knowledge-verticals-internetspeedtest__test_button")
run_button.click()
sleep(50)

dl_speed = driver.find_element(By.XPATH, '//*[@id="knowledge-verticals-internetspeedtest__download"]/p[1]').text
ul_speed = driver.find_element(By.XPATH, '//*[@id="knowledge-verticals-internetspeedtest__upload"]/p[1]').text
print(dl_speed, ul_speed)
tweet = f"#100DaysOfCode\nDay 41: Twitter Bot to post internet speeds.\nDownload Speed = {dl_speed}\nUpload Speed = {ul_speed}"

driver.get(TWITTER)
sleep(2)
username_field = driver.find_element(By.CSS_SELECTOR, "input[name='text']")
username_field.click()
username_field.send_keys(TWITTER_EMAIL)
username_field.send_keys(Keys.ENTER)

sleep(2)
password_field = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
password_field.click()
password_field.send_keys(TWITTER_PASSWORD)
password_field.send_keys(Keys.ENTER)

sleep(2)
new_tweet_field = driver.find_element(By.CSS_SELECTOR,
                                      "div.public-DraftStyleDefault-block.public-DraftStyleDefault-ltr")
new_tweet_field.send_keys(tweet)

tweet_button = driver.find_element(By.CSS_SELECTOR, "div[data-testid='tweetButtonInline']")
tweet_button.click()
