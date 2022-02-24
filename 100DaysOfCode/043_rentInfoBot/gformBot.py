from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

G_FORM = "https://forms.gle/oapvpxupVp4r2haNA"


class GformBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def open_page(self):
        self.driver.get(G_FORM)
        sleep(2)

    def fill_form(self, rent_prices, mod_dates, addresses, links):

        for x in range(len(rent_prices)):
            input_fields = self.driver.find_elements(By.CLASS_NAME, "quantumWizTextinputPaperinputInput")

            rent_field = input_fields[0]
            date_field = input_fields[1]
            addr_field = input_fields[2]
            link_field = input_fields[3]

            rent_field.click()
            rent_field.send_keys(rent_prices[x])

            date_field.click()
            date_field.send_keys(mod_dates[x])

            addr_field.click()
            addr_field.send_keys(addresses[x])

            link_field.click()
            link_field.send_keys(links[x])


            sleep(1)
            submit_button = self.driver.find_element(By.CSS_SELECTOR, ".freebirdFormviewerViewNavigationLeftButtons div[role='button']")
            submit_button.click()
            sleep(2)
            new_response_button = self.driver.find_element_by_link_text("Submit another response")
            new_response_button.click()
            sleep(2)