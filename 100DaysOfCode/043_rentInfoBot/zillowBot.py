from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

ZILLOW = "https://www.zillow.com/homes/for_rent/Washington,-DC_rb/"
MAX_PRICE = "1400"


class ZillowBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.rent_prices = []
        self.mod_dates = []
        self.addresses = []
        self.links = []
        self.next_page_button = ""

    def open_page(self):
        self.driver.get(ZILLOW)
        sleep(2)

    def filter_results(self):
        # SET LISTING TYPE TO RENTAL _______________________________________________________________
        list_type_btn = self.driver.find_element(By.ID, "listing-type")
        list_type_btn.click()
        sleep(1)
        for_rent_btn = self.driver.find_element(By.ID, "isForRent")
        for_rent_btn.click()
        sleep(1)

        # SET MAX PRICE TO $X _______________________________________________________________
        price_btn = self.driver.find_element(By.ID, "price")
        price_btn.click()
        sleep(1)
        max_price_fld = self.driver.find_element(By.ID, "price-exposed-max")
        max_price_fld.click()
        max_price_fld.send_keys(MAX_PRICE)
        max_price_fld.send_keys(Keys.ENTER)
        sleep(10)

    def get_info(self):

        page_count = int(self.driver.find_elements(By.CLASS_NAME,"PaginationNumberItem-c11n-8-62-4__sc-bnmlxt-0")[-1].text)
        print(page_count)




        for i in range(page_count):
            self.driver.execute_script("window.scrollTo(0, 1000)")
            sleep(3)
            # GATHER & CLEAN RENT PRICES _______________________________________________________________
            ele_rent_prices = self.driver.find_elements(By.CLASS_NAME, "list-card-price")
            self.rent_prices += [str(x.text.split(" ")[0].split("/")[0]) for x in ele_rent_prices]
            print("get rent prices")

            # MODIFIED/UPDATED DATE _______________________________________________________________
            ele_mod_dates = self.driver.find_elements(By.CSS_SELECTOR, "div.list-card-variable-text.list-card-img-overlay")
            self.mod_dates += [x.text for x in ele_mod_dates]
            print("get mod dates")

            # ADDRESSES _______________________________________________________________
            ele_addresses = self.driver.find_elements(By.TAG_NAME, "address")
            self.addresses += [x.text for x in ele_addresses]

            print(self.addresses)

            # HYPERLINK _______________________________________________________________
            ele_links = self.driver.find_elements(By.CSS_SELECTOR, ".list-card-info [href]")
            self.links += [x.get_attribute('href') for x in ele_links]

            if i in range(page_count - 1):
                self.nav_next_page()
                sleep(4)

        return self.rent_prices, self.mod_dates, self.addresses, self.links


        # if self.final_page():
        #     return self.rent_prices, self.mod_dates, self.addresses, self.links
        # else:
        #     self.nav_next_page()
        #     sleep(4)
        #     self.get_info()

    # def final_page(self):
    #     try:
    #         self.driver.find_element(By.CSS_SELECTOR, "a[title='Next page'] [disabled]")
    #     except NoSuchElementException:
    #         return False
    #         print("no next page")
    #     else:
    #         return True
    #         print("next page")
    #
    def nav_next_page(self):
        self.next_page_button = self.driver.find_element(By.CSS_SELECTOR, "a[title='Next page']")
        self.next_page_button.click()
        print("moved to next page")




