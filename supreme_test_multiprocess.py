import os
import sys
import traceback
import datetime
import time
import random

from multiprocessing import Process, Lock
from multiprocessing import Value
from multiprocessing import Array
import multiprocessing

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import store_info

try:
    import cpickle as pickle
except ModuleNotFoundError:
    import pickle


import selenium.common.exceptions
import csv

from bs4 import BeautifulSoup
import lxml

#first must install selenium
#also must have firefox and geckodriver (newest is best)
# os.environ['MOZ_HEADLESS'] = '1'



def create_drone(requests, mp_request_inv,url, size, payment, name):
    num_times =  mp_request_inv[requests[name][4]]
    # num_times = int(self._requests[name][3])
    print(url)
    while(num_times > 0):
        try:
            productBot = ProductBot(url, size, payment)
            productBot.add_to_cart()
            productBot.checkout()
            productBot.close()
            num_times -= 1

        except:
            traceback.print_exc()
            print("Unable to get item, retrying")
        finally:
            productBot.close()

    mp_request_inv[requests[name][4]] = 0

class SupremeBot():

    #NEED ATTRIBUTE OF DICTIONARY OF DICTIONARIES
    #Current Attributes
    # requests =
    # mp_request_status is a multiprocess array to indicate the
    # mp_request_inv is a multiprocess array indicating the inventory of each request, based on index
    #needs to be given an input file for both
    def __init__(self, input_csv,*args):

        self._driver = webdriver.Firefox(firefox_binary=FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe', log_file=sys.stdout))
        self._requests = {}
        self.get_request(input_csv)
        if len(args) > 1:
            self._payment = args[0]
            self._time = args[1]


    def get_request(self, input_csv):
        row_count = len(open(input_csv).readlines()) -1
        self._mp_request_status = Array('i', row_count)
        self._mp_request_inv = Array('i', row_count)

        with open(input_csv, newline = '') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=",")
            i = 0
            for row in reader:

                ##SEND THE PROCESS ID INTO SELF._REQUESTS
                self._requests[row['Name'].strip()] = [row['Type'].strip().lower(), row['Color'].strip(), row['Size'].strip(), row['Number'].strip(), i]
                self._mp_request_inv[i] = int(row['Number'].strip())
                i+=1
        print("inventory", self._mp_request_inv[:])


    def chooseCategory(self,type):
        url = ""
        if type[-1]!="s":
            type += "s"
        if type == "jackets":
            url = "https://www.supremenewyork.com/shop/all/jackets"
        elif type == "shirts":
            url = "https://www.supremenewyork.com/shop/all/shirts"
        elif (type == "tops" or type == "sweaters" or type == "tops/ sweaters"):
            url = "https://www.supremenewyork.com/shop/all/tops_sweaters"
        elif (type == "sweatshirts"):
            url = "https://www.supremenewyork.com/shop/all/sweatshirts"
        elif (type =="t-shirts"):
            url = "https://www.supremenewyork.com/shop/all/t-shirts"
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

        if self._driver.current_url != url and url != '':
            self._driver.get(url)

    def run(self):
        #tester##############################
        # holder = self._requests
        # self._requests = {}
        ##################################
        end_time = datetime.datetime.now() + datetime.timedelta(minutes = self._time)
        while (datetime.datetime.now() <= end_time):
            #ALSO PART OF TEST, REMOVE AFTER
            # if(random.randint(0,100) > 99):
            #     self._requests = holder
                ############################

            processes = []
            #Used to determine which payment info, currently should alternate
            payment_selection = 0
            for key in self._requests:

                payment = self._payment[payment_selection % len(self._payment)]
                self.chooseCategory(self._requests[key][0])
                try:
                    print(key)
                    #THIS IS WHERE THEY FIND THE STUFF
                    elems = self._driver.find_elements_by_partial_link_text(key)
                    for elem in elems:
                        right_elem = elem.find_element_by_xpath("../../p/a".format(self._requests[key][1]))
                        if (right_elem.text.lower() == self._requests[key][1].lower()):
                            #RUN THE DRONE
                            print("Status", self._mp_request_status[:])
                            url = right_elem.get_property("href")
                            if int(self._mp_request_status[self._requests[key][4]]) == 0:
                                self._mp_request_status[self._requests[key][4]] = 1
                                proc = Process(target=create_drone, args=(self._requests, self._mp_request_inv,url, self._requests[key][2], payment, key))

                                processes.append(proc)
                            #self.start_drone(right_elem.get_property("href"), self._requests[key][2], self._payment, key)
                                proc.start()

                            break


                except selenium.common.exceptions.NoSuchElementException:
                    print("Couldnt find ", key)
                    traceback.print_exc()

                except selenium.common.exceptions.ElementNotInteractableException:
                    traceback.print_exc()

                payment_selection +=1

            for proc in processes:
                proc.join()

            print("refresh")
            print("new inv", self._mp_request_inv[:])
            self._driver.refresh()

            #elems = self._driver.find_elements_by_xpath("//div/h1/a[contains(text(),{})]".format(key))
          #  for elem in elems:
                #if elem.find_element_by_xpath()
            #elem = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, key)))
            #try to find item
            # try:
            #     elem = WebDriverWait(self._driver, 10).until(EC.presence_of_element_located(By.PARTIAL_LINK_TEXT,key))
            #     elem = self._driver.find_element_by_partial_link_text(self, key)
            #     print(elem)
            # except:
            #     print("Cannot find specified item:", key)

    def start_drone(requests, mp_request_inv,url, size, payment, name):
        num_times =  mp_request_inv[requests[name][4]]
       # num_times = int(self._requests[name][3])
        while(num_times > 0):
            try:
                productBot = ProductBot(url, size, payment)
                productBot.add_to_cart()
                productBot.checkout()
                productBot.close()
                num_times -= 1

            except:
                traceback.print_exc()
                print("Unable to get item, retrying")
            finally:
                productBot.close()

        mp_request_inv[requests[name][4]] = 0



    def purchase(self,link,color):
        pass

    def update(self):
        self._elems = self._driver.find_elements_by_class_name('inner-article')
        for elem in elems:
            print(elem.find_element_by_tag_name('h1').text, elem.find_element_by_tag_name('p').text)

    def print_selections(self):
        print(self._selections)

    def close(self):
        self._driver.close()


