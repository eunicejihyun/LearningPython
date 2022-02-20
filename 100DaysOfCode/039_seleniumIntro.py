from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r"C:\Users\YOUR_PATH\Desktop\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)


# AMAZON.COM ___________________________________________________________________________________________________________
# driver.get(url)
# url = "https://www.amazon.com/Winnie-Pooh-Little-Things-Life/dp/1368076092/ref=cm_cr_arp_d_product_top?ie=UTF8"
# price = driver.find_element_by_id("corePrice_feature_div")
# print(price.text)
#
# search_bar = driver.find_element_by_name("site-search")
# print(search_bar.get_attribute("action"))
#
# photo = driver.find_element_by_id("imgBlkFront")
# print(photo.size)

# top_review = driver.find_element_by_xpath('//*[@id="customer_review-R2XHZ1LM7EUL51"]/div[4]/span/div/div[1]/span')
# print(top_review.text)

# PYTHON.COM __________________________________________________________________________________________________________
# driver.get(url2)
# url2 = "https://www.python.org/"
# event_times = driver.find_elements_by_css_selector(".event-widget time")
# event_names = driver.find_elements_by_css_selector(".event-widget li a")
#
# for name in event_names:
#     print(name.text)
#
# events = {_:{"time": event_times[_].text, "name": event_names[_].text} for _ in range(len(event_times))}
# print(events)


# # WIKIPEDIA.COM ______________________________________________________________________________________________________
# url3 = "https://en.wikipedia.org/wiki/Main_Page"
#
# driver.get(url3)
#
# article_count = driver.find_element_by_css_selector("#articlecount a")
# print(article_count.text)
#
# # article_count.click()
#
# # all_portals = driver.find_element_by_link_text("All portals")
# # all_portals.click()
#
# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# NEWSLETTER SIGN-UP ___________________________________________________________________________________________________

# url4 = "http://secure-retreat-92358.herokuapp.com/"
#
# driver.get(url4)
#
# first_name = driver.find_element_by_name("fName")
# first_name.send_keys("John")
#
# last_name = driver.find_element_by_name("lName")
# last_name.send_keys("Smith")
#
# email = driver.find_element_by_name("email")
# email.send_keys("john@email.com")
#
# button = driver.find_element_by_css_selector("button")
# button.click()


# COOKIE CLICKER GAME __________________________________________________________________________________________________

from datetime import datetime

minutes = 5
minutes_added = datetime.timedelta(minutes=minutes)
end_time = datetime.now() + minutes_added

seconds = 5
seconds_added = datetime.timedelta(seconds=seconds)
check_time = datetime.now() + seconds_added

cookie_url = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(cookie_url)

cookie = driver.find_element_by_id("bigCookie")
print("found cookie")

while datetime.now() < end_time:
    cookie.click()

    if datetime.now() > check_time:
        check_time = datetime.now() + seconds_added
        enabled_products = driver.find_elements_by_class_name("product unlocked enabled")
        enabled_products[-1].click()


# Close only closes one tab - This quits the entire browser
driver.quit()