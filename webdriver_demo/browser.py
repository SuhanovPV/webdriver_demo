from typing import Tuple

from selenium.common import WebDriverException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import _element_if_visible
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver


class Browser:
    def __init__(self, driver: WebDriver, wait: WebDriverWait = None):
        self.driver = driver
        self.wait = wait if wait else WebDriverWait(driver, timeout=5, ignored_exceptions=(WebDriverException,))

    def open(self, url):
        self.driver.get('https://www.ecosia.org/')

    def element(self, selector):
        def command(_):
            return _element_if_visible(self.driver.find_element(*self.to_locator(selector)))

        self.wait.until(command)

    def click_on(self, selector):
        def command(_):
            webelement = self.driver.find_element(*self.to_locator(selector))
            webelement.click()
            return webelement

        self.wait.until(command)

    def type_to(self, selector, value):
        def command(_):
            webelement = self.driver.find_element(*self.to_locator(selector))
            is_element_covered = self.driver.execute_script(
                '''
                        element=arguments[0];
                        rectangle = element.getBoundingClientRect();
                        let x = rectangle.x + Math.floor(rectangle.width/2);
                        let y = rectangle.y + Math.floor(rectangle.height/2);
                        return !element.isSameNode(document.elementFromPoint(x,y));
                        ''',
                webelement)

            if is_element_covered:
                raise TimeoutException

            webelement.send_keys(value)
            return webelement

        self.wait.until(command)

    def number_of_elements(self, selector):
        def command(_):
            return len(self.driver.find_elements(*self.to_locator(selector)))

        return self.wait.until(command)

    @staticmethod
    def asser_that(actual_value, value):
        assert actual_value == value

    @staticmethod
    def to_locator(selector) -> Tuple[str, str]:
        return (By.XPATH, selector) if (
                selector.startswith('/') or
                selector.startswith('//') or
                selector.startswith('./') or
                selector.startswith('..') or
                selector.startswith('(')
        ) else (By.CSS_SELECTOR, selector)
