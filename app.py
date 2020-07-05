from selenium import webdriver

with webdriver.Chrome() as driver:
    driver.get("https://selenium.dev")
