from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from webdriver_demo.conditions import click_on_element, type_to_element, number_of_elements

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, timeout=5, ignored_exceptions=(WebDriverException,))

driver.get('https://www.ecosia.org/')
driver.find_element(By.CSS_SELECTOR, '[name=q]').send_keys()

wait.until(type_to_element('[name=q]', 'selene yashaka' + Keys.ENTER))
wait.until(click_on_element('[data-test-id="mainline-result-web"] .result__header :nth-of-type(1)'))
wait.until(click_on_element('#pull-requests-tab'))

number_of_pulls = number_of_elements('[id^=issue_]:not([id$=_link])', 9)
