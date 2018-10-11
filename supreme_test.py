import os
import sys
from multiprocessing import Process
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

#first must install selenium
#also must have firefox and geckodriver (newest is best)
os.environ['MOZ_HEADLESS'] = '1'

class SupremeBot():

    #needs to be given an input file for both
    def __init__(self, input_csv,*args):
        self.get_request(input_csv)

    def get_request(self, input_csv):
        with open(input_csv, newline = '') as csvfile:
            self._requests = csv.DictReader(csvfile, delimiter=",")

    def chooseCategory(self,type):
        url = ""
        if type[-1]!="s":
            type += s
        if type == "jackets":
            url = "https://www.supremenewyork.com/shop/all/jackets"
        elif type == "shirts":
            url = "https://www.supremenewyork.com/shop/all/shirts"
        elif (type == "tops" or type == "sweaters" or type == "tops/ sweaters"):
            url = "https://www.supremenewyork.com/shop/all/tops_sweaters"
        elif (type == "sweatshirts"):
            url = "https://www.supremenewyork.com/shop/all/sweatshirts"
        elif (type == "pants"):
            url = "https://www.supremenewyork.com/shop/all/pants"
        elif (type == "hats"):
            url = "https://www.supremenewyork.com/shop/all/hats"
        elif (type == "bags"):
            url = "https://www.supremenewyork.com/shop/all/bags"
        elif (type == "accessories"):
            url = "https://www.supremenewyork.com/shop/all/accessories"
        elif (type == "shoes"):
            url = "https://www.supremenewyork.com/shop/all/shoes"
        elif (type == "skates"):
            url = "https://www.supremenewyork.com/shop/all/skates"

        if self._driver.current_url != url:
            self._driver.get(url)

    def run(self):
        for key in self._requests:
            #set url
            chooseCategory(self._requests[key][0])
            #try to find item
            try:
                elem = self._driver.find_element_by_partial_link_text(self, key)
            except:
                print("Cannot find specified item:", key)

    def purchase(self,link,color):
        pass

    def update(self):
        self._selection = []
        elems = self._driver.find_elements_by_class_name('inner-article')
        for elem in elems:
            print(elem.find_element_by_tag_name('h1').text, elem.find_element_by_tag_name('p').text)

    def print_selections(self):
        print(self._selections)

    def close(self):
        self._driver.close()

class ProductBot:
    #assume url specifies color
    def __init__(self, url, size, *args):
        self._url = url
        self._size = size
        #ASSERT args =
        # ["name", "email", "telephone", "address" , "zip", "city", "State ABBREVIATION", "Country", "credit card number",
        #  "Month expires", "Year expires", "CVV"]
        #
        #
        #

        if (len(args) > 0):
            self._info = args[0]
        #start web browser
        self._driver = webdriver.Firefox(firefox_binary=FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe', log_file=sys.stdout))

    def add_to_cart(self):
        if (self._driver.current_url != self._url):
            self._driver.get(self._url)
        self.select_size()
        self._driver.find_element_by_xpath("//input[@name='commit']").click()
        self._driver.find_element_by_xpath("//a[@class='button checkout']").click()
        pass
    # url holds color, so just pass in a product bot that holds color
    # def select_color(self):
    #     elem =  self._driver.find_element_by_class_name("three-images")
    #     for elements in elem:
    #         pass
    #
    #     pass

    def select_size(self):
        select = Select(self._driver.find_element_by_id('s'))
        select.select_by_visible_text(self._size)
        pass

    def checkout(self):
        self._driver.get("https://www.supremenewyork.com/checkout")
        self.fill_payment()


    def fill_payment(self):
        self._driver.find_element_by_xpath("//input[@name='order[billing_name]']").send_keys(payment_info[0])
        self._driver.find_element_by_xpath("//input[@name='order[email]']").send_keys(payment_info[1])
        self._driver.find_element_by_xpath("//input[@name='order[tel]']").send_keys(payment_info[2])
        self._driver.find_element_by_xpath("//input[@id='")

    def pay(self):

        pass

    pass


def main():
    #supreme_bot = SupremeBot('supreme_test.csv')
    #supreme_bot.close()
    payment_info = ["name", "email", "9995551111", "address" , "99999", "city", "AZ", "USA", "8888779955446632",
          "10", "2020", "336"]
    testBot = ProductBot("https://www.supremenewyork.com/shop/jackets/fewna2yb6/nr1felatu","Large", payment_info)
    testBot.add_to_cart()
    testBot.checkout()

main()