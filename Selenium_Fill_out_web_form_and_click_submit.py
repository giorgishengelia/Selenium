from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")


# Find the "Search" <input> by Name
name = driver.find_element(By.NAME, value="fName")
lastname = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
# Sending keyboard input to Selenium
name.send_keys("Georgi")
lastname.send_keys("Shengi")
email.send_keys("myemail@gmail.com")#, Keys.ENTER)

submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()





#driver.quit()