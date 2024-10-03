# Import Selenium and By
from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the website
driver.get("https://www.amazon.com/Bambaw-Metal-Water-Bottle-Flask/dp/B0834X3YY9/ref=sr_1_1_sspa?crid=305HSHSMAL7QS&dib=eyJ2IjoiMSJ9.oKRgIaCTa48oTANq-L4lccXe26nIhbWxtRGufhL77XaqyL4wuAmnci2LBtZTdFb7SNKA0Pw77rC4S9cI3ZJwPZOuQtBKQ_GPRk_C-QY0Vqp_KkN2MhA48qbw_gpMvTb1zefKQnWWo3lavEIk86tE1k_QgvHfP4XWlyHGNdvXFiCLG8WIPVKMkJxShFu1Fi1XKQb6Inrc47d2ACRkxzD8WdpzzDXtyMWLrgJV-0w6tW1DWj6mIKt_gBg6ybCs-82qYT78z4oc_NIYK9sGd61MLLRpGo-mqA5GR213AYFO-gk.-g409XrUke7DKrBpclBNHdzQMv4j5v5TervFjUgp0YA&dib_tag=se&keywords=bambaw+water+bottle&qid=1727980155&sprefix=bambaw+wat%2Caps%2C178&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")

# Find the element using CLASS_NAME 
price_dollar = driver.find_element(By. CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By. CLASS_NAME, value="a-price-fraction")

# Print the element
print(f"The price is {price_dollar.text}.{price_cents.text}")

## driver.close()
driver.quit()


