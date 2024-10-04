from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#To keep the browser open 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Webdriver
driver = webdriver.Chrome(options=chrome_options)
# Address 
driver.get("https://secure-retreat-92358.herokuapp.com/")


# Find the <input> by Name
name = driver.find_element(By.NAME, value="fName")
lastname = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
# Sending keyboard input to Selenium
name.send_keys("NameExample")
lastname.send_keys("LastnameExample")
email.send_keys("myemail@gmail.com")#, Keys.ENTER) <- To submit with using Enter key

# Clicking the submit button 
submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()





#driver.quit()
