from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
driver = webdriver.Chrome()
url = "https://www.pandora.com/"
driver.get(url)
print('transitioning../...')
print("Hard Rock")
sleep(10)
print("Live")
task1 = driver.find_element_by_class_name("SearchField__input")
#select = Select(driver.find_element_by_id('priceTo'))
#select.select_by_value('15000')
#driver.find_element_by_xpath("//*[contains(text(), 'GO')]").click(
#x = input("Input a Search Term: ")
task1.send_keys("Today's Hits")
sleep(5)
driver.find_element_by_class_name('SearchListItem__img').click()
#task1.submit()
#driver.find_element_by_xpath("//*[contains(text(), '$15,000')]").click()
#sleep(3)
#driver.find_element_by_class_name('Icon').click()
#driver.find_element_by_id('csnSearchButton').click()
