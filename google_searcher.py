import xlwt #pandasla excele yazmaq ucun pip install etmisem burda da import edirem.
import numpy as np
import pandas as pd
#import json
import time
import requests
#import bs4
import selenium
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver import Firefox
#from selenium.webdriver.firefox.options import Options
import selenium.common.exceptions
print("Imports Done")

options=Options()
options.binary_location='C:\Program Files\Google\Chrome\Application\chrome.exe'
browser=Chrome(executable_path='chromedriver.exe', options=options)
domain="https:www.google.az"
browser.get(domain)
element=browser.find_element_by_name("q")
element.send_keys("monitor\n")
try:
    element.submit()
except:
    "Error"
    rs=browser.find_elements_by_class_name("iUh30")
    for i in rs:
        print (i.text)
