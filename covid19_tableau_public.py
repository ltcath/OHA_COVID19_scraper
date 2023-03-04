#Import necessary programs
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.select import Select
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
import wget
import urllib.request
from bs4 import BeautifulSoup as bs
import requests
import re
import pandas as pd

 
#Set up url to contact
#Currently the filter on this are statewide. 
url_statewide = 'https://public.tableau.com/app/profile/oregon.health.authority.covid.19/viz/OregonCOVID-19TestingandOutcomesbyCounty-SummaryTable/Tests-SummaryTable'

#Pull up the website
driver=webdriver.Chrome(executable_path = '/Users/lukecathcart/Downloads/chromedriver')
driver.get(url_statewide) 
driver.maximize_window()
time.sleep(5) #To combat against web scraper protections, we need to ensure that the time it takes to click and type anything similates that of a human

#Accept cookies if necessary
try:
    driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
except (NoSuchElementException,TimeoutException):
    pass
time.sleep(5)

#To interact with the image, we need to go inside the iframe in the html code.
driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "iframe[title='Data Visualization']"))
time.sleep(10)

#We need to change the Filter Date Range to Last 20 Days
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[id='dijit_form_DropDownButton_0_label']"))).click()
#driver.find_element(By.CSS_SELECTOR, "span[class='dijitReset dijitInline dijitArrowButtonInner']").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "span[id='dijit_form_ToggleButton_4_label']").click()
time.sleep(5)
date_range = driver.find_element(By.CSS_SELECTOR, "input[aria-describedby='rdf-Lastn-label']")
date_range.clear()
date_range.send_keys('20')
driver.find_element(By.CSS_SELECTOR, "span[class='dijitReset dijitInline dijitButtonText tab-ctrl-formatted-fixedsize']").click()

#We need to change Filter County to Washington and remove Statewide
driver.find_element(By.CSS_SELECTOR, "div[class='tabComboBoxNameContainer tab-ctrl-formatted-fixedsize']").click()
time.sleep(5)
driver.find_element(By.NAME, 'FI_sqlproxy.0t4xf9k164ywie1csopq40rkm2ug,none:county:nk1866872308770826228_11233774043253875313_28').click()
time.sleep(5)
driver.find_element(By.NAME, 'FI_sqlproxy.0t4xf9k164ywie1csopq40rkm2ug,none:county:nk1866872308770826228_11233774043253875313_34').click()
time.sleep(5)

#We've finished interacting with the iframe, so now we can switch the driver to the rest of the page (now the iframe is just an image on the page)
driver.switch_to.default_content()

#Click the Download button
driver.find_element(By.CSS_SELECTOR, "i[id='downloadIcon']").click()
time.sleep(5)

#Now we have to go back into the iframe to click the Crosstab Button
driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "iframe[title='Data Visualization']"))
driver.find_element(By. CSS_SELECTOR, "button[data-tb-test-id='DownloadCrosstab-Button']").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "div[data-tb-test-id='sheet-thumbnail-2']").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "button[data-tb-test-id='export-crosstab-export-Button']").click()
time.sleep(50)

#We've now downloaded the data, so we can close the program
driver.quit()




