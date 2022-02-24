# IMPORTS
from time import sleep
from zillowBot import ZillowBot
from gformBot import GformBot

chrome_driver_path = r"C:\Users\Your Path\Desktop\Development\chromedriver.exe"

zillowBot = ZillowBot(chrome_driver_path)
zillowBot.open_page()
zillowBot.filter_results()
rent_prices, mod_dates, addresses, links = zillowBot.get_info()
sleep(10)

gformBot = GformBot(chrome_driver_path)
gformBot.open_page()
gformBot.fill_form(rent_prices, mod_dates, addresses, links)

print("complete")
sleep(20)

