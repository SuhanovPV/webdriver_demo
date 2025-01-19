from selenium.webdriver import Keys
from config import driver

from webdriver_demo.conditions import click_on, number_of_elements, type_to, asser_that

driver = driver

driver.get('https://www.ecosia.org/')

type_to('[name=q]', 'selene yashaka' + Keys.ENTER)
click_on('[data-test-id="mainline-result-web"] .result__header :nth-of-type(1)')
click_on('#pull-requests-tab')

asser_that(number_of_elements('[id^=issue_]:not([id$=_link])'), 9)