#   INPUT FOR info should be:
#   ["name", "email", "telephone", "address" , "zip", "city", "State ABBREVIATION", "Country", "credit card number",
#   "Month expires", "Year expires", "CVV"]

class ProductBot:
    #assume url specifies color
    def __init__(self, url, size, pmt):
        self._url = url
        self._size = size

        self._info = pmt
        print(self._info)

        #start web browser
        self._driver = webdriver.Firefox(firefox_binary=FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe', log_file=sys.stdout))

    def add_to_cart(self):

        if (self._driver.current_url != self._url):
            self._driver.get(self._url)
        self.select_size()
        try:

            WebDriverWait(self._driver,30).until(EC.element_to_be_clickable((By.XPATH,"//input[@name='commit']"))).click()
            #self._driver.find_element_by_xpath("//input[@name='commit']").click()
        except selenium.common.exceptions.NoSuchElementException:
            #IF SOLD OUT

            print("Unable to add to cart")
            traceback.print_exc()

            ##MODIFY THE BUY LIST

        WebDriverWait(self._driver, 30).until(EC.presence_of_element_located((By.XPATH,"//a[@class='button checkout']"))).click()
        #self._driver.find_element_by_xpath("//a[@class='button checkout']").click()
        pass

    def select_size(self):
        if (self._size == ''):
            return
        select = Select(self._driver.find_element_by_id('s'))
        select.select_by_visible_text(self._size)
        pass

    def checkout(self):

        if (self._driver.current_url != "https://www.supremenewyork.com/checkout"):
            self._driver.get("https://www.supremenewyork.com/checkout")
        self.fill_payment()

        #BUY BUTTON
        buy_button = self._driver.find_element_by_xpath("//input[@value='process payment']")

        self.check_validity_and_pay(buy_button)



    def fill_payment(self):

        time.sleep(0.3)
        self._driver.find_element_by_xpath("//input[@name='order[billing_name]']").send_keys(self._info[0])
        self._driver.find_element_by_xpath("//input[@name='order[email]']").send_keys(self._info[1])
        self._driver.find_element_by_xpath("//input[@name='order[tel]']").send_keys(self._info[2])
        self._driver.find_element_by_xpath("//input[@name='order[billing_address]']").send_keys(self._info[3])
        time.sleep(0.1)
        if(self._info[4].strip()!=""):
            self._driver.find_element_by_xpath("//input[@name='order[billing_address_2]']").send_keys(self._info[4])
        self._driver.find_element_by_xpath("//input[@name='order[billing_zip]']").send_keys(self._info[5])
        self._driver.find_element_by_xpath("//input[@name='order[billing_city]']").send_keys(self._info[6])
        time.sleep(0.12)

        self._driver.find_element_by_xpath("//select[@id='order_billing_country']/option[text()= '{}']".format(self._info[8])).click()
        #select = Select(self._driver.find_element_by_id('order_billing_country'))
        #select.select_by_value(self._info[8])

        self._driver.find_element_by_xpath("//select[@id='order_billing_state']/option[text()= '{}']".format(self._info[7])).click()
        #select = Select(self._driver.find_element_by_id('order_billing_state'))
        #select.select_by_value(self._info[7])
        time.sleep(0.18)
        self._driver.find_element_by_xpath("//input[@name='credit_card[nlb]']").send_keys(self._info[9])

        self._driver.find_element_by_xpath("//select[@id='credit_card_month']/option[text()= '{}']".format(self._info[10])).click()
        #select = Select(self._driver.find_element_by_id('credit_card_month'))
        #select.select_by_value(self._info[10])

        self._driver.find_element_by_xpath("//select[@id='credit_card_year']/option[text()= '{}']".format(self._info[11])).click()
        #select = Select(self._driver.find_element_by_id('credit_card_year'))
        #select.select_by_value(self._info[11])
        time.sleep(0.15)
        self._driver.find_element_by_xpath("//input[@name='credit_card[rvv]']").send_keys(self._info[12])

        #Actions action = new Actions(self._driver)

        checkbox = self._driver.find_element_by_xpath("//label[@class='has-checkbox terms']").click()
        #builder.moveToElement(checkbox).perform();
        time.sleep(2)


    def close(self):
        self._driver.quit()

    def check_validity_and_pay(self, buy_button):
        #add check

        #print("Should have bought")
        #buy_button.click()

        time.sleep(60)


if __name__ == '__main__':
    multiprocessing.freeze_support()
    payment_infoTest = ["Name Here", "Some Email", "111-111-1111", "123 East Blvd", "Apt 333", "99999", "City", "State", "USA", "4444888855551111",
                        "10", "1010", "000"]
    payment_test = [payment_infoTest]
    supreme_bot = SupremeBot('Oct25Drop.csv',payment_test, 10)
    supreme_bot.run()

