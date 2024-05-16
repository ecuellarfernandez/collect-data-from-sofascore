from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Open the browser and navigate to the webpage
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.set_window_size(1400, 1000)
driver.get("https://www.sofascore.com/es-la/torneo/futbol/spain/laliga/8#id:52376")

# Wait for the page to load
time.sleep(5)

# Wait until the "Por Ronda" button is clickable and then click on it
wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Por Ronda"]'))).click()

# Wait for the dropdown menu to load
time.sleep(5)

# Wait until the dropdown button is clickable and then click on it
dropdown_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="DropdownButton jQruaf"]')))
dropdown_button.click()

# Wait for the list of rounds to load
time.sleep(5)

# Find all rounds (list items)
rounds = driver.find_elements(By.XPATH,'//li[@role="option"]')

# Iterate over each round
for i in range(len(rounds)):
    # Scroll to the current round
    driver.execute_script("arguments[0].scrollIntoView();", rounds[i])

    # Wait until the current round is clickable and then click on it
    wait.until(EC.element_to_be_clickable((By.XPATH, '//li[@role="option" and text()="' + rounds[i].text + '"]'))).click()

    # Wait for the round matches to load
    time.sleep(5)

    # Find the link associated with the round
    link = rounds[i].find_element(By.TAG_NAME, 'a')

    # Get the href attribute of the link
    url = link.get_attribute('href')

    # Print the URL
    print(url)

    # You can also navigate to the URL using driver.get(url)

    # Go back to the dropdown menu (click dropdown button again)
    dropdown_button.click()

    # Wait until the dropdown button is clickable again
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="DropdownButton jQruaf"]')))

    # Wait for the list of rounds to load again
    time.sleep(5)

    # Find all rounds (list items) again
    rounds = driver.find_elements(By.XPATH,'//li[@role="option"]')

# Close the browser
driver.quit()