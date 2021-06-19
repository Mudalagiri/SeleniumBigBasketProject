import time
from argparse import Action

import selenium as selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

items = []
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.bigbasket.com/")

action = ActionChains(driver)

driver.implicitly_wait(5)

driver.find_element_by_id('input').send_keys("carrot")
driver.find_element_by_xpath("//button[@type= 'submit']").click()


items = driver.find_elements_by_xpath("//div[@qa='product']")
print(len(items))

window_before = driver.window_handles[0]  # to get handle of parent window
window_before_title = driver.title
print(window_before_title)

# selecting directly by name
driver.find_element_by_link_text("Carrot - Organically Grown").click()

driver.find_element_by_xpath("//div[@data-qa = 'addToBasket']/span[1]").click()

# increasing the qty by 1
# driver.find_element_by_xpath("//div[@data-qa = 'add']").click()
# driver.find_element_by_class_name("_1aJzw").click()

# using mouse hover to check and select listed categories
action.move_to_element(driver.find_element_by_class_name("mImHu")).perform()

action.move_to_element(driver.find_element_by_link_text("Beauty & Hygiene")).click().perform()

# Refining search by sorting listings in high-to-low preference
driver.find_element_by_xpath("//div[@class='form-group']/select[1]").click()
driver.find_element_by_xpath("//select[@id = 'sel1']/option[3]").click()

driver.find_element_by_class_name("basket-content").click()

driver.close()




