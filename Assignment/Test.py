from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
'''
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


#driver = webdriver.Chrome(chrome_driver_path, options=options)
'''

chrome_driver_path = r"D:\Keerthana\Selenium\chromedriverv88.exe"
url = "https://www.saucedemo.com"

driver=webdriver.Chrome(chrome_driver_path)
driver.maximize_window()
driver.get(url)

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID,"user-name")),"Login Page is not displayed")
driver.find_element_by_id("user-name").send_keys("standard_user")
driver.find_element_by_id("password").send_keys("secret_sauce")
driver.find_element_by_id("login-button").click()
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,"//*[@class='btn_primary btn_inventory']")),"Products Page is not displayed")
driver.find_element_by_xpath("(//*[@class='btn_primary btn_inventory'])[1]").click()
driver.find_element_by_xpath("(//*[@class='btn_primary btn_inventory'])[2]").click()
driver.find_element_by_id("shopping_cart_container").click()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID,"cart_contents_container")),"Cart Page is not displayed")
checkOutBtn = driver.find_element_by_link_text("CHECKOUT")
checkOutBtn.send_keys(Keys.END)
checkOutBtn.click()

driver.close()
driver.quit()
