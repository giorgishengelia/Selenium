# Import Selenium & By 
from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdrvier
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the website 
driver.get("https://www.python.org/")

# Get the text using CSS selectors
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
# Dictionary 
events = {}

# Add the gathered data to the dictionary
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

# Print the results 
print(events)

## driver.close()
driver.quit()
