from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)