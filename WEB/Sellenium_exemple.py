from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#telecharger le driver Chrome/mozila sur le site de selenium

# creer une variable pour déclencher le driver
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://fra-vsgdt-01/webquartz/ux/login")


#LOGIN
Log=driver.find_element_by_id("name-log")
mdp=driver.find_element_by_id("password-log")

Log.send_keys("")
mdp.send_keys("")
loggin=driver.find_element_by_class_name("btn-lg")
loggin.click()

badgeages=driver.find_element_by_xpath('/html/body/form/main/div/div/div/div[1]/div[2]/div/div[2]/button[1]')
badgeages.click()

BADGER=driver.find_element_by_class_name("btnbad_btn")
BADGER.click()

Confirm=driver.find_element_by_xpath('//*[@id="BTN_BAD_MODALMSG_BTNA"]')
Confirm.click()
