from selenium.common import WebDriverException
from selenium.webdriver import Keys
from webdriver_demo.custom_wait import Wait
from webdriver_demo import browser
from webdriver_demo.condition import that
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
browser.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
browser.wait = Wait(browser.driver, timeout=2, ignored_exceptions=(WebDriverException,))

browser.open('https://www.ecosia.org/')
browser.type_to('[name=q]', 'selene yashaka' + Keys.ENTER)
browser.click_on('[data-test-id="mainline-result-web"] .result__header :nth-of-type(1)')
browser.click_on('#pull-requests-tab')

browser.assert_(that.number_of_elements('[id^=issue_]:not([id$=_link])', 9))

browser.quit()