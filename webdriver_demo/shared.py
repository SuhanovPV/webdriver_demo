from webdriver_demo.custom_wait import Wait
from selenium.webdriver.remote.webdriver import WebDriver

driver: WebDriver = ...
wait: Wait = ...


def assert_that(condition):
    return wait.until(condition)