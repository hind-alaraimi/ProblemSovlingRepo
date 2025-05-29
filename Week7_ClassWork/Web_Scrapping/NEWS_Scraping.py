from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

driver = webdriver.Chrome()
driver.get("https://www.bbc.com/innovation")

wait = WebDriverWait(driver, 10)

cards = wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, '//div[@data-testid="dundee-card"]')
))

results = []

for card in cards:
    title = card.find_element(By.XPATH, './/h2[@data-testid="card-headline"]').text
    summary = card.find_element(By.XPATH, './/p[@data-testid="card-description"]').text
    img = card.find_element(By.XPATH, './/img')
    img_url = img.get_attribute('src')

    results.append({
        "title": title,
        "summary": summary,
        "image_url": img_url,
        })

driver.quit()

with open("bbc_dundee_cards.json", "w") as f:
    json.dump(results, f, indent=2)
