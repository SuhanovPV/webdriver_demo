from selenium.common import WebDriverException
from selenium.webdriver import Keys
from webdriver_demo.custom_wait import Wait
from webdriver_demo.shared import assert_that, driver
from webdriver_demo.conditions import number_of_elements
from webdriver_demo.commands import click_on, type_to
from webdriver_demo import shared
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
shared.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
shared.wait = Wait(shared.driver, timeout=2, ignored_exceptions=(WebDriverException,))

shared.driver.get('https://www.ecosia.org/')
type_to('[name=q]', 'selene yashaka' + Keys.ENTER)
click_on('[data-test-id="mainline-result-web"] .result__header :nth-of-type(1)')
click_on('#pull-requests-tab')

assert_that(number_of_elements('[id^=issue_]:not([id$=_link])', 9))

shared.driver.quit()