from selenium.webdriver import Keys
from config import driver
from webdriver_demo.browser import Browser

browser = Browser(driver)

browser.open('https://www.ecosia.org/')
browser.type_to('[name=q]', 'selene yashaka' + Keys.ENTER)
browser.click_on('[data-test-id="mainline-result-web"] .result__header :nth-of-type(1)')
browser.click_on('#pull-requests-tab')
browser.asser_that(browser.number_of_elements('[id^=issue_]:not([id$=_link])'), 10)
