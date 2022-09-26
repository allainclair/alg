# from requests import get
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC

from icecream import ic



URL_QUERY_USER = 'https://twitter.com/search?q={}&src=typed_query&f=user'
DELAY = 20
Q = 'influencer'

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get(URL_QUERY_USER.format(Q))
# element = driver.find_element_by_xpath('//input[@data-testid="cellInnerDiv"]')
driver.implicitly_wait(40)
elements = driver.find_elements('xpath', '//input[@data-testid="cellInnerDiv"]')
ic(elements)


# try:
#     myElem = WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
#     print "Page is ready!"
# except TimeoutException:
#     print "Loading took too much time!"
