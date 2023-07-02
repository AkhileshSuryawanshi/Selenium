from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()


driver.get("https://www.amazon.in/")


search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("Wrist Watches")
search_button = driver.find_element(By.XPATH, "//input[@value='Go']")
search_button.click()


filter_analogue = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//li[@aria-label='Analogue']")))
filter_analogue.click()

filter_material = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//li[@aria-label='Leather']")))
filter_material.click()

filter_brand = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[@class='a-size-base a-color-base' and contains(text(), 'Titan')]")))
filter_brand.click()

filter_discount = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), '25% Off or more')]")))
filter_discount.click()


search_results = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[@data-component-type='s-search-result']")))

if len(search_results) >= 5:
    fifth_element = search_results[4].text
    print("Fifth Element:", fifth_element)
else:
    print("There are fewer than five elements in the search results.")

