from typing import Tuple

from selenium.common import TimeoutException

from config import wait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import _element_if_visible

wait = wait


def to_locator(selector: str) -> Tuple[str, str]:
    return (By.XPATH, selector) if (
            selector.startswith('/') or
            selector.startswith('//') or
            selector.startswith('./') or
            selector.startswith('..') or
            selector.startswith('(')
    ) else (By.CSS_SELECTOR, selector)


def element(selector):
    def command(driver: WebDriver):
        return _element_if_visible(driver.find_element(*to_locator(selector)))

    wait.until(command)


def click_on(selector):
    def command(driver: WebDriver):
        webelement = driver.find_element(*to_locator(selector))
        webelement.click()
        return webelement

    wait.until(command)


def type_to(selector, value):
    def command(driver: WebDriver):
        webelement = driver.find_element(*to_locator(selector))
        is_element_covered = driver.execute_script(
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

    wait.until(command)


def number_of_elements(selector):
    def command(driver: WebDriver):
        return len(driver.find_elements(*to_locator(selector)))

    return wait.until(command)


def asser_that(actual_value, value):
    assert actual_value == value
